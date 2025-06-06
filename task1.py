# Takes a list of digits (like [1, 2, 3]) and turns it into a single number (like 123).
# How it works: It starts with 0 and builds the number step-by-step. For each digit, it shifts the current
# number left (by multiplying by 10) and adds the new digit.

digit_list = [8,3,5,1]

# Start with 0. This will grow into our final number
number = 0
    
# Go through each digit in the list one by one
for digit in digit_list:
  # Shift the current number left by multiplying by 10 (e.g. 8 becomes 80)
  current_number = number * 10
  # Add the new digit to the shifted number (e.g. 80 + 3 becomes 83)
  number = current_number + digit

# After every digit is added, output the final number (should be 8351)
print(number)  
