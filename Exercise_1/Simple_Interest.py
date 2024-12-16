principal_amount = int(input("Enter the Principal Amount : "))
rate_of_interest = float(input("Enter the Rate of Interest : "))
time_period = float(input("Enter the Time Period (in years) : "))
simple_interest = (principal_amount * rate_of_interest * time_period) / 100
print("Simple Interest : " + str(simple_interest))