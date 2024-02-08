from blinkpy.blinkpy import Blink
from tkinter import *
from blinkpy.api import *
from BCconfig import * # aware of the bad code practice, will fix later.
import tkinter

# Change 'NAME OF SYNC DEVICE' and 'NAME OF CAMERA' with your camera and sync devices, respectively. Learn more in the README.
blink = Blink()
blink.start()
screen = tkinter.Tk()


# When initialized, print some useful information.
for name, camera in blink.cameras.items():
  print(name + ' loaded.')       
  camerastats = camera.attributes     
  print(camera.attributes)     
  print(camera.get_sensor_info())


# Arms the camera by enabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def armCamera():
    blink.sync["NAME OF SYNC DEVICE"].arm = True
    blink.refresh()

# Disarms the camera by disabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def disarmCamera():
    blink.sync["NAME OF SYNC DEVICE"].arm = False
    blink.refresh()
    
    
# Downloads all videos from the past week days of this app being created.
# You can customize the delay, and since parameters.
def downloadAllVideos():
    # blink.download_videos('/home/blink', since='2023/01/01 12:00', delay=4)
    messagebox.showinfo("Videos have been downloaded successfully.")

# Initalize and pack UI elements here.
top.title("Blink Controls")

screen.configure(bg='white') 
screen.mainloop()
