# Enkel email, kun tekst ikke emne
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ksdraege@gmail.com','passord')
melding = 'Test av email sendt fra ett Python program.'
server.sendmail('ksdraege@gmail.com','ksdraege@gmail.com',melding)
server.quit()