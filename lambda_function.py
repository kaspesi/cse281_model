import base64
import cv2
import numpy as np
import base64
from cgi import parse_multipart, parse_header
from io import BytesIO

# grab environment variables
#ENDPOINT_NAME = "knn-ml-t2-medium-1605500056-360014"
ENDPOINT_NAME = "knn-ml-t2-medium-1605503932-9556243"
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

c_type, c_data = parse_header(event['headers']['Content-Type'])
    assert c_type == 'multipart/form-data'
    decoded_string = base64.b64decode(event['body'])
    form_data = parse_multipart(BytesIO(decoded_string), c_data)

    files = []
    print("ATTEMPTING TO GET FILE")
for image_str in form_data['image']:
print(type(image_str))
imgdata = base64.b64decode(image_str)
#image = np.asarray(bytearray(imgdata), dtype="uint8")
image = np.asarray(bytearray(image_str), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
pixels = cv2.resize(image, (32,32)).flatten()
        
datalist = pixels.tolist()
        payload = ','.join(map(str, datalist)) 
        response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                ContentType='text/csv', 
                Body=payload)
        result = json.loads(response['Body'].read())
        return {'statusCode': 200,
                'body': json.dumps(result),
                'isBase64Encoded': False}
    return {'statusCode': 200,'body': '','isBase64Encoded': False}