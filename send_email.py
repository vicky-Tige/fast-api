import mailtrap

token="3b95059dc7b5602140a61c06f90cfe1a"

def email(to,subject,message):
    mail=mailtrap.Mail(
        sender=mailtrap.Address(email="hello@demomailtrap.co",name="FLASK_API"),
        to=[mailtrap.Address(email=to)],
        subject=subject,
        text=message,
        category="mailtrap intergration test"
    )


    client=mailtrap.MailtrapClient(token=token)
    response=client.send(mail)
    print("this is mailtrap---------")
    print(response)
