""" Brilliant School sets an exam wherein, 
    English exam is for 80 marks, 
    Science for 90 marks and 
    Mathematics for 100 marks. 

Ask the student to enter the marks scored in each of these exams. 
Calculate the total percentage marks and rank the student as below :
   - First Class if score is more than or equal to 90 %
   - Second Class if score is more than or equal to 75%
   - Average if student has not failed
   - Failed if score is less than or equal to 35 %
"""

def marks(English,Science,Mathematics):
    Total=(English+Science+Mathematics)/3
    if Total>=int(90):
        print("The student has scored first class")
    elif Total>=int(75):
         print("The student  has scored second class")
    elif Total<=int(50) and Total>int(35):
         print("The student has scored Average")
    elif Total<=int(35):
         print("The student has failed")    
        
    

def main():
    subj1=int(input("Enter the marks  scored in English:"))
    subj2=int(input("Enter the marks  scored in Science:"))
    subj3=int(input("Enter the marks  scored in Mathematics:"))
    marks(subj1,subj2,subj3)

# Main starts from here
main()
