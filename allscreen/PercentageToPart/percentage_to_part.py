from kivy.uix.screenmanager import Screen

class PercentageToPartView(Screen):
    def tax(self):
        try:
            price=float(self.ids.tax_price.text)
            rate=float(self.ids.tax_rate.text)
            res_tax=str((rate/100)*price)
            tax_res=self.ids.tax_res
            tax_res.text=res_tax+" Rs."
        except:
            tax_res=self.ids.tax_res
            tax_res.text="Error!"