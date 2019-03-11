import os
import json
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendors'))
from MyQR import myqr

def lambda_handler(event, context):
    OUT_FILE = 'target.gif'
    OUT_DIR = '/tmp'
    BUCKET = 'yumaeda'

    text = 'https://github.com/yumaeda/python-qr'
    if 'text' in event:
        text = event['text']

    img = 'src.jpg'
    if 'img' in event:
        img = event['img']

    try:
        version, level, qr_name = myqr.run(
            text,
            version = 10,
            level = 'H',
            picture = img,
            colorized = True,
            contrast = 1.0,
            brightness = 1.0,
            save_name = OUT_FILE,
            save_dir = OUT_DIR
        )

        import boto3
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
        'img': json.dumps(img),
        'text': json.dumps(text)
    }
