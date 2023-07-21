from franciscologginglib import myfunctions, logging

def main():
    value = myfunctions.add(7, 6)
    logging.log("7 + 6 = " + value.__str__())

if __name__ == "__main__":
    main()