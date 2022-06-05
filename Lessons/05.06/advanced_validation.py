def validate_int_param(low_val, high_val, name):

    while True:
        x = input(f"Please enter some value for {name} bigger than {low_val}, lower than {high_val}:\n")

        try:
            x = int(x)

            if x <= low_val:
                raise RuntimeError("The value is too low, try again")
            if x >= high_val:
                raise RuntimeError("The value is too high, try again")
        except ValueError:
            print("The value must be integer, try again")
            continue
        except RuntimeError as e:
            print(e)
            continue
        else:
            break


validate_int_param(10, 100, "velocity (km/h)")