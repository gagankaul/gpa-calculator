# A program to calculate Grade Point Average (GPA)

print("Welcome to the Grade Point Average (GPA) Calculator App\n")

#Get user input
name = input("What is your name: ").title()
num_grades = int(input("How many grades would you like to enter: "))

grades = []

for grade in range(num_grades):
    grades.append(int(input("Enter grade: ")))

#Organize the grades in descending order
grades.sort(reverse=True)

#Print the output in a structured format from highest to lowest
print("\nGrades Highest to Lowest:")

for grade in grades:
    print("\t\t" + str(grade))

average_gpa = round(sum(grades) / len(grades),2)

print(f"\n{name}'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average_gpa))


#Get user input for his/her desired gpa
desired_gpa = float(input("\nWhat is your desired average: "))

#Calculate grade required on the next assignment to get the desired gpa
grade_req = (desired_gpa * (len(grades) + 1)) - sum(grades)
grade_req = round(grade_req, 2)

print("\nGood luck " + name + "!")
print(f"You will need to score {grade_req} on your next assignment to get an average gpa of {desired_gpa}.")

#Copy of your original grades
grades_copy = grades[:]

edit_grade = int(input("\nWhat grade value would you like to change? "))
new_grade = int(input("\nWhat value would you like this grade to be changed to? "))

#Finding the index of the grade to be edited and then updating it
grade_index = grades.index(edit_grade)
grades_copy[grade_index] = new_grade

#Calculating the new average gpa
average_gpa = round(sum(grades_copy) / len(grades_copy),2)

print(f"\n{name}'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades_copy)))
print("\tHighest Grade: " + str(max(grades_copy)))
print("\tLowest Grade: " + str(min(grades_copy)))
print("\tThe new average is: " + str(average_gpa))