def calculate_capitalization(initial_amount, percent, number_of_years):
   final_amount = initial_amount * (1 + percent/1200)**(number_of_years*12)
   return round(final_amount, 2)
if __name__ == "__main__":
   init_amount = 20000.0
   perc = 15
   deposit_term = 5
   fin_amount = calculate_capitalization(init_amount, perc, deposit_term)
   print("Your final amount: ", fin_amount)
