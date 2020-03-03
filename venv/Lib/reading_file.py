# Pascal to C and the other way round translator
# Sebastian Dabek, Magdalena Zajac
# Projekt kompilatory

import sys

try:
    # Open file and print content
    f = open("C:/Users/sdabek/PycharmProjects/PascalCTranslator/inputFiles/inputfile.txt", "r")
    if f.mode == 'r':
        content = f.read()
    print(content)

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print("Hello")
