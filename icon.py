import pystray

from PIL import Image
from pystray import MenuItem as item

def on_quit():
    icon.visible = False
    icon.stop()

image = Image.open("D:\[res]\RAE_16x16.jpg")

menu = (
    item('MenuItem0', None),
    item('MenuItem1', None),
    item('Quit', on_quit)
)

icon = pystray.Icon("name", image, "title", menu)
icon.run()