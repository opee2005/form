Discipline = ["computer engineering","computer science","electrical and electronic engineering","computer technology","information technology"]
First_Name = input("please Enter Your First Name: ")
Last_Name = input("Enter Your Last Name: ")
Email = list(input("Please Provide Your Functional Email Address: "))
Phone_Number = float(input("Enter Your Phone Number: "))
Age = eval(input("Enter Your Age: "))
Course_Of_Study = input("Enter Your Course Of Study: ")
if Course_Of_Study in Discipline and 22<=Age<35:
    print("Congrat", First_Name,"Proceed to the Aptitude Test")
    questions = ["Who won Nigeria 2019 Presidential Election?: ","The current Nigeria Senate President is from which State?: ","Akinwumi Ambode is the governor of which state?: ",
                 "Who is the richest man in Africa?: ", "The current Nigeria Minister of Power is Who?: " ]
    answers = ["Mohammed Buhari","Kwara","Lagos","Aliko Dangote","Raji Fashola"]
    num_right = 0
    for i in range(len(questions)):
        guess = input(questions[i])
        if guess.lower()==answers[i].lower():
            print("Correct")
            num_right =num_right+1
        else:
            print("Wrong. The Answer is", answers[i])
        print("You have", num_right, "out of",i+1, "right")
    print(First_Name,"Your Final Score is", num_right,"You will be Contact for the next line of action. Thanks")
else:
     print("Thanks", First_Name,"for your interest, But You are not Qualified for this Post")
    
