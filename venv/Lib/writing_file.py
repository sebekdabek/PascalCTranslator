# Pascal to C and the other way round translator
# Sebastian Dabek, Magdalena Zajac
# Projekt kompilatory

import sys

output_file_location = "C:/Users/sdabek/PycharmProjects/PascalCTranslator/outputFiles/outputFile.txt"

try:
    # Write and append file with some content (test)
    # If file doesnot exist - create new
    f = open(output_file_location, "w+")
    f = open(output_file_location, "a+")
    for i in range(20):
       f.write("This is line %d\r\n" % (i+1))
    f.close()

# except ValueError:
#    print("Cannot convert data to an integer")

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print("File successfully written")
