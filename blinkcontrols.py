from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.api import *
from tkinter import *
from BCconfig import * # aware of the bad code practice, will fix later.
import tkinter
import requests

blink = Blink()
blink.auth = Auth()
screen = tkinter.Tk()

headers = {
    'Content-Type': 'application/json',
}
json_data = {
    'unique_id': '00000000-0000-0000-0000-000000000000',
    'password': BCconfig.password,
    'email': BCconfig.email,
}
response = requests.post('https://rest-prod.immedia-semi.com/api/v5/account/login', headers=headers, json=json_data)
print(response)

blink.start()

# When initialized, print some useful information.
for name, camera in blink.cameras.items():
  print(name + ' loaded.')       
  camerastats = camera.attributes     
  print(camera.attributes)     
  print(camera.get_sensor_info())


# Arms the camera by enabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def armCamera():
    blink.sync[BCconfig.syncmodule].arm = True
    blink.refresh()

# Disarms the camera by disabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def disarmCamera():
    blink.sync[BCconfig.syncmodule].arm = False
    blink.refresh()
    
    
# Downloads all videos from the past week days of this app being created.
# You can customize the delay, and since parameters.
def downloadAllVideos():
    # blink.download_videos('BCconfig.downloaddirectory', since='BCconfig.downloaddate', delay=BCconfig.downloaddelay)
    messagebox.showinfo("Videos have been downloaded successfully.")


# Updates the picture that shows up when you open the app.
def takePicture():
    camera = blink.cameras[BCconfig.cameramodule]
    camera.snap_picture()
    blink.refresh(force=True)

# uhh i forgot?
def downloadLatest():
    camera = blink.cameras[BCconfig.cameramodule]
    camera.get_thumbnail()
    camera.image_from_cache.raw


# Initalize and pack UI elements here.
top.title("Blink Controls")

screen.configure(bg=BCconfig.backgroundcolor) 
screen.mainloop()
