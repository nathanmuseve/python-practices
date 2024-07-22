        # THE QUESTION 
# Write a function that prompts the user to input student marks. The input should be between 0 and 100. The output should correspond the correct grade, as shown below: 
# A > 79, B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40.

    #Prompt to let the Student enter makrs entered between o and 100
print("Enter your marks.Note that marks should be between 0 and 100")
marks = int(input()) 
grades = ["A", "B", "C", "D", "E"] #grades
comment = ["Excellent", "Very Good", "Good", "Average", "Failed.Please apply for retake exams."]
nomarks = str()
if 0 <= marks >= 79 and marks <= 100: 
        print("Your grade is:", grades[0],".", comment[0],".",  "And ") 
        print("Your makrs is:", marks)
        
elif 60 <= marks <= 78:
        print("Your grade is:", grades[1],".", comment[1],".", "And ") 
        print("Your makrs is:", marks)
        
elif 49 <= marks <= 59: 
        print("Your grade is:", grades[2],".", comment[2],".", "And ") 
        print("Your makrs is:", marks)
        
elif 40 <= marks <= 48: 
        print("Your grade is:", grades[3],".", comment[3],".", "And ") 
        print("Your makrs is:", marks)
        
elif 0 <= marks <= 39: 
        print("Your grade is:", grades[4],".", comment[4],".", "And ")
        print("Your makrs is:", marks)
        
elif nomarks:
        print("Invalid marks!")
        print("Enter your marks.Note that marks should be between 0 and 100") 
        print("Your makrs is:", marks)
elif marks == marks:
        print("Done Processing marks! No grade for such marks. Please enter the correct Marks!")
else:
        print("Seek medication!")
                
            # THE END OF THE PROGRAM 