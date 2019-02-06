N = int(input())

while N > 0:
    n1 = int(input())
    sumOdd = 0
    sumEven = 0
    temp = n1
    
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        if rem % 2 == 0:
            sumEven += rem
        elif rem % 2 != 0:
            sumOdd += rem
            
    if sumEven % 4 == 0 or sumOdd % 3 == 0:
        print('Yes')
    else:
        print('No')

        

    N -= 1