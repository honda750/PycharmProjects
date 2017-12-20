"""
    SEND EMAIL
    Med emne og innhold
"""
def send_email(emne, innhold, til_addr):            # Sender en email.
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fra_addr = 'ksdraege@gmail.com'
    passord = 'passord'  # mcxx
    msg = MIMEMultipart()
    msg['From'] = fra_addr
    msg['To'] = til_addr
    msg['Subject'] = emne
    msg.attach(MIMEText(innhold, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    text = msg.as_string()
    server.login(fra_addr,passord)
    text = msg.as_string()
    server.sendmail(fra_addr,til_addr,text)
    server.quit()

emne = 'Test5!'
tekst = '-' #('Denne email er sendt fra fra ett python program.')
til = 'ksdraege@gmail.com'
send_email(emne,tekst,til)