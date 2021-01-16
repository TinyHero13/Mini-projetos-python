import PySimpleGUI as sg
from pytube import YouTube as yt

sg.theme("LightBrown7")
layout = [
            [sg.Text("Enter the link of the video that you want to download!")],
            [sg.Input()],
            [sg.Text("Wait until the video is downloaded!",size=(40,1),key="resp")],
            [sg.Button('Ok'), sg.Button('Quit')]
          ]

window = sg.Window("YouTube Video Downloader", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    yt(values[0]).streams.first().download()
    window["resp"].update("Done!")

window.close()