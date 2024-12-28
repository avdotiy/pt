def middle (numbers):
    if len(numbers)%2 == 1:   
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
        return numbers[len(numbers)//2]
    else:
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
        dop = int((numbers[(len(numbers)//2+ 1/2)] + numbers[(len(numbers)/2- 1/2)])//2 )
    return dop
print(middle([1,3,4,2,5]))
print(middle([2,4,6,8]))