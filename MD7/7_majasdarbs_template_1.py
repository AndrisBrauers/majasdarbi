
'''
Python 7 mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot jaunu datu tipu, kurš paņem vārdisku un skaitlisku vērtību, un pēc tam spēj atdod numeriskas vērtības
Datu tips atļauj sekojošos ievadvērtības:
- "one", "two", "three", "four", "five"
'''

class JaunsDatuTips:

    def __init__(self, vertiba):
        # pārbaudīt vērtību "vertiba" vai sastāv no atļautām skatiliskiem vārdiem
        # un izveidot loģiku, kas savieno "one" kā 1; "two" kā 2 utt.
        # TODO

        if vertiba == "one" or vertiba == 1:
            vertiba = (1, "one")
        elif vertiba == "two" or vertiba == 2:
            vertiba = (2, "two")
        elif vertiba == "three" or vertiba == 3:
            vertiba = (3, "three")
        elif vertiba == "four" or vertiba == 4:
            vertiba = (4, "four")
        elif vertiba == "five" or vertiba == 5:
            vertiba = (5, "five")
        else: 
            print("Wrong input")
            return 0
        self.vertiba = vertiba 

    def get_int(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā integer datu tipu
        # TODO
        return self.vertiba[0]

    def get_float(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā float datu tipu
        # TODO        
        return float(self.vertiba[0])

    def get_string(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā string datu tipu
        # TODO
        return self.vertiba[1]

if __name__ == "__main__":
    x1 = JaunsDatuTips("one")
    x2 = JaunsDatuTips("two")
    x3 = JaunsDatuTips("three")
    x4 = JaunsDatuTips("four")
    x5 = JaunsDatuTips("five")

    # Kad uzvedums izpildīts, var pārbaudīt vai rezultāts ir pareizs, atkomentējot assert
    # TODO
    assert x1.get_int()==1
    assert x2.get_int()==2
    assert x3.get_int()==3
    assert x4.get_int()==4
    assert x5.get_int()==5

    assert x1.get_float()==1.0
    assert x2.get_float()==2.0
    assert x3.get_float()==3.0
    assert x4.get_float()==4.0
    assert x5.get_float()==5.0

    assert x1.get_string()=="one"
    assert x2.get_string()=="two"
    assert x3.get_string()=="three"
    assert x4.get_string()=="four"
    assert x5.get_string()=="five"
