from franciscologginglib import myfunctions

def main():
    value = myfunctions.add(7, 6)
    print("7 + 6 = " + value.__str__())

if __name__ == "__main__":
    main()