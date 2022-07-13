class Product:
    def __init__(self, line):
        row = line.split(",")
        self.id = int(row[0])
        self.name = row[1]
        self.category = row[2]
        self.price = int(row[3])
        self.amount = int(row[4])

    def to_string(self):
        return str(self.id) + "," + self.name + "," + self.category + "," + str(self.price) + "," + str(self.amount)
