#assignment pre_8
sub1 = int(input("Enter marks of subject1 : "))
sub2 = int(input("Enter marks of subject2 : "))
sub3 = int(input("Enter marks of subject3 : "))
sub4 = int(input("Enter marks of subject4 : "))
sub5 = int(input("Enter marks of subject5 : "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage	>=	90:     Grade = 'O'
elif percentage	>=	80:	    Grade = 'A'
elif percentage	>=	70:	    Grade = 'B'
elif percentage	>=	60:	    Grade = 'C'
elif percentage	>=	50:     Grade = 'D'
elif percentage	>=	40:	    Grade = 'E'
elif percentage <   40:     Grade = 'F'
print("^^^"*25)
print("\nsubject 1 : ",sub1,
      "\nsubject 2 : ",sub2,
      "\nsubject 3 : ",sub3,
      "\nsubject 4 : ",sub4,
      "\nsubject 5 : ",sub5)
print("Total marks is :",total)
print("Your Percentage is :",percentage)
print("Percentage = {:.2f}%".format(percentage))
print("Your Grade is : ",Grade)
print("^^^"*25)