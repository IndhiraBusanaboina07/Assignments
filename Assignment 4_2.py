def histogram(frequency_dictionary, design = '===', show = True, align = False):
    maximum_frequency = max(frequency_dictionary.values())
    
    for i  in frequency_dictionary:
        print(i, end = ' | ')

        print(design * frequency_dictionary[i], end = ' ')
        
        if(align): 
            print((maximum_frequency - frequency_dictionary[i]) * ((' '*len(design))), end = '')

        if(show): 
            print(frequency_dictionary[i])

        else:
            print()

histogram({1:5,2:6, 3:2,4:4,5:3}, align=True, show=True, design='+++')