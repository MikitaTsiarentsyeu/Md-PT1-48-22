initial_amount = 20000
term = 5
percent = 15

total_amount = round(initial_amount * (1 + percent/(100*12))**(term*12), 2)

print(f"""With a deposit of {initial_amount} BYN 
Total deposit amount will be {total_amount} BYN""")
