# Create a function that receives a list of numbers
# and returns the sum of all elements.

# Test with: [10, 20, 30, 40]

def total(number_list):
    result = 0
    for number in number_list:
        result += number
    return result

numbers = [10, 20, 30, 40]

print(f"Sum = {total(numbers)}")
