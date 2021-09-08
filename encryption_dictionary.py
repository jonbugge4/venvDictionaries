# Create Main Function

def main():

    # Create Encryption Dictionary
    encryption_dictionary = {'A': '<','a': '>', 'B': '+', 'b': '=', 'C': ',', 'c': '.', 'D': '1', 'd': '!', 
    'E': '}', 'e': ']', 'F': '-', 'f': '[', 'G': '{', 'g': ')', 'H': '(', 'h': '"', 'I': '@', 'i': '*', 'J': '2',
    'j': '#', 'K': '^', 'k': '0', 'L': ':', 'l': ';', 'M': '&', 'm': '4', 'N': '~', 'n': '0', 'O': '?', 'o': '5',
    'P': '7', 'p': '_', 'Q': '9', 'q': '8', 'R': '3', 'r': '$', 'S': '6', 's': '10', 'T': '00', 't': '62', 'U': '{-',
    'u': '31', 'V': '@(', 'v': '^2', 'W': '<<', 'w': '**', 'X': '101', 'x': '=+', 'Y': '.:.', 'y': '*_*', 'Z': '!2', 
    'z': '-_'}

  
    # Import TXT file
    file_guy = open("info_security.txt", 'r')
    
    #Create Encrypte thing
    encrypt = ""

    #create for loop
    for letter in file_guy:
        if letter in encryption_dictionary:
            encrypt += encryption_dictionary[letter]
        else: encrypt += letter
    print(encrypt)


    

main()
