def find_min_while(arr):
    if not arr:
        return None  # Return None if the array is empty
    
    min_element = arr[0]
    index = 1
    while index < len(arr):
        if arr[index] < min_element:
            min_element = arr[index]
        index += 1
            
    return min_element

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value = find_min_while(array)
print(f"The minimum element in the array is: {min_value}")
