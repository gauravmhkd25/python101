print("*************************************",'\n')
print(" "*5+"\033[1;32;40mBODY MASS INDEX calculator\033[0m\n")
print("*************************************")

weight=int(input("Your weight in Kg: "))
height=int(input("Your height in cms: "))

bmi_value=round((weight*10000/height**2),1)

print("Your Body mass index is: ",bmi_value,end=', ')

if bmi_value < 18.5:
    print("which is \033[1;33;40munderweight\033[0m")

elif 18.5 < bmi_value <= 25:
    print("Which is \033[1;32;40mnormal weight\033[0m")

elif 25 < bmi_value < 30:
    print("Which is \033[1;35m;40moverweight\033[0m")

else: print("Which is \033[1;31;40mObese\033[0m")
