
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 2 saturu par klasi

'''
import json
import matplotlib.pyplot as plt
import numpy as np

class TopWords:
    '''
    Izveidot klasi, kurai ir 2 publiskas metodes:
    - setVardnica -  definē failu
    - grafiks - izvada grafiku

    Klasei nav pieejami publiski parametri
    '''
    def set_dict(self,vardnicaFails):
        f = open(vardnicaFails)
        self.__vardnica = json.load(f)
        f.close()

    def get_bar_plot(self):
        # izsaucot šo metodi izvada bar tipa grafiku. dati ir parametrs __vardnica
        # TODO    
        x = list(self.__vardnica.keys())
        y = list(self.__vardnica.values())    
        plt.bar(x,y)
        plt.show() 
        return 0


if __name__ == "__main__":
    obj = TopWords()
    obj.set_dict("majasdarbi/MD7/top_vardi.json")
