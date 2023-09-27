def histogram(freq_dict):

    for i  in freq_dict:

        print(i, end = ' | ')

        print("=====" * freq_dict[i], end = ' ')

        print(freq_dict[i])

freq_dict = {1:4,2:3,3:3,4:3,5:2}

print(histogram(freq_dict)) 