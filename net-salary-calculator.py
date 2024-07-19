# Write a program whose major task is to calculate an individual’s Net Salary by getting the inputs of basic salary and benefits. Calculate the payee (i.e. Tax), NHIF Deductions, NSSF Deductions, gross salary, and net salary. 


# Monthly Taxable Pay (Ksh)	Annual Taxable Pay (Ksh)	Rate of Tax (%)
# Up to 24,000	Up to 288,000	10.0
# 24,001 - 32,333	288,001 - 388,000	25.0
# 32,334 - 500,000	388,001 - 6,000,000	30.0
# 500,001 - 800,000	6,000,001 - 9,600,000	32.5
# Above 800,000	Above 9,600,000	35.0

import random
basic_salary = int(input("Enter your Basic Income:"))
total_loans = int(input("Enter any amount of pending loans:"))
house_allowances = int(input("Enter your House allowance:"))
medical_allowances = int(input("Enter your Medical allowances:"))
commuter_allowances = int(input("Enter your Commuter allowances:"))
any_other_benefits = int(input("Enter any other allowances(combined) that you receive monthly. eg sitting allowances, laughing and smiling allowances etc:"))

#gross salary 
gross_salary = basic_salary + house_allowances + medical_allowances + commuter_allowances  + any_other_benefits
print(f"Your Gross salary is: {gross_salary:.2f}.")
#Tax earning categories or tax bands
first_band = 24000 #rate = 0.10
second_band = 32333 #rate = 0.25
third_band = 500000 #rate = 0.30
fourth_band = 800000 #rate = 0.325
above_band = 800000 #rate = 0.35

# paye
first_band_tax = (first_band ) * 0.10
second_band_tax = (second_band - first_band) * 0.25
third_band_tax = (gross_salary - second_band) * 0.30
fourth_band_tax = (gross_salary - third_band) * 0.325
above_band_tax = (gross_salary - fourth_band) * 0.35

paye1 = first_band_tax 
paye2 = first_band_tax + second_band_tax
paye3 = first_band_tax + second_band_tax + third_band_tax
paye4 = first_band_tax + second_band_tax + third_band_tax + fourth_band_tax
paye_above = first_band_tax + second_band_tax + third_band_tax + fourth_band_tax + above_band_tax

# Tier	Pensionable Pay NSSF
# I	Up to 7,000
# II	7,001 - 36,000
nssf = 0.06

##housing levy 
house_levy = 0.015 #on income_after tax
   #OTHER PAYE PARAMETERS 
personal_relief = 2400	
insurance_relief =	5000
total_relief = personal_relief
disability_exemption = 150000

#total deductions
total_deductions = total_loans  + (house_levy * gross_salary) + insurance_relief
#taxable income. PAYE CALCULATION
def pAYE():
  global paye
  paye = 0
  if gross_salary < first_band:
    paye
    print(f"You have paid a tax amount of: {paye:.2f}")
  elif gross_salary == first_band:
    paye += paye1
    print(f"You have paid a tax amount of: {paye1:.2f}")
  elif gross_salary > first_band and gross_salary <= second_band:
    paye += paye2
    print(f"You have paid a tax amount of: {paye2:.2f}")
  elif gross_salary > second_band and gross_salary <= third_band:
    paye += paye3
    print(f"You have paid a tax amount of: {paye3:.2f}")
  elif gross_salary > third_band and gross_salary <= fourth_band:
    paye += paye4
    print(f"You have paid a tax amount of: {paye4:.2f}")
  elif gross_salary > fourth_band and gross_salary >= fourth_band:
    paye += paye_above
    print(f"You have paid a tax amount of: {paye_above:.2f}")
  else:
    print("Oops! Invalid Gross Salary amount!")
pAYE()


  #  DEDUCTIONS 
# NHIF Deductions 
# Gross Pay (Ksh)	Deduction (Ksh)	 	Gross Pay (Ksh)	Deduction (Ksh)
# Up to 5,999	150	 	40,000 - 44,999	1,000
# 6,000 - 7,999	300	 	45,000 - 49,999	1,100
# 8,000 - 11,999	400	 	50,000 - 59,999	1,200
# 12,000 - 14,999	500	 	60,000 - 69,999	1,300
# 15,000 - 19,999	600	 	70,000 - 79,999	1,400
# 20,000 - 24,999	750	 	80,000 - 89,999	1,500
# 25,000 - 29,999	850	 	90,000 - 99,999	1,600
# 30,000 - 34,999	900	 	100,000 and above	1,700
# 35,000 - 39,999	950	

def nHIF():
  global nhif
  if gross_salary <= 5999:
    nhif = 150
  elif gross_salary <= 7999:
    nhif = 300
  elif gross_salary <= 11999:
    nhif = 400
  elif gross_salary <= 14999:
    nhif = 500
  elif gross_salary <= 19999:
    nhif = 600
  elif gross_salary <= 24999:
    nhif = 750
  elif gross_salary <= 34999:
    nhif = 850
  elif gross_salary <= 39999:
    nhif = 900
  elif gross_salary <= 44999:
    nhif = 1000
  elif gross_salary <= 49999:
    nhif = 1100
  elif gross_salary <= 59999:
    nhif = 1200
  elif gross_salary <= 69999:
    nhif = 1300
  elif gross_salary <= 79999:
    nhif = 1400
  elif gross_salary <= 89999:
    nhif = 1500
  elif gross_salary <= 99999:
    nhif = 1600
  else:
    nhif = 1700
nHIF()

income_after_tax = gross_salary - paye 
print(f"Your income after tax is :{(income_after_tax + personal_relief):.2f}")
print(f"Your NSSF contribution of {(nssf * income_after_tax):.2f} has been sumitted to your NSSF account.")
print(f"Your NHIF contribution of {nhif:.2f}  has been submitted to your NHIF account.")
net_income = income_after_tax - (total_deductions + nhif + (nssf * income_after_tax))
print(f"Your Net income is {net_income:.2f}")
 

  # print("")
  # print("")