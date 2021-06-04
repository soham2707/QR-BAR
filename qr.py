import qrcode
print("enter the name you want to convert in QR bar: ")
data=input()

qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='white')
s=input("enter your file name")
img.save('D:/PYTHON PROJECTS/QR code/sample/'+s+'.jpg')
