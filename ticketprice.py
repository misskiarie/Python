#python prgram to calculate ticket price of theater based on age
#0-5 (free) 6-12 (500/=) 13-17 (1000/=) 18+ (1500/=)

age = int(input("Enter age"))
if age >= 0 and age <= 5:
    print("Price is free")
if age > 5 and age <= 12:
    print("Price is 500/=")
if age > 12 and age <= 17:
    print("Price is 1000/=")
if age > 17:
    print("Price is 1500/=")
