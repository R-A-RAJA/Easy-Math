from kivy.uix.screenmanager import Screen

class MatrixCalculatorView(Screen):
#Matrix_add
    def add_mat(self):
        try:
            a11,a21,a31,a12,a22,a32,a13,a23,a33,b11,b21,b31,b12,b22,b32,b13,b23,b33,c11,c21,c31,c12,c22,c32,c13,c23,c33=mat(self)
        #condition of a11
            if a13=="" and b13=='' and a21=="" and b21=='' and a22=="" and b22=='' and a23=="" and b23== ''and a31=="" and b31=='' and a32=="" and b32=='' and a33 == "" and b33=='':
                a11=int(a11)
                a12=int(a12)
                b11=int(b11)
                b12=int(b12)
                a,b=a11+b11,a12+b12
                c11.text=str(a)
                c21.text="-"
                c31.text="-"
                c12.text=str(b)
                c22.text="-"
                c32.text="-"
                c13.text="-"
                c23.text="-"
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
            elif a21=="" and b21=='' and a22=='' and b22=='' and a23=='' and b23==''and a31=='' and b31==''and a32=='' and b32==''and a33=='' and b33=="":
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                a,b,c=a11+b11,a12+b12,a13+b13
                c11.text=str(a)
                c21.text="-"
                c31.text="-"
                c12.text=str(b)
                c22.text="-"
                c32.text="-"
                c13.text=str(c)
                c23.text="-"
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
            elif a31==''and b31=='' and a32=='' and b32=='' and a33==''and b33=='' and a11!="" and a12!="" and a13!="" and a21!="" and a22!="" and a23!=""and b11!="" and b12!="" and b13!="" and b21!="" and b22!="" and b23!="":
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                b21=int(b21)
                b22=int(b22)
                b23=int(b23)
                a,b,c,d,e,f=a11+b11,a12+b12,a13+b13,a21+b21,a22+b22,a23+b23
                c11.text=str(a)
                c21.text=str(d)
                c31.text="-"
                c12.text=str(b)
                c22.text=str(e)
                c32.text="-"
                c13.text=str(c)
                c23.text=str(f)
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
            elif a12==''and a13==''and a22=='' and a23=='' and a31=='' and a32=='' and a33=='' and b12==''and b13==''and b22=='' and b23=='' and b31=='' and b32=='' and b33=='' and a11!=''and b11!='' and a21!='' and b21!='':
                a11=int(a11)
                a21=int(a21)
                b11=int(b11)
                b21=int(b21)
                a,b=a11+b11,a21+b21
                c11.text=str(a)
                c21.text=str(b)
                c31.text="-"
                c12.text='-'
                c22.text='-'
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
            elif a12=='' and a13==''and a22=='' and a23=='' and a32=='' and a33==''and b12=='' and b13==''and b22=='' and b23=='' and b32=='' and b33=='':
                a11=int(a11)
                a21=int(a21)
                a31=int(a31)
                b11=int(b11)
                b21=int(b21)
                b31=int(b31)
                a,b,c=a11+b11,a21+b21,a31+b31
                c11.text=str(a)
                c21.text=str(b)
                c31.text=str(c)
                c12.text='-'
                c22.text='-'
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
            elif a13==''and a23=='' and a31=='' and a32=='' and a33==''and  b13==''and b23=='' and b31=='' and b32=='' and b33=='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                b11=int(b11)
                b12=int(b12)
                b21=int(b21)
                b22=int(b22)
                a,b,c,d=a11+b11,a12+b12,a21+b21,a22+b22
                c11.text=str(a)
                c21.text=str(c)
                c31.text='-'
                c12.text=str(b)
                c22.text=str(d)
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "               
            elif a13=='' and a23=='' and a33==''and b13=='' and b23=='' and b33=='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                a31=int(a31)
                a32=int(a32)
                b11=int(b11)
                b12=int(b12)
                b21=int(b21)
                b22=int(b22)
                b31=int(b31)
                b32=int(b32)
                a,b,c,d,e,f=a11+b11,a12+b12,a21+b21,a22+b22,a31+b31,a32+b32
                c11.text=str(a)
                c21.text=str(c)
                c31.text=str(e)
                c12.text=str(b)
                c22.text=str(d)
                c32.text=str(f)
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : " 
            else:
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                a31=int(a31)
                a32=int(a32)
                a33=int(a33)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                b21=int(b21)
                b22=int(b22)
                b23=int(b23)
                b31=int(b31)
                b32=int(b32)
                b33=int(b33)
                a,b,c,d,e,f,g,h,i=a11+b11,a12+b12,a13+b13,a21+b21,a22+b22,a23+b23,a31+b31,a32+b32,a33+b33
                c11.text=str(a)
                c21.text=str(d)
                c31.text=str(g)
                c12.text=str(b)
                c22.text=str(e)
                c32.text=str(h)
                c13.text=str(c)
                c23.text=str(f)
                c33.text=str(i)
                l_mat=self.ids.l_mat
                l_mat.text="Result (Add) : "
        except:
            c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
#Matrix_sub
    def sub_mat(self):
        try:
            a11,a21,a31,a12,a22,a32,a13,a23,a33,b11,b21,b31,b12,b22,b32,b13,b23,b33,c11,c21,c31,c12,c22,c32,c13,c23,c33=mat(self)
        #condition of a11
            if a13=="" and b13=='' and a21=="" and b21=='' and a22=="" and b22=='' and a23=="" and b23== ''and a31=="" and b31=='' and a32=="" and b32=='' and a33 == "" and b33=='':
                a11=int(a11)
                a12=int(a12)
                b11=int(b11)
                b12=int(b12)
                a,b=a11-b11,a12-b12
                c11.text=str(a)
                c21.text="-"
                c31.text="-"
                c12.text=str(b)
                c22.text="-"
                c32.text="-"
                c13.text="-"
                c23.text="-"
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
            elif a21=="" and b21=='' and a22=='' and b22=='' and a23=='' and b23==''and a31=='' and b31==''and a32=='' and b32==''and a33=='' and b33=="":
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                a,b,c=a11-b11,a12-b12,a13-b13
                c11.text=str(a)
                c21.text="-"
                c31.text="-"
                c12.text=str(b)
                c22.text="-"
                c32.text="-"
                c13.text=str(c)
                c23.text="-"
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
            elif a31==''and b31=='' and a32=='' and b32=='' and a33==''and b33=='' and a11!="" and a12!="" and a13!="" and a21!="" and a22!="" and a23!=""and b11!="" and b12!="" and b13!="" and b21!="" and b22!="" and b23!="":
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                b21=int(b21)
                b22=int(b22)
                b23=int(b23)
                a,b,c,d,e,f=a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23
                c11.text=str(a)
                c21.text=str(d)
                c31.text="-"
                c12.text=str(b)
                c22.text=str(e)
                c32.text="-"
                c13.text=str(c)
                c23.text=str(f)
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
            elif a12==''and a13==''and a22=='' and a23=='' and a31=='' and a32=='' and a33=='' and b12==''and b13==''and b22=='' and b23=='' and b31=='' and b32=='' and b33=='' and a11!=''and b11!='' and a21!='' and b21!='':
                a11=int(a11)
                a21=int(a21)
                b11=int(b11)
                b21=int(b21)
                a,b=a11-b11,a21-b21
                c11.text=str(a)
                c21.text=str(b)
                c31.text="-"
                c12.text='-'
                c22.text='-'
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-"
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
            elif a12=='' and a13==''and a22=='' and a23=='' and a32=='' and a33==''and b12=='' and b13==''and b22=='' and b23=='' and b32=='' and b33=='':
                a11=int(a11)
                a21=int(a21)
                a31=int(a31)
                b11=int(b11)
                b21=int(b21)
                b31=int(b31)
                a,b,c=a11-b11,a21-b21,a31-b31
                c11.text=str(a)
                c21.text=str(b)
                c31.text=str(c)
                c12.text='-'
                c22.text='-'
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
            elif a13==''and a23=='' and a31=='' and a32=='' and a33==''and  b13==''and b23=='' and b31=='' and b32=='' and b33=='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                b11=int(b11)
                b12=int(b12)
                b21=int(b21)
                b22=int(b22)
                a,b,c,d=a11-b11,a12-b12,a21-b21,a22-b22
                c11.text=str(a)
                c21.text=str(c)
                c31.text='-'
                c12.text=str(b)
                c22.text=str(d)
                c32.text="-"
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "               
            elif a13=='' and a23=='' and a33==''and b13=='' and b23=='' and b33=='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                a31=int(a31)
                a32=int(a32)
                b11=int(b11)
                b12=int(b12)
                b21=int(b21)
                b22=int(b22)
                b31=int(b31)
                b32=int(b32)
                a,b,c,d,e,f=a11-b11,a12-b12,a21-b21,a22-b22,a31-b31,a32-b32
                c11.text=str(a)
                c21.text=str(c)
                c31.text=str(e)
                c12.text=str(b)
                c22.text=str(d)
                c32.text=str(f)
                c13.text='-'
                c23.text='-'
                c33.text="-" 
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : " 
            else:
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                a31=int(a31)
                a32=int(a32)
                a33=int(a33)
                b11=int(b11)
                b12=int(b12)
                b13=int(b13)
                b21=int(b21)
                b22=int(b22)
                b23=int(b23)
                b31=int(b31)
                b32=int(b32)
                b33=int(b33)
                a,b,c,d,e,f,g,h,i=a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23,a31-b31,a32-b32,a33-b33
                c11.text=str(a)
                c21.text=str(d)
                c31.text=str(g)
                c12.text=str(b)
                c22.text=str(e)
                c32.text=str(h)
                c13.text=str(c)
                c23.text=str(f)
                c33.text=str(i)
                l_mat=self.ids.l_mat
                l_mat.text="Result (Subtract) : "
        except:
            c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
#Matrix_mul
    def mul_mat(self):
        try:
            a11,a21,a31,a12,a22,a32,a13,a23,a33,b11,b21,b31,b12,b22,b32,b13,b23,b33,c11,c21,c31,c12,c22,c32,c13,c23,c33=mat(self)
        #condition of a11
        #1
            if a13==''and a21==''and a22==''and a23== ''and a31==''and a32==''and a33=='' and a11!='' and a12!='':
                a11=int(a11)
                a12=int(a12)
                if b31==''and b32==''and b33==''and b11!="" and b12!="" and b13!="" and b21!="" and b22!="" and b23!="":
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    a,b,c=(a11*b11)+(a12*b21),(a11*b12)+(a12*b22),(a11*b13)+(a12*b23)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text=str(b)
                    c22.text="-"
                    c32.text="-"
                    c13.text=str(c)
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "

                elif b12==''and b13==''and b22=='' and b23=='' and b31=='' and b32=='' and b33=='' and b11!=''and b21!='':
                    b11=int(b11)
                    b21=int(b21)
                    a=(a11*b11)+(a12*b21)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text='-'
                    c22.text="-"
                    c32.text="-"
                    c13.text='-'
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "

                elif b13==''and b23=='' and b31=='' and b32=='' and b33=='' and b11!='' and b12!='' and b21!='' and b22!='':
                    b11=int(b11)
                    b12=int(b12)
                    b21=int(b21)
                    b22=int(b22)
                    a,b=(a11*b11)+(a12*b21),(a11*b12)+(a12*b22)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text=str(b)
                    c22.text="-"
                    c32.text="-"
                    c13.text='-'
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)

        #2
            elif a21==''and a22==''and a23==''and a31==''and a32==''and a33=="" and a11!='' and a12!='' and a13!='':
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                if b11!="" and b12!='' and b13!='' and b21!='' and b22!='' and b23!='' and b31!='' and b32!="" and b33!='':
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    b31=int(b31)
                    b32=int(b32)
                    b33=int(b33)
                    a,b,c=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32),(a11*b13)+(a12*b23)+(a13*b33)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text=str(b)
                    c22.text="-"
                    c32.text="-"
                    c13.text=str(c)
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b12=='' and b13==''and b22=='' and b23=='' and b32=='' and b33==''and b11!='' and b21!='' and b31!='':
                    b11=int(b11)
                    b21=int(b21)
                    b31=int(b31)
                    a=(a11*b11)+(a12*b21)+(a13*b31)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text='-'
                    c22.text="-"
                    c32.text="-"
                    c13.text='-'
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b13=='' and b23=='' and b33=='' and b11!='' and b12!='' and b21!='' and b22!='' and b31!='' and b32!='':
                    b11=int(b11)
                    b12=int(b12)
                    b21=int(b21)
                    b22=int(b22)
                    b31=int(b31)
                    b32=int(b32)
                    a,b=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32)
                    c11.text=str(a)
                    c21.text="-"
                    c31.text="-"
                    c12.text=str(b)
                    c22.text="-"
                    c32.text="-"
                    c13.text='-'
                    c23.text="-"
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #3
            elif a31==''and a32==''and a33==''and a11!="" and a12!="" and a13!="" and a21!="" and a22!="" and a23!="":
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                if b11!="" and b12!='' and b13!='' and b21!='' and b22!='' and b23!='' and b31!='' and b32!="" and b33!='':
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    b31=int(b31)
                    b32=int(b32)
                    b33=int(b33)
                    a,b,c,d,e,f=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32),(a11*b13)+(a12*b23)+(a13*b33),(a21*b11)+(a22*b21)+(a23*b31),(a21*b12)+(a22*b22)+(a23*b32),(a21*b13)+(a22*b23)+(a23*b33)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text="-"
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b12=='' and b13==''and b22=='' and b23=='' and b32=='' and b33==''and b11!='' and b21!='' and b31!='':
                    b11=int(b11)
                    b21=int(b21)
                    b31=int(b31)
                    a,b=(a11*b11)+(a12*b21)+(a13*b31),(a21*b11)+(a22*b21)+(a23*b31)
                    c11.text=str(a)
                    c21.text=str(b)
                    c31.text="-"
                    c12.text='-'
                    c22.text='-'
                    c32.text="-"
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b13=='' and b23=='' and b33=='' and b11!='' and b12!='' and b21!='' and b22!='' and b31!='' and b32!='':
                    b11=int(b11)
                    b12=int(b12)
                    b21=int(b21)
                    b22=int(b22)
                    b31=int(b31)
                    b32=int(b32)
                    a,b,c,d=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32),(a21*b11)+(a22*b21)+(a23*b31),(a21*b12)+(a22*b22)+(a23*b32)
                    c11.text=str(a)
                    c21.text=str(c)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(d)
                    c32.text="-"
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #4
            elif a12==''and a13==''and a22=='' and a23=='' and a31=='' and a32=='' and a33=='' and a11!=''and a21!='':
                a11=int(a11)
                a21=int(a21)
                if b13==''and b21==''and b22==''and b23== ''and b31==''and b32==''and b33=='' and b11!='' and b12!='':
                    b11=int(b11)
                    b12=int(b12)
                    a,b,c,d=(a11*b11),(a11*b12),(a21*b11),(a21*b12)
                    c11.text=str(a)
                    c21.text=str(c)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(d)
                    c32.text="-"
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b21==''and b22==''and b23==''and b31==''and b32==''and b33=="" and b11!='' and b12!='' and b13!='':
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    a,b,c,d,e,f=(a11*b11),(a11*b12),(a11*b13),(a21*b11),(a21*b12),(a21*b13)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text="-"
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #5
            elif a12=='' and a13==''and a22=='' and a23=='' and a32=='' and a33==''and a11!='' and a21!='' and a31!='':
                a11=int(a11)
                a21=int(a21)
                a31=int(a31)
                if b13==''and b21==''and b22==''and b23== ''and b31==''and b32==''and b33=='' and b11!='' and b12!='':
                    b11=int(b11)
                    b12=int(b12)
                    a,b,c,d,e,f=(a11*b11),(a11*b12),(a21*b11),(a21*b12),(a31*b11),(a31*b12)
                    c11.text=str(a)
                    c21.text=str(c)
                    c31.text=str(e)
                    c12.text=str(b)
                    c22.text=str(d)
                    c32.text=str(f)
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b21==''and b22==''and b23==''and b31==''and b32==''and b33=="" and b11!='' and b12!='' and b13!='':
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    a,b,c,d,e,f,g,h,i=(a11*b11),(a11*b12),(a11*b13),(a21*b11),(a21*b12),(a21*b13),(a31*b11),(a31*b12),(a31*b13)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text=str(g)
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text=str(h)
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text=str(i)
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #6
            elif a13==''and a23=='' and a31=='' and a32=='' and a33=='' and a11!='' and a12!='' and a21!='' and a22!='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                if b31==''and b32==''and b33==''and b11!="" and b12!="" and b13!="" and b21!="" and b22!="" and b23!="":
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    a,b,c,d,e,f=(a11*b11)+(a12*b21),(a11*b12)+(a12*b22),(a11*b13)+(a12*b23),(a21*b11)+(a22*b21),(a21*b12)+(a22*b22),(a21*b13)+(a22*b23)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text="-"
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b12==''and b13==''and b22=='' and b23=='' and b31=='' and b32=='' and b33=='' and b11!=''and b21!='':
                    b11=int(b11)
                    b21=int(b21)
                    a,b=(a11*b11)+(a12*b21),(a21*b11)+(a22*b21)
                    c11.text=str(a)
                    c21.text=str(b)
                    c31.text="-"
                    c12.text='-'
                    c22.text='-'
                    c32.text="-"
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b13==''and b23=='' and b31=='' and b32=='' and b33=='' and b11!='' and b12!='' and b21!='' and b22!='':
                    b11=int(b11)
                    b12=int(b12)
                    b21=int(b21)
                    b22=int(b22)
                    a,b,c,d=(a11*b11)+(a12*b21),(a11*b12)+(a12*b22),(a21*b11)+(a22*b21),(a21*b12)+(a22*b22)
                    c11.text=str(a)
                    c21.text=str(c)
                    c31.text="-"
                    c12.text=str(b)
                    c22.text=str(d)
                    c32.text="-"
                    c13.text='-'
                    c23.text='-'
                    c33.text="-"
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #7              
            elif a13=='' and a23=='' and a33=='' and a11!='' and a12!='' and a21!='' and a22!='' and a31!='' and a32!='':
                a11=int(a11)
                a12=int(a12)
                a21=int(a21)
                a22=int(a22)
                a31=int(a31)
                a32=int(a32)
                if b31==''and b32==''and b33==''and b11!="" and b12!="" and b13!="" and b21!="" and b22!="" and b23!="":
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    a,b,c,d,e,f,g,h,i=(a11*b11)+(a12*b21),(a11*b12)+(a12*b22),(a11*b13)+(a12*b23),(a21*b11)+(a22*b21),(a21*b12)+(a22*b22),(a21*b13)+(a22*b23),(a31*b11)+(a32*b21),(a31*b12)+(a32*b22),(a31*b13)+(a32*b23)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text=str(g)
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text=str(h)
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text=str(i)
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b12==''and b13==''and b22=='' and b23=='' and b31=='' and b32=='' and b33=='' and b11!=''and b21!='':
                    b11=int(b11)
                    b21=int(b21)
                    a,b,c=(a11*b11)+(a12*b21),(a21*b11)+(a22*b21),(a31*b11)+(a32*b21)
                    c11.text=str(a)
                    c21.text=str(b)
                    c31.text=str(c)
                    c12.text='-'
                    c22.text='-'
                    c32.text='-'
                    c13.text='-'
                    c23.text='-'
                    c33.text='-'
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        #8
            elif a11!="" and a12!='' and a13!='' and a21!='' and a22!='' and a23!='' and a31!='' and a32!="" and a33!='':
                a11=int(a11)
                a12=int(a12)
                a13=int(a13)
                a21=int(a21)
                a22=int(a22)
                a23=int(a23)
                a31=int(a31)
                a32=int(a32)
                a33=int(a33)
                if b11!="" and b12!='' and b13!='' and b21!='' and b22!='' and b23!='' and b31!='' and b32!="" and b33!='':
                    b11=int(b11)
                    b12=int(b12)
                    b13=int(b13)
                    b21=int(b21)
                    b22=int(b22)
                    b23=int(b23)
                    b31=int(b31)
                    b32=int(b32)
                    b33=int(b33)
                    a,b,c,d,e,f,g,h,i=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32),(a11*b13)+(a12*b23)+(a13*b33),(a21*b11)+(a22*b21)+(a23*b31),(a21*b12)+(a22*b22)+(a23*b32),(a21*b13)+(a22*b23)+(a23*b33),(a31*b11)+(a32*b21)+(a33*b31),(a31*b12)+(a32*b22)+(a33*b32),(a31*b13)+(a32*b23)+(a33*b33)
                    c11.text=str(a)
                    c21.text=str(d)
                    c31.text=str(g)
                    c12.text=str(b)
                    c22.text=str(e)
                    c32.text=str(h)
                    c13.text=str(c)
                    c23.text=str(f)
                    c33.text=str(i)
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b12=='' and b13==''and b22=='' and b23=='' and b32=='' and b33==''and b11!='' and b21!='' and b31!='':
                    b11=int(b11)
                    b21=int(b21)
                    b31=int(b31)
                    a,b,c=(a11*b11)+(a12*b21)+(a13*b31),(a21*b11)+(a22*b21)+(a23*b31),(a31*b11)+(a32*b21)+(a33*b31)
                    c11.text=str(a)
                    c21.text=str(b)
                    c31.text=str(c)
                    c12.text='-'
                    c22.text='-'
                    c32.text='-'
                    c13.text='-'
                    c23.text='-'
                    c33.text='-'
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                elif b13=='' and b23=='' and b33=='' and b11!='' and b12!='' and b21!='' and b22!='' and b31!='' and b32!='':
                    b11=int(b11)
                    b12=int(b12)
                    b21=int(b21)
                    b22=int(b22)
                    b31=int(b31)
                    b32=int(b32)
                    a,b,c,d,e,f=(a11*b11)+(a12*b21)+(a13*b31),(a11*b12)+(a12*b22)+(a13*b32),(a21*b11)+(a22*b21)+(a23*b31),(a21*b12)+(a22*b22)+(a23*b32),(a31*b11)+(a32*b21)+(a33*b31),(a31*b12)+(a32*b22)+(a33*b32)
                    c11.text=str(a)
                    c21.text=str(c)
                    c31.text=str(e)
                    c12.text=str(b)
                    c22.text=str(d)
                    c32.text=str(f)
                    c13.text='-'
                    c23.text='-'
                    c33.text='-'
                    l_mat=self.ids.l_mat
                    l_mat.text="Result (Multiply) : "
                else:
                    c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
            else:
                c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)
        except:
            c11,c21,c31,c12,c22,c32,c13,c23,c33=mat_error(self)


#Matrix Function for add, sub, mul, div
def mat(self):
    a11=self.ids.a11.text
    a21=self.ids.a21.text
    a31=self.ids.a31.text
    a12=self.ids.a12.text
    a22=self.ids.a22.text
    a32=self.ids.a32.text
    a13=self.ids.a13.text
    a23=self.ids.a23.text
    a33=self.ids.a33.text
    b11=self.ids.b11.text
    b21=self.ids.b21.text
    b31=self.ids.b31.text
    b12=self.ids.b12.text
    b22=self.ids.b22.text
    b32=self.ids.b32.text
    b13=self.ids.b13.text
    b23=self.ids.b23.text
    b33=self.ids.b33.text
    c11=self.ids.c11
    c21=self.ids.c21
    c31=self.ids.c31
    c12=self.ids.c12
    c22=self.ids.c22
    c32=self.ids.c32
    c13=self.ids.c13
    c23=self.ids.c23
    c33=self.ids.c33
    return a11,a21,a31,a12,a22,a32,a13,a23,a33,b11,b21,b31,b12,b22,b32,b13,b23,b33,c11,c21,c31,c12,c22,c32,c13,c23,c33

#Matrix Exception for all operations(+,-,*)
def mat_error(self):
    c11=self.ids.c11
    c21=self.ids.c21
    c31=self.ids.c31
    c12=self.ids.c12
    c22=self.ids.c22
    c32=self.ids.c32
    c13=self.ids.c13
    c23=self.ids.c23
    c33=self.ids.c33
    c11.text=""
    c21.text=""
    c31.text=""
    c12.text=""
    c22.text="Error!"
    c32.text=""
    c13.text=""
    c23.text=""
    c33.text=""
    return c11,c21,c31,c12,c22,c32,c13,c23,c33
