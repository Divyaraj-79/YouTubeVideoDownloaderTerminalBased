from pytube import YouTube

# Enter the YouTube video URL
url = input("Enter the URL of YouTube Video: ")

# Create a YouTube object and get the highest resolution video stream
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()

# Download the video
print(f"Downloading {yt.title} in {stream.resolution}...")
stream.download()
print("Download complete!")