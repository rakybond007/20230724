def add(add_list):
    return sum(add_list)

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