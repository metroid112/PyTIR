from decimal import *

ITERATIONS = 1000
PRECISION = Decimal(0.00000000001)
LOWEST_RATE = Decimal(0.001)
HIGHEST_RATE = Decimal(1)


def npv(cash_flow, rate):
    npv_flow = Decimal(0)
    for i in range(len(cash_flow)):
        period = Decimal(i)
        print(f'{cash_flow[i]} -> [{i}] {cash_flow[i] / ((1 + rate) ** period)}')
        npv_flow += cash_flow[i] / ((1 + rate) ** period)
    return npv_flow


def npv_non_periodic(cash_flow, rate, days):
    npv_flow = Decimal(0)
    for i in range(len(cash_flow)):
        period = Decimal(days[i] / 365)
        print(f'{cash_flow[i]} -> [{i}] {cash_flow[i] / ((1 + rate) ** period)}')
        npv_flow += cash_flow[i] / ((1 + rate) ** period)
    return npv_flow


def irr_non_periodic(cash_flow, days):
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
        new_npv = npv_non_periodic(cash_flow, irr_rate, days)
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
    Decimal(-149000000),
    Decimal(2627700),
    Decimal(2627700),
    Decimal(152627700)
]
print(irr(example_cash_flow))
