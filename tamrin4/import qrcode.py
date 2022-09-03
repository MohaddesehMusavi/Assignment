import qrcode 

email_account = (input("Enter your email account : \n "))
qr = qrcode.make(email_account)
qr.save('qrcode.jpg')
