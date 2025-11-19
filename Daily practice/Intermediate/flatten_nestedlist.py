def flatten_iterative(nested_list):
    stack = nested_list[::-1]
    flat_list = []
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            flat_list.append(item)
    return flat_list

nested = [1, [2, [3, 4], 5], 6]
print(flatten_iterative(nested))  
