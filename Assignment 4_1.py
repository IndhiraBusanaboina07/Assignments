def sum(*values):
    result = 0    
    for i in values:
        result+= i
    
    return res

def average(*values):
    sum_values = sum(*values)
    return sum_values/len(values)

average(1,2,3)