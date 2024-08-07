from kivy.uix.screenmanager import Screen
from datetime import date

class AgeFinderView(Screen):
    def age(self):
        try:
            d=int(self.ids.day.text)
            m=int(self.ids.month.text)
            y=int(self.ids.year.text)

            today=date.today()
            age_res=self.ids.age_res
            if date(y,m,d)<=today:
                age=today.year-y-((today.month,today.day)<(m,d))
                age_res.text=str(age)+" years"
            else:
                age_res.text="Invalid date"

        except:
            age_res=self.ids.age_res
            age_res.text="Invalid date"