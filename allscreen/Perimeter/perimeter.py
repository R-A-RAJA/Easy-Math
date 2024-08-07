from kivy.uix.screenmanager import Screen

class PerimeterView(Screen):
#Pere_Square
    def p_sqr(self):
        try:
            p_sqr_s=float(self.ids.p_sqr_s.text)
            res_p_sqr=str(4*p_sqr_s)
            p_res_sqr=self.ids.p_res_sqr
            p_res_sqr.text=res_p_sqr+" units"
        except:
            p_res_sqr=self.ids.p_res_sqr
            p_res_sqr.text="Error!"
#Pere_Rectangle
    def p_rect(self):
        try:
            p_rect_l=float(self.ids.p_rect_l.text)
            p_rect_b=float(self.ids.p_rect_b.text)
            res_p_rect=str(2*(p_rect_b+p_rect_l))
            p_res_rect=self.ids.p_res_rect
            p_res_rect.text=res_p_rect+" units"
        except:
            p_res_rect=self.ids.p_res_rect
            p_res_rect.text='Error!'
#Pere_triangle
    def p_tri(self):
        try:
            p_tri_a=float(self.ids.p_tri_a.text)
            p_tri_b=float(self.ids.p_tri_b.text)
            p_tri_c=float(self.ids.p_tri_c.text)
            res_p_tri=str(p_tri_a+p_tri_b+p_tri_c)
            p_res_tri=self.ids.p_res_tri
            p_res_tri.text=res_p_tri+" units"
        except:
            p_res_tri=self.ids.p_res_tri
            p_res_tri.text="Error!"
#Pere_circle
    def p_cir(self):
        try:
            p_cir_r=float(self.ids.p_cir_r.text)
            res_p_cir=str(round(2*(22/7)*p_cir_r,2))
            p_res_cir=self.ids.p_res_cir
            p_res_cir.text=res_p_cir+" units"
        except:
            p_res_cir=self.ids.p_res_cir
            p_res_cir.text='Error!'
#Pere_parallogram
    def p_para(self):
        try:
            p_para_l=float(self.ids.p_para_l.text)
            p_para_b=float(self.ids.p_para_b.text)
            res_p_para=str(2*(p_para_b+p_para_l))
            p_res_para=self.ids.p_res_para
            p_res_para.text=res_p_para+" units"
        except:
            p_res_para=self.ids.p_res_para
            p_res_para.text='Error!'
#Pere_rhombus
    def p_rhom(self):
        try:
            p_rhom_s=float(self.ids.p_rhom_s.text)
            res_p_rhom=str(4*p_rhom_s)
            p_res_rhom=self.ids.p_res_rhom
            p_res_rhom.text=res_p_rhom+" units"
        except:
            p_res_rhom=self.ids.p_res_rhom
            p_res_rhom.text='Error!'
#Pere_trapeziun
    def p_trap(self):
        try:
            p_trap_a=float(self.ids.p_trap_a.text)
            p_trap_b=float(self.ids.p_trap_b.text)
            p_trap_c=float(self.ids.p_trap_c.text)
            p_trap_d=float(self.ids.p_trap_d.text)
            res_p_trap=str(p_trap_a+p_trap_b+p_trap_c+p_trap_d)
            p_res_trap=self.ids.p_res_trap
            p_res_trap.text=res_p_trap+" units"
        except:
            p_res_trap=self.ids.p_res_trap
            p_res_trap.text='Error!'
   