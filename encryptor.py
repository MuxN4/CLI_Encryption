import argparse
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
def generate_key():
    return Fernet.generate_key()

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Encrypt and Decrypt files or messages")
    
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands help')
    
    # Key generation command
    keygen_parser = subparsers.add_parser('keygen', help='Generate a new encryption key')
    keygen_parser.add_argument('keyfile', type=str, help='File to save the encryption key')

    # Encrypt message command
    encrypt_message_parser = subparsers.add_parser('encrypt_message', help='Encrypt a message')
    encrypt_message_parser.add_argument('keyfile', type=str, help='File containing the encryption key')
    encrypt_message_parser.add_argument('message', type=str, help='Message to encrypt')
    
    # Decrypt message command
    decrypt_message_parser = subparsers.add_parser('decrypt_message', help='Decrypt a message')
    decrypt_message_parser.add_argument('keyfile', type=str, help='File containing the encryption key')
    decrypt_message_parser.add_argument('message', type=str, help='Message to decrypt')
    
    # Encrypt file command
    encrypt_file_parser = subparsers.add_parser('encrypt_file', help='Encrypt a file')
    encrypt_file_parser.add_argument('keyfile', type=str, help='File containing the encryption key')
    encrypt_file_parser.add_argument('inputfile', type=str, help='Input file to encrypt')
    encrypt_file_parser.add_argument('outputfile', type=str, help='Output file to save encrypted data')
    
    # Decrypt file command
    decrypt_file_parser = subparsers.add_parser('decrypt_file', help='Decrypt a file')
    decrypt_file_parser.add_argument('keyfile', type=str, help='File containing the encryption key')
    decrypt_file_parser.add_argument('inputfile', type=str, help='Input file to decrypt')
    decrypt_file_parser.add_argument('outputfile', type=str, help='Output file to save decrypted data')
    
    args = parser.parse_args()
    
    if args.command == 'keygen':
        key = generate_key()
        save_key(key, args.keyfile)
        print(f"Key saved to {args.keyfile}")
    elif args.command == 'encrypt_message':
        key = load_key(args.keyfile)
        encrypted_message = encrypt_message(key, args.message)
        print(f"Encrypted message: {encrypted_message.decode()}")
    elif args.command == 'decrypt_message':
        key = load_key(args.keyfile)
        decrypted_message = decrypt_message(key, args.message.encode())
        print(f"Decrypted message: {decrypted_message}")
    elif args.command == 'encrypt_file':
        key = load_key(args.keyfile)
        encrypt_file(key, args.inputfile, args.outputfile)
        print(f"File encrypted to {args.outputfile}")
    elif args.command == 'decrypt_file':
        key = load_key(args.keyfile)
        decrypt_file(key, args.inputfile, args.outputfile)
        print(f"File decrypted to {args.outputfile}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
