

def GetPermutationsAmount(n: int)-> int: # 1 done
    if n == 0:
        return 1
    
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    
    return result



def GetPermutationByPosition(position: int, n: int): #4 done
    usedDigits = []
    result = ""
    
    for i in range(1, n + 1):
        sc = position // GetPermutationsAmount(n - i)
        position = position % GetPermutationsAmount(n - i)
        j = 1
        
        while (sc != 0) or (j in usedDigits):
            if not(j in usedDigits):
                sc -= 1
            j += 1
        
        usedDigits.append(j)

        result += str(j)
    
    return int(result)
    


def GetPositionByPermutation(n: int, permutation: int): #5 done
    usedDigits = []
    permutationIndex = 1
    
    for i in range(1, n + 1):
        j = 1
        digitsAmount = 0
        
        while j < permutation[i - 1]:
            if not(j in usedDigits):
                digitsAmount += 1
            j += 1
        
        usedDigits.append(permutation[i - 1])
        permutationIndex += GetPermutationsAmount(n - i) * digitsAmount
    
    return permutationIndex