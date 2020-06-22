import youtube_dl
from subprocess import call

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ydl_opts1 = {}

title = """                 
#(______)                  
#_     _ ___  _ _ _ ____  
# |   | / _ \| | | |  _ \ 
# |__/ / |_| | | | | | | |
#_____/ \___/ \___/|_| |_|
by Void Light
                                                 """

if __name__ == "__main__":

	print(title)

	select = input("Select audio(1) or video(2)")

	if select == "1":
		url = input("bitte hier den youtube Link: ")
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		print("done.")


	if select == "2":
		url = input("bitte hier den youtube Link: ")
		with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
			ydl.download([url])
		print("done.")
