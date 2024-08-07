from kivy.uix.screenmanager import Screen

class AreaView(Screen):
#area_Square
    def a_sqr(self):
        try:
            a_sqr_s=float(self.ids.a_sqr_s.text)
            res_a_sqr=str(a_sqr_s**2)
            a_res_sqr=self.ids.a_res_sqr
            a_res_sqr.text=res_a_sqr+" sq. units"
        except:
            a_res_sqr=self.ids.a_res_sqr
            a_res_sqr.text="Error!"
#area_Rectangle
    def a_rect(self):
        try:
            a_rect_l=float(self.ids.a_rect_l.text)
            a_rect_b=float(self.ids.a_rect_b.text)
            res_a_rect=str(a_rect_l*a_rect_b)
            a_res_rect=self.ids.a_res_rect
            a_res_rect.text=res_a_rect+" sq. units"
        except:
            a_res_rect=self.ids.a_res_rect
            a_res_rect.text='Error!'
#area_triangle
    def a_tri(self):
        try:
            a_tri_b=float(self.ids.a_tri_b.text)
            a_tri_h=float(self.ids.a_tri_h.text)
            res_a_tri=str(0.5*(a_tri_b*a_tri_h))
            a_res_tri=self.ids.a_res_tri
            a_res_tri.text=res_a_tri+" sq. units"
        except:
            a_res_tri=self.ids.a_res_tri
            a_res_tri.text="Error!"
#area_circle
    def a_cir(self):
        try:
            a_cir_r=float(self.ids.a_cir_r.text)
            res_a_cir=str(round((22/7)*(a_cir_r**2),2))
            a_res_cir=self.ids.a_res_cir
            a_res_cir.text=res_a_cir+" sq. units"
        except:
            a_res_cir=self.ids.a_res_cir
            a_res_cir.text='Error!'
#area_parallogram
    def a_para(self):
        try:
            a_para_b=float(self.ids.a_para_b.text)
            a_para_h=float(self.ids.a_para_h.text)
            res_a_para=str(a_para_b*a_para_h)
            a_res_para=self.ids.a_res_para
            a_res_para.text=res_a_para+" sq. units"
        except:
            a_res_para=self.ids.a_res_para
            a_res_para.text='Error!'
#area_rhombus
    def a_rhom(self):
        try:
            a_rhom_l=float(self.ids.a_rhom_l.text)
            a_rhom_h=float(self.ids.a_rhom_h.text)
            res_a_rhom=str((a_rhom_l*a_rhom_h)/2)
            a_res_rhom=self.ids.a_res_rhom
            a_res_rhom.text=res_a_rhom+" sq. units"
        except:
            a_res_rhom=self.ids.a_res_rhom
            a_res_rhom.text='Error!'
#area_trapeziun
    def a_trap(self):
        try:
            a_trap_a=float(self.ids.a_trap_a.text)
            a_trap_b=float(self.ids.a_trap_b.text)
            a_trap_h=float(self.ids.a_trap_h.text)
            res_a_trap=str(0.5*(a_trap_a+a_trap_b)*a_trap_h)
            a_res_trap=self.ids.a_res_trap
            a_res_trap.text=res_a_trap+" sq. units"
        except:
            a_res_trap=self.ids.a_res_trap
            a_res_trap.text='Error!'
