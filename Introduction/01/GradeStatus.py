
#average courses
def StudentConditionChecker(average):
    if average >= 17:
        result = "Great"
    elif average >= 12:
        result="Normal"

    elif average <12:
        result="Fail"
    
    else : 
        result="Somethings Wrong happened"
    return result


for i in range (1,4):
    StudentName=input("please Write Student Name,surename")
    Course1 = float (input("Course 1 Score of Student"))
    Course2 = float (input("Course 1 Score of Student")) 
    Course3 = float (input("Course 1 Score of Student"))
    averageStudent =(Course1+Course2+Course3)/3  

    print("Student:",StudentName,"\n","Condition:",StudentConditionChecker(averageStudent))





