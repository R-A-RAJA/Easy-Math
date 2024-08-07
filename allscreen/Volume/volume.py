from kivy.uix.screenmanager import Screen

class VolumeView(Screen):
#Volume_cube
    def v_cub(self):
        try:
            v_cub=float(self.ids.v_cub.text)
            res_v_cub=str(v_cub**3)
            v_res_cub=self.ids.v_res_cub
            v_res_cub.text=res_v_cub+" cube. units"
        except:
            v_res_cub=self.ids.v_res_cub
            v_res_cub.text='Error!'
#Volume_Cuboid
    def v_cuboid(self):
        try:
            v_cuboid_l=float(self.ids.v_cuboid_l.text)
            v_cuboid_b=float(self.ids.v_cuboid_b.text)
            v_cuboid_h=float(self.ids.v_cuboid_h.text)
            res_v_cuboid=str(v_cuboid_b*v_cuboid_h*v_cuboid_l)
            v_res_cuboid=self.ids.v_res_cuboid
            v_res_cuboid.text=res_v_cuboid+" cube. units"
        except:
            v_res_cuboid=self.ids.v_res_cuboid
            v_res_cuboid.text='Error!'
#Volume_Cylinder
    def v_cy(self):
        try:
            v_cy_r=float(self.ids.v_cy_r.text)
            v_cy_h=float(self.ids.v_cy_h.text)
            res_v_cy=str(round((22/7)*(v_cy_r**2)*v_cy_h,2))
            v_res_cy=self.ids.v_res_cy
            v_res_cy.text=res_v_cy+" cube. units"
        except:
            v_res_cy=self.ids.v_res_cy
            v_res_cy.text='Error!'
#Volume_cone
    def v_cone(self):
        try:
            v_cone_r=float(self.ids.v_cone_r.text)
            v_cone_h=float(self.ids.v_cone_h.text)
            res_v_cone=str(round((1/3)*((22/7)*(v_cone_r**2)*v_cone_h),2))
            v_res_cone=self.ids.v_res_cone
            v_res_cone.text=res_v_cone+" cube. units"
        except:
            v_res_cone=self.ids.v_res_cone
            v_res_cone.text='Error!'
#Volume_Sphere
    def v_sp(self):
        try:
            v_sp_r=float(self.ids.v_sp_r.text)
            res_v_sp=str(round((4/3)*(22/7)*(v_sp_r**3),2))
            v_res_sp=self.ids.v_res_sp
            v_res_sp.text=res_v_sp+" cube. units"
        except:
            v_res_sp=self.ids.v_res_sp
            v_res_sp.text='Error!'
#Volume_HemiSphere
    def v_hsp(self):
        try:
            v_hsp_r=float(self.ids.v_hsp_r.text)
            res_v_hsp=str(round((2/3)*(22/7)*(v_hsp_r**3),2))
            v_res_hsp=self.ids.v_res_hsp
            v_res_hsp.text=res_v_hsp+" cube. units"
        except:
            v_res_hsp=self.ids.v_res_hsp
            v_res_hsp.text='Error!'
#Volume_Hollow Cylinder
    def v_hocy(self):
        try:
            v_hocy_r=float(self.ids.v_hocy_r.text)
            v_hocy_R=float(self.ids.v_hocy_R.text)
            v_hocy_h=float(self.ids.v_hocy_h.text)
            res_v_hocy=str(round((22/7)*((v_hocy_R**2)-(v_hocy_r**2))*v_hocy_h,2))
            v_res_hocy=self.ids.v_res_hocy
            v_res_hocy.text=res_v_hocy+" cube. units"
        except:
            v_res_hocy=self.ids.v_res_hocy
            v_res_hocy.text='Error!'
#Volume_HollowSphere
    def v_hosp(self):
        try:
            v_hosp_R=float(self.ids.v_hosp_R.text)
            v_hosp_r=float(self.ids.v_hosp_r.text)
            res_v_hosp=str(round((4/3)*(22/7)*((v_hosp_R**3)-(v_hosp_r**3)),2))
            v_res_hosp=self.ids.v_res_hosp
            v_res_hosp.text=res_v_hosp+" cube. units"
        except:
            v_res_hosp=self.ids.v_res_hosp
            v_res_hosp.text='Error!'
#Volume_HollowHemiSphere
    def v_hohsp(self):
        try:
            v_hohsp_r=float(self.ids.v_hohsp_r.text)
            v_hohsp_R=float(self.ids.v_hohsp_R.text)
            res_v_hohsp=str(round((2/3)*(22/7)*((v_hohsp_R**3)-(v_hohsp_r**3)),2))
            v_res_hohsp=self.ids.v_res_hohsp
            v_res_hohsp.text=res_v_hohsp+" cube. units"
        except:
            v_res_hohsp=self.ids.v_res_hohsp
            v_res_hohsp.text='Error!'
#Volume_Frustum
    def v_frus(self):
        try:
            v_frus_r=float(self.ids.v_frus_r.text)
            v_frus_R=float(self.ids.v_frus_R.text)
            v_frus_h=float(self.ids.v_frus_h.text)
            res_v_frus=str(round((1/3)*(22/7)*v_frus_h*((v_frus_R**2)+(v_frus_r**2)+(v_frus_R*v_frus_r)),2))
            v_res_frus=self.ids.v_res_frus
            v_res_frus.text=res_v_frus+" cube. units"
        except:
            v_res_frus=self.ids.v_res_frus
            v_res_frus.text='Error!'

