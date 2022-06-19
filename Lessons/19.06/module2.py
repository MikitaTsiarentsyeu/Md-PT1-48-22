global_value = [5]

def print_global_value():
    print(f"the global value is {global_value}")

print(__name__)

if __name__ == "__main__":
    print("Some main busines logic goes here")
    print_global_value()