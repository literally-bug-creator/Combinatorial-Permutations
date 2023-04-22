from itertools import permutations


index = 1

for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    if perm == (5, 3, 8, 7, 1, 4, 6, 2, ):
        print(index)
    
    else:
        index += 1
        