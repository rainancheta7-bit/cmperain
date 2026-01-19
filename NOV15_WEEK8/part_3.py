ListofNumbers = [890, 33, 44, 69, 90]

def add_function(a, b):
    """This function is used to add two numbers and return sum"""
    return a + b


def average_function(inputList):
    """This function is used to get and return average"""
    totalsum = 0
    for i in inputList:
        totalsum = add_function(totalsum, i)
    average = totalsum / len(inputList)
    return average


print(average_function(ListofNumbers))