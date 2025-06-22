# bounce.py
#
# Exercise 1.5
initial_height = 100
actual_height = initial_height
ratio = 3/5
for i in range(10):
    actual_height = actual_height * ratio
    print(round(actual_height, 4))