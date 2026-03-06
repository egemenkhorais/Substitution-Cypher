# 8-bit Substitution Cipher Tool

## Description
This is a command-line application that implements a Substitution Cipher for 8-bit ASCII characters. It replaces every byte in the plaintext with a corresponding byte from a predefined substitution table. It supports both encryption and decryption of any file type (text or binary).

## Implementation Approach
- **8-bit Mapping:** The cipher works on the byte level (0-255). It uses a mathematical mapping ($f(x) = (x + 42) \pmod{256}$) to ensure every possible ASCII character has a unique substitute.
- **CLI Design:** The application uses the `argparse` library to handle command-line arguments. The order of arguments is flexible (e.g., `-e` can come before or after `-i`).
- **Binary Processing:** Files are read and written in binary mode (`'rb'`, `'wb'`) to prevent data corruption and handle non-printable characters.

## How to Run
The application requires Python 3.x. No external libraries are needed.

### Encryption
To encrypt a file:
python script.py -i test_input.txt -o output.bin -e 

### Decryption 
To decrypt a encrypted file:
python script.py -i output.bin -o original_back.txt -d


Test Cases
Large Text File: A 15 KB text file was encrypted. The resulting output.bin contained non-readable characters, confirming encryption.

Integrity Check: The encrypted file was decrypted. The final original_back.txt was compared with the source test_input.txt using a checksum/manual comparison, and they were identical.

Flexible Arguments: Verified that app -e -i file -o out and app -o out -i file -e produce the same result.
