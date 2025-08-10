import requests
import urllib.parse

BASE_URL = "http://127.0.0.1:8080"

def upload_image(file_path):
    url = f"{BASE_URL}/upload"
    with open(file_path, "rb") as img:
        files = {"image": img}
        response = requests.post(url, files=files)
    print("POST /upload:", response.status_code, response.json())
    return response.json().get("image_url")

def get_image_url(filename):
    encoded_filename = urllib.parse.quote(filename)
    url = f"{BASE_URL}/image/{encoded_filename}"
    headers = {"Content-Type": "text"}
    response = requests.get(url, headers=headers)
    print("GET /image:", response.status_code, response.json())
    return response.json().get("image_url")

def delete_image(filename):
    encoded_filename = urllib.parse.quote(filename)
    url = f"{BASE_URL}/delete/{encoded_filename}"
    response = requests.delete(url)
    print("DELETE /delete:", response.status_code, response.json())

if __name__ == "__main__":
    uploaded_url = upload_image("example.jpg")
    if not uploaded_url:
        print("Помилка завантаження!")
        exit()

    filename = uploaded_url.split("/")[-1]

    get_image_url(filename)

    delete_image(filename)
