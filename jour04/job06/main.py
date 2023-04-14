l = ["a","b","c","d","e"]
idx1 = l.index("a")
idx2 = l.index("e")
l[idx1], l[idx2], = l[idx2], l[idx1]

print(l)
