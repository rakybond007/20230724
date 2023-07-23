def add(add_list):
    result = 0
    for each_num in add_list:
        if each_num >= 0:
            result += each_num
    return result

def sub(sub_list):
    result = []
    for from_num, sub_num in sub_list[0],sub_list[1]:
        result += [from_num - sub_num]
    return result

add_numbers = [1,3]
sub_numbers = [[5,4],[4,3]]

add_result = add(add_numbers)
sub_result = sub(sub_numbers)

print(add_result, sub_result)