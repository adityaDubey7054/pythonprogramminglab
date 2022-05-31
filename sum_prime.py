he_sum = 0
for number in range(20):
    if number > 3:
        for i in range(2,number):
            if (number%i)==0:
                break
            elif i == (number-1):
                the_sum += number
                print(number)
print (the_sum)