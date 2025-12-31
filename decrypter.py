from cryptography.fernet import Fernet
from generate_key import find_key
from sys import exit
from pathlib import Path

ransomwaretroll = Path("teste.txt.ransomwaretroll.bin")

if not ransomwaretroll.exists(): exit()

# buscando a chave secreta.
fernet = Fernet(find_key())

# Lê o arquivo criptografado
with open("teste.txt.ransomwaretroll.bin", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

# Descriptografa
decrypted = fernet.decrypt(encrypted)

# Salva o arquivo descriptografado
with open("teste.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted)

ransomwaretroll.unlink()