# '''
# Python 6 nodarbības mājasdarbs Nr.2

# Uzdevums: aizpildīt vietas ar atzīmi TODO
# '''
import matplotlib.pyplot as plt
import json
import numpy as np

# # Importēt failu "top_vardi.json" un saglabāt atslēgas kā listi ar nosaukumu "x"
# # vērtības kā listi ar nosaukumu "y"
# # TODO
f = open("top_vardi.json")
dic = json.load(f)
f.close()
x = list(dic.keys())
y = list(dic.values())
print(x)
print(y)

# # izveidot stabiņveidu grafiku kas rāda vārdu biežumu (y ass), Vārdus uz x ass
# # piemērs ir mājasdarbu failā
# fig, ax = plt.plot(2,2)
# # TODO
plt.bar(x,y)
plt.show()


# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

