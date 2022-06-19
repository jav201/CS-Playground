
elements = list('012')

# Create a set from these elements
set_ = set([''])
copySet = set_.copy()
while len(set_) < 1000:
    for l in elements:
        for _ in set_:
            copySet.add(_+l)
    set_ = copySet.copy()
# print(set_)
print(sorted(set_, key=len))
