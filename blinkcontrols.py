from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.api import *
from tkinter import *
from pathlib import Path
from aiohttp import ClientSession
from BCconfig import * # aware of the bad code practice, will fix later.
import tkinter
import os
import requests
import asyncio

screen = tkinter.Tk()

async def start():
    blink = Blink(session=ClientSession())
    auth = Auth({"username": BCconfig.email, "password": BCconfig.password}, no_prompt=True)
    blink.auth = auth
    await blink.start()
    return blink
blink = asyncio.run(start())

# await auth.send_auth_key(blink, BCconfig.key) or change to login prompt
# await blink.setup_post_verify()

# When initialized, print some useful information.
for name, camera in blink.cameras.items():
  print(name + ' loaded.')       
  camerastats = camera.attributes     
  print(camera.attributes)     
  print(camera.get_sensor_info())


# Arms the camera by enabling motion alerts.
# Note: You can disable motion controls for individual cameras.
async def armCamera():
    await blink.sync[BCconfig.syncmodule].async_arm(True)
    await blink.refresh()

# Disarms the camera by disabling motion alerts.
# Note: You can disable motion controls for individual cameras.
async def disarmCamera():
    await blink.sync[BCconfig.syncmodule].async_arm(False)
    await blink.refresh()
    
    
# Downloads all videos from the past week days of this app being created.
# You can customize the delay, and since parameters.
async def downloadAllVideos():
    if os.path.isdir(BCconfig.downloaddirectory):
        print("Directory exists, now downloading files.")
        await blink.download_videos('BCconfig.downloaddirectory', since='BCconfig.downloaddate', delay=BCconfig.downloaddelay)
    else:
            print(f"The directory specified in BCconfig.py does not exist, now creating")
            os.mkdir(BCConfig.downloaddirectory)
            blink.download_videos('BCconfig.downloaddirectory', since='BCconfig.downloaddate', delay=BCconfig.downloaddelay)
   
    messagebox.showinfo("Videos have been downloaded successfully.")


# Updates the picture that shows up when you open the app.
async def takePicture():
    camera = blink.cameras[BCconfig.cameramodule]
    await camera.snap_picture()
    await blink.refresh(force=True)


# Initalize and pack UI elements here.
top.title("Blink Controls")

screen.configure(bg=BCconfig.backgroundcolor) 
screen.mainloop()

#def downloadLatest():
 #   camera = blink.cameras[BCconfig.cameramodule]
 #  await camera.get_thumbnail()
 # await camera.image_from_cache.raw