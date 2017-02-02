# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

# def make_hashtable(nbuckets):
#     i = 0
#     table = []
#     while i < nbuckets :
#         table.append([])
#         i = i + 1
#
#     return table
#print make_hashtable(3)

#better code
def make_hashtable(nbuckets):
    table = []
    for unused in range (0, nbuckets):
        table.append([])
        return table

print make_hashtable(3)
