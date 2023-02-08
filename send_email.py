import os
import smtplib


def send_email(message):
    username = os.getenv("PYDEVEMAILUSERNAME")
    password = os.getenv("PYDEVEMAILPASSWORD")

    receiver = username

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=username, password=password)
        server.sendmail(
            from_addr=username,
            to_addrs=receiver,
            msg=message.format(username, receiver, message).encode("utf-8")
        )
