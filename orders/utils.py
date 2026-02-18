from decimal import Decimal
import json
import datetime


def generate_order_number(pk):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%S")
    order_number = current_datetime + str(pk)
    return order_number

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type Decimal is not JSON serializable")
