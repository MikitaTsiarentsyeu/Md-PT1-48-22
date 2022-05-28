import csv

make_title = "make"
model_title = "model"
color_title = "color"
id_title = "identifier"
headline = [make_title,model_title,color_title,id_title]
sneakers = []

with open("test.csv", 'r') as f:
     reader = csv.DictReader(f,headline)
     isFirst = True
     for line in reader:
        if isFirst:
            isFirst = False
            continue
        # print(line)
        sneakers.append(line)
        print(f"{line[id_title]}: {line[color_title]} {line[make_title]} {line[model_title]}")

# with open("test.csv", 'r') as f:
#     reader = csv.reader(f)
#     isFirst = True
#     for line in reader:
#         if isFirst:
#             isFirst = False
#             continue
        # print(line)
        # print(f"{line[3]}: {line[2]} {line[0]} {line[1]}")
        

# with open("test.csv", 'r') as f:
#     isFirst = True
#     for line in f:
#         print(repr(line))
#         if isFirst:
#             isFirst = False
#             continue
#         values = line.split(',')
#         print(f"{values[3]}: {values[2]} {values[0]} {values[1]}")
        # print(f"{values[2]} {values[0]} {values[1]} with id {values[3]}")

# print([list(line.values()) for line in sneakers])

with open('new.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(sneakers)
    # writer.writerows([list(line.values()) for line in sneakers])

# with open('new.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(headline)
#     writer.writerows([list(line.values()) for line in sneakers])

# with open('new.csv', 'w') as f:
#     f.write(','.join(headline)+"\n")
#     for line in sneakers:
#         f.write(','.join(line.values())+"\n")