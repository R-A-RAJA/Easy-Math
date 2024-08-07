from kivy.uix.screenmanager import Screen

class MatrixTypeFinderView(Screen):
    def type_matrix(self):
        try:
            d11=self.ids.d11.text
            d21=self.ids.d21.text
            d31=self.ids.d31.text
            d12=self.ids.d12.text
            d22=self.ids.d22.text
            d32=self.ids.d32.text
            d13=self.ids.d13.text
            d23=self.ids.d23.text
            d33=self.ids.d33.text
            res_type_matrix=self.ids.res_type_matrix
        #condition of a11
        #column matrix
            if d12=='' and d13==''and d22=='' and d23=='' and d32=='' and d33==''and d11!='' and d21!='' and d31=='':
                d11=int(d11)
                d21=int(d21)
                if d11==d21==0:
                    res_type_matrix.text="Column Matrix, Null or Zero Matrix"
                else:
                    res_type_matrix.text="Column Matrix"
        #column matrix_2
            elif d12=='' and d13==''and d22=='' and d23=='' and d32=='' and d33==''and d11!='' and d21!='' and d31!='':
                d11=int(d11)
                d21=int(d21)
                d31=int(d31)
                if d11==d21==d31==0:
                    res_type_matrix.text="Column Matrix, Null or Zero Matrix"
                else:
                    res_type_matrix.text="Column Matrix"
        #row matrix
            elif d21==''and d22==''and d23==''and d31==''and d32==''and d33=="" and d11!='' and d12!='' and d13=='':
                d11=int(d11)
                d12=int(d12)
                if d11==d12==0:
                    res_type_matrix.text="Row Matrix, Null or Zero Matrix"
                else:
                    res_type_matrix.text="Row Matrix"
        #row matrix_2
            elif d21==''and d22==''and d23==''and d31==''and d32==''and d33=="" and d11!='' and d12!='' and d13!='':
                d11=int(d11)
                d12=int(d12)
                d13=int(d13)
                if d11==d12==d13==0:
                    res_type_matrix.text="Row Matrix, Null or Zero Matrix"
                else:
                    res_type_matrix.text="Row Matrix"
        #squar matrix 1
            elif d13==''and d23=='' and d31=='' and d32=='' and d33=='' and d11!='' and d12!='' and d21!='' and d22!='':
                d11=int(d11)
                d12=int(d12)
                d21=int(d21)
                d22=int(d22)
                #diagonal matrix1
                if d12==0 and d21==0 and d11!=0 and d22!=0:
                    if d11==d22 and d11!=1 and d22!=1:
                        res_type_matrix.text="Square, Diagonal & Scalar Matrix"
                    elif d11==1 and d22==1:
                        res_type_matrix.text="Square, Diagonal & Identity or Unit Matrix"
                    else:
                        res_type_matrix.text="Square, Diagonal Matrix"
                #Null matrix1
                elif d11==d12==d21==d22==0:
                    res_type_matrix.text="Square, Null Matrix"
                else:
                    res_type_matrix.text="Square Matrix"
                    
        #squar matrix 2
            elif d13!=''and d23!='' and d31!='' and d32!='' and d33!='' and d11!='' and d12!='' and d21!='' and d22!='':
                d11=int(d11)
                d12=int(d12)
                d13=int(d13)
                d21=int(d21)
                d22=int(d22)
                d23=int(d23)
                d31=int(d31)
                d32=int(d32)
                d33=int(d33)
            #diagonal matrix2
                if d12==0 and d13==0 and d23==0 and d21==0 and d31==0 and d32==0:
                    if d11==d22==d33 and d11!=1 and d22!=1 and d33!=1:
                        res_type_matrix.text="Square, Diagonal & Scalar Matrix"
                    elif d11==1 and d22==1 and d33==1:
                        res_type_matrix.text="Square, Diagonal & Identity or Unit Matrix"
                    else:
                        res_type_matrix.text="Square, Diagonal Matrix"
                elif d11==0 and d12==0 and d33==0 :
                    res_type_matrix.text="Square, Null Matrix"
                elif (d12==0 and d13==0 and d23==0)and(d21!=0 or d31!=0 or d32!=0):
                    res_type_matrix.text="Square, Lower Triangular Matrix"
                elif (d12!=0 or d13!=0 or d23!=0)and(d21==0 and d31==0 and d32==0):
                    res_type_matrix.text="Square, Upper Triangular Matrix"
                else:
                    res_type_matrix.text="Square Matrix"
            else:
                if d31==''and d32==''and d33==''and d11!="" and d12!="" and d13!="" and d21!="" and d22!="" and d23!="":
                    res_type_matrix.text="Normal Matrix"
                elif d13=='' and d23=='' and d33=='' and d11!='' and d12!='' and d21!='' and d22!='' and d31!='' and d32!='':
                    res_type_matrix.text="Normal Matrix"
                else:
                    res_type_matrix.text="Error!"
                    
        except:
            res_type_matrix=self.ids.res_type_matrix
            res_type_matrix.text="Error!"
