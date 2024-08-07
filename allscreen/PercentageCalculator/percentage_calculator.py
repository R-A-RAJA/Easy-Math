from kivy.uix.screenmanager import Screen

class PercentageCalculatorView(Screen):
    def percent(self):
        try:
            mark=float(self.ids.i_percent_1.text)
            outof=float(self.ids.i_percent_2.text)
            res_percent=str(round((mark/outof)*100,2))
            percent_res=self.ids.percent_res
            percent_res.text=res_percent+" %"
        except:
            percent_res=self.ids.percent_res
            percent_res.text="Error!"
