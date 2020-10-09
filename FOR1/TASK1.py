string = 'b22%2mZUk$hv3^b^3s85Q#'
integer = 0
write = ''
for integer in range(22):
    if(string[integer].isalpha() == True):
        write = write + '1'
    elif(string[integer].isdigit() == True):
        write = write + '2'
    else:
        write = write + '3'
print(write)
