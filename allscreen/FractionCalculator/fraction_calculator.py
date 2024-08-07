from kivy.uix.screenmanager import Screen
import math

class FractionCalculatorView(Screen):
#Fraction_add
    def add_fra(self):
        try:
            n1,n2,d1,d2=fra(self)
            l=math.lcm(d1,d2)
            c3=(l/d1)*n1
            c4=(l/d2)*n2
            x=int(c3+c4)
            d=math.gcd(x,l)
            x=str(x//d)
            l=str(l//d)
            res_nume=self.ids.res_nume
            res_deno=self.ids.res_deno
            l_fra=self.ids.l_fra
            res_nume.text=x
            res_deno.text=l
            l_fra.text="Result (Add) : "
        except:
            res_nume,res_deno=fra_error(self)
#Fraction_sub
    def sub_fra(self):
        try:
            n1,n2,d1,d2=fra(self)
            l=math.lcm(d1,d2)
            c3=(l/d1)*n1
            c4=(l/d2)*n2
            x=int(c3-c4)
            d=math.gcd(x,l)
            x=str(x//d)
            l=str(l//d)
            res_nume=self.ids.res_nume
            res_deno=self.ids.res_deno
            res_nume.text=x
            res_deno.text=l
            l_fra=self.ids.l_fra
            l_fra.text="Result (Subtract) : "
        except:
            res_nume,res_deno=fra_error(self)
#Fraction_mul
    def mul_fra(self):
        try:
            n1,n2,d1,d2=fra(self)
            x=n1*n2
            l=d1*d2
            d=math.gcd(x,l)
            x=str(x//d)
            l=str(l//d)
            res_nume=self.ids.res_nume
            res_deno=self.ids.res_deno
            res_nume.text=x
            res_deno.text=l
            l_fra=self.ids.l_fra
            l_fra.text="Result (Multiply) : "
        except:
            res_nume,res_deno=fra_error(self)
#Fraction_div
    def div_fra(self):
        try:
            n1,n2,d1,d2=fra(self)
            x=n1*d2
            l=n2*d1
            d=math.gcd(x,l)
            x=str(x//d)
            l=str(l//d)
            res_nume=self.ids.res_nume
            res_deno=self.ids.res_deno
            res_nume.text=x
            res_deno.text=l
            l_fra=self.ids.l_fra
            l_fra.text="Result (Divide) : "
        except:
            res_nume,res_deno=fra_error(self)



#TextInput
def fra(self):
    n1=int(self.ids.a_nume.text)
    n2=int(self.ids.b_nume.text)
    d1=int(self.ids.a_deno.text)
    d2=int(self.ids.b_deno.text)
    return n1,n2,d1,d2

#Fraction Error display
def fra_error(self):
    res_nume=self.ids.res_nume
    res_deno=self.ids.res_deno
    res_nume.text="Error!"
    res_deno.text="Error!"
    return res_nume,res_deno