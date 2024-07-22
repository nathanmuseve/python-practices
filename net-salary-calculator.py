# Write a program whose major task is to calculate an individual’s Net Salary by getting the inputs of basic salary and benefits. Calculate the payee (i.e. Tax), NHIF Deductions, NSSF Deductions, gross salary, and net salary. 

  #Instruction
print(f"This program intends to collect your Basic Salary and allowances and returns Gross Salary, Income Tax(PAYE), Income After Tax, NSSF and NHIF contributions, Housing Levy deduction and your Net Icome(Net salary). Enter a valid value greater than 0. Gross Salary below Ksh{24000:,.2f} is Exempted from Tax.")
"\n"
basic_salary = int(input("Enter your Basic Income:"))
total_loans = int(input("Enter any amount of pending loans:"))
house_allowances = int(input("Enter your House allowance:"))
medical_allowances = int(input("Enter your Medical allowances:"))
commuter_allowances = int(input("Enter your Commuter allowances:"))
any_other_benefits = int(input("Enter any other allowances(combined) that you receive monthly. eg sitting allowances, laughing and smiling allowances etc:"))
print("\n") 
   #OTHER PAYE PARAMETERS 
personal_relief = 2400	
insurance_relief =	5000
total_relief = personal_relief
disability_exemption = 150000

#gross salary 
gross_salary = basic_salary + house_allowances + medical_allowances + commuter_allowances  + any_other_benefits - personal_relief

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

#Tax Calculations
paye1 = first_band_tax 
paye2 = first_band_tax + second_band_tax
paye3 = first_band_tax + second_band_tax + third_band_tax
paye4 = first_band_tax + second_band_tax + third_band_tax + fourth_band_tax
paye_above = first_band_tax + second_band_tax + third_band_tax + fourth_band_tax + above_band_tax

# Tier	Pensionable Pay NSSF
# I	Up to 7,000
# II	7,001 - 36,000
nssf = 0.06 #of income_after_tax

##housing levy 
house_levy = 0.015 #on income_after tax

#total deductions
total_deductions = total_loans  + (house_levy * gross_salary) + insurance_relief
#taxable income. PAYE CALCULATION
def pAYE():
  global paye
  paye = 0
  if gross_salary < first_band:
    paye
  elif gross_salary == first_band:
    paye += paye1
  elif gross_salary > first_band and gross_salary <= second_band:
    paye += paye2
  elif gross_salary > second_band and gross_salary <= third_band:
    paye += paye3
  elif gross_salary > third_band and gross_salary <= fourth_band:
    paye += paye4
  elif gross_salary > fourth_band and gross_salary >= fourth_band:
    paye += paye_above
  else:
    raise Exception("Oops! Invalid Gross Salary amount!")
pAYE()


  #  DEDUCTIONS 
  #NHIF Calculation
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

  # income_after_tax Calculation
income_after_tax = gross_salary - paye +personal_relief
   #net_income Calcution
net_income = income_after_tax - (total_deductions + nhif + (nssf * income_after_tax))
print(f"Your Gross salary is Ksh{gross_salary:,.2f}.\n")
  #PAYE
print(f"You have paid a tax amount, PAYE of Ksh{paye:,.2f}\n")
 #income_after_tax
print(f"Your Income after tax is Ksh{(income_after_tax):,.2f}\n")
 #NSSF Contribution
print(f"Your NSSF contribution of Ksh{(nssf * income_after_tax):,.2f} has been sumitted to your NSSF account.\n")
 #NHIF Contribution
print(f"Your NHIF contribution of Ksh{nhif:,.2f}  has been submitted to your NHIF account.")
 #Personal_relief
print(f"Did you know that for every Taxable/Gross income the government gives you a tax relief of Ksh{personal_relief:,.2f}? Now you know.\n")

 #Housing Levy
print(f"But did you know that Ksh{(house_levy * gross_salary):,.2f} was taken as an Housing levy? \n")
  #net_income 
print(f"Your Net income is Ksh{net_income:,.2f}\n")
print("You were served by Nathan Museve.")

    # THE END OF THE PROGRAM 