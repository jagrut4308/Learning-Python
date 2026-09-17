try:
    number=int(input("Enter a number:"))
    print(10/number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)
except:
    print("Default output.Unknown error")