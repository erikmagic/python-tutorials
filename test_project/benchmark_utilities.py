import re
from utilities import StringConverters


if __name__ == '__main__':
    import timeit
    s = """
sc = StringConverters()
with open("sherlock.txt") as f:
    lines = f.readlines()
meme_lines = [sc.translate_to_internet_meme(l) for l in lines[:100]]
    """

    print(timeit.timeit(stmt=s, setup="from __main__ import  StringConverters", number=1000))


