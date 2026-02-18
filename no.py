#wap to count the digits in no.

n=int(input("Enter a number: "))
count=0
while n>0:
    n=n//10
    count +=1

print(count)

#wap to reverse the digits in a no.

n=int(input("Enter a number: "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print(rev)

if n<0:
    sign= -1
    n=n*-1

    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10

    print(rev*sign)
