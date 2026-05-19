import qrcode as qr
img= qr.make("Hello world","Upload link")
img.save("qrcode.png")
