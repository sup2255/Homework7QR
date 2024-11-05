import qrcode

# URL to your GitHub profile
url = 'https://github.com/sup2255'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")
img.save('github_qr.png')

print("QR code generated successfully!")
