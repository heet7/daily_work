data = [104,101,4,105,308,103,5,107,100,306,106,102,108]
# min_value = 100
# max_value = 200

# l = len(data) - 1
# # print(l)
# for index , value in enumerate(reversed(data)):
#     if value<min_value or value>max_value:
#         print('{:>2} : {:^3}'.format(index,value))        
#         del data[l - index]
#     # print('{:>2} : {:^3}'.format(index,value))
        

# print(data)

def remove_outliers(data,min_limit,max_limit) -> list:
    """
    this function removes outliers from the data
    
    Parameters:
        data : data which want's to remove
        min_limit : set the minimum limit to remove outliers from downstairs
        max_limit : set the maximum limit to remove outliers from upstairs

    Return:
        list : list of data without outliers
    """
    print('your data has this much of outliers...')
    for index , value in enumerate(data):
        if  value < min_limit or value > max_limit:
            del data[index]
            print(index,value)
    print('\nyour data withour outliers.!')
    print(data)

x = remove_outliers(data=data,min_limit=100,max_limit=200)
