# Program to perform different set operations like in mathematics

# define two sets
E = {0, 2, 4, 6, 7,8};
N = {1, 2, 3, 4, 5};

print("Set of E")
print(E)
print("Length of set E")
print(len(E))
print("Set of N")
print(N)
print("Length of set N")
print(len(N))

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)

#subset
print("Is E Subset of N",E<=N)

#superset
print("Is E Superset of N",E>=N)
