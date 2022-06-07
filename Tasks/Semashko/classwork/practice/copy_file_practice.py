# writing table into csv, jason and pickle files.
import csv
import json
import pickle

# first variant - CSV
spisok = {'model':['80 1.6 Specs', '80 1.6 Specs'], 'year':[1989, 1993], 'horsepower':[69, 102], 'engine size':['1595cm3 (97.3 cu-in)', '1595cm3 (97.3 cu-in)']}
with open ('car.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(spisok.keys())
    for i in range(len(list(spisok.values())[0])):
        row = []
        for k,v in spisok.items():
            row.append(v[i])
        writer.writerow(row)

# second variant - CSV
spisok2 = [{'model':'80 1.6 Specs', 'year':1989, 'horsepower':69, 'engine size':'1595cm3 (97.3 cu-in)'},
           {'model':'80 1.6 Specs', 'year':1993, 'horsepower':102, 'engine size':'1595cm3 (97.3 cu-in)'}]
model_title = 'model'
year_title = 'year'
horsepower_title = 'horsepower'
engine_size_title = 'engine size'
headline = [model_title, year_title, horsepower_title, engine_size_title]
with open ('car2.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(spisok2)

# third variant - JSON
spisok = {'model':['80 1.6 Specs', '80 1.6 Specs'], 'year':[1989, 1993], 'horsepower':[69, 102], 'engine size':['1595cm3 (97.3 cu-in)', '1595cm3 (97.3 cu-in)']}
with open('cars3.json', 'w') as f:
    json.dump(spisok, f)

# fourth variant - Pickle
spisok = {'model':['80 1.6 Specs', '80 1.6 Specs'], 'year':[1989, 1993], 'horsepower':[69, 102], 'engine size':['1595cm3 (97.3 cu-in)', '1595cm3 (97.3 cu-in)']}
with open('car4.pickle', 'wb') as f:
    pickle.dump(spisok, f)