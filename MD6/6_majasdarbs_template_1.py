'''
Python 6 nodarbības mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import numpy as np

# izveidot numpy random 3x3 matricu
arr = np.random.rand(3,3)
print(arr)

# izveidot citu numpy matricu, kas ir inversā matrica no pirmās matricas
arr_inv = np.linalg.inv(arr) 
print(arr_inv)

# sareizināt abas matricas un noapaļot līdz integer precizitātei
reizinājums = np.matmul(arr, arr_inv) # TODO
reizinājums = np.rint(reizinājums)
print(reizinājums)

# Izveidot trešo matricu, kas ir 3x3 identitātes matrica 
identitates_matrica = np.identity(3)
print(identitates_matrica)

# Pārbaudīt vai identitates_matrica ir vienāda ar reizinājumu!
vienads = np.array_equal(reizinājums, identitates_matrica)
print(vienads)

# Lai pārbaudītu iznākumu, atkomentēt nākamo rindu
assert vienads == True