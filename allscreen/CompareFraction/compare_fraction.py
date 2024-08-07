from kivy.uix.screenmanager import Screen

class CompareFractionView(Screen):
    def comp_fra(self):
        try:
            cn1=int(self.ids.a_nume_c.text)
            cn2=int(self.ids.b_nume_c.text)
            cd1=int(self.ids.a_deno_c.text)
            cd2=int(self.ids.b_deno_c.text)
            res_nume1=self.ids.res_nume1
            res_deno1=self.ids.res_deno1
            res_nume2=self.ids.res_nume2
            res_deno2=self.ids.res_deno2
            comp_res=self.ids.comp_res
            if (cn1/cd1)>(cn2/cd2):
                res_nume1.text=str(cn1)
                res_deno1.text=str(cd1)
                res_nume2.text=str(cn2)
                res_deno2.text=str(cd2)
                comp_res.text=" > "
            elif (cn1/cd1)<(cn2/cd2):
                res_nume1.text=str(cn1)
                res_deno1.text=str(cd1)
                res_nume2.text=str(cn2)
                res_deno2.text=str(cd2)
                comp_res.text=" < "
            elif (cn1/cd1)==(cn2/cd2):
                res_nume1.text=str(cn1)
                res_deno1.text=str(cd1)
                res_nume2.text=str(cn2)
                res_deno2.text=str(cd2)
                comp_res.text=" = "
        except:
            res_nume1=self.ids.res_nume1
            res_deno1=self.ids.res_deno1
            res_nume1.text="Error!"
            res_deno1.text="Error!"
            res_nume2=self.ids.res_nume2
            res_deno2=self.ids.res_deno2
            res_nume2.text="Error!"
            res_deno2.text="Error!"
            comp_res=self.ids.comp_res
            comp_res.text=" - "
