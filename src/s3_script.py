import boto3

# Use Amazon S3, this also looks in `~.aws/credentials` for my access keys on my local client for use by the app.
s3 = boto3.resource('s3')

# Below script prints out the bucket names in aws s3 account associated with keys.  will leave it commented out for later use:
# for bucket in s3.buckets.all():
#     print(bucket.name)

print('Copy all files greater than the threshold size from one bucket to another.\n')
# Bucket name that contains the files we will copy from
src_bucket_name = input('Enter source bucket name: ')
# Bucket name that we will copy files into
dest_bucket_name = input('Enter destination bucket name: ')
# Threshld size im MB
file_size = float(input('Enter threshold size in MB: '))*1000000

# Declare variable for number of files copied
copied_files = 0

# Check each file size in bucket one and if it is above file_size threshhold then copy to second bucket
src_bucket = s3.Bucket(src_bucket_name)
# Loop through items in source bucket
for item in src_bucket.objects.all():
    if item.size > file_size:
        # increment for every file that is above threshold
        copied_files += 1
        s3.meta.client.copy_object(
            Bucket=dest_bucket_name,
            CopySource={'Bucket': src_bucket_name, 'Key': item.key},
            Key=item.key
        )

# print number of files copied
print('\nFiles copied: ' + str(copied_files))