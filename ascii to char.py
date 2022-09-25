ini_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
  
# Printing initial list
print ("Initial list", ini_list)
  
# Using Naive Method
res = ""
for val in ini_list:
    res = res + chr(val)
  
# Printing resultant string
print ("Resultant string", str(res))