import pyqrcode
import png
from pyqrcode import QRCode


s = "Hello My Name Is Siddhesh......."
  
url = pyqrcode.create(s)

url.png('myqr.png', scale = 6)
