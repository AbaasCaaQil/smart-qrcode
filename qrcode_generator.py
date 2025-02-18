import qrcode
import os

def create_file():
    while True:
        try:
            file_path = input("Enter the file name: ")

            # Get data input
            file_data = input("Enter the data to store: ")

            # Write to file (create if doesn't exist, overwrite if it does)
            with open(file_path, 'w') as file:
                file.write(file_data)

            # Default file name if user doesn't enter one
            file_name = input("Enter the QR code file name (with .jpg or .png): ")
            if not file_name:
                file_name = "qrcode.jpg"

            # Create QR code
            qr = qrcode.QRCode(
                version=1,  # Small QR code version
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(file_data)
            qr.make(fit=True)
            image = qr.make_image(fill="black", back_color="white")
            image.save(file_name)

            print(f"QR code created successfully as {file_name}")

        except Exception as e:
            print(f"Error: {e}")

        # Ask user if they want to continue
        try_again = input("Do you want to create another QR code? (Y/n): ").strip().lower()
        if try_again != "y":
            break

create_file()