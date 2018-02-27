'''
Write a function, persistence, that takes in a positive parameter num and returns 
its multiplicative persistence, which is the number of times you must multiply the 
digits in num until you reach a single digit.
For example:
 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
 persistence(4) => 0   # Because 4 is already a one-digit number.
'''
def persistence(n):
    # your code
    #print(n%10)
    
    total = 0
    while (n>9):
        ten = 10
        count = 1
        result = 1   
        while True:
            if((n%ten)==n): 
                break
            ten = ten * 10
            count = count + 1
        #print (ten)
        #print (count)
        ten = ten / 10
        for i in range(0,count):
            result = result * (n-(n%ten))/ten
            n = n%ten
            ten = ten / 10
            i=i+1
        total = total + 1
    #n = persistenceInter(n, total)
        if(result > 9):
            print (result)
            n = result
        else:
            break
    print (result)
    print (total)
    return total
persistence(999)
    