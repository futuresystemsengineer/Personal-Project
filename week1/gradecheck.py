first_grade = int(input("How much was your first grade? "))
second_grade = int(input("How much was your second grade? "))
third_grade = int(input("How much was your third grade? "))

average = float(first_grade + second_grade + third_grade) /3
if average >= 10:
    print(f"Your average was {average:.2f}, congratulations, you approved")
else:
    print(f"Your average was {average:.2f}, unfortunately, you didn't approve :(")