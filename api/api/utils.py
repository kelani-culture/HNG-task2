import secrets

def generate_id():
    secret_key = secrets.randbelow(10**4)
    return secret_key