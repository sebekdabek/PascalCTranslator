# Pascal to C and the other way round translator
# Sebastian Dabek, Magdalena Zajac
# Projekt kompilatory

import sys

input_file_location = "C:/Users/sdabek/PycharmProjects/PascalCTranslator/inputFiles/inputfile.txt"

try:
    # Open file and print content
    f = open(input_file_location, "r")
    if f.mode == 'r':
        content = f.read()
    print(content)
    print("File successfully read.")

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


