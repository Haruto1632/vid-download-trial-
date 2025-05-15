import yt_dlp

url = input("Enter the video URL: ")

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Save as video title
    'format': 'bestvideo+bestaudio/best',  # Highest quality
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("✅ Download complete!")
except Exception as e:
    print("❌ Error:", e)