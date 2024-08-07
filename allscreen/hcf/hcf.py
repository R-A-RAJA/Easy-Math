from kivy.uix.screenmanager import Screen

class HCFView(Screen):
    def hcf(self):
        try:
            x1=int(self.ids.hcf_1.text)
            y1=int(self.ids.hcf_2.text)
            if x1>y1:
                smaller=y1
            else:
                smaller=x1
            for i in range(1,smaller+1):
                if((x1%i==0)and (y1%i==0)):
                    hcf_res=i
            
            res_hcf=self.ids.res_hcf
            res_hcf.text="HCF : "+str(hcf_res)
        except:
            res_hcf=self.ids.res_hcf
            res_hcf.text="Error!"   