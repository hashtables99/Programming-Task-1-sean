# This function takes a list of digits (like [1, 2, 3]) and turns it into a single number (like 123).
# How it works: It starts with 0 and builds the number step-by-step. For each digit, it shifts the current
# number left (by multiplying by 10) and adds the new digit.

def list_to_number(digit_list):
  # Start with 0. This will grow into our final number
  number = 0

  # Go through each digit in the list one by one
  for digit in digit_list:
    # Shift the current number left by multiplying by 10 (e.g. 8 becomes 80)
    current_number = number * 10
    # Add the new digit to the shifted number (e.g. 80 + 3 becomes 83)
    number = current_number + digit

  # After every digit is added, send back the final number  
  return number  

# Let's test and see if this works :)
print(list_to_number([8,3,5,1])) # Should print 8351
print(list_to_number([1,2,3])) # Should print 123
print(list_to_number([0,7])) # Should print 7
