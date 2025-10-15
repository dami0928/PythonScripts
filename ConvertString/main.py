from Crypto.Hash import MD4,MD5

def md4_hash(data,encoding):
    md4 = MD4.new()
    md4.update(data.encode(encoding))
    return md4.hexdigest()

def md5_hash(data,encoding):
    md5 = MD5.new()
    md5.update(data.encode(encoding))
    return md5.hexdigest()


if __name__ == "__main__":
    message = "Hello, MD4!"
    hash_value = md5_hash(message,'utf-8')
    print(f"MD5 Hash: {hash_value}")


