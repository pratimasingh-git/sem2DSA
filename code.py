
n= 3465621
counter= 0
while n>0:
    n//10
    counter+= 1
print(counter)

num= 454334
r_num= 0
while num>0:
    digit=num%10
    r_num=r_num*10+digit
    num//=10
print(r_num)

def is_palindromatic(number):
    orignal_number=number
    reversed_num>0
    while number>0:
        digit=number%0
        reversed_num=reversed_num*10+digit
        number//10=10
    return orignal_number==reversed_num
test_number=235421
print(is_palindromatic(test_number))

original_num=624361
num_digits=len(str(original_num))
sum_of_digits=0
while original_num>0:
    digit=original_num%10