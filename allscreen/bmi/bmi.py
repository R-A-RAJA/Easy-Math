from kivy.uix.screenmanager import Screen

class BMIView(Screen):
    def bmi(self):
        try:
            bmi_w=float(self.ids.bmi_w.text)
            bmi_h=float(self.ids.bmi_h.text)
            bmi_h=bmi_h/100
            res_bmi=round(bmi_w/(bmi_h*bmi_h),1)
            bmi_res=self.ids.bmi_res
            bmi_c=self.ids.bmi_c
            if res_bmi<18.5:
                bmi_c.text="Under Weight"
            elif res_bmi>=18.5 and res_bmi<=24.9:
                bmi_c.text="Normal Weight"
            elif res_bmi>=25.0 and res_bmi<=39.9:
                bmi_c.text="Overweight"
            else:
                bmi_c.text="Obese"
            bmi_res.text=str(res_bmi)
        except:
            bmi_res=self.ids.bmi_res
            bmi_res.text="Error!"
            bmi_c=self.ids.bmi_c
            bmi_c.text="Error!"