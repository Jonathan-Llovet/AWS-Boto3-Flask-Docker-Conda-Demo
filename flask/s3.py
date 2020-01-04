import os
from flask import Flask, request
import boto3

# inspired by prettyprinted https://www.youtube.com/watch?v=7gqvV4tUxmY

# boto3 will search for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in environment variables
# Preferred best practice is to use AWS IAM roles whenever possible, rather than access key
# Since this is being used with a docker container designed to be run in a sandbox,
# the credentials will not leave the sandbox host.
# Configure your lambda functions or EC2 instances to use IAM roles

# Uses an environment variable to get the name of the target S3 bucket
BUCKET_NAME = os.environ.get("BUCKET_NAME")

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return app.send_static_file('upload-form.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['myfile']
    name = uploaded_file.filename
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).put_object(Key=name, Body=uploaded_file)
    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
    # needs to run on 0.0.0.0 for docker to be reachable outside container
    # see this explanation for why localhost won't work here
    # https://pythonspeed.com/articles/docker-connection-refused/
    app.run(debug=True, port=3000, host='0.0.0.0')