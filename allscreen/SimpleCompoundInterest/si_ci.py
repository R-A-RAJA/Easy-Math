from kivy.uix.screenmanager import Screen

class SimpleCompoundInterestView(Screen):
#si
    def si(self):
        try:
            p=float(self.ids.si_p.text)
            r=float(self.ids.si_rate.text)
            t=float(self.ids.si_time.text)
            res_a=round(p*(1+((r/100)*t)),5)
            res_si=str(res_a-p)
            res_l=self.ids.si_l
            res_l.text="Result (SI)"
            res=self.ids.si_res
            res.text="Rs. "+res_si
            res_t=self.ids.si_res_t
            res_t.text="Rs. "+str(res_a)
        except:
            res=self.ids.si_res
            res.text='Error!'
            res_t=self.ids.si_res_t
            res_t.text='Error!'
#ci
    def ci(self):
        try:
            p=float(self.ids.si_p.text)
            r=float(self.ids.si_rate.text)
            t=float(self.ids.si_time.text)
            res_a=round(p*(1+(r/100))**(t),2)
            res_si=str(round(res_a-p,2))
            res_l=self.ids.si_l
            res_l.text="Result (CI)"
            res=self.ids.si_res
            res.text="Rs. "+res_si
            res_t=self.ids.si_res_t
            res_t.text="Rs. "+str(res_a)
        except:
            res=self.ids.si_res
            res.text='Error!'
            res_t=self.ids.si_res_t
            res_t.text='Error!'
