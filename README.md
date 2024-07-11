# CLI-Encryption

## Overview

Encryptor is a Command Line Interface (CLI) tool for encrypting and decrypting files or messages. It uses the `cryptography` library to provide secure encryption algorithms.

## Features

- Generate a new encryption key
- Encrypt messages
- Decrypt messages
- Encrypt files
- Decrypt files

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone the repository or download the `encryptor.py` file to your local machine.
2. Install the required packages using `pip`:

   ```sh
   pip install cryptography
   ```
## Usage

Run the encryptor.py script with the appropriate command and arguments. Below are the available commands:

Generate a New Encryption Key
    ```sh
    python encryptor.py keygen <keyfile>
    ```
`<keyfile>`: The file to save the generated encryption key.

## Example:

    ```sh
    python encryptor.py keygen mykey.key
    ```
Encrypt a Message
    ```sh
    python encryptor.py encrypt_message <keyfile> <message>
    ```
`<keyfile>`: The file containing the encryption key.
`<message>`: The message to encrypt.

## Example:

    ```sh
    python encryptor.py encrypt_message mykey.key "Hello, World!"
    ```
## Decrypt a Message

    ```sh
    python encryptor.py decrypt_message <keyfile> <message>
    ```
`<keyfile>`: The file containing the encryption key.
`<message>`: The encrypted message to decrypt.

## Example:

    ```sh
    python encryptor.py decrypt_message mykey.key "<encrypted_message>"
    ```

## Encrypt a File

    ```sh
    python encryptor.py encrypt_file <keyfile> <inputfile> <outputfile>
    ```
`<keyfile>`: The file containing the encryption key.
`<inputfile>`: The input file to encrypt.
`<outputfile>`: The output file to save the encrypted data.

## Example:

    ```sh
    python encryptor.py encrypt_file mykey.key input.txt encrypted.txt
    ```
## Decrypt a File

    ```sh
    python encryptor.py decrypt_file <keyfile> <inputfile> <outputfile>
    ```
`<keyfile>`: The file containing the encryption key.
`<inputfile>`: The input file to decrypt.
`<outputfile>`: The output file to save the decrypted data.

## Example:

    ```sh
    python encryptor.py decrypt_file mykey.key encrypted.txt decrypted.txt
    ```

License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements

This tool uses the cryptography library. For more information, visit the cryptography documentation.

# Conclusion

This README provides an overview of the CLI tool, instructions for installation and usage, and details about the available commands. Adjust any sections as necessary to fit your specific needs or project requirements.





