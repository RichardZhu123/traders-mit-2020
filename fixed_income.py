import math


def bond_A(k):
    """
    Bond A notional expiring in k years
    """
    return (4-k) * 600000


def bond_B(k):
    """
    Bond B notional expiring in k years
    """
    return (4-k) * 300000


def bond_yield(k):
    """
    Yield as percent for bond expiring in k years
    """
    return (5 + math.sqrt(k))


def coupon_payment(notional):
    """
    Coupon payment (5%)
    C/N = 0.05
    """
    return 0.05 * notional


def price(time, bond):
    sum = 0

    if time == 0:
        if bond == 'A':
            notional = bond_A(0)
            coupon = coupon_payment(notional)

        elif bond == 'B':
            notional = bond_B(0)
            coupon = coupon_payment(notional)

        sum += coupon + notional

    if bond == 'A':
        notional = bond_A(time)
        coupon = coupon_payment(notional)

    elif bond == 'B':
        notional = bond_B(time)
        coupon = coupon_payment(notional)

    for year in range(1, time + 1):

        b_yield = bond_yield(time - year)

        if (year == time):
            sum += coupon + notional / ((1 + b_yield/100) ** year)
        else:
            sum += coupon / ((1 + b_yield/100) ** year)

    return sum


print("3 YEAR:", price(3, 'A'))
print("2 YEAR:", price(2, 'A'))
print("1 YEAR:", price(1, 'A'))
print("0 YEAR:", price(0, 'A'))
print("____________________")
print("3 YEAR:", price(3, 'B'))
print("2 YEAR:", price(2, 'B'))
print("1 YEAR:", price(1, 'B'))
print("0 YEAR:", price(0, 'B'))


# TO-DO
#   - make table of available notionals for both bond A and bond B
#   -
