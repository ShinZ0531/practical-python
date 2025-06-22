# mortgage.py
#
# Exercise 1.7
# Not finished. Don't like mortgage calculations.

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
first_month = 12

while principal > 0:
    # Pay the extra payment if within the specified range
    if first_month > 0:
        first_month -= 1
        actual_payment = payment + extra_payment
    else:
        actual_payment = payment
        
    principal = principal * (1+rate/12) - actual_payment
    total_paid = total_paid + actual_payment

print(f'Total paid {total_paid}')