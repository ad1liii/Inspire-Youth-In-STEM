#Write a program that calculates 16% tax on income ranging between 100k-150k

#19% tax if income is between 150k-300k

#30% if income is above 300k

#5% if income is less than 100k

#Print gross income and net income

income=input("Enter your net income")

gross_income= int(input("What is your gross income?"))

tax_group_a=(gross_income*0.05)
tax_group_b=(gross_income*1.6)
tax_group_c=(gross_income*1.9)
tax_group_d=(gross_income*0.3)

if gross_income <= 100000:
    print("Gross income:",gross_income)
    print("Tax:",tax_group_a)
    print("Net income:",gross_income-tax_group_a)
elif (gross_income >= 100001) & (gross_income <= 150000):
    print("Gross income:",gross_income)
    print("Tax:",tax_group_b)
    print("Net income:",gross_income-tax_group_b)

elif (gross_income <= 150001) & (gross_income <= 300000):
    print("Gross income:",gross_income)
    print("Tax:",tax_group_c)
    print("Net income:",gross_income-tax_group_c)
elif (gross_income > 300000):
    print("Gross income:",gross_income)
    print("Tax:",tax_group_d)
    print("Net income:",gross_income-tax_group_d)


    
