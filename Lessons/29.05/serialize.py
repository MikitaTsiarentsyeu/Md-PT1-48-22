from asyncore import write
import json
import pickle
import csv
'''
test_data = {
  123: "test",
  "width": 3840,
  "height": 2100,
  "resolution": 90,
  "quality": 90,
  "settings": (
    {
      "filename": "_largePreview1.jpg",
      "seek": 10
    },
    {
      "filename": "_largePreview2.jpg",
      "seek": 35
    },
    {
      "filename": "_largePreview3.jpg",
      "seek": 70
    },
    {
      "filename": "_largePreview4.jpg",
      "seek": 95
    }
  )
}

print(json.dumps(test_data))

with open("test.json", 'w') as f:
    json.dump(test_data, f)

with open("test.json", 'r') as f:
    new_test_data = json.load(f)

print(new_test_data)
print(new_test_data == test_data)

# json.dumps(print) error

with open("test.pickle", 'wb') as f:
    pickle.dump(test_data, f)

with open("test.pickle", 'rb') as f:
    new_test_data = pickle.load(f)

print(new_test_data == test_data)
print(new_test_data is test_data)
print(new_test_data)

with open("test.pickle", 'wb') as f:
    pickle.dump(print, f)

with open("test.pickle", 'rb') as f:
    new_print = pickle.load(f)

print(new_print is test_data)
new_print("some test print from the new_print")

x = print
print(x is print)
'''
model_title = "model"
year_title = "year"
horsepowers_title = "horsepower"
engine_size_title = "engine size"

headline = [model_title, year_title, horsepowers_title, engine_size_title]


data_v1 = {model_title:["80 1.6 Specs", "80 1.6 Specs"], year_title:[1989, 1993], horsepowers_title:[69, 102], engine_size_title:[1595, 1595]}

data_v2 = [{model_title:"80 1.6 Specs", year_title:1989, horsepowers_title:69, engine_size_title:1595},
            {model_title:"80 1.6 Specs", year_title:1993, horsepowers_title:102, engine_size_title:1595}]

with open("data_v1.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data_v1.keys())
    for i in range(len(list(data_v1.values())[0])):
        row = []
        for k, v in data_v1.items():
            row.append(v[i])
        writer.writerow(row)

with open("data_v2.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(data_v2)