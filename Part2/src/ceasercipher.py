import sys


def implement_caesar_cipher(message, key, decrypt=False):
   result = ""
   shift = -key if decrypt else key
   for character in message:
       # Check if the character is an alphabet letter.
       if character.isalpha():
           if character.islower():
               #transformation for lowercase letters.
               result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
           else:
               #transformation for uppercase letters.
               result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
       else:
           # Preserve non-alphabet characters as they are.
           result += character
   return result

# ask whether to encrypt or decrypt
mode = input("[?] Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
if mode not in ("e", "d"):
    print("[!] Please enter 'E' for encrypt or 'D' for decrypt.")
    sys.exit()

text = input("[?] Please enter your text/message: ")

# checks if the key is a number
try:
    key = int(input("[?] Please specify the shift length (0-25): "))
except ValueError:
    print("[!] Your shift length must be a whole number.")
    sys.exit()

if key < 0 or key > 25:
    print("[!] Your shift length should be between 0 and 25.")
    sys.exit()

if mode == "e":
    encrypted = implement_caesar_cipher(text, key)
    print(f"[+] '{text}' has been encrypted as '{encrypted}'")
else:
    decrypted = implement_caesar_cipher(text, key, decrypt=True)
    print(f"[+] '{text}' has been decrypted as '{decrypted}'")