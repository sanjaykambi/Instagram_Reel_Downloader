import http.client
import json
import requests
from io import BytesIO
from PIL import Image, ImageTk

conn = http.client.HTTPSConnection("instagram-bulk-scraper-latest.p.rapidapi.com")

# Get the Instagram reel link from user input
reel_link = input("Enter the Instagram reel link: ")
payload = f"{{\r\n    \"url\": \"{reel_link}\"\r\n}}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "dc8644b4f3msh447042b639dd52dp1377bcjsn803154187884",
    'X-RapidAPI-Host': "instagram-bulk-scraper-latest.p.rapidapi.com"
}

conn.request("POST", "/media_download_from_url", payload, headers)

res = conn.getresponse()
data = res.read()

response_json = json.loads(data.decode("utf-8"))
video_url = response_json["data"]["main_media_hd"]
print("Video URL:", video_url)

# Download and display the video using requests and PIL
response = requests.get(video_url)
if response.status_code == 200:
    video_bytes = response.content
    video_file = "downloaded_video.mp4"
    with open(video_file, "wb") as f:
        f.write(video_bytes)
    print("Video downloaded and saved as:", video_file)
else:
    print("Failed to download video.")
