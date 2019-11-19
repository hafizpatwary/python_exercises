#unique sum

def uniqueSum():
    sum_number = int(input('Enter number of element you want to sum: '))
    array = []
    my_sum = 0
    for i in range(sum_number):
        print('Enter number ' + str((i+1)) + ' of ' + str(sum_number) + ': ', end='')
        value = int(input())
        array.append(value)


    for item in array:
        count = array.count(item)
        if count < 2:
            my_sum += item

    print(my_sum)

if __name__=='__main__':
    uniqueSum()
        
    
    
