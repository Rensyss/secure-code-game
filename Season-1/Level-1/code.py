'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

MAX_AMOUNT = 100000
MAX_QUANTITY = 1000
MIN_QUANTITY = 0
MAX_TOTAL = 1e6



Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order):
    pay = Decimal('0')
    exp = Decimal('0')


    for item in order.items:
        if item.type == 'payment':
            if -MAX_AMOUNT <= item.amount <= MAX_AMOUNT:
                pay += Decimal(str(item.amount))
        elif item.type == 'product':
            if MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_AMOUNT:
                exp += Decimal(str(item.amount)) * Decimal(item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if abs(pay) > MAX_TOTAL or exp > MAX_TOTAL:
        return "Total amount payable for an order exceeded"
    elif pay != exp:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, pay - exp)
    else:
        return "Order ID: %s - Full payment received!" % order.id