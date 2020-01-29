x=' ';

#The 'x' variable is used to create spacing in the program text.

import math

#The math plugin is used to truncate decimal places later in the program.

print("Welcome to the rate calculator - By Nick H!")
print("Options currently only include A+ Life Insurance for ACTIVE employees.")
print(x)
H5=(-1)
while True:
    try:
       H5=(float(input("Please enter the EE's High 5 NSTAE amount here: ")))
       while H5<0:
         print(x)
         print("invalid input!")
         print(x)
         H5=(float(input("Please enter the EE's High 5 NSTAE amount here: ")))
       break
    except ValueError:
        print(x)
        print("invalid input!")
        print(x)


#The H5 variable is the High 5 NSTAE amount determined by the software. It can also be manually calculated using the OLR.

print(x)
print("The employee's H5 NSTAE amount = $",H5,"")
print(x)

while True:
    try:
       CL=(float(input("Please enter the EE's desired coverage level between 1 and 12 here: ")))
       while CL<0 or CL>12:
         print(x)
         print("invalid input!")
         print(x)
         CL=(float(input("Please enter the EE's desired coverage level here: ")))
       break
    except ValueError:
        print(x)
        print("invalid input!")
        print(x)

print(x)
print("The desired coverage amount is = ",CL,"x the employee's salary, which is $",CL*H5,"")
print(x)

#H5 gets divided by 1000 as per the calculation instructions in the OLR. See below.

while True:
    try:
       AgeC=(float(input("Please enter the EE's age here: ")))
       while AgeC<0:
         print(x)
         print("invalid input!")
         print(x)
         AgeC=(float(input("Please enter the EE's age here: ")))
       break
    except ValueError:
        print(x)
        print("invalid input!")
        print(x)

AgeC=math.trunc(AgeC)
print(x)
print("The employees age is ",AgeC,"years old.")
print(x)

#The AgeC variable will be used to calculate either the employees Term or GUL age-specific rate.

TorGList= ["t", "T", "g", "G"]

#The TorGList is a list to make sure that the upcoming user input is actually 't' or 'g', in any possible capitalization. Any input is converted to lowercase below.

TorG=("f")
TorG=(input("Please enter 't' or 'g' to select whether the employee is enrolled in a Term or GUL type plan: "))

#The TorG string variable is used to determine the type of A+ plan the EE is enrolled in (Term or GUL).

while TorG not in TorGList:
  print(x)
  print("invalid input!")
  print(x)
  TorG=(input("Please enter 't' or 'g' to select whether the employee is enrolled in a Term or GUL type plan: "))

while TorG is ("t"):
  if AgeC in range(int(15, 24)):
    tRate=0.0066
  elif AgeC>=25 and AgeC<30:
    tRate=0.0079
  elif AgeC>=30 and AgeC<35:
    tRate=0.0105
  elif AgeC>=35 and AgeC<40:
    tRate=0.0118
  elif AgeC>=40 and AgeC<45:
    tRate=0.0147
  elif AgeC>=45 and AgeC<50:
    tRate=0.0220
  elif AgeC>=50 and AgeC<55:
    tRate=0.0338
  elif AgeC>=55 and AgeC<60:
    tRate=0.0632
  elif AgeC>=60 and AgeC<65:
    tRate=0.0999
  elif AgeC>=65 and AgeC<70:
    tRate=0.2760
  elif AgeC>=70 and AgeC<75:
    tRate=0.4509
  elif AgeC>=75 and AgeC<80:
    tRate=0.7683
  elif AgeC>=80 and AgeC<85:
    tRate=1.2445
  elif AgeC>=85 and AgeC<90:
    tRate=2.0151
  elif AgeC>=90 and AgeC<95:
    tRate=3.2642
  elif AgeC>=95:
    tRate=5.2884
  else:
    break
    