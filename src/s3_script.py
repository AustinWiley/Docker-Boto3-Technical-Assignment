import boto3

# Use Amazon S3, this also looks in `~.aws/credentials` for my access keys on my local client for use by the app. 
s3 = boto3.resource('s3')

# Bucket name that contains the files we will copy from
src_bucket_name=input('Enter first: ')
# Bucket name that we will copy files into
dest_bucket_name=input('Enter second: ')
# Threshld size im MB
file_size=float(input('Enter mb size: '))*1000000

#Check each file size in bucket one and and if it is above threshhold copy to file second bucket

#Use boto SDK to perform transfer