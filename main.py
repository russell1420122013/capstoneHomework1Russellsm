from dataclasses import dataclass

MAINE_SALES_TAX = 0.055
MASSACHUSETTS_SALES_TAX = 0.0625
NEW_HAMPSHIRE_SALES_TAX = 0.0


@dataclass
class Record:
    name: str
    price: float
    item_type: str


def total_charge(state, records):
    total = 0.0
    err = None
    for i in records:
        if i.price < 0:
            return 0.0, "Value entered is less than zero"
        total += i.price
    if state == "ME":
        total_tax = total * MAINE_SALES_TAX
    elif state == "MA":
        total_tax = total * MASSACHUSETTS_SALES_TAX
    elif state == "NH":
        total_tax = total * NEW_HAMPSHIRE_SALES_TAX
    else:
        total_tax = 0
        err = "No acceptable value entered"
    return total + total_tax, err


if __name__ == '__main__':
    test = Record("whatever", 2.99, "Clothing")
    print(test.price)
    print(test)
    wever = [Record("doo", 3.00, "clothing"), Record("fud", 5.00, "Wic Eligible food"),
             Record("koij", 80.45, "everything else")]
    charge = total_charge("MA", wever)
    print(charge)
