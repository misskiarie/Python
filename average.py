def calculate_average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average

dataset=[4,5,7,8,9,3,1,2,6]
answer=calculate_average(dataset)
print("Average is ", answer)