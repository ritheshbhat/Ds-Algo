a = {}

a["a"] = "apple"
a["b"] = "ball"

for k, v in a.items():
    print(k, v)

c = a.keys()

b = [1, 2, 3]

b.append(4)

v = b.insert(0, 2)
print(b)

print(set(b))

a = [(0, "pine"), (1, "test"), (2, "ok"), (0, "in")]
a = sorted(a, key=lambda x: x[0])
b = sorted(a, key=lambda x: (x[0], x[1]))
print(b)
names = ["pine", "test", "ok", "in"]
print(a)
