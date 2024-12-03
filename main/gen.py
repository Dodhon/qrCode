import requests
import os

def generate_qr_code(link, name):
    endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={link}"
    directory = os.getcwd()
    folder = f"{directory}/qr_codes"

    if not os.path.exists(folder):
        os.makedirs(folder)


    image_path = os.path.join(folder, f"{name}_qr_code.png")
    response = requests.get(endpoint)
    with open(image_path, 'wb') as f:
        f.write(response.content)