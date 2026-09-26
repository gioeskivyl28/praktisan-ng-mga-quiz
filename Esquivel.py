owner_age = int(input("enter owner age -->"))
monthly_revenue = float(input("Monthly revenue -->"))
credit_score = int(input("your credit score -->"))
years_in_business = float(input("Your years in business -->"))
has_defaults = bool(eval(input("Do you have defaults? (True/False) -->")))
collateral_name = str(input("Your collateral name -->"))
collateral_value = float(input("what's the value of your collateral? -->"))

if owner_age < 21 or years_in_business < 2.0 or has_defaults == True:
    print("Rejected: High risk Application or Inelligible Owner")
    
    #Tier 1
    max_loan_limit = 0
    fee_rate = 0

    if credit_score >= 720:
        max_Loan_limit = 3 * monthly_revenue
        if monthly_revenue >= 50000:
            fee_rate = 1.5
        else:
            fee_rate = 2.5
            tier_passed = True

    #Tier 2
    elif 620 <= credit_score <720:
        max_loan_limit = 1.5 * monthly_revenue
        if years_in_business >= 5.0:
            fee_rate = 2.0
        else:
            fee_rate = 3.5
            tier_passed = True

    #Tier 3
    else:
        credit_score < 620
        print("rejected: Credit score below requirement") 
        tier_passed = False

# collateral and modulus fee rules (tier 1 and tier 2 only)
    if tier_passed == True:

        if collateral_value < max_loan_limit:
            print("Rejected: Insufficient collateral value for", collateral_name)

        else:
            base_fee = max_loan_limit * fee_rate 
            if int(collateral_value) % 5000 != 0:
                final_fee = base_fee + 250

print("Application approved")
print("mamamammam")
print("Next tym ko po tatapusin")
        
