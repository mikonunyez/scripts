import hashlib

def hash(filepath, validHash, hashType):
    if (hashType == "SHA1"):
        h = hashlib.sha1()
    elif (hashType == "SHA256"):
        h = hashlib.sha256()
    
    with open(filepath, 'rb') as file:
        byte_block = 0
        while byte_block != b'':
            byte_block = file.read(4096)
            h.update(byte_block)

    fileHash = h.hexdigest()
    print("\nFile hash is: " + fileHash)
    print("Expected hash: " + validHash)
    if  fileHash == validHash:
        print("\nFile hash is VALID!")
    else:
        print("\nFile hash is INVALID!")

def hashType():
    h_type = input("Hash type? [SHA1/SHA256]: ")
    h_type = h_type.upper()
    
    if (h_type != 'SHA1') and (h_type != 'SHA256'):
        print("Invalid hash type")
        hashType()
    else:
        return h_type

print("SHA256 checker\n")
filepath = input("Enter filepath: ")
h_type = hashType()
validHash = input("Enter expected hash: ")
hash(filepath, validHash, h_type)