string = 'b22%2mZUk$hv3^b^3s85Q#'

write = ''

for integer in range(len(string)):
    if (string[integer].isalpha() == True):
        write = write + '1'
    elif (string[integer].isdigit() == True):
        write = write + '2'
    else:
        write = write + '3'

print(write)
