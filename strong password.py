import random
import array
max_len=12
Digits =['0','1','2','3','4','5','6','7','8','9']
LowerCaseChar=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
UpperCaseChar=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
Symboll=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
CombineList=Digits+LowerCaseChar+UpperCaseChar+Symboll
RandDigit=random.choice(Digits)
RandLower=random.choice(LowerCaseChar)
RandUpper=random.choice(UpperCaseChar)
RandSymb=random.choice(Symboll)
TempPass=RandDigit+RandLower+RandSymb+RandUpper
for i in range(max_len-4):
    TempPass=TempPass+random.choice(CombineList)
    TempPassList = array.array('u', TempPass)
    random.shuffle(TempPassList)
password=""
for i in TempPassList:
    password=password+i
print("\nStrogn password is : " ,password)


