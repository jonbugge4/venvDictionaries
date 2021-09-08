# This program writes three lines of data
 # to a file.
def main():
 # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')
 
# Write the names of three philosphers to the file – 
# John Locke, David Hume and Edmund Burke
    outfile.write('John Locke '+ '\n')
    outfile.write('david Humme' + '\n')
    outfile.write('Edmund Burke' + '\n')


# Close the file.
    outfile.close()

    
# Call the main function.
main()

outfile = open('philosophers.txt', 'a')

outfile.write('Jonathan Bugge' + '\n')

outfile.close()


def main():

    infile = open('philosophers.txt', 'r')

    file_contents = infile.read()

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline()
    line3 = infile.readline()

    print(line1)
    print(line2.rstrip('\n'))
    print(line3)

    print(file_contents)



main()