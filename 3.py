no_of_months=36	#Number of Months for down payment													
portion_down_payment=0.25	#down payment fraction(default)
Annual_ROI = 0.04 #annual ROI on savings(default)
monthly_ROI=Annual_ROI/12 #monthly ROI on savings
semi_annual_raise=.07
total_cost=1000000.0
low=0
high=10000
down_payment_amount=total_cost*portion_down_payment   #calculate down payment amount
bisect_steps=0
#savings +-100
#bisection search
# annual_salary=float(input("Enter your starting salary : "))	#input annual salary
annual_salary=300000/2.0
monthly_salary=annual_salary/12 #calculating monthly salary
if down_payment_amount>monthly_salary*no_of_months:
    raise Exception("Down payment for house can't be done in 36 months")



while (1):
    monthly_salary=annual_salary/12
    current_savings=0.0	#current savings
    portion_saved=int((low+high)/2)
    bisect_steps+=1

    for i in range(0,no_of_months):	#loop checks if the savings has reached more than the down payment value
        
        current_savings+=(portion_saved*monthly_salary/10000)+(current_savings*monthly_ROI) #calculating new savings based on ROI
        if  (no_of_months % 6) == 0 and (no_of_months!= 0):   #checking if its time for a raise
            monthly_salary+=monthly_salary*semi_annual_raise        #accounting for rise in salary every 6 months         
    current_savings=round(current_savings,2)
    print(portion_saved)
    if current_savings>(down_payment_amount+100):
        high=portion_saved
    elif current_savings<(down_payment_amount-100):
        low=portion_saved
    else:
        print("low: ",low, "high: ",high, "mid:", portion_saved,"+sav",current_savings)
        break
    
print("Portion of salary to be saved : ",portion_saved/10000.0)
print(" bisect steps : ",bisect_steps)        



# raise NotImplementedError()


