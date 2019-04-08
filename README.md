# Docker-Boto3-Technical-Assignment


### Overview

This app is a Containerized with Docker. The container will take the names of two S3 buckets in a single region (e.g. us-east-1) and a threshold size in MB.  Arguments that will be passed on to the Python application that can copy all files greater than the threshold size from one bucket to another.

## Docker Image

* Click the link to get an Image of the app from dockerhub. [Docker-Image](https://hub.docker.com/u/awiley)
* Or enter this in commandline: `docker pull awiley/technical-assignment`
##

### Instructions on how to containerize image with docker

1. Copy the `technical-assignment` image to your computer.
2. Open a docker teminal (im using Docker toolbox) and enter the following in the terminal:

   * Replace keys with your own

   * This command will create and run a Docker container and add your access keys to the environment varaibles inside of the container session.

```
docker run -e AWS_ACCESS_KEY_ID=xyz -e AWS_SECRET_ACCESS_KEY=aaa -it awiley/technical-assignment
```


3. Once the Container is runing is will prompt for three arguments:

   * `Enter source bucket name: `

   * `Enter destination bucket name: `

   * `Enter threshold size in MB: `

   * Once the app runs it will tell you how many files were transfered and the container will stop running.
