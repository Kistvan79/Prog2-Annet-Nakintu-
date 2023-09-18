#Krav för musik projectet
#Den ska kunna: Pausa, Starta, Skipa, Skipa tillbaka, Spola fram & tillbaka 10sec.
#Kunna lägga till music I en enorm library och fortsätta låter utifrån lista.

from pydub import AudioSegment
from pydub.playback import play

from pytube import YouTube
import os

def download_music():
    # url input from user
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")

song = AudioSegment.from_file('C:/Users/Elev/Music')

play(song)