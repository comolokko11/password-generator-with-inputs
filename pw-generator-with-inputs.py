#Password Generator with first and last digit of Name, Surname + The sum of the odd numbers in the last 4 digits of the school number.

name = input("Enter your name: ")
surname = input("Enter you surname: ")
school_number = input("Enter your school number: ")

pwName = name[0] + name[-1]
pwSurname = surname[0] + surname[-1]
last4digits = school_number[-4:]
sumOfPw = 0

for oddSum in last4digits:
    if int(oddSum) % 2 == 1:
        sumOfPw += int(oddSum)


print(pwName + pwSurname + str(sumOfPw))