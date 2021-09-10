# 6.	Calculate the mean and standard deviation of the following list:
# Numbers = [1,2,3,5,88,99,55,33,41,52]

import math
from statistics import stdev,mean

def meanCalculation(data):
    """
    calculating mean of a list
    """
    return sum(data)/len(data)

def sdCalculation(data):
    """
    calculating standard deviation of a list
    """
    mean = meanCalculation(data)
    value = [ pow(mean-x,2) for x in data]
    value = sum(value)/len(data)
    var = math.sqrt(value)
    return var

def main():
    Numbers = [1,2,3,5,88,99,55,33,41,52]
    print("\nMean is {} and variance is {}".format(meanCalculation(Numbers),sdCalculation(Numbers)))
    print("\nUsing Statistics Module")
    print("\tMean is {} and standard deviation is {}\n".format(mean(Numbers),stdev(Numbers)))

if __name__ == '__main__':
    main()
