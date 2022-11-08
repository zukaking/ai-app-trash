import decode_img
import boto3
import logging
import sys
import base64
import json
from PIL import Image
from io import BytesIO

#s3にデータアップロードsagemakerをcallする関数(mikada)
def callsm(img_base64):
    data = img_base64.split(b'base64,')[1]
    data = base64.b64decode(data)
    image = Image.open(BytesIO(data))
    image.save('upImage.jpg')

    client = boto3.client('runtime.sagemaker', 'ap-northeast-1')
    res = client.invoke_endpoint(EndpointName='jumpstart-dft-tf-ic-imagenet-mobilenet-v2-100-224-clas', ContentType='application/x-image',Body=data, Accept='application/json;verbose')
    model_predictions = json.loads(res['Body'].read())
    predicted_label = model_predictions['predicted_label']
    labels = model_predictions['labels']
    probabilities = model_predictions['probabilities']
    output = {
            #"predicted_label" : predicted_label[0:5],
            "labels" : model_predictions["labels"][0:5],
            "probabilities" : model_predictions["probabilities"][0:5]
            }
    print(output)
    return  output