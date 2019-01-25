yob = int(input("Enter your year of birth"))
current_year = 2019
age = current_year - yob
print (age)

if 0 < age < 18:
    print ("minor")
elif 18 < age < 36:
    print ("youth")
else: print ("elder")       

