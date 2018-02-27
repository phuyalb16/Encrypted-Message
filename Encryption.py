'''
Created by Basanta Phuyal
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = int(input("What is your encryption key? (1-9) "))                             #key that aids with encryption
user_input= input("Message: ")       #stores user's message
mail_input= input("Gmail: ")         #stores user's gmail address
password_input= input("Password:")   #stores user's gmail password
to_input= input("Email to send to: ")
message=''
user_message= user_input.lower()

'''for loop where the encryption takes place'''
for letter in user_message:
    if letter in alphabet:
        position= alphabet.find(letter)
        new_position = (position+key) % 26
        new_character = alphabet[new_position]
        message += new_character
    else:
        message += letter
encrypted_message = message  #final encrypted message

