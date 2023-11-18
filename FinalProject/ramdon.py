import random

left_right_up = [[0,0],[0,1], [0,2], [0,3], [0,4], [0,5], [0,6]]
down_top_right = [ [6,0], [5,0], [4,0], [3,0],[2,0],[1,0],[0,0]  ]
right_left_down = [[6,6], [6,5], [6,4], [6,3], [6,2], [6,1],[6,0]]
top_dow_right = [[0,6],[1,6], [2,6], [3,6], [4,6], [5,6], [6,6]]

# Shuffle the list
temp=-1
roll=random.randrange(0,7)
while roll<temp:
    roll=random.randrange(0,7)
temp=roll
temp=left_right_up[roll][1]

#print(my_list)

#random.shuffle(my_list)

print(left_right_up)

print(left_right_up[roll])

print(left_right_up[roll][1])


def my_function():
    return 10, 20

result1, result2 = my_function()

print(result1)