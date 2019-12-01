# Based on https://www.youtube.com/watch?v=LkIK8f4yvOU.
# The Difference of Two Squares.

number = int(input("Please enter a positive odd number: "))

while number % 2 == 0 or number < 0:
    number = int(input(
        "Please enter a positive number: " if number < 0 
        else "Please enter an odd number: "
    ))

root_2 = number // 2
root_1 = root_2 + 1

print(f"The roots are { root_1 } and { root_2 }.")
print(f"The squares are { root_1 ** 2 } and { root_2 ** 2 }.")
print(f"{ root_1 ** 2 } - { root_2 ** 2 } = { number }.")