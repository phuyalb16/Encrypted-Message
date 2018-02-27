from Encryption import *
import smtplib

'''
Run this file to send encrypted message to the recipient 
'''
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(mail_input, password_input)
mail.sendmail(mail_input, to_input, encrypted_message)
mail.close()
