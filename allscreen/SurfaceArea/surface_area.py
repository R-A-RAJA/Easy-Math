from kivy.uix.screenmanager import Screen
import math

class SurfaceAreaView(Screen):
#CSA of 3D

#CSA_cube
    def csa_cub(self):
        try:
            a_cub=float(self.ids.a_cub.text)
            res_a_cub=str(4*(a_cub**2))
            a_res_cub=self.ids.a_res_cub
            a_res_cub.text=res_a_cub+" sq. units"
            l_a_res_cub=self.ids.l_a_res_cub
            l_a_res_cub.text='Result(CSA)'
        except:
            a_res_cub=self.ids.a_res_cub
            a_res_cub.text='Error!'
#CSA_Cuboid
    def csa_cuboid(self):
        try:
            a_cuboid_l=float(self.ids.a_cuboid_l.text)
            a_cuboid_b=float(self.ids.a_cuboid_b.text)
            a_cuboid_h=float(self.ids.a_cuboid_h.text)
            res_a_cuboid=str(2*a_cuboid_h*(a_cuboid_l+a_cuboid_b))
            a_res_cuboid=self.ids.a_res_cuboid
            a_res_cuboid.text=res_a_cuboid+" sq. units"
            l_a_res_cuboid=self.ids.l_a_res_cuboid
            l_a_res_cuboid.text='Result(CSA)'
        except:
            a_res_cuboid=self.ids.a_res_cuboid
            a_res_cuboid.text='Error!'
#CSA_Cylinder
    def csa_cy(self):
        try:
            a_cy_r=float(self.ids.a_cy_r.text)
            a_cy_h=float(self.ids.a_cy_h.text)
            res_a_cy=str(round(2*(22/7)*a_cy_r*a_cy_h,2))
            a_res_cy=self.ids.a_res_cy
            a_res_cy.text=res_a_cy+" sq. units"
            l_a_res_cy=self.ids.l_a_res_cy
            l_a_res_cy.text='Result(CSA)'
        except:
            a_res_cy=self.ids.a_res_cy
            a_res_cy.text='Error!'
#CSA_cone
    def csa_cone(self):
        try:
            a_cone_r=float(self.ids.a_cone_r.text)
            a_cone_h=float(self.ids.a_cone_h.text)
            res_a_cone=str(round((22/7)*a_cone_r*(math.sqrt((a_cone_r**2)+(a_cone_h**2))),2))
            a_res_cone=self.ids.a_res_cone
            a_res_cone.text=res_a_cone+" sq. units"
            l_a_res_cone=self.ids.l_a_res_cone
            l_a_res_cone.text='Result(CSA)'
        except:
            a_res_cone=self.ids.a_res_cone
            a_res_cone.text='Error!'
#CSA_Sphere
    def csa_sp(self):
        try:
            a_sp_r=float(self.ids.a_sp_r.text)
            res_a_sp=str(round(4*(22/7)*(a_sp_r**2),2))
            a_res_sp=self.ids.a_res_sp
            a_res_sp.text=res_a_sp+" sq. units"
            l_a_res_sp=self.ids.l_a_res_sp
            l_a_res_sp.text='Result(CSA)'
        except:
            a_res_sp=self.ids.a_res_sp
            a_res_sp.text='Error!'
#CSA_HemiSphere
    def csa_hsp(self):
        try:
            a_hsp_r=float(self.ids.a_hsp_r.text)
            res_a_hsp=str(round(2*(22/7)*(a_hsp_r**2),2))
            a_res_hsp=self.ids.a_res_hsp
            a_res_hsp.text=res_a_hsp+" sq. units"
            l_a_res_hsp=self.ids.l_a_res_hsp
            l_a_res_hsp.text='Result(CSA)'
        except:
            a_res_hsp=self.ids.a_res_hsp
            a_res_hsp.text='Error!'
#CSA_Hollow Cylinder
    def csa_hocy(self):
        try:
            a_hocy_r=float(self.ids.a_hocy_r.text)
            a_hocy_R=float(self.ids.a_hocy_R.text)
            a_hocy_h=float(self.ids.a_hocy_h.text)
            res_a_hocy=str(round(2*(22/7)*(a_hocy_r+a_hocy_R)*a_hocy_h,2))
            a_res_hocy=self.ids.a_res_hocy
            a_res_hocy.text=res_a_hocy+" sq. units"
            l_a_res_hocy=self.ids.l_a_res_hocy
            l_a_res_hocy.text='Result(CSA)'
        except:
            a_res_hocy=self.ids.a_res_hocy
            a_res_hocy.text='Error!'
#CSA_HollowSphere
    def csa_hosp(self):
        try:
            a_hosp_R=float(self.ids.a_hosp_R.text)
            res_a_hosp=str(round(4*(22/7)*(a_hosp_R**2),2))
            a_res_hosp=self.ids.a_res_hosp
            a_res_hosp.text=res_a_hosp+" sq. units"
            l_a_res_hosp=self.ids.l_a_res_hosp
            l_a_res_hosp.text='Result(CSA)'
        except:
            a_res_hosp=self.ids.a_res_hosp
            a_res_hosp.text='Error!'
#CSA_HollowHemiSphere
    def csa_hohsp(self):
        try:
            a_hohsp_r=float(self.ids.a_hohsp_r.text)
            a_hohsp_R=float(self.ids.a_hohsp_R.text)
            res_a_hohsp=str(round(2*(22/7)*((a_hohsp_R**2)+(a_hohsp_r**2)),2))
            a_res_hohsp=self.ids.a_res_hohsp
            a_res_hohsp.text=res_a_hohsp+" sq. units"
            l_a_res_hohsp=self.ids.l_a_res_hohsp
            l_a_res_hohsp.text='Result(CSA)'
        except:
            a_res_hohsp=self.ids.a_res_hohsp
            a_res_hohsp.text='Error!'
#CSA_Frustum
    def csa_frus(self):
        try:
            a_frus_r=float(self.ids.a_frus_r.text)
            a_frus_R=float(self.ids.a_frus_R.text)
            a_frus_h=float(self.ids.a_frus_h.text)
            res_a_frus=str(round((22/7)*(a_frus_r+a_frus_R)*(math.sqrt((a_frus_h**2)+((a_frus_R-a_frus_r)**2))),2))
            a_res_frus=self.ids.a_res_frus
            a_res_frus.text=res_a_frus+" sq. units"
            l_a_res_frus=self.ids.l_a_res_frus
            l_a_res_frus.text='Result(CSA)'
        except:
            a_res_frus=self.ids.a_res_frus
            a_res_frus.text='Error!'

#TSA of 3D

#TSA_cube
    def tsa_cub(self):
        try:
            a_cub=float(self.ids.a_cub.text)
            res_a_cub=str(6*(a_cub**2))
            a_res_cub=self.ids.a_res_cub
            a_res_cub.text=res_a_cub+" sq. units"
            l_a_res_cub=self.ids.l_a_res_cub
            l_a_res_cub.text='Result(TSA)'
        except:
            a_res_cub=self.ids.a_res_cub
            a_res_cub.text='Error!'
#TSA_Cuboid
    def tsa_cuboid(self):
        try:
            a_cuboid_l=float(self.ids.a_cuboid_l.text)
            a_cuboid_b=float(self.ids.a_cuboid_b.text)
            a_cuboid_h=float(self.ids.a_cuboid_h.text)
            res_a_cuboid=str(2*((a_cuboid_l*a_cuboid_b)+(a_cuboid_b*a_cuboid_h)+(a_cuboid_h*a_cuboid_l)))
            a_res_cuboid=self.ids.a_res_cuboid
            a_res_cuboid.text=res_a_cuboid+" sq. units"
            l_a_res_cuboid=self.ids.l_a_res_cuboid
            l_a_res_cuboid.text='Result(TSA)'
        except:
            a_res_cuboid=self.ids.a_res_cuboid
            a_res_cuboid.text='Error!'
#TSA_Cylinder
    def tsa_cy(self):
        try:
            a_cy_r=float(self.ids.a_cy_r.text)
            a_cy_h=float(self.ids.a_cy_h.text)
            res_a_cy=str(round(2*(22/7)*a_cy_r*(a_cy_h+a_cy_r),2))
            a_res_cy=self.ids.a_res_cy
            a_res_cy.text=res_a_cy+" sq. units"
            l_a_res_cy=self.ids.l_a_res_cy
            l_a_res_cy.text='Result(TSA)'
        except:
            a_res_cy=self.ids.a_res_cy
            a_res_cy.text='Error!'
#TSA_cone
    def tsa_cone(self):
        try:
            a_cone_r=float(self.ids.a_cone_r.text)
            a_cone_h=float(self.ids.a_cone_h.text)
            res_a_cone=str(round((22/7)*a_cone_r*(math.sqrt((a_cone_r**2)+(a_cone_h**2)))+(((22/7)*a_cone_r**2)),2))
            a_res_cone=self.ids.a_res_cone
            a_res_cone.text=res_a_cone+" sq. units"
            l_a_res_cone=self.ids.l_a_res_cone
            l_a_res_cone.text='Result(TSA)'
        except:
            a_res_cone=self.ids.a_res_cone
            a_res_cone.text='Error!'
#TSA_Sphere
    def tsa_sp(self):
        try:
            a_sp_r=float(self.ids.a_sp_r.text)
            res_a_sp=str(round(4*(22/7)*(a_sp_r**2),2))
            a_res_sp=self.ids.a_res_sp
            a_res_sp.text=res_a_sp+" sq. units"
            l_a_res_sp=self.ids.l_a_res_sp
            l_a_res_sp.text='Result(TSA)'
        except:
            a_res_sp=self.ids.a_res_sp
            a_res_sp.text='Error!'
#TSA_HemiSphere
    def tsa_hsp(self):
        try:
            a_hsp_r=float(self.ids.a_hsp_r.text)
            res_a_hsp=str(round(3*(22/7)*(a_hsp_r**2),2))
            a_res_hsp=self.ids.a_res_hsp
            a_res_hsp.text=res_a_hsp+" sq. units"
            l_a_res_hsp=self.ids.l_a_res_hsp
            l_a_res_hsp.text='Result(TSA)'
        except:
            a_res_hsp=self.ids.a_res_hsp
            a_res_hsp.text='Error!'
#TSA_Hollow Cylinder
    def tsa_hocy(self):
        try:
            a_hocy_r=float(self.ids.a_hocy_r.text)
            a_hocy_R=float(self.ids.a_hocy_R.text)
            a_hocy_h=float(self.ids.a_hocy_h.text)
            res_a_hocy=str(round(2*(22/7)*(a_hocy_r+a_hocy_R)*(a_hocy_R-a_hocy_r+a_hocy_h),2))
            a_res_hocy=self.ids.a_res_hocy
            a_res_hocy.text=res_a_hocy+" sq. units"
            l_a_res_hocy=self.ids.l_a_res_hocy
            l_a_res_hocy.text='Result(TSA)'
        except:
            a_res_hocy=self.ids.a_res_hocy
            a_res_hocy.text='Error!'
#TSA_HollowSphere
    def tsa_hosp(self):
        try:
            a_hosp_R=float(self.ids.a_hosp_R.text)
            a_hosp_r=float(self.ids.a_hosp_r.text)
            res_a_hosp=str(round(4*(22/7)*((a_hosp_R**2)+(a_hosp_r**2)),2))
            a_res_hosp=self.ids.a_res_hosp
            a_res_hosp.text=res_a_hosp+" sq. units"
            l_a_res_hosp=self.ids.l_a_res_hosp
            l_a_res_hosp.text='Result(TSA)'
        except:
            a_res_hosp=self.ids.a_res_hosp
            a_res_hosp.text='Error!'
#TSA_HollowHemiSphere
    def tsa_hohsp(self):
        try:
            a_hohsp_r=float(self.ids.a_hohsp_r.text)
            a_hohsp_R=float(self.ids.a_hohsp_R.text)
            res_a_hohsp=str(round((22/7)*((3*(a_hohsp_R**2))+(a_hohsp_r**2)),2))
            a_res_hohsp=self.ids.a_res_hohsp
            a_res_hohsp.text=res_a_hohsp+" sq. units"
            l_a_res_hohsp=self.ids.l_a_res_hohsp
            l_a_res_hohsp.text='Result(TSA)'
        except:
            a_res_hohsp=self.ids.a_res_hohsp
            a_res_hohsp.text='Error!'
#TSA_Frustum
    def tsa_frus(self):
        try:
            a_frus_r=float(self.ids.a_frus_r.text)
            a_frus_R=float(self.ids.a_frus_R.text)
            a_frus_h=float(self.ids.a_frus_h.text)
            res_a_frus=str(round((22/7)*(a_frus_r+a_frus_R)*(math.sqrt((a_frus_h**2)+((a_frus_R-a_frus_r)**2)))+((22/7)*a_frus_r**2)+((22/7)*a_frus_r**2),2))
            a_res_frus=self.ids.a_res_frus
            a_res_frus.text=res_a_frus+" sq. units"
            l_a_res_frus=self.ids.l_a_res_frus
            l_a_res_frus.text='Result(TSA)'
        except:
            a_res_frus=self.ids.a_res_frus
            a_res_frus.text='Error!'
