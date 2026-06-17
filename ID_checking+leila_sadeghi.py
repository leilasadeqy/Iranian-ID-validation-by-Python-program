while True:
    ID=input('please enter your ID number: ')
    if len(ID)==10:
        try:
            int_ID=int(ID)
            break
        except:
            print('enter a valid ID in English numbers, please!')
            continue
    else:
        print('ID number should contain 10 characters. try again!')
        continue
int_ID=list((map(lambda number:int(number),ID)))
mult_ID_numbers=[]
jaygah=len(int_ID)
ID_numbers=int_ID[0]
while True:
    mult_ID_numbers.append(ID_numbers*jaygah)
    if len(mult_ID_numbers)==9:
        break
    else:
      jaygah=jaygah-1
      ID_numbers=int_ID[len(mult_ID_numbers)]
      continue
baghimande=sum(mult_ID_numbers)%11
if len(set(str(ID_numbers))) == 1:
    print("fake ID!")
elif baghimande <2 and baghimande==int_ID[9] :
    print('ID confimed!')
elif baghimande>=2 and 11-baghimande==int_ID[9]:
    print('ID confimed!')
else:
    print('fake ID!')
    