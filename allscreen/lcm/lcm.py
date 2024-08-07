from kivy.uix.screenmanager import Screen
import math
class LCMView(Screen):
    def lcm(self):
        try:
            i_lcm_1=int(self.ids.i_lcm_1.text)
            i_lcm_2=int(self.ids.i_lcm_2.text)
            res_lcm=str(math.lcm(i_lcm_1,i_lcm_2))
            lcm_res=self.ids.lcm_res
            lcm_res.text="LCM : "+res_lcm
        except:
            lcm_res=self.ids.lcm_res
            lcm_res.text="Error!"
    def gcd(self):
        try:
            i_lcm_1=int(self.ids.i_lcm_1.text)
            i_lcm_2=int(self.ids.i_lcm_2.text)
            res_lcm=str(math.gcd(i_lcm_1,i_lcm_2))
            lcm_res=self.ids.lcm_res
            lcm_res.text="GCD : "+res_lcm
        except:
            lcm_res=self.ids.lcm_res
            lcm_res.text="Error!"