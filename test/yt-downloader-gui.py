import PySimpleGUI as sg
from pytube import YouTube as yt

sg.theme("LightBrown7")
layout = [
            [sg.Text("Enter the link of the video you want to download!")],
            [sg.Input()],
            [sg.Text("Wait until the video is downloaded!",size=(40,1),key="resp")],
            [sg.Button('Video'), sg.Button('Audio'), sg.Button('Quit')]
          ]

window = sg.Window("YouTube Video Downloader", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == "Video":
        yt(values[0]).streams.first().download()

    else: 
        yt(values[0]).streams.filter(only_audio=True).first().download()
        
    window["resp"].update("Done!")
window.close()