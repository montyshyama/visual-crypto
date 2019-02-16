from PIL import Image, ImageDraw, ImageFont
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
image = Image.open('images/background.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size = 75)
(x, y) = (200, 100)
#(x, y) = (50, 50)
color = 'rgb(0, 0, 0)'
print("[+]Enter username:")
message = raw_input()
draw.text((x, y), message, fill = color, font = font)
image.save('images/image.png')