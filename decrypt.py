import cv2
import sys
from PIL import Image
import PIL.ImageOps
from pytesseract import image_to_string

sys.path.append('/usr/local/lib/python2.7/site-packages')
img1 = cv2.imread('/home/monty/Desktop/visual_crypto/share_1.png', 1)  
img2 = cv2.imread('/home/monty/Desktop/visual_crypto/share_2.png', 1)
img = cv2.add(img1, img2) 
final = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('results/decrypted_image.png', final)
dst = cv2.GaussianBlur(final, (5,5), cv2.BORDER_DEFAULT)
cv2.imwrite('results/decrypted_gassuian.png', dst)
ret3,th3 = cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('results/decrypted_otsu.png', th3)
image = Image.open('results/decrypted_otsu.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('results/inverted.png')

print (image_to_string(Image.open('/home/monty/Desktop/visual_crypto/results/inverted.png')))



  