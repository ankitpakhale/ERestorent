import qrcode
import qrcode.image.svg
img = qrcode.make('http://www.ankitpakhale.netlify.app/', image_factory=qrcode.image.svg.SvgImage)
with open('qr.svg', 'wb') as qr:
    img.save(qr)