#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The celcius to fahrenheit calculator


def area(base, height):
    # this function converts celsius to fahrenheit

    # process & output
    area_number = (base * height) / 2

    print("the area of your triangle is {0} cm²".format(area_number))


def main():
    # this function get base and height then calls the function
    height_string = input("Enter height (cm): ")
    base_string = input("Enter base (cm): ")
    try:
        base = int(base_string)
        height = int(height_string)
        area(base, height)

    except Exception:
        print("not a number")
    print("\nDone.")


if __name__ == "__main__":
    main()
