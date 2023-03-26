from pytube import YouTube

link = input("Enter a youtube video's URL") # i.e. https://youtu.be/dQw4w9WgXcQ


yt = YouTube(link)
# video = YouTube('mylink')
highresvid = yt.streams.get_highest_resolution()
highresvid.download()
# print(yt.streams)
# # filter(res="1080p").first().download()

print("downloaded", link)