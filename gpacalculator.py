#A program to calculate Grade Point Average (GPA)

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
    print("\t" + str(grade))

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
print(f"You will need to earn {grade_req} on your next assignment to get {desired_gpa} average gpa.")

#Make a copy of the original grades, get user input and swap one grade
grades_copy = grades[:]

print("\nLet's see what your average gpa would have been if you did better / worse on an assignment.")
edit_grade = int(input("\nWhat grade would you like to change: "))
new_grade = int(input(f"What grade would you like to change {edit_grade} to: "))

#Finding the index of the grade to be modified and then updating it
#Another way to do this is to use the remove() method on grades_copy and then append the new grade to the list.

grade_index = grades.index(edit_grade)
grades_copy[grade_index] = new_grade

grades_copy.sort(reverse=True)

print("\nGrades Highest to Lowest:")

for grade in grades_copy:
    print("\t" + str(grade))


#Calculating the new average gpa
#We should write a function to calculate average gpa so that we do not need to rewrite the same code
new_average_gpa = round(sum(grades_copy) / len(grades_copy),2)

print(f"\n{name}'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades_copy)))
print("\tHighest Grade: " + str(max(grades_copy)))
print("\tLowest Grade: " + str(min(grades_copy)))
print("\tThe new average gpa is: " + str(new_average_gpa))

#Print a summary on how the average gpa changed
print(f"\nYour new average would be {new_average_gpa} compared to your real average of {average_gpa}.")
average_change = new_average_gpa - average_gpa
average_change = round(average_change,2)
print(f"That is a change of {average_change} points.")

#Too bad the original grades are still intact :).
print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go and ask for extra credit.\n")
