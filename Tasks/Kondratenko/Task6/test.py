import csv
import os
import decimal
import random
from decimal import Decimal

data = []

with open("PLC.csv", "r", encoding="utf-8", newline="") as csv_table:
    reader = csv.DictReader(csv_table)
    for i in reader:
        data.append(i)
#
#
# print(data)
# with open("new_PLC.csv", "w", encoding="utf-8", newline="") as csv_table:
#     writer = csv.writer(csv_table)
#     for index, item in enumerate(data):
#         if index == 0:
#             item[3] = item[3] + ', \u20ac'
#         if index > 0:
#             number = decimal.Decimal(item[3])
#             item[3] = number.quantize(Decimal("1.00"))
#         writer.writerow(item)

with open("new_PLC.csv", "w", encoding="utf-8", newline="") as csv_table:
    writer = csv.DictWriter(csv_table, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    if os.path.exists("new_PLC.csv"):
        print("Order has been successfully placed")
    else:
        print("An error occurred while placing an order")

