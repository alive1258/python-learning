# ============================================================
# PART 1: Your original set example (fixed)
# ============================================================
print("=" * 50)
print("BASIC SET EXAMPLE")
print("=" * 50)

# set: unique collection of elements
numbers = [1, 2, 3, 4, 5]
print("List            :", numbers)

number_set = set(numbers)
print("Set from list   :", number_set)

number_set.add(6)
print("After add(6)    :", number_set)
print("Length          :", len(number_set))

number_set.remove(3)
print("After remove(3) :", number_set)

# Loop through set
print("Iterating set:")
for item in number_set:
    print("  item:", item)

# Membership check (if / elif)
if 2 in number_set:
    print("Yes, 2 is in the set")
elif 3 in number_set:
    print("Yes, 3 is in the set")


# ============================================================
# PART 2: Examples of ALL set methods
# ============================================================
print("\n" + "=" * 50)
print("SET METHODS EXAMPLES")
print("=" * 50)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# ---------- add() ----------
s = {1, 2, 3}
s.add(4)
print("add(4)                    :", s)

# ---------- clear() ----------
s = {1, 2, 3}
s.clear()
print("clear()                   :", s)

# ---------- copy() ----------
s = {1, 2, 3}
c = s.copy()
print("copy()                    :", c)

# ---------- difference() (-) ----------
print("A.difference(B)           :", A.difference(B))     # A - B
print("A - B                     :", A - B)

# ---------- difference_update() (-=) ----------
X = A.copy()
X.difference_update(B)
print("difference_update()       :", X)

# ---------- discard() ----------
s = {1, 2, 3, 4}
s.discard(2)
print("discard(2)                :", s)
s.discard(99)   # no error if not found
print("discard(99) (no error)    :", s)

# ---------- intersection() (&) ----------
print("A.intersection(B)         :", A.intersection(B))
print("A & B                     :", A & B)

# ---------- intersection_update() (&=) ----------
X = A.copy()
X.intersection_update(B)
print("intersection_update()     :", X)

# ---------- isdisjoint() ----------
print("A.isdisjoint(B)           :", A.isdisjoint(B))
print("{1,2}.isdisjoint({3,4})    :", {1, 2}.isdisjoint({3, 4}))

# ---------- issubset() (<=) and (<) ----------
small = {1, 2}
big   = {1, 2, 3, 4}
print("small.issubset(big)       :", small.issubset(big))
print("small <= big              :", small <= big)
print("small < big (strict)      :", small < big)
print("{1,2} < {1,2} (strict)    :", {1, 2} < {1, 2})   # False

# ---------- issuperset() (>=) and (>) ----------
print("big.issuperset(small)     :", big.issuperset(small))
print("big >= small              :", big >= small)
print("big > small (strict)      :", big > small)
print("{1,2} > {1,2} (strict)    :", {1, 2} > {1, 2})   # False

# ---------- pop() ----------
s = {10, 20, 30}
popped = s.pop()
print("pop() removed             :", popped, "| remaining:", s)

# ---------- remove() ----------
s = {1, 2, 3, 4}
s.remove(3)
print("remove(3)                 :", s)
# s.remove(99)  # <-- raises KeyError if not found

# ---------- symmetric_difference() (^) ----------
print("A.symmetric_difference(B) :", A.symmetric_difference(B))
print("A ^ B                     :", A ^ B)

# ---------- symmetric_difference_update() (^=) ----------
X = A.copy()
X.symmetric_difference_update(B)
print("symmetric_difference_upd():", X)

# ---------- union() (|) ----------
print("A.union(B)                :", A.union(B))
print("A | B                     :", A | B)

# ---------- update() ----------
s = {1, 2}
s.update([3, 4, 5])
print("update([3,4,5])           :", s)
s.update({6, 7}, {8, 9})
print("update(two sets)          :", s)