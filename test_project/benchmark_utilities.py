import re
import utilities as ut
import timeit

if __name__ == '__main__':
    with open("sherlock.txt") as f:
        lines = f.readlines()
    s = """
meme_lines = [ut.translate_to_internet_meme(l) for l in lines[:100]]
    """

    print(timeit.timeit(stmt=s, setup="from __main__ import ut, lines", number=1000))


