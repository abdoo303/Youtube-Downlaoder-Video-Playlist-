from pytube import YouTube,Playlist
def code(link):

    #res= input('enter the resolution:  \n')
    save_path=r"D:\videos_py"
    #YouTube(link).streams.filter(resolution=None).first().download(save_path)
    YouTube(link).streams.get_highest_resolution().download(save_path)

def playlist(link):

    playlist = Playlist(link)
    for v in playlist.videos:
        code(v.watch_url)
i = int(input("one video -> (0) or a playlist -> (1)"))
link= input('enter the link')
if i==0:
    code(link)
else:
    playlist(link)

