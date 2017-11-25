# if n even , divide by 2
# if n is odd , multi by 3 and add 1
# find number of steps to reach 1

i=1
while True:
    num=int(input("enter the number greater than 1:"))

    if num>1:
        while True:
            if num/2==1:
                break
            elif num%2==0:
                num/=2
                i+=1
            elif num%2==1 and num/2!=1:
                num=(num*3)+1
                i+=1

        break

    else:
        print("enter the number again:")
        continue

print("the number of steps taken to reach 1 is :", i)

