yr = "3000"
yri = int(yr)
if(yri % 4 == 0 and (yri % 400 == 0 or yri % 100 != 0)):
    print(yri, "is a leap year")
else:
    print(yri, "is NOT a leap year")
        
        
