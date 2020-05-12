import qrcode

qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data('file://C:/Users/regen/OneDrive/%E6%96%87%E4%BB%B6/0512/000211012.html')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

img_qr_big.save('000211012.png')
