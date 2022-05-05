import boto3
from datetime import datetime, date

def lambda_handler(event, context):
    src_bucket = '<your source bucket>'
    dst_bucket = '<your source bucket>'
    backup_folder_name = 'backup_' + datetime.now().strftime("%H-%M-%S-") + date.today().strftime("-%d-%m-%Y")

    s3 = boto3.client('s3')
    s3_copy = boto3.resource('s3')

    src_obj_list = s3.list_objects_v2(Bucket=str(src_bucket))

    for src_key in src_obj_list['Contents']:
        copy_source = {'Bucket': src_bucket, 'Key': src_key['Key']}

        dst_key = backup_folder_name + "/" + src_key['Key']
        s3_copy.meta.client.copy(copy_source, dst_bucket, dst_key)
        print(dst_key)
