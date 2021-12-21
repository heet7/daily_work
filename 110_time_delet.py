import timeit

max_value = 100000000  # 100000000
min_valid = 10
max_valid = 99999997  # 99999997

data = list(range(max_value))

def oneway(data):
    """
        in this function we can remove the outlier
        param:
            data = pass a list of data
    """
    main_index = len(data) - 1
    for index,value in enumerate(reversed(data)):
        if value<=min_valid or value >=max_valid:
            del data[main_index - index]
    # print(data)

def secondway(data):
    """
        in this function delet outliers using range reverce slicing
        param:
            data = pass list data
    """
    for value in range(len(data)-1,-1,-1):
        if data[value] <=min_valid or data[value]>=max_valid:
            del data[value]
    # print(data)

if __name__ == "__main__":
    print('calculate compilation time')
    first_function = timeit.timeit("oneway(data)","from __main__ import oneway,data",number=1)    
    second_funciton = timeit.timeit("secondway(data)","from __main__ import secondway,data",number=1)

    print("1:->")
    print("{:15.15f}".format(first_function))
    print("2:->")
    print("{:15.15f}".format(second_funciton))