import hashlib

def hash(filepath, validHash):
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as file:
        byte_block = 0
        while byte_block != b'':
            byte_block = file.read(4096)
            sha256_hash.update(byte_block)

    fileHash = sha256_hash.hexdigest()
    print("\nFile hash is: " + fileHash)
    print("Expected hash: " + validHash)
    if  fileHash == validHash:
        print("\nFile hash is VALID!")
    else:
        print("\nFile hash is INVALID!")


print("SHA256 checker\n")
filepath = input("Enter filepath: ")
validHash = input("Enter expected hash: ")
hash(filepath, validHash)