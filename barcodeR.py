from pyzbar.pyzbar import decode
from PIL import Image
d=decode(Image.open("2.png"))
print(d[0].data.decode())
