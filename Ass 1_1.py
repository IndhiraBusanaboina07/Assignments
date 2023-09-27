def frequency_distribution(input_sequence):

    dictionary = {}

    for i in input_sequence:

        if i in dictionary:

            dictionary[i] += 1
        else :
            dictionary[i] = 1

    return dictionary 

input_sequence = input('Enter input:\t')

print(frequency_distribution(input_sequence))