yearsSinceBirth = input("Enter the number of years since your birth: ")
monthsSinceLastBirthday = input("Enter the number of months since your last birthday: ")
daysSinceBirthDateLastMonth = input("Enter the days since your birth date last month: ")
daysOld = yearsSinceBirth * 365 + monthsSinceLastBirthday * 30 + daysSinceBirthDateLastMonth
print("Days since your birth: " + str(daysOld))