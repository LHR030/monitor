import requests
import base64
import cv2 as cv


# opencv 图片
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"

    # 编码图像并转换为字符串
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}

    # 更新access_token
    access_token = '24.4514e24a35ea4582b85e3c5c0c048a17.2592000.1722480572.282335-89935393'
    request_url = f"{request_url}?access_token={access_token}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.post(request_url, data=params, headers=headers)
        response.raise_for_status()  # 抛出HTTP错误
        num = 0

        if response.ok:
            try:
                data = response.json()
                if 'vehicle_num' in data:
                    for item in data['vehicle_num']:
                        num += data['vehicle_num'][item]

                if 'vehicle_info' in data:
                    for item in data['vehicle_info']:
                        location = item.get('location', {})
                        x1 = location.get('left', 0)
                        y1 = location.get('top', 0)
                        x2 = x1 + location.get('width', 0)
                        y2 = y1 + location.get('height', 0)
                        cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

                        # 定义要绘制的文字
                        text = item.get('type', '')
                        position = (x1, y1 - 2)
                        font = cv.FONT_HERSHEY_SIMPLEX
                        font_scale = 1
                        color = (0, 0, 255)  # 红色
                        thickness = 1
                        img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
            except Exception as e:
                print(f"Error processing response data: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

    return img, num
