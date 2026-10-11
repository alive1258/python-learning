numbers=[12, 34, 56, 78, 90, 23, 45, 67, 89, 10]
person={
    "name": "John",
      "age": 30, 
      "city": "New York",
       "is_student": False,
        "grades": [85, 90, 78], 
        "address": {"street": "123 Main St", "zip_code": "10001"}}


print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print(person.keys())
print(person.values())
person["age"] = 31
print("Updated Age:", person["age"])

# ============================================================
# PART 1: LIST METHODS (from Python docs section 5.1)
# ============================================================
print("=" * 60)
print("LIST METHODS EXAMPLES")
print("=" * 60)

# ---------- append() ----------
a = [1, 2, 3]
a.append(4)
print("append(4)              :", a)

# ---------- extend() ----------
a = [1, 2, 3]
a.extend([4, 5, 6])
print("extend([4,5,6])        :", a)

# ---------- insert() ----------
a = [1, 2, 3]
a.insert(0, 0)          # front
a.insert(len(a), 99)    # end (like append)
print("insert(0,0), insert(len,99):", a)

# ---------- remove() ----------
a = [1, 2, 3, 2, 4]
a.remove(2)             # removes FIRST occurrence
print("remove(2)              :", a)

# ---------- pop() ----------
a = [10, 20, 30, 40]
last = a.pop()
print("pop() returned         :", last, "| list:", a)
second = a.pop(1)
print("pop(1) returned        :", second, "| list:", a)

# ---------- clear() ----------
a = [1, 2, 3]
a.clear()
print("clear()                :", a)

# ---------- index() ----------
a = [10, 20, 30, 20, 40]
print("index(20)              :", a.index(20))
print("index(20, 2)           :", a.index(20, 2))   # start search at index 2
print("index(20, 0, 2)        :", a.index(20, 0, 2)) # search between 0 and 2

# ---------- count() ----------
a = [1, 1, 2, 3, 1, 4]
print("count(1)               :", a.count(1))

# ---------- sort() ----------
a = [5, 2, 9, 1, 7]
a.sort()
print("sort()                 :", a)
a.sort(reverse=True)
print("sort(reverse=True)     :", a)

# sort with key
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print("sort(key=len)          :", words)

# ---------- reverse() ----------
a = [1, 2, 3, 4]
a.reverse()
print("reverse()              :", a)

# ---------- copy() ----------
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("original a             :", a)
print("copy b (modified)      :", b)

# ---------- Practical: using lists as stacks and queues ----------
print("\n--- Stack (LIFO) ---")
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print("Stack pop             :", stack.pop())
print("Stack pop             :", stack.pop())
print("Stack now             :", stack)

print("\n--- Queue (FIFO) ---")
from collections import deque
queue = deque(["Alice", "Bob", "Charlie"])
queue.append("David")
print("Queue popleft         :", queue.popleft())
print("Queue now             :", list(queue))


# ============================================================
# PART 2: DICTIONARY METHODS
# ============================================================
print("\n" + "=" * 60)
print("DICTIONARY METHODS EXAMPLES")
print("=" * 60)

# ---------- clear() ----------
d = {"a": 1, "b": 2}
d.clear()
print("clear()                :", d)

# ---------- copy() ----------
d = {"a": 1, "b": 2}
c = d.copy()
c["c"] = 3
print("original d             :", d)
print("copy c (modified)      :", c)

# ---------- fromkeys() ----------
keys = ["x", "y", "z"]
d = dict.fromkeys(keys, 0)
print("fromkeys(keys, 0)      :", d)

# ---------- get() ----------
person = {"name": "John", "age": 30}
print("get('name')            :", person.get("name"))
print("get('salary')          :", person.get("salary"))           # None
print("get('salary', 'N/A')   :", person.get("salary", "N/A"))   # default

# ---------- items() ----------
print("items()                :", list(person.items()))

# ---------- keys() ----------
print("keys()                 :", list(person.keys()))

# ---------- values() ----------
print("values()               :", list(person.values()))

# ---------- pop() ----------
d = {"a": 1, "b": 2, "c": 3}
val = d.pop("b")
print("pop('b') returned      :", val, "| dict:", d)

# ---------- popitem() ----------
d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()   # removes LAST inserted pair (LIFO in Python 3.7+)
print("popitem() returned     :", item, "| dict:", d)

# ---------- setdefault() ----------
d = {"a": 1}
print("setdefault('a', 99)    :", d.setdefault("a", 99), "| dict:", d)
print("setdefault('b', 2)     :", d.setdefault("b", 2), "| dict:", d)

# ---------- update() ----------
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})
print("update(...)            :", d)


# ============================================================
# PART 3: Your original dictionary example (fixed)
# ============================================================
print("\n" + "=" * 60)
print("YOUR ORIGINAL DICTIONARY EXAMPLE")
print("=" * 60)

numbers = [12, 34, 56, 78, 90, 23, 45, 67, 89, 10]

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 90, 78],
    "address": {"street": "123 Main St", "zip_code": "10001"}
}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Nested access
print("Street:", person["address"]["street"])
print("First grade:", person["grades"][0])

person["age"] = 31
print("Updated Age:", person["age"])

# Add a new key
person["email"] = "john@example.com"
print("After adding email:", person)

# Safe access with get()
print("Phone (get):", person.get("phone", "Not provided"))


# ============================================================
# PART 4: Numbers list — useful operations
# ============================================================
print("\n" + "=" * 60)
print("NUMBERS LIST OPERATIONS")
print("=" * 60)

print("Original numbers       :", numbers)
print("Length                 :", len(numbers))
print("Min / Max              :", min(numbers), "/", max(numbers))
print("Sum                    :", sum(numbers))
print("Sorted                 :", sorted(numbers))
print("Sorted reverse         :", sorted(numbers, reverse=True))
print("Count of 45            :", numbers.count(45))
print("Index of 90            :", numbers.index(90))
