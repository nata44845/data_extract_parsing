# import requests
#
url = "https://cdn1.ozone.ru/s3/multimedia-g/6100657600.jpg"
#
# response = requests.get(url)
# with open('owl.jpg', 'wb') as file:
#     file.write(response.content)


import wget
wget.download(url)


