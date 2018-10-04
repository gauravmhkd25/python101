print("*************************************",'\n')
print(" "*5+"\033[1;32;40mBODY MASS INDEX calculator\033[0m\n")
print("*************************************")
#Header with allignment and coloured Text

weight=int(input("Your weight in Kg: "))
height=int(input("Your height in cms: "))
#accepting user Weight and Height in respective variables

bmi_value=round((weight*10000/height**2),1)
#calculating bmi using the formula and storing it in bmi_value
#formula: weight(in kg)/height(in m^2)

print("Your Body mass index is: ",bmi_value,end=', ')
#printing result

if bmi_value < 18.5:
    print("which is \033[1;33;40munderweight\033[0m")
#if bmi is belore 18.5, the person is underweight, \033[1;33;40 is a colour code
elif 18.5 < bmi_value <= 25:
    print("Which is \033[1;32;40mnormal weight\033[0m")

elif 25 < bmi_value < 30:
    print("Which is \033[1;35m;40moverweight\033[0m")

else: print("Which is \033[1;31;40mObese\033[0m")
#if-else statement to catagorise the result and printing associated facts

#results: ✔
#1
#py ml_3_BodyMassIndex_calculator.py
#*************************************

#     BODY MASS INDEX calculator

#*************************************
#Your weight in Kg: 65
#Your height in cms: 174
#Your Body mass index is:  21.5, Which is normal weight

#2
#*************************************

#     BODY MASS INDEX calculator

#*************************************
#Your weight in Kg: 50
#Your height in cms: 123
#Your Body mass index is:  33.0, Which is Obese

#3
#*************************************

#     BODY MASS INDEX calculator

#*************************************
#Your weight in Kg: 45665
#Your height in cms: 12544
#Your Body mass index is:  2.9, which is underweight
