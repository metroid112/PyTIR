from decimal import *

ITERATIONS = 100
PRECISION = Decimal(0.00000000000000000000001)
LOWEST_RATE = Decimal(0.001)
HIGHEST_RATE = Decimal(1)


def npv(cash_flow, rate):
    npv_flow = Decimal(0)
    for i in range(len(cash_flow)):
        npv_flow += cash_flow[i] / ((1 + rate) ** (i + 1))
    return npv_flow


def irr(cash_flow):
    irr_rate = Decimal(0)
    low_rate = LOWEST_RATE
    high_rate = HIGHEST_RATE
    old_npv = npv(cash_flow, irr_rate)
    print(f'Flow: {cash_flow}')
    print(f'NPV: {old_npv} at {irr_rate * 100}%')
    if old_npv == 0:
        return irr_rate
    irr_rate = (low_rate + high_rate) / 2
    for i in range(ITERATIONS):
        new_npv = npv(cash_flow, irr_rate)
        print(f'Iteration: {i}')
        print(f'\tCurrent IRR: {irr_rate}')
        print(f'\tCurrent NPV: {new_npv}')
        if PRECISION > new_npv > 0:
            print(f'Found IRR! {irr_rate * 100}%')
            return irr_rate
        else:
            if new_npv < 0:
                high_rate = irr_rate
            elif new_npv > 0:
                low_rate = irr_rate
            irr_rate = (low_rate + high_rate) / 2
    return irr_rate


example_cash_flow = [
    Decimal(-10000.0),
    Decimal(1000.0),
    Decimal(2000.0),
    Decimal(3000.0),
    Decimal(4000.0),
    Decimal(8000.0)
]
print(irr(example_cash_flow))
