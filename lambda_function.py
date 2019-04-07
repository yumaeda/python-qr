import os
import json
import urllib.request
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendors'))
from MyQR import myqr

def lambda_handler(event, context):
    S3_ROOT  = 'https://s3.amazonaws.com'
    S3_DIR   = 'qrcode'
    SRC_FILE = 'src.jpg'
    OUT_FILE = 'output_{}.gif'.format(int(round(time.time() * 1000)))
    OUT_DIR  = '/tmp'
    BUCKET   = 'yumaeda'

    # Get parameters
    img  = event['img']
    text = event['text']

    # Download and save the image as /tmp/src.jpg
    filename = '{}/{}'.format(OUT_DIR, SRC_FILE)
    urllib.request.urlretrieve(img, filename)

    try:
        version, level, qr_name = myqr.run(
            text,
            version = 10,
            level = 'M',
            picture = filename,
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
            '{0}/{1}'.format(S3_DIR, OUT_FILE)
        )

        # Set public-read ACL
        s3.ObjectAcl(
            BUCKET, 
            '{0}/{1}'.format(S3_DIR, OUT_FILE)
        ).put(ACL='public-read')
    except:
        import traceback
        traceback.print_exc()

    return {
        'statusCode': 200,
        'img': json.dumps(
            '{0}/{1}/{2}/{3}'.format(
                S3_ROOT, BUCKET, S3_DIR, OUT_FILE
            )
        ),
        'text': json.dumps(text)
    }
