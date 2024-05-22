# Create a function that takes in a list.
# If the first number, is less than the last number,
# print "Hi". If the first number is greater than the last number, 
# print "Bye". If they are equal, alert "We close in an hour"

def takes_list(numbers):
    if len(numbers) < 2:
        print("The list must have at least two elements.")
        return
    
    if numbers[0] < numbers[-1]:
        print("Hi")
    elif numbers[0] > numbers[-1]:
        print("Bye")
    else:
        print("We close in an hour")

# Example usage:
takes_list([1, 2, 3])  # Output: Hi
takes_list([3, 2, 1])  # Output: Bye
takes_list([2, 2, 2])  # Output: We close in an hour