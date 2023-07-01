import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

payload = {"image_url": "http://telegra.ph//file/54a16ae112d8d8694cdee.jpg"}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "b541373892mshfe4e4241dcb3fe8p15dd47jsn9c9683a22e78",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# payload = {"image_url": "http://telegra.ph//file/54a16ae112d8d8694cdee.jpg"}
async def remove_background(img_url):
    payload = {"image_url": f"{img_url}"}
    response = requests.post(url, data=payload, headers=headers)
    logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']


