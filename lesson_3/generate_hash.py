import hashlib

def generate_salt_to_hash(user):
    gen_salt_sha = hashlib.sha512(user.encode('UTF-8')).hexdigest()
    return gen_salt_sha

def generate_pass_to_hash(name, secret) :
    salt = generate_salt_to_hash(name)
    if salt != False:
        generate_hash = hashlib.sha512(secret.encode('UTF-8')+salt.encode('UTF-8')).hexdigest()
    else:
        generate_hash = False
    return generate_hash
