"""Author: Amzuloiu Andrei-Ciprian"""
from playfair import crypt, decrypt

INPUT_DECRYPT_PATH = "input/input_decrypt.txt"
INPUT_CRYPT_PATH = "input/input_crypt.txt"
OUTPUT_PATH = "output/output.txt"

"""The main function"""
def main():
    print("1 - Crypt the text from input_crypt.txt using a given key. \n\
2 - Decrypt the text from input_decrypt.txt using a given key.\n\
Other - Exit\n")
    loop = True
    key = ''
    text = ''

    while loop:
        print("Enter your option: ")
        option = int(input())

        if option == 1:
            file = open(INPUT_CRYPT_PATH, 'r')
            text = file.read()
            file.close()
            print("Enter the key: ")
            key = input()
            output = open(OUTPUT_PATH, 'w')
            output.write(crypt(text, key))
            output.close()

        elif option == 2:
            file = open(INPUT_DECRYPT_PATH, 'r')
            text = file.read()
            file.close()
            print("Enter the key: ")
            key = input()
            output = open(OUTPUT_PATH, 'w')
            output.write(decrypt(text, key))
            output.close()

        else:
            loop = False

if __name__ == "__main__":
    main()
