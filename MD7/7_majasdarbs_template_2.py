'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

'''

from IntroOpenCV import IntroOpenCV
from TopWords import TopWords

# definēt klasi, kura manto klases TopVardi un IevadsOpenCV
# TODO
class Majasdarbs(TopWords, IntroOpenCV):
    def __init__(self):
        self = TopWords()
        self = IntroOpenCV()



if __name__ == "__main__":
    obj = Majasdarbs()

    # Atkomentēt sekojošās rindas, lai pārbaudītu vai klases ir mantotas
    # TODO
    obj.set_picture("majasdarbi/MD7/python.jpg")
    obj.get_blue_red()
    obj.set_dict("majasdarbi/MD7/top_vardi.json")
    obj.get_bar_plot()
