# Connecting to AWS S3 Through Boto3 From Flask in Docker Container
Demo application for uploading files to S3 from a web form.

## Prerequisites
Have an AWS IAM use that has S3 permissions and an Access Key (See the docs [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))

Have an S3 Bucket to add objects to. (See the docs for creating S3 buckets [here](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html))

Have Docker installed on your machine (See the docs [here](https://docs.docker.com/v17.09/engine/installation/))

## Environment Variables
The docker container that you will be creating, along with the Flask server itself, will be using environment variables.

Change the name of `.env-sample` to `.env` and update the values there to match your environment.

## Running
From within the project root directory, run `docker-compose up --build` to run the setup.

After the container starts, you will be prompted that you can access the page at [http://0.0.0.0/3000/](http://0.0.0.0/3000/)