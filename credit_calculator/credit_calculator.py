import math
import argparse


def periods_calc(inputted_principal, inputted_payment, inputted_interest):
    calc_periods = math.ceil(math.log(inputted_payment / (inputted_payment - inputted_interest * inputted_principal), 1 + inputted_interest))
    years = f'{calc_periods // 12} year{"s" * bool(calc_periods // 12 - 1)}' * bool(calc_periods // 12)
    months = f'{calc_periods % 12} month{"s" * bool(calc_periods % 12 - 1)}' * bool(calc_periods % 12)
    print(f'It will takes {years}{" and " * int(bool(months) and bool(years))}{months} to repay this loan!')
    return calc_periods


def payment_calc(inputted_periods, inputted_principal, inputted_interest):
    calc_payment = math.ceil(inputted_principal * ((inputted_interest * (1 + inputted_interest) ** inputted_periods) / ((1 + inputted_interest) ** inputted_periods - 1)))
    print(f'Your monthly payment = {calc_payment}!')
    return calc_payment


def principal_calc(inputted_payment, inputted_periods, inputted_interest):
    calc_principal = int(inputted_payment / ((inputted_interest * (1 + inputted_interest) ** inputted_periods) / ((1 + inputted_interest) ** inputted_periods - 1)))
    print(f'Your loan principal = {calc_principal}!')
    return calc_principal


def diff_payment_calc(inputted_periods, inputted_principal, inputted_interest):
    calc_months = [math.ceil(inputted_principal / inputted_periods + inputted_interest * (inputted_principal - (inputted_principal * (i - 1) / inputted_periods)))
              for i in range(1, inputted_periods + 1)]
    calc_overpayment = 0
    for calc_month, inputted_payment in enumerate(calc_months):
        print(f'Month {calc_month + 1}: payment is {inputted_payment}!')
        calc_overpayment += inputted_payment
    print(f'Overpayment {calc_overpayment - inputted_principal}')


def annuity_overpayment_calc(inputted_payment, inputted_periods, inputted_principal):
    return math.ceil(inputted_payment) * math.ceil(inputted_periods) - inputted_principal


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type", )
parser.add_argument("--principal", help="principal", type=int)
parser.add_argument("--periods", help="periods", type=int)
parser.add_argument("--interest", help="interest", type=float)
parser.add_argument("--payment", help="payment", type=float)

args = parser.parse_args()

credit_type = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
if credit_type not in ['annuity', 'diff'] or interest is None:
    print('Incorrect parameters')
elif credit_type == 'diff' and payment is not None or credit_type == 'diff' and None in [periods, principal]:
    print('Incorrect parameters')
elif credit_type == 'annuity' and [periods, principal, payment].count(None) > 1:
    print('Incorrect parameters')
elif credit_type == 'diff' and False in [periods >= 1, principal >= 1, interest >= 0]:
    print('Incorrect parameters')
else:
    nominal_interest = interest / (12 * 100)
    if credit_type == 'diff':
        diff_payment_calc(periods, principal, inputted_interest=nominal_interest)
    elif credit_type == 'annuity':
        if periods is None:
            periods = periods_calc(principal, payment, inputted_interest=nominal_interest)
        elif payment is None:
            payment = payment_calc(periods, principal, inputted_interest=nominal_interest)
        elif principal is None:
            principal = principal_calc(payment, periods, inputted_interest=nominal_interest)
        else:
            print('Incorrect parameters ')
        overpayment = annuity_overpayment_calc(payment, periods, principal)
        print(f'Overpayment = {overpayment:.2f}')
