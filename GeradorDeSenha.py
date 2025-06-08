# Criando um gerador de senha

import string
import random

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
resposta = ""

while resposta not in ["s", "n"]: 
    resposta = input("Do you want a secure password? (s/n): ").lower().strip()
    if resposta not in ["s", "n"]:
        print("Just 's' or 'n'")

if resposta == "s":
    print("Generating password..")
    senha = "".join(random.choices(caracteres, k=10))
    print("Your password is: ", senha)
else:
    print("Closing program")