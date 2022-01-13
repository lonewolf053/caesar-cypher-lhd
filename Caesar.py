# Caesar cipher
def encrypt(text,shift):
    ans = ""
    for char in text:
        if char.isupper():
            ans+=chr((ord(char)+shift-65)%26+65)
        elif char.islower():
            ans += chr((ord(char)+shift-97)%26+97)
        else:
            ans+=char
    return ans

def decrypt(text,shift):
    ans = ""
    for char in text:
        if char.isupper():
            ans+=chr((ord(char)-shift-65)%26+65)
        elif char.islower():
            ans += chr((ord(char)-shift-97)%26+97)
        else:
            ans+=char
    return ans


text = input("Enter text to encrypt or decrypt: \n")

while True:
    if "choice" not in globals():
        try:
            choice = int(input("Type 1 to encrypt and 2 to decrypt: \n"))
        except:
            print("Input invalid, please try again")
            continue

    try:
        shift = int(input("Enter Key to Shift: \n"))
        break
    except:
        print("Input invalid, please try again")
        
    
if choice == 1:
    print("Your encrypted text: \n"encrypt(text,shift))
elif choice == 2:
    print("Your decrypted text: \n"decrypt(text,shift))
        
        
