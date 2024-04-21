import boto3
from aws_wrapper import show_buckets, upload_file, list_files
s3_obj = boto3.resource('s3')

file_path = "test.txt"

# list_files(s3_obj, bucket_name='python-wrapper-bucket-om')
# upload_file(s3_obj,'python-wrapper-bucket-om',file_path,'test.txt')
# show_buckets(s3_obj)