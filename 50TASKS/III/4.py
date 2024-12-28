def sum(s):
    total_sum = 0
    current_num = ""
    for char in s:
        if char.isdigit():  
            current_num += char  
        else:
            if current_num:  
                total_sum += int(current_num)  
                current_num = ""  
    if current_num:
        total_sum += int(current_num)
    return total_sum
print(sum("matvey777 krutoy52"))