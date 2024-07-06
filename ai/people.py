import numpy as np
import requests
import base64
import cv2 as cv

def people_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"

    # 编码图像并转换为字符串
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image, "show": "true"}


    access_token = '24.aec927fd26cf453e1f15cac3bb4993d5.2592000.1722762504.282335-91012202'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'
               }

    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        print(response.json())
        img = data['image']
        img = base64.b64decode(img)
        img = np.frombuffer(img, np.uint8)
        img = cv.imdecode(img, cv.IMREAD_COLOR)
        num = data['person_num']
        return img, num