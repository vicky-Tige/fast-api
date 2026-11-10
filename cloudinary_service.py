import cloudinary
import cloudinary.uploader
from send_email import email
Cloud_name='e23erfxz'
Api_key='698831731941554'
Secret_key='vbGhialZ_Lg3xBuxqavq70g1Np4'
# connecting to cloudinary
cloudinary.config(
    cloud_name=Cloud_name,
    api_key=Api_key,
    api_secret=Secret_key
)
def upload_pdf(pdf_file):
    try:
        file_path=f'receipts/{pdf_file}.pdf'
        # upload pdf
        upload= cloudinary.uploader.upload(file_path,resource_type='raw')
        
        receipt_url=upload['secure_url']

        print(receipt_url)
        #send email.
        email("tigevictoria2008@gmail.com","Payment Received",f"Thankyou we have received your payments.\n\n" f"Receipt:{receipt_url}")
        print("Successfull file upload")
        return 'success'
    except Exception as e:
        print(f'upload failed: {e}')
        return 'failed'