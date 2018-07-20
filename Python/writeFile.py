f = open("countries.txt","w")

while True:
    country = input("Enter country name")
    
    if country == 'N':
        break
    else:
        f.write(country+"\n")
        
f.close()

f = open("countries.txt","r")

for line in f:
    line = line.strip()
    print(line)
    
f.close()
