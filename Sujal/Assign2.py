a = int(input('Enter number of students : '))
marks = []
for i in range(a):
    mark = int(input(f'Enter marks of {i+1} student : '))
    marks.append(mark)

print('Marks of student are : ', marks)

# Average Score of the Class
sum = 0
for i in marks:
    sum += i
print('Average Score of the Class is : ', sum/a)

# Highest score
highest = marks[0]
for i in marks:
    if i > highest:
        highest = i
print('Highest score : ', highest)

# Lowest score
lowest = marks[0]
for i in marks:
    if i != -1:
        if i < lowest:
            lowest = marks[i]
print('Lowest score : ', lowest)

# number absent students
count = 0
for i in marks:
    if i == -1:
        count += 1
print('Number of students who were absent : ', count)

# Frequency
count = {}
for i in marks:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
