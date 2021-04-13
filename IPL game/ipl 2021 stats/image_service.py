'''captcha '''
import boto3


def process_image(filename):
    '''process_image'''
    client = boto3.client('rekognition', aws_access_key_id="AKIAJGSQORKEZFXZX3RA",
                          aws_secret_access_key="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",
                          region_name='us-east-1')

    with open(filename, 'rb') as image_file:
        img = image_file.read()
        response = client.detect_text(Image={'Bytes': img})

    return response
