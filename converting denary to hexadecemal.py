#Christopher pullen
#18-09-2014
#converting binary to hexadecimal.

denary_value = int(input("Please enter a denary value:"))

hex_string= ("")
while denary_value > 0:
      hex_string = str(denary_value % 16) + hex_string
      denary_value = denary_value //16
       
print("The hexadecimal equivalent is {0}" .format (hex_string))



