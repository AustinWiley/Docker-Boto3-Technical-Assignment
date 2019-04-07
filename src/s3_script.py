import boto3

# Use Amazon S3, this also looks in `~.aws/credentials` for my access keys on my local client for use by the app.
s3 = boto3.resource('s3')

# Bucket name that contains the files we will copy from
src_bucket_name = input('Enter first: ')
# Bucket name that we will copy files into
dest_bucket_name = input('Enter second: ')
# Threshld size im MB
file_size = float(input('Enter mb size: '))*1000000

# Declare variable for number of files copied
copied_files = 0

# Check each file size in bucket one and if it is above file_size threshhold then copy to second bucket
src_bucket = s3.Bucket(src_bucket_name)
# src_bucket = s3.Bucket('wiley-test-one')
for stuff in src_bucket.objects.all():
    # print(stuff.key)
    # print(stuff.size)
    if stuff.size > file_size:
        print(stuff.key)
        # increment for every file that is abouve threshold
        copied_files += 1
        s3.meta.client.copy_object(
            Bucket=dest_bucket_name,
            CopySource={'Bucket': src_bucket_name, 'Key': stuff.key},
            Key=stuff.key
        )

# print number of files copied
print('Files copied: ' + str(copied_files))