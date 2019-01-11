import  boto3, os, glob
from botocore.client import Config
i=0
def upload():                   # uploading the data to AWS
    global i
    ACCESS_KEY_ID = '****'
    ACCESS_SECRET_KEY = '*****'
    BUCKET_NAME = '****'
    s3C = boto3.client('s3',aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
        )


    for root,dirs,files in os.walk('/mnt/usbdrive/odolift/data'):
        for file in files:
            s3C.upload_file(os.path.join(root,file),BUCKET_NAME,file)
    print ("data uploaded to AWS")
    files = glob.glob('/mnt/usbdrive/odolift/data/*')
    for f in files:
        os.remove(f)
    print ("data removed")
upload()
