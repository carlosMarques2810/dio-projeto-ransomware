def find_key():
    """
    Responsável por buscar a chave secreta.
    """
    with open("secret.key", "rb") as secret_key:
        secret_key = secret_key.read()
    return secret_key

def create_secret_key():
    """
    Reponsável gerar a chave secreta, que será usado tanta pra o encrypter quanto ao decrypter.
    """
    from pathlib import Path

    if Path("secret.key").exists(): return

    from cryptography.fernet import Fernet
    key = Fernet.generate_key()

    with open("secret.key", "wb") as secret_file:
        secret_file.write(key)