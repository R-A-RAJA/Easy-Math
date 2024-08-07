from kivy.uix.screenmanager import Screen

class RatioView(Screen):
    def ratio(self):
        try:
            a=float(self.ids.an1.text)
            b=float(self.ids.con1.text)
            c=float(self.ids.an2.text)

            d=round((c*b)/a,2)

            con2=self.ids.con2
            con2.text=str(d)

        except:
            con2=self.ids.con2
            con2.text='Error!'
