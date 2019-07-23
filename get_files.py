from PIL import Image
import requests
from io import BytesIO
import os

response = requests.get("https://art.hearthstonejson.com/v1/256x/EX1_001.jpg")
img = Image.open(BytesIO(response.content))

img.save("test.jpg")