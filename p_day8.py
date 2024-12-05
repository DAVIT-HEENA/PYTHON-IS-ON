alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cypher_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            cypher_text += alphabet[new_index]
        else:
            cypher_text += letter  # Keep non-alphabet characters unchanged
    print(f"Encrypted text: {cypher_text}")

def decrypt(text, shift):
    cypher_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % len(alphabet)
            cypher_text += alphabet[new_index]
        else:
            cypher_text += letter  # Keep non-alphabet characters unchanged
    print(f"Decrypted text: {cypher_text}")

# Main Program
direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid direction. Please type 'encode' or 'decode'.")
