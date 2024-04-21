def show_buckets(s3_obj):
    try:
        for bucket in s3_obj.buckets.all():
            print(bucket.name)
    except Exception as e:
        print("Following Error has occured While Connecting to aws")
        print(e)

def upload_file(s3_obj, bucket_name, file_path, key):
    try:
        file = open(file_path, 'rb')
        s3_obj.Bucket(bucket_name).put_object(Key=key, Body=file)
        file.close()
        print('File Uploaded Successfully')
    except Exception as e:
        print("Following Error has occured While Uploading the File")
        print(e)

def list_files(s3_obj, bucket_name):
    try:
        for object in s3_obj.Bucket(bucket_name).objects.all():
            print(object.key)
    except Exception as e:
        print("Following Error has occured while listing the files")
        print(e)

def create_bucket(s3_obj, bucket_name, region):
    try:
        s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={
            'LocationConstraint': region
        })
        print(f'{bucket_name} Bucket created successfully in {region} region')
    except Exception as e:
        print("Following Error has occured while creating the bucket")
        print(e)


