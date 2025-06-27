import qrcode

# taking UPI ID as a Input
upi_id=input("enter your UPI ID= ")


# PAYMENT FORMAT
# upi://pay?pa=UPI_id&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# pa=payment id,pn=receipt name,am=amount,cu=indian currency(INR)and other country currency,tn=message box(after payment such as thanks)

# Defining the payment URL based on the UPI ID and the payment app
# You can modify these urls bassed on the payment apps you want to support

# mc=merchant code
phonepe_url=f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mmc=1234' 
paytm_url=f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mmc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mmc=1234'  

# create QR code for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

# Save the QR code to image file(opti0nal) 
# phonepe_qr.save('phonepay_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

# Display the Qr code(you may need to install pil/pilow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()