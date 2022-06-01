from tkinter import Scale 
from tkinter import Tk
import pyqrcode 
import io 
from datetime import datetime
import time

now = datetime.now()

current_time = now.strftime("%H Uhr %M Minuten")


link = Tk().clipboard_get()


url = pyqrcode.create(link)

url.svg("QR.Code" + current_time + ".svg", scale=4)
buffer = io.BytesIO()
url.svg(buffer) 
time.sleep(1)
print("Fertig!")
