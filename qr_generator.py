import qrcode
from io import BytesIO

def generate_qr_code(user_email: str, event_id: str):
    # Combine user_email and event_id into one string
    data = f"{user_email}_{event_id}"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")

    # Save QR code in memory using BytesIO (avoiding file IO)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    return img_byte_arr

# Test the function
user_email = "user@example.com"
event_id = "event123"
qr_image = generate_qr_code(user_email, event_id)

# The generated image is in memory, you can use it directly or save it to a file
with open("generated_qr.png", "wb") as f:
    f.write(qr_image.read())
