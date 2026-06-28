students = {
    "John": [85.5, 90.0, 88.5],
    "Alex": [75.0, 80.5, 70.5],
    "Sam": [90.0, 95.0, 92.5]
}

name = input("Enter student name: ")

marks = students[name]

average = sum(marks) / len(marks)

print("Average percentage:", average)