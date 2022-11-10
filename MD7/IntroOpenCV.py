
'''
Python 7 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 3 saturu par klasi
'''
import cv2

class IntroOpenCV:
    '''
    Izveidot klasi, kurai ir 5 publiskas metodes:
    - setBilde -  definē bildes failu
    - bilde 
    - melnbalts
    - EdgeDetection
    - ZilsSarkans

    !Klasei nav neviena publiski pieejami parametri!
    '''
    def set_picture(self,BildeFails):
        img = cv2.imread(BildeFails)
        self.__picture = img

    def get_picture(self):
        cv2.imshow("Regular image",self.__picture)
        cv2.waitKey(0)
        return 0

    def get_black_white(self):
        img_melnbalts = cv2.cvtColor(self.__picture, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Black and White image",img_melnbalts)
        cv2.waitKey(0)
        return 0

    def get_edge_detection(self):
        img_caddy = cv2.Canny(image=self.__picture, threshold1=100, threshold2=200)
        cv2.imshow("Caddy image",img_caddy)
        cv2.waitKey(0)
        return 0


    def get_blue_red(self):
        img_zils_sarkans = cv2.cvtColor(self.__picture, cv2.COLOR_BGR2RGB)
        cv2.imshow("Blue to Red image",img_zils_sarkans)
        cv2.waitKey(0)
        return 0


if __name__ == "__main__":
    obj = IntroOpenCV()
    obj.set_picture("majasdarbi/MD7/python.jpg")


