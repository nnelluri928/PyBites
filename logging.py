#!/usr/bin/env pytho3
import logging
FORMAT = "%(asctime)s   %(message)s "
logging.basicConfig(filename = "example.log",
                    format = FORMAT,
                    level = logging.DEBUG)
def divide_numbers(numerator,denominator):
    try:
        numerator / denominator
    except (ZeroDivisionError, TypeError):
        logging.exception(f"Inputs: {numerator=}, {denominator=}")

if __name__ == "__main__":
    divide_numbers(1,2)
    divide_numbers(2,0)
    divide_numbers("a",2)
        