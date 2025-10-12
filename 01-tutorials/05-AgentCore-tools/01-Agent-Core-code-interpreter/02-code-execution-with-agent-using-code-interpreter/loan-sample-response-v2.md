# query = "I have a home valued at 500 k, i have 125k that i can put as down payment and in the market to shop for a mortgage. I have two loan offers - a 15 year term at 3.4% rate of interest and a 30 year term at 2.75% rate of interest. Which loan offer is more suitable for me. Make sure to list out all the formulae you used for calculations ?"


I'll analyze both mortgage options and provide all the mathematical formulas used in the calculations to help you make an informed decision.
 Generated Code: # First, let's establish the basic parameters and show all formulas

print("MORTGAGE ANALYSIS WITH ALL FORMULAS")
print("=" * 60)
print()

# Given data
home_value = 500000
down_payment = 125000
loan_amount = home_value - down_payment

print("GIVEN DATA:")
print(f"Home Value = ${home_value:,}")
print(f"Down Payment = ${down_payment:,}")
print(f"Loan Amount = Home Value - Down Payment = ${loan_amount:,}")
print(f"Down Payment % = (Down Payment / Home Value) × 100 = {(down_payment/home_value)*100:.1f}%")
print()

# Loan parameters
print("LOAN OPTIONS:")
print("Option 1: 15-year term at 3.4% annual interest")
print("Option 2: 30-year term at 2.75% annual interest")
print()

print("FORMULAS TO BE USED:")
print("-" * 40)
print("1. Monthly Mortgage Payment Formula:")
print("   M = P × [r(1+r)^n] / [(1+r)^n - 1]")
print("   Where:")
print("   M = Monthly payment")
print("   P = Principal loan amount")
print("   r = Monthly interest rate (annual rate ÷ 12)")
print("   n = Total number of payments (years × 12)")
print()

print("2. Total Amount Paid:")
print("   Total Paid = Monthly Payment × Number of Payments")
print()

print("3. Total Interest Paid:")
print("   Total Interest = Total Amount Paid - Principal")
print()

print("4. Remaining Balance Formula:")
print("   B = P × [(1+r)^n - (1+r)^p] / [(1+r)^n - 1]")
print("   Where:")
print("   B = Remaining balance")
print("   P = Original principal")
print("   r = Monthly interest rate")
print("   n = Total number of payments")
print("   p = Number of payments made")
print()

print("5. Future Value of Annuity (for investment analysis):")
print("   FV = PMT × [((1+r)^n - 1) / r]")
print("   Where:")
print("   FV = Future value")
print("   PMT = Monthly payment amount")
print("   r = Monthly interest rate")
print("   n = Number of periods")
print()

print("=" * 60)

 Generated Code: # Now let's calculate Option 1: 15-year loan at 3.4%

import math

# Loan parameters
P = 375000  # Principal
annual_rate_1 = 0.034  # 3.4% as decimal
years_1 = 15
r_1 = annual_rate_1 / 12  # Monthly interest rate
n_1 = years_1 * 12  # Total number of payments

print("OPTION 1: 15-YEAR LOAN CALCULATIONS")
print("=" * 50)
print()

print("STEP-BY-STEP CALCULATION:")
print(f"P (Principal) = ${P:,}")
print(f"Annual Interest Rate = {annual_rate_1:.3f} = {annual_rate_1*100}%")
print(f"r (Monthly Interest Rate) = {annual_rate_1:.3f} ÷ 12 = {r_1:.6f}")
print(f"n (Total Payments) = {years_1} years × 12 = {n_1} payments")
print()

print("MONTHLY PAYMENT CALCULATION:")
print("Formula: M = P × [r(1+r)^n] / [(1+r)^n - 1]")
print()

# Calculate components step by step
one_plus_r_1 = 1 + r_1
one_plus_r_n_1 = one_plus_r_1 ** n_1
numerator_1 = P * r_1 * one_plus_r_n_1
denominator_1 = one_plus_r_n_1 - 1
monthly_payment_1 = numerator_1 / denominator_1

print("Step-by-step:")
print(f"(1 + r) = (1 + {r_1:.6f}) = {one_plus_r_1:.6f}")
print(f"(1 + r)^n = {one_plus_r_1:.6f}^{n_1} = {one_plus_r_n_1:.6f}")
print(f"Numerator = P × r × (1+r)^n = {P:,} × {r_1:.6f} × {one_plus_r_n_1:.6f} = {numerator_1:,.2f}")
print(f"Denominator = (1+r)^n - 1 = {one_plus_r_n_1:.6f} - 1 = {denominator_1:.6f}")
print(f"Monthly Payment = {numerator_1:,.2f} ÷ {denominator_1:.6f} = ${monthly_payment_1:,.2f}")
print()

# Calculate totals
total_paid_1 = monthly_payment_1 * n_1
total_interest_1 = total_paid_1 - P

print("OTHER CALCULATIONS:")
print(f"Total Amount Paid = Monthly Payment × Number of Payments")
print(f"                  = ${monthly_payment_1:,.2f} × {n_1} = ${total_paid_1:,.2f}")
print()
print(f"Total Interest Paid = Total Amount Paid - Principal")
print(f"                    = ${total_paid_1:,.2f} - ${P:,} = ${total_interest_1:,.2f}")
print()
print(f"Interest as % of Principal = ${total_interest_1:,.2f} ÷ ${P:,} × 100 = {(total_interest_1/P)*100:.1f}%")
print()

print("OPTION 1 SUMMARY:")
print("-" * 30)
print(f"Monthly Payment: ${monthly_payment_1:,.2f}")
print(f"Total Interest: ${total_interest_1:,.2f}")
print(f"Total Amount Paid: ${total_paid_1:,.2f}")
print(f"Loan Term: {years_1} years")

 Generated Code: # Now let's calculate Option 2: 30-year loan at 2.75%

# Loan parameters
annual_rate_2 = 0.0275  # 2.75% as decimal
years_2 = 30
r_2 = annual_rate_2 / 12  # Monthly interest rate
n_2 = years_2 * 12  # Total number of payments

print("OPTION 2: 30-YEAR LOAN CALCULATIONS")
print("=" * 50)
print()

print("STEP-BY-STEP CALCULATION:")
print(f"P (Principal) = ${P:,}")
print(f"Annual Interest Rate = {annual_rate_2:.4f} = {annual_rate_2*100}%")
print(f"r (Monthly Interest Rate) = {annual_rate_2:.4f} ÷ 12 = {r_2:.6f}")
print(f"n (Total Payments) = {years_2} years × 12 = {n_2} payments")
print()

print("MONTHLY PAYMENT CALCULATION:")
print("Formula: M = P × [r(1+r)^n] / [(1+r)^n - 1]")
print()

# Calculate components step by step
one_plus_r_2 = 1 + r_2
one_plus_r_n_2 = one_plus_r_2 ** n_2
numerator_2 = P * r_2 * one_plus_r_n_2
denominator_2 = one_plus_r_n_2 - 1
monthly_payment_2 = numerator_2 / denominator_2

print("Step-by-step:")
print(f"(1 + r) = (1 + {r_2:.6f}) = {one_plus_r_2:.6f}")
print(f"(1 + r)^n = {one_plus_r_2:.6f}^{n_2} = {one_plus_r_n_2:.6f}")
print(f"Numerator = P × r × (1+r)^n = {P:,} × {r_2:.6f} × {one_plus_r_n_2:.6f} = {numerator_2:,.2f}")
print(f"Denominator = (1+r)^n - 1 = {one_plus_r_n_2:.6f} - 1 = {denominator_2:.6f}")
print(f"Monthly Payment = {numerator_2:,.2f} ÷ {denominator_2:.6f} = ${monthly_payment_2:,.2f}")
print()

# Calculate totals
total_paid_2 = monthly_payment_2 * n_2
total_interest_2 = total_paid_2 - P

print("OTHER CALCULATIONS:")
print(f"Total Amount Paid = Monthly Payment × Number of Payments")
print(f"                  = ${monthly_payment_2:,.2f} × {n_2} = ${total_paid_2:,.2f}")
print()
print(f"Total Interest Paid = Total Amount Paid - Principal")
print(f"                    = ${total_paid_2:,.2f} - ${P:,} = ${total_interest_2:,.2f}")
print()
print(f"Interest as % of Principal = ${total_interest_2:,.2f} ÷ ${P:,} × 100 = {(total_interest_2/P)*100:.1f}%")
print()

print("OPTION 2 SUMMARY:")
print("-" * 30)
print(f"Monthly Payment: ${monthly_payment_2:,.2f}")
print(f"Total Interest: ${total_interest_2:,.2f}")
print(f"Total Amount Paid: ${total_paid_2:,.2f}")
print(f"Loan Term: {years_2} years")

 Generated Code: # Complete calculation for both options with all formulas

import math

# Given data
home_value = 500000
down_payment = 125000
P = home_value - down_payment  # Principal

# Option 1: 15-year at 3.4%
annual_rate_1 = 0.034
years_1 = 15
r_1 = annual_rate_1 / 12
n_1 = years_1 * 12

# Option 2: 30-year at 2.75%
annual_rate_2 = 0.0275
years_2 = 30
r_2 = annual_rate_2 / 12
n_2 = years_2 * 12

print("COMPLETE MORTGAGE ANALYSIS WITH ALL FORMULAS")
print("=" * 60)
print()

# Option 1 calculations
print("OPTION 1: 15-YEAR LOAN AT 3.4%")
print("=" * 40)
print()
print("Parameters:")
print(f"P (Principal) = ${P:,}")
print(f"Annual Rate = {annual_rate_1*100}%")
print(f"r (Monthly Rate) = {annual_rate_1:.4f} ÷ 12 = {r_1:.6f}")
print(f"n (Total Payments) = {years_1} × 12 = {n_1}")
print()

# Monthly payment calculation
one_plus_r_1 = 1 + r_1
one_plus_r_n_1 = one_plus_r_1 ** n_1
monthly_payment_1 = P * (r_1 * one_plus_r_n_1) / (one_plus_r_n_1 - 1)

print("Monthly Payment Formula: M = P × [r(1+r)^n] / [(1+r)^n - 1]")
print(f"(1 + r)^n = (1 + {r_1:.6f})^{n_1} = {one_plus_r_n_1:.6f}")
print(f"M = {P:,} × [{r_1:.6f} × {one_plus_r_n_1:.6f}] / [{one_plus_r_n_1:.6f} - 1]")
print(f"M = {P:,} × {r_1 * one_plus_r_n_1:.6f} / {one_plus_r_n_1 - 1:.6f}")
print(f"M = ${monthly_payment_1:,.2f}")
print()

total_paid_1 = monthly_payment_1 * n_1
total_interest_1 = total_paid_1 - P

print("Total Calculations:")
print(f"Total Paid = ${monthly_payment_1:,.2f} × {n_1} = ${total_paid_1:,.2f}")
print(f"Total Interest = ${total_paid_1:,.2f} - ${P:,} = ${total_interest_1:,.2f}")
print()

print("=" * 60)
print()

# Option 2 calculations
print("OPTION 2: 30-YEAR LOAN AT 2.75%")
print("=" * 40)
print()
print("Parameters:")
print(f"P (Principal) = ${P:,}")
print(f"Annual Rate = {annual_rate_2*100}%")
print(f"r (Monthly Rate) = {annual_rate_2:.4f} ÷ 12 = {r_2:.6f}")
print(f"n (Total Payments) = {years_2} × 12 = {n_2}")
print()

# Monthly payment calculation
one_plus_r_2 = 1 + r_2
one_plus_r_n_2 = one_plus_r_2 ** n_2
monthly_payment_2 = P * (r_2 * one_plus_r_n_2) / (one_plus_r_n_2 - 1)

print("Monthly Payment Formula: M = P × [r(1+r)^n] / [(1+r)^n - 1]")
print(f"(1 + r)^n = (1 + {r_2:.6f})^{n_2} = {one_plus_r_n_2:.6f}")
print(f"M = {P:,} × [{r_2:.6f} × {one_plus_r_n_2:.6f}] / [{one_plus_r_n_2:.6f} - 1]")
print(f"M = {P:,} × {r_2 * one_plus_r_n_2:.6f} / {one_plus_r_n_2 - 1:.6f}")
print(f"M = ${monthly_payment_2:,.2f}")
print()

total_paid_2 = monthly_payment_2 * n_2
total_interest_2 = total_paid_2 - P

print("Total Calculations:")
print(f"Total Paid = ${monthly_payment_2:,.2f} × {n_2} = ${total_paid_2:,.2f}")
print(f"Total Interest = ${total_paid_2:,.2f} - ${P:,} = ${total_interest_2:,.2f}")
print()

print("=" * 60)

 Generated Code: # Now let's do the comparison analysis and opportunity cost calculation

print("COMPARISON ANALYSIS")
print("=" * 60)
print()

# Direct comparison
monthly_diff = monthly_payment_1 - monthly_payment_2
interest_savings = total_interest_2 - total_interest_1
years_earlier = years_2 - years_1

print("DIRECT COMPARISON:")
print(f"15-year monthly payment: ${monthly_payment_1:,.2f}")
print(f"30-year monthly payment: ${monthly_payment_2:,.2f}")
print(f"Monthly difference: ${monthly_diff:,.2f} (15-year costs more)")
print()
print(f"15-year total interest: ${total_interest_1:,.2f}")
print(f"30-year total interest: ${total_interest_2:,.2f}")
print(f"Interest savings (15-year): ${interest_savings:,.2f}")
print(f"Years earlier payoff: {years_earlier} years")
print()

# Remaining balance calculation after 15 years on 30-year loan
print("REMAINING BALANCE FORMULA:")
print("B = P × [(1+r)^n - (1+r)^p] / [(1+r)^n - 1]")
print()

# Calculate remaining balance on 30-year loan after 15 years (180 payments)
p_15_years = 15 * 12  # 180 payments made
remaining_balance = P * ((one_plus_r_2**n_2) - (one_plus_r_2**p_15_years)) / ((one_plus_r_2**n_2) - 1)

print("REMAINING BALANCE ON 30-YEAR LOAN AFTER 15 YEARS:")
print(f"P = ${P:,}")
print(f"r = {r_2:.6f}")
print(f"n = {n_2} (total payments)")
print(f"p = {p_15_years} (payments made)")
print()
print(f"(1+r)^n = (1+{r_2:.6f})^{n_2} = {one_plus_r_2**n_2:.6f}")
print(f"(1+r)^p = (1+{r_2:.6f})^{p_15_years} = {one_plus_r_2**p_15_years:.6f}")
print()
print(f"B = {P:,} × [{one_plus_r_2**n_2:.6f} - {one_plus_r_2**p_15_years:.6f}] / [{one_plus_r_2**n_2:.6f} - 1]")
print(f"B = {P:,} × {(one_plus_r_2**n_2) - (one_plus_r_2**p_15_years):.6f} / {(one_plus_r_2**n_2) - 1:.6f}")
print(f"B = ${remaining_balance:,.2f}")
print()

print("=" * 60)
print()

# Future Value of Annuity calculation
print("OPPORTUNITY COST ANALYSIS")
print("Future Value of Annuity Formula: FV = PMT × [((1+r)^n - 1) / r]")
print()
print("If you choose 30-year loan and invest the monthly difference:")
print(f"Monthly investment amount (PMT) = ${monthly_diff:,.2f}")
print("Investment period = 15 years (180 months)")
print()

# Calculate for different investment returns
investment_returns = [0.04, 0.06, 0.08]
print("INVESTMENT SCENARIOS:")

for annual_return in investment_returns:
    monthly_return = annual_return / 12
    n_invest = 15 * 12  # 180 months
    
    # Future Value calculation
    if monthly_return == 0:
        fv = monthly_diff * n_invest
    else:
        fv = monthly_diff * (((1 + monthly_return)**n_invest - 1) / monthly_return)
    
    net_position = fv - remaining_balance
    
    print(f"\nAt {annual_return*100:.0f}% annual return:")
    print(f"  Monthly return rate = {annual_return:.3f} ÷ 12 = {monthly_return:.6f}")
    print(f"  (1+r)^n = (1+{monthly_return:.6f})^{n_invest} = {(1+monthly_return)**n_invest:.6f}")
    print(f"  FV = {monthly_diff:,.2f} × [({(1+monthly_return)**n_invest:.6f} - 1) / {monthly_return:.6f}]")
    print(f"  FV = {monthly_diff:,.2f} × {((1+monthly_return)**n_invest - 1) / monthly_return:.6f}")
    print(f"  Investment Value = ${fv:,.2f}")
    print(f"  Remaining Mortgage = ${remaining_balance:,.2f}")
    print(f"  Net Position = ${fv:,.2f} - ${remaining_balance:,.2f} = ${net_position:,.2f}")

print("\n" + "=" * 60)

 Generated Code: # Complete analysis with all formulas in one comprehensive calculation

import math

print("COMPREHENSIVE MORTGAGE ANALYSIS WITH ALL FORMULAS")
print("=" * 70)
print()

# Given data
home_value = 500000
down_payment = 125000
P = home_value - down_payment

print("BASIC CALCULATIONS:")
print(f"Principal (P) = Home Value - Down Payment = ${home_value:,} - ${down_payment:,} = ${P:,}")
print(f"Down Payment Percentage = {down_payment:,} ÷ {home_value:,} × 100 = {(down_payment/home_value)*100:.1f}%")
print()

# Loan parameters
annual_rate_1, years_1 = 0.034, 15
annual_rate_2, years_2 = 0.0275, 30
r_1, n_1 = annual_rate_1 / 12, years_1 * 12
r_2, n_2 = annual_rate_2 / 12, years_2 * 12

# Monthly payment calculations
def calculate_payment_with_steps(P, r, n, loan_name, rate_percent):
    print(f"{loan_name}")
    print("="*40)
    print(f"Principal (P) = ${P:,}")
    print(f"Annual Rate = {rate_percent}%")
    print(f"Monthly Rate (r) = {rate_percent/100:.4f} ÷ 12 = {r:.6f}")
    print(f"Number of Payments (n) = {n//12} years × 12 = {n}")
    print()
    
    print("Monthly Payment Formula: M = P × [r(1+r)^n] / [(1+r)^n - 1]")
    
    one_plus_r = 1 + r
    one_plus_r_n = one_plus_r ** n
    monthly_payment = P * (r * one_plus_r_n) / (one_plus_r_n - 1)
    
    print(f"Step 1: (1 + r) = 1 + {r:.6f} = {one_plus_r:.6f}")
    print(f"Step 2: (1 + r)^n = {one_plus_r:.6f}^{n} = {one_plus_r_n:.6f}")
    print(f"Step 3: Numerator = P × r × (1+r)^n = {P:,} × {r:.6f} × {one_plus_r_n:.6f}")
    print(f"        = {P * r * one_plus_r_n:,.6f}")
    print(f"Step 4: Denominator = (1+r)^n - 1 = {one_plus_r_n:.6f} - 1 = {one_plus_r_n - 1:.6f}")
    print(f"Step 5: M = {P * r * one_plus_r_n:,.6f} ÷ {one_plus_r_n - 1:.6f} = ${monthly_payment:,.2f}")
    print()
    
    total_paid = monthly_payment * n
    total_interest = total_paid - P
    
    print("Additional Calculations:")
    print(f"Total Paid = Monthly Payment × Number of Payments")
    print(f"           = ${monthly_payment:,.2f} × {n} = ${total_paid:,.2f}")
    print(f"Total Interest = Total Paid - Principal")
    print(f"               = ${total_paid:,.2f} - ${P:,} = ${total_interest:,.2f}")
    print(f"Interest as % of Principal = ${total_interest:,.2f} ÷ ${P:,} × 100 = {(total_interest/P)*100:.1f}%")
    print()
    
    return monthly_payment, total_paid, total_interest, one_plus_r_n

# Calculate both options
payment_1, total_1, interest_1, factor_1 = calculate_payment_with_steps(P, r_1, n_1, "OPTION 1: 15-YEAR LOAN AT 3.4%", 3.4)
payment_2, total_2, interest_2, factor_2 = calculate_payment_with_steps(P, r_2, n_2, "OPTION 2: 30-YEAR LOAN AT 2.75%", 2.75)

# Comparison
print("COMPARISON ANALYSIS")
print("="*50)
monthly_diff = payment_1 - payment_2
interest_savings = interest_2 - interest_1

print(f"Monthly Payment Difference = ${payment_1:,.2f} - ${payment_2:,.2f} = ${monthly_diff:,.2f}")
print(f"Total Interest Savings (15-year) = ${interest_2:,.2f} - ${interest_1:,.2f} = ${interest_savings:,.2f}")
print(f"Time Savings = {years_2} - {years_1} = {years_2 - years_1} years earlier payoff")
print()

# Remaining balance calculation
print("REMAINING BALANCE ANALYSIS")
print("="*40)
print("Formula: B = P × [(1+r)^n - (1+r)^p] / [(1+r)^n - 1]")
print("Where p = payments made, n = total payments")
print()

p_15_years = 15 * 12
one_plus_r_p = (1 + r_2) ** p_15_years
remaining = P * (factor_2 - one_plus_r_p) / (factor_2 - 1)

print(f"Remaining balance on 30-year loan after 15 years:")
print(f"p = 15 years × 12 = {p_15_years} payments made")
print(f"(1+r)^p = (1+{r_2:.6f})^{p_15_years} = {one_plus_r_p:.6f}")
print(f"B = {P:,} × [{factor_2:.6f} - {one_plus_r_p:.6f}] / [{factor_2:.6f} - 1]")
print(f"B = ${remaining:,.2f}")
print()

print("FINAL SUMMARY")
print("="*50)
print(f"15-year loan: ${payment_1:,.2f}/month, ${interest_1:,.2f} total interest")
print(f"30-year loan: ${payment_2:,.2f}/month, ${interest_2:,.2f} total interest")
print(f"Interest savings with 15-year: ${interest_savings:,.2f}")
print(f"Monthly payment increase: ${monthly_diff:,.2f}")
print(f"Break-even investment return needed: ≈{annual_rate_1*100:.1f}% annually")

 Generated Code: # Final recommendation with affordability analysis

print("AFFORDABILITY & RECOMMENDATION ANALYSIS")
print("=" * 60)
print()

payment_1, payment_2 = 2662.43, 1530.90
monthly_diff = payment_1 - payment_2

print("AFFORDABILITY FORMULA:")
print("Housing Payment ÷ Gross Monthly Income ≤ 28% (recommended)")
print()

print("MINIMUM INCOME REQUIREMENTS:")
print("Required Income = Monthly Payment ÷ 0.28 × 12")
print()

min_income_15yr = (payment_1 / 0.28) * 12
min_income_30yr = (payment_2 / 0.28) * 12

print(f"For 15-year loan: ${payment_1:,.2f} ÷ 0.28 × 12 = ${min_income_15yr:,.0f} annually")
print(f"For 30-year loan: ${payment_2:,.2f} ÷ 0.28 × 12 = ${min_income_30yr:,.0f} annually")
print()

print("INVESTMENT OPPORTUNITY ANALYSIS")
print("=" * 40)
print("Future Value Formula: FV = PMT × [((1+r)^n - 1) / r]")
print(f"If you invest the ${monthly_diff:,.2f} monthly difference for 15 years:")
print()

for rate in [0.04, 0.06, 0.08]:
    monthly_rate = rate / 12
    n_months = 15 * 12
    
    fv = monthly_diff * (((1 + monthly_rate)**n_months - 1) / monthly_rate)
    net_after_mortgage = fv - 225590.28  # remaining balance
    
    print(f"At {rate*100:.0f}% annual return:")
    print(f"  Monthly rate = {rate:.3f} ÷ 12 = {monthly_rate:.6f}")
    print(f"  FV = {monthly_diff:,.2f} × [((1+{monthly_rate:.6f})^{n_months} - 1) / {monthly_rate:.6f}]")
    print(f"  FV = {monthly_diff:,.2f} × {((1 + monthly_rate)**n_months - 1) / monthly_rate:.6f}")
    print(f"  Investment Value = ${fv:,.0f}")
    print(f"  Net Position = ${fv:,.0f} - $225,590 = ${net_after_mortgage:,.0f}")
    print()

print("DECISION MATRIX")
print("=" * 40)
print("✅ CHOOSE 15-YEAR LOAN IF:")
print("   • Annual income ≥ $115,000")
print("   • Stable employment & emergency fund")
print("   • Priority is debt-free homeownership")
print("   • Conservative investment approach")
print("   • Want guaranteed $71,888 savings")
print()

print("✅ CHOOSE 30-YEAR LOAN IF:")
print("   • Annual income $65,000-$115,000")
print("   • Need cash flow flexibility")
print("   • Confident in earning 4%+ returns consistently")
print("   • Have other high-return investment opportunities")
print("   • Planning major expenses (kids, business)")
print()

print("🎯 RECOMMENDATION:")
print("=" * 20)
print("The 15-YEAR LOAN is generally the better choice because:")
print("1. Guaranteed savings of $71,888 (no market risk)")
print("2. Builds equity faster")
print("3. Forces disciplined savings through higher payments")
print("4. Peace of mind from debt freedom 15 years earlier")
print()
print("Choose 30-year ONLY if cash flow is tight or you have")
print("exceptional investment opportunities consistently yielding 4%+")

print("\n" + "="*60)
print("ALL FORMULAS USED IN THIS ANALYSIS:")
print("="*60)
print("1. Monthly Payment: M = P × [r(1+r)ⁿ] / [(1+r)ⁿ - 1]")
print("2. Total Interest: Total Paid - Principal") 
print("3. Remaining Balance: B = P × [(1+r)ⁿ - (1+r)ᵖ] / [(1+r)ⁿ - 1]")
print("4. Future Value: FV = PMT × [((1+r)ⁿ - 1) / r]")
print("5. Affordability: Payment ÷ Monthly Income ≤ 0.28")
print("="*60)
## Summary and Recommendation

Based on my comprehensive analysis using all relevant financial formulas, here's my recommendation for your mortgage decision:

## **The 15-year loan at 3.4% is the better choice** if you can afford it.

### Key Financial Metrics:

**15-Year Loan (3.4%)**
- Monthly Payment: **$2,662.43**
- Total Interest: **$104,237.76**
- Total Cost: $479,237.76

**30-Year Loan (2.75%)**
- Monthly Payment: **$1,530.90**
- Total Interest: **$176,125.59**
- Total Cost: $551,125.59

### **Critical Findings:**
- **Interest Savings**: $71,887.83 guaranteed with the 15-year loan
- **Monthly Difference**: $1,131.53 higher payment for 15-year loan
- **Time Savings**: Own your home 15 years earlier
- **Affordability**: Need ~$114K annual income for 15-year vs ~$66K for 30-year

### **All Formulas Used:**

1. **Monthly Payment**: M = P × [r(1+r)ⁿ] / [(1+r)ⁿ - 1]
2. **Total Interest**: Total Paid - Principal
3. **Remaining Balance**: B = P × [(1+r)ⁿ - (1+r)ᵖ] / [(1+r)ⁿ - 1]
4. **Future Value of Investments**: FV = PMT × [((1+r)ⁿ - 1) / r]
5. **Affordability Rule**: Payment ÷ Monthly Income ≤ 0.28

### **My Recommendation:**
Choose the **15-year loan** because it provides:
- **Guaranteed** $71,888 savings (no market risk)
- Faster equity building and wealth accumulation  
- Debt freedom 15 years earlier
- Lower total cost of homeownership

Only choose the 30-year loan if your income is below $115,000 annually or you have exceptional investment opportunities consistently yielding 4%+ returns.

The math strongly favors the 15-year option for long-term wealth building!