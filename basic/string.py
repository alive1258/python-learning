# ============================================================
# PART 1: Your original multiline example (fixed)
# ============================================================
name = """
    Akibul Hassan
    majarul isla
    klasfd
"""
name2 = "zamirul kabir"

print("=" * 50)
print("MULTILINE STRING EXAMPLE")
print("=" * 50)
print(name)

# Loop through each character (only print char inside loop)
for char in name:
    print(char)

# These slicing operations should be OUTSIDE the loop
print("name[3]      :", repr(name[3]))
print("name[1:4]    :", repr(name[1:4]))
print("name[1:4:2]  :", repr(name[1:4:2]))
print("name[::-1]   :", repr(name[::-1]))


# ============================================================
# PART 2: Examples of ALL string methods
# ============================================================
print("\n" + "=" * 50)
print("STRING METHODS EXAMPLES")
print("=" * 50)

s = "hello world python"

# capitalize()
print("capitalize()    :", s.capitalize())

# casefold()
print("casefold()      :", "HELLO WORLD".casefold())

# center()
print("center()        :", s.center(30, "*"))

# count()
print("count('o')      :", s.count("o"))

# encode()
print("encode()        :", s.encode())

# endswith()
print("endswith('thon'):", s.endswith("thon"))

# expandtabs()
print("expandtabs()    :", "a\tb\tc".expandtabs(4))

# find()
print("find('world')   :", s.find("world"))

# format()
print("format()        :", "My name is {}".format("Akibul"))

# format_map()
print("format_map()    :", "{a} and {b}".format_map({"a": "cat", "b": "dog"}))

# index()
print("index('world')  :", s.index("world"))

# isalnum()
print("isalnum()       :", "abc123".isalnum())

# isalpha()
print("isalpha()       :", "abc".isalpha())

# isascii()
print("isascii()       :", "abc".isascii())

# isdecimal()
print("isdecimal()     :", "123".isdecimal())

# isdigit()
print("isdigit()       :", "123".isdigit())

# isidentifier()
print("isidentifier()  :", "myVar".isidentifier())

# islower()
print("islower()       :", "abc".islower())

# isnumeric()
print("isnumeric()     :", "123".isnumeric())

# isprintable()
print("isprintable()   :", "abc".isprintable())

# isspace()
print("isspace()       :", "   ".isspace())

# istitle()
print("istitle()       :", "Hello World".istitle())

# isupper()
print("isupper()       :", "ABC".isupper())

# join()
print("join()          :", "-".join(["a", "b", "c"]))

# ljust()
print("ljust()         :", "abc".ljust(10, "."))

# lower()
print("lower()         :", "HELLO".lower())

# lstrip()
print("lstrip()        :", "   hello".lstrip())

# maketrans() + translate()
table = str.maketrans("aeiou", "12345")
print("maketrans()     :", table)
print("translate()     :", "hello world".translate(table))

# partition()
print("partition()     :", s.partition(" "))

# replace()
print("replace()       :", s.replace("python", "java"))

# rfind()
print("rfind('o')      :", s.rfind("o"))

# rindex()
print("rindex('o')     :", s.rindex("o"))

# rjust()
print("rjust()         :", "abc".rjust(10, "."))

# rpartition()
print("rpartition()    :", s.rpartition(" "))

# rsplit()
print("rsplit()        :", s.rsplit(" ", 1))

# rstrip()
print("rstrip()        :", "hello   ".rstrip())

# split()
print("split()         :", s.split())

# splitlines()
print("splitlines()    :", "a\nb\nc".splitlines())

# startswith()
print("startswith('he'):", s.startswith("he"))

# strip()
print("strip()         :", "   hello   ".strip())

# swapcase()
print("swapcase()      :", "Hello World".swapcase())

# title()
print("title()         :", "hello world".title())

# upper()
print("upper()         :", "hello".upper())

# zfill()
print("zfill()         :", "42".zfill(5))