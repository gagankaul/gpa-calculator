# A program to calculate Grade Point Average (GPA)

print("Welcome to the Grade Point Average (GPA) Calculator App\n")

name = input("What is your name: ").title()
num_grades = int(input("How many grades would you like to enter: "))

grades = []

for grade in range(num_grades):
    grades.append(int(input("Enter grade: ")))

grades.sort(reverse=True)

print("\nGrades Highest to Lowest:")


for grade in grades:
    print("\t\t" + str(grade))

average_gpa = round(sum(grades) / len(grades),2)

print(f"\n{name}'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average_gpa))

desired_gpa = float(input("\nWhat is your desired average: "))

grade_req = (desired_gpa * (len(grades) + 1)) - sum(grades)

print(f"You will need to score {grade_req} to get an average gpa of {desired_gpa}.")


print("\nGood luck " + name + "!")
