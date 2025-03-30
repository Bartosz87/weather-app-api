import smtplib, ssl


def send_email(message=""):
    global host, port, username, password, context
    host = "smtp.gmail.com"
    port = 465
    username = "zielu13op@gmail.com"
    password = "bbty gnvf ukly etqu"
    receiver = "zielu13op@gmail.com"
    context = ssl.create_default_context()
    # message = '''\
    # Subject: test email
    # Hello, this is testing email
    #
    # '''
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



