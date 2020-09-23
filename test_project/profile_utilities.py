import re
from utilities import StringConverters

if __name__ == "__main__":
    sc = StringConverters()
    line = """as i walk through the valley of the doubt i take a look at my life 
    and realize there is nothing"""
    print(sc.translate_to_internet_meme(line))
