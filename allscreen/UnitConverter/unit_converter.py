from kivy.uix.screenmanager import Screen

class UnitConverterView(Screen):
#Dropdown menu1 Conversion
    def select_spinner1(self):
        a=self.ids.spinner1.text
        if a=='inch':
            self.ids.spinner2.values=["mm",'cm',"feet",'m']
            self.ids.l_convert.text="Inches"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='mm':
            self.ids.spinner2.values=["inch",'cm',"feet",'m','km']
            self.ids.l_convert.text="Millimeters"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='cm':
            self.ids.spinner2.values=["inch",'mm',"feet",'m','km']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Centimeters"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='feet':
            self.ids.spinner2.values=["inch",'mm',"cm",'m']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Feet"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='m':
            self.ids.spinner2.values=["inch",'mm','cm',"feet",'km']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Meters"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='km':
            self.ids.spinner2.values=['mm','cm','m',"miles"]
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Kilometers"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='miles':
            self.ids.spinner2.values=["km"]
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Miles"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='mg':
            self.ids.spinner2.values=['g','kg']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Milligrams"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='g':
            self.ids.spinner2.values=['mg','kg']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Grams"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='kg':
            self.ids.spinner2.values=['g','mg']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Kilograms"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='ml':
            self.ids.spinner2.values=['l']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Millilitres"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'
        elif a=='l':
            self.ids.spinner2.values=['ml']
            b=self.ids.spinner2.text
            self.ids.l_convert.text="Litres"
            self.ids.m_convert.text=''
            self.ids.spinner2.text='Select'
            self.ids.res_convert.text='Result'

#Conversion
    def convert(self):
        try:
            v=float(self.ids.m_convert.text)
            a=self.ids.spinner1.text
            if a=='inch':
                b=self.ids.spinner2.text
                if b=='cm':
                    r=str(v*2.54)
                    self.ids.res_convert.text=str(v)+" inch  =  "+r+' cm'
                elif b=='m':
                    r=str(v*0.0254)
                    self.ids.res_convert.text=str(v)+" inch  =  "+r+' m'
                elif b=='feet':
                    r=str(v/12)
                    self.ids.res_convert.text=str(v)+" inch  =  "+r+' ft'
                elif b=='mm':
                    r=str(v*25.4)
                    self.ids.res_convert.text=str(v)+" inch  =  "+r+' m'
            elif a=='mm':
                b=self.ids.spinner2.text
                if b=='cm':
                    r=str(v/10)
                    self.ids.res_convert.text=str(v)+" mm  =  "+r+' cm'
                elif b=='inch':
                    r=str(v/25.4)
                    self.ids.res_convert.text=str(v)+" mm  =  "+r+' inch'
                elif b=='m':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" mm  =  "+r+' m'
                elif b=='feet':
                    r=str(v / 304.8)
                    self.ids.res_convert.text=str(v)+" mm  =  "+r+' ft'
                elif b=='km':
                    r=str(v/1000000)
                    self.ids.res_convert.text=str(v)+" mm  =  "+r+' km'
            elif a=='cm':
                b=self.ids.spinner2.text
                if b=='mm':
                    r=str(10*v)
                    self.ids.res_convert.text=str(v)+" cm  =  "+r+' mm'
                elif b=='inch':
                    r=str(v/2.54)
                    self.ids.res_convert.text=str(v)+" cm  =  "+r+' inch'
                elif b=='m':
                    r=str(v/100)
                    self.ids.res_convert.text=str(v)+" cm  =  "+r+' m'
                elif b=='feet':
                    r=str(v/ 30.48)
                    self.ids.res_convert.text=str(v)+" cm  =  "+r+' ft'
                elif b=='km':
                    r=str(v/100000)
                    self.ids.res_convert.text=str(v)+" cm  =  "+r+' km'
            elif a=='m':
                b=self.ids.spinner2.text
                if b=='mm':
                    r=str(v*1000)
                    self.ids.res_convert.text=str(v)+" m  =  "+r+' mm'
                elif b=='cm':
                    r=str(v*100)
                    self.ids.res_convert.text=str(v)+" m  =  "+r+' cm'
                elif b=='inch':
                    r=str(v/ 0.0254)
                    self.ids.res_convert.text=str(v)+" m  =  "+r+' inch'
                elif b=='feet':
                    r=str(v*3.280839895)
                    self.ids.res_convert.text=str(v)+" m  =  "+r+' ft'
                elif b=='km':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" m  =  "+r+' km'
            elif a=='km':
                b=self.ids.spinner2.text
                if b=='mm':
                    r=str(v*1000000)
                    self.ids.res_convert.text=str(v)+" km  =  "+r+' mm'
                elif b=='cm':
                    r=str(v*100000)
                    self.ids.res_convert.text=str(v)+" km  =  "+r+' cm'
                elif b=='miles':
                    r=str(v / 1.609344)
                    self.ids.res_convert.text=str(v)+" km  =  "+r+' miles'
                elif b=='m':
                    r=str(v*1000)
                    self.ids.res_convert.text=str(v)+" km  =  "+r+' m'
            elif a=='miles':
                b=self.ids.spinner2.text
                if b=='km':
                    r=str(v*1.609344)
                    self.ids.res_convert.text=str(v)+" miles  =  "+r+' km'
            elif a=='mg':
                b=self.ids.spinner2.text
                if b=='g':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" mg  =  "+r+' g'
                elif b=='kg':
                    r=str(v/1000000)
                    self.ids.res_convert.text=str(v)+" mg  =  "+r+' kg'
            elif a=='g':
                b=self.ids.spinner2.text
                if b=='mg':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" g  =  "+r+' mg'
                elif b=='kg':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" g  =  "+r+' kg'
            elif a=='kg':
                b=self.ids.spinner2.text
                if b=='mg':
                    r=str(v*1000000)
                    self.ids.res_convert.text=str(v)+" kg  =  "+r+' mg'
                elif b=='g':
                    r=str(v*1000)
                    self.ids.res_convert.text=str(v)+" kg  =  "+r+' g'
            elif a=='ml':
                b=self.ids.spinner2.text
                if b=='l':
                    r=str(v/1000)
                    self.ids.res_convert.text=str(v)+" ml  =  "+r+' l'
            elif a=='l':
                b=self.ids.spinner2.text
                if b=='ml':
                    r=str(v*1000)
                    self.ids.res_convert.text=str(v)+" l  =  "+r+' ml'

        except:
            self.ids.res_convert.text="Error!"
