def add(add_list):
    result = 0
    for each_num in add_list:
        if each_num >= 0:
            result += each_num
    return result

def sub(a,b):
    return a-b

add_numbers = [1,3]
sub_numbers = [[5,4],[4,3]]

#add_result = add(add_numbers[0], add_numbers[1])
add_result = add(add_numbers)
sub_result1 = sub(sub_numbers[0][0], sub_numbers[1][0])
sub_result2 = sub(sub_numbers[0][1], sub_numbers[1][1])

print(add_result, sub_result1, sub_result2)