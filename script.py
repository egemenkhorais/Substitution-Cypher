import argparse
import sys
import random

with open("test_input.txt", "w") as f:
    f.write("This is a test value brothaa " * 500) # Approx 15kb.

def load_key():
    # Random but to make same matching for decryption we use seed
    seed_value = 42
    random.seed(seed_value)

    chars = list(range(256))
    shuffled = chars.copy()
    random.shuffle(shuffled)

    encrypt_table = {original: replacement for original, replacement in zip(chars, shuffled)}
    decrypt_table = {replacement: original for original, replacement in encrypt_table.items()}

    return encrypt_table, decrypt_table


def process_file(input_path, output_path, mode):
    encrypt_table, decrypt_table = load_key()
    table = encrypt_table if mode == 'encrypt' else decrypt_table

    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            data = f_in.read()
            # change with the exact value for every byte
            processed_data = bytes([table[b] for b in data])
            f_out.write(processed_data)
        print(f"Completed Successfully: {output_path}")
    except FileNotFoundError:
        print("Error : could not find input file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitution Cipher CLI")

    # to make turns unimportant
    parser.add_argument("-i", "--input", required=True, help="Input file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true", help="Encryption mode")
    group.add_argument("-d", "--decrypt", action="store_true", help="Decryption mode")

    args = parser.parse_args()

    if args.encrypt:
        process_file(args.input, args.output, 'encrypt')
    else:
        process_file(args.input, args.output, 'decrypt')