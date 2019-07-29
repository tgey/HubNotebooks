import requests
import pyunsplash
from PIL import Image

class UnsplashClient:
    def __init__(self, access_key):
        self.pu = pyunsplash.PyUnsplash(api_key=access_key)

    @staticmethod
    def get_image_resolution(image_path: str) -> int:
        size = Image.open(image_path).size
        width, height = size
        return width*height, size

    def download_images(self, query, count, path):
        photos = self.pu.photos(type_='random', count=count, query=query)
        for photo in photos.entries:
            print(photo.id, photo.link_download)
            img_data = requests.get(photo.link_download).content
            img_path = path + 'image_{}_{}.jpg'.format(query, photo.id)
            with open(img_path, 'wb') as handler:
                handler.write(img_data)
                img_pixels, img_size = self.get_image_resolution(img_path)
                print(img_size, img_pixels)

access_key = '6bae78ecb263777ab1adbd762c01dcc5f03dcf7074f47987f0a077be8c9fb668'
UnsplashClient(access_key).download_images("Simpson", 4, 'data/')