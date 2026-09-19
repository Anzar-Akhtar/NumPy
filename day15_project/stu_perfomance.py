import numpy as np

students = np.array([
    [101, 20, 4, 85, 78, 72, 80],
    [102, 21, 2, 65, 60, 55, 58],
    [103, 20, 6, 92, 88, 90, 94],
    [104, 22, 3, 70, 65, 62, 68],
    [105, 21, 5, 88, 82, 79, 85],
    [106, 20, 1, 55, 48, 45, 50],
    [107, 23, 7, 96, 94, 91, 97],
    [108, 21, 4, 80, 75, 70, 76],
    [109, 22, 2, 60, 55, 52, 57],
    [110, 20, 5, 90, 85, 82, 89],
    [111, 21, 3, 75, 70, 68, 72],
    [112, 22, 6, 94, 90, 88, 93],
    [113, 20, 2, 62, 58, 50, 55],
    [114, 23, 5, 86, 80, 78, 84],
    [115, 21, 4, 82, 77, 74, 79],
    [116, 22, 1, 50, 45, 42, 48],
    [117, 20, 7, 98, 95, 94, 99],
    [118, 21, 3, 72, 68, 65, 70],
    [119, 22, 5, 89, 84, 81, 87],
    [120, 20, 2, 58, 52, 48, 54]
])

# shape
print(np.shape(students))


# extract column
stu_id = students[:, 0]
age = students[:, 1]
study_hours = students[:, 2]
attendence = students[:, 3]
assignment = students[:, 4]
midterm = students[:, 5]
final = students[:, 6]

# basic statistic
avg_study_hours = np.mean(study_hours)
avg_attendence = np.mean(attendence)
avg_assign_score = np.mean(assignment)
avg_mid = np.mean(midterm)
avg_final = np.mean(final)


print("\n----- BASIC STATISTICS -----")
print()

print("Average Study Hours:",
      avg_study_hours)

print("Average Attendence:",
      avg_attendence)

print("Average Assignment Score:",
      avg_assign_score)

print("Average Midterm Score:",
      avg_mid)

print("Average Final Score:",
      avg_final)


# highest performing students

high_ind = np.argmax(final)
high_score = final[high_ind]

print("---- TOP STUDENT ----")
print()

print("Highest Final Score:",
      high_score)


# complete row of the top student
print("Top Student Data:",
      students[high_ind])


# lowest performing student
low_ind = np.argmin(final)
low_score = final[low_ind]

print("\n ---- LOWEST STUDENTS ----")
print()

print("Lowest Student Score:",
      low_score)

print("Lowest Student Data:",
      students[low_ind])


#  At risk student

at_risk = students[students[:, 6] < 60]

print("\n ---- AT-RISK STUDENTS ----")
print(at_risk)


# attendence risk

att_risk = students[students[:, 3] < 75]

print("\n ---- ATTENDENCE RISK ----")
print(att_risk)


# critical condition

critical_students = students[
    (students[:, 3] < 75) &
    (students[:, 6]) < 60
]

print("\n ---- CRITICAL CONDITIONS ----")
print(critical_students)


# top performing students

top_stu = students[students[:, 6] >= 85]

print("\n ---- TOP PERFORMING STUDENTS ----")
print(top_stu)


# high study hours
high_study = students[students[:, 2] >= 5]
print("\n ---- HIGH STUDY STUDENTS ----")
print(high_study)


# low study hours
low_study = students[students[:, 2] < 5]
print("\n ---- LOW STUDY STUDENTS ----")
print(low_study)

# overall

overall = (
    assignment * 0.20
    + midterm * 0.30
    + final * 0.50
)

print("\n ---- OVERALL SCORES ----")
print(overall)

# performance categories

performance = np.where(
    overall >= 80,
    "Excellent",
    np.where(
        overall >= 60,
        "Good",
        "Needs Improvement"
    )
)

print("\n----- PERFORMANCE CATEGORY -----")

for i in range(len(students)):

    print(
        "Student ID:",
        stu_id[i],
        "| Overall:",
        round(overall[i], 2),
        "| Performance:",
        performance[i]
    )