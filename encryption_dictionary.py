# Create Main Function

def main():

    # Create Encryption Dictionary
    encryption_dictionary = {'A': '<','a': '>', 'B': '+', 'b': '=', 'C': ',', 'c': '.', 'D': '1', 'd': '!', 
    'E': '}', 'e': ']', 'F': '-', 'f': '[', 'G': '{', 'g': ')', 'H': '(', 'h': '"', 'I': '@', 'i': '*', 'J': '2',
    'j': '#', 'K': '^', 'k': '0', 'L': ':', 'l': ';', 'M': '&', 'm': '4', 'N': '~', 'n': '0', 'O': '?', 'o': '5',
    'P': '7', 'p': '_', 'Q': '9', 'q': '8', 'R': '3', 'r': '$', 'S': '6', 's': '10', 'T': '00', 't': '62', 'U': '{-',
    'u': '31', 'V': '@(', 'v': '^2', 'W': '<<', 'w': '**', 'X': '101', 'x': '=+', 'Y': '.:.', 'y': '*_*', 'Z': '!2', 
    'z': '-_', ' ': ' ', '.': ',', ':': 'lol'}

  
    # Import TXT file
    outfile = open("info_security.txt", 'r')
    encrypt = open('encrypted_doc.txt', 'w')

    file_contents = outfile.read()



    for x in file_contents:
        encryption_dictionary[x]

        encrypt.write(encryption_dictionary[x])
    encrypt.close() 


main()
