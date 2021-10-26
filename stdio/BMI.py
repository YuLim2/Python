weight = int(input("체중은? "))
height = int(input("키는? "))
BMI = weight / ((height/100) * (height/100))
print(f'당신의 BMI는 {BMI:.2f} 입니다.')