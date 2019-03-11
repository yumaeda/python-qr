import boto3
import os
import json
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendors'))
from MyQR import myqr

def lambda_handler(event, context):
    url = 'https://github.com/yumaeda/python-qr'
    srcImg = 'src.jpg'
    OUT_FILE = 'target.gif'
    OUT_DIR = '/tmp'
    BUCKET = 'yumaeda'

    try:
        version, level, qr_name = myqr.run(
            url,
            version = 10,
            level = 'H',
            picture = srcImg,
            colorized = True,
            contrast = 1.0,
            brightness = 1.0,
            save_name = OUT_FILE,
            save_dir = OUT_DIR
        )

        s3 = boto3.resource('s3')
        bucket = s3.Bucket(BUCKET)
        bucket.upload_file(
            '{0}/{1}'.format(OUT_DIR, OUT_FILE),
            'qrcode/{}'.format(OUT_FILE)
        )
    except:
        import traceback
        traceback.print_exc()

    return {
        'statusCode': 200,
        'body': json.dumps('SUCCESS')
    }
