owner_age = int(input("enter owner age -->"))
monthly_revenue = float(input("Monthly revenue -->"))
credit_score = int(input("your credit score -->"))
years_in_business = float(input("Your years in business -->"))
has_defaults = bool(eval(input("Do you have defaults? (True/False) -->")))
collateral_name = str(input("Your collateral name -->"))
collateral_value = float(input("what's the value of your collateral? -->"))

ml = 0
bf = 0

if owner_age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    #tier 1:
    if credit_score >= 720:
        ml = 3 * monthly_revenue
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", ml)
        print("HIGH CREDIT SCORE")
        if monthly_revenue >= 50000:
            print("REVENUE HIGHER THAN 50K")
            bf = ml * 0.015
            print("BASE FEE IS SET TO", bf)
        else:
            bf = ml * 0.025
            print("BASE FEE IS SET TO", bf)
        if collateral_value >= ml:
            print("Collateral", collateral_name, "with a value of", collateral_value, "is accepted")
        else: 
            print("rejected: insufficient collateral value for", collateral_name)
        #surcharge
        sfr
        if collateral_value % 5000:
            pass
    #tier 2
    elif 620 <= credit_score < 720:
        print("Credit score within 620 and 720")
        ml = monthly_revenue * 0.015
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", ml)
        if years_in_business >= 5.0:
            bf = 0.02
            print("BASELINE FEE IS SET TO", bf)
        else:
            bf = 0.035
            print("BASELINE FEE IS SET TO", bf)
            if collateral_value >= ml:
                print("collateral", collateral_name, "With a value of", collateral_value)
            else: 
                print("Rejected for the collateral value of collateral named", collateral_name)

    #tier 3
    elif credit_score < 620:
        print("Rejected: Credit score is too low")
#collateral and modulus fee rules part






else:
    print("YOU'RE NOT QUALIFIED")
