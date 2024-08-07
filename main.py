#############################################################################
#                           PROJECT : Easy Math                             # 
#    Language used : Python(kivy, kivymd framework)                         #
#    Importing     : Builder, MDApp, GridLayout, sqlite3, math ,date        #                                                       
#    Class used    :                                                        #
#             1) MyGridLayout  ----For simple and scientific calculator     #
#             2) MainApp       ----button functions present in it           #
#    Other module  : design.kv ----For designing                            #                                         
#############################################################################

from kivy.lang import Builder
from kivymd.app import MDAppld
from kivy.uix.gridlayout import GridLayout
import sqlite3
from kivymd.uix.button import MDFlatButton
import math
from kivymd.uix.dialog import MDDialog
from allscreen.screens import screens


from kivy.core.window import Window

#size of screen
#Window.size=(720,1640)

#############################################################################
#                           Class : MyGridLayout                            #                                                       
#    Class used    : For simple and scientific calculator                   #
#    Functions used:                                                        #
#          1) calculate1      ---when = is pressed in simple calculator     #
#          2) calculate1Back  ---when backspace is pressed in sim..cal      #
#          3) calculate       ---when = is pressed in scientific calculator #
#          4) calculate2Back  ---when backspace is pressed in sci..cal      #                    
#############################################################################
class MyGridLayout(GridLayout):
#Normal calculator
    def calculate1(self, calculation1):
        
        try:
            if calculation1!='':
                #cal is used as question to store in database
                cal=calculation1
                # create and use database
                mydb = sqlite3.connect('history.db')
                #create curser
                mycursor =mydb.cursor()

                # x to *
                if "x" in calculation1:
                    calculation1=calculation1.replace("x","*")
                    
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display1.text = str(round(eval(calculation1),9)) 

                #crete table
                mycursor.execute("create table if not exists history (quest text,res text)")
                #insert into table
                mycursor.execute("insert into history values (:f,:s)",{'f':cal,'s':str(round(eval(calculation1),9))})
                mydb.commit()
                mydb.close()
        except Exception:
            self.display1.text = "Error!"
    #For back space
    def calculate1Back(self,calculation1):
        if 'del' in calculation1:
            a=[]
            for i in calculation1:
                a.append(i)
                b=''.join(a[:-4])
            self.display1.text = b 
#Scientific Calculator
    def calculate(self, calculation):
        
        try:
            if calculation!='':
                #cal to store in db
                cal=calculation
                #db
                mydb = sqlite3.connect('history.db')
                #curser
                mycursor = mydb.cursor()

                #condition for scientific calculator
                
                if "sin(" in calculation:
                    if ')' in calculation:
                        calculation=calculation.replace(")","))")
                    calculation=calculation.replace("sin(","math.sin(math.radians(")
                if "cos(" in calculation:
                    if ')' in calculation:
                        calculation=calculation.replace(")","))")
                    calculation=calculation.replace("cos(","math.cos(math.radians(")
                if "tan(" in calculation:
                    if ')' in calculation:
                        calculation=calculation.replace(")","))")
                    calculation=calculation.replace("tan(","math.tan(math.radians(")
                if '^' in calculation:
                    calculation=calculation.replace("^","**")
                if "sqrt(" in calculation:
                    calculation=calculation.replace("sqrt(","math.sqrt(")
                if "log(" in calculation:
                    calculation=calculation.replace("log(","math.log10(")
                if "e" in calculation:
                    calculation=calculation.replace("e","2.71828182846")
                if "pi" in calculation:
                    calculation=calculation.replace("pi","math.pi")
                if "x" in calculation:
                    calculation=calculation.replace("x","*")
                # Solve formula and display it in entry
                # which is pointed at by display
                
                self.display.text = str(round(eval(calculation),9))

                #create table
                mycursor.execute("create table if not exists history2 (quest text,res text)")
                #insert into table
                mycursor.execute("insert into history2 values (:f,:s)",{'f':cal,'s':str(round(eval(calculation),9))})
                mydb.commit()
                mydb.close()
        except Exception:
            self.display.text = "Error!"
    #For back space
    def calculate2Back(self,calculation):
        if '<<' in calculation:
            a=[]
            for i in calculation:
                a.append(i)
                b=''.join(a[:-3])
            self.display.text = b 

#App whole data
class MainApp(MDApp):
    dialog=None
    #### For back button in android
    def __init__(self,**kwargs):
        super(MainApp,self).__init__(**kwargs)
        #code goes here and add:
        Window.bind(on_keyboard=self.Android_back_click)
    def Android_back_click(self,window,key,*largs):
        if key == 27:
            if self.root.ids.sm_sub.current=="normal":
                self.show_alert_dialog()
            else:
                self.root.ids.sm_sub.current="normal" 
                self.help()

        return True
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Exit App",
                text="Do you want to exit?",
                buttons=[
                    MDFlatButton(
                        text="NO",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="YES",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.exit_app
                    ),
                ],
            )
        self.dialog.open()
    #close dialog box 
    def close_dialog(self,obj):
        self.dialog.dismiss()
    #exit app
    def exit_app(self,obj):
        MainApp().stop()

#calculator
#History of normal calculator
    def history1(self):
        mydb = sqlite3.connect('history.db')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM history")
        myresult = mycursor.fetchall()
        res_nume=self.root.ids.cal_his
    #Join list with = and \n
        res = list(map("=".join, myresult))
        res.reverse()
        #result = '\n'.join(str(myresult))
        res1=str('\n\n'.join(res))
        res_nume.text=res1
        mydb.commit()
        mydb.close()
        
#clear History of normal calculator
    def history1_clear(self):
        mydb = sqlite3.connect('history.db')
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM history")
        mydb.commit()
        mydb.close()
        res_nume=self.root.ids.cal_his
        res_nume.text="no history"
        
#History of scientific calculator
    def history2(self):
        mydb = sqlite3.connect('history.db')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM history2")
        myresult = mycursor.fetchall()
        res_nume=self.root.ids.sci_his
    #Join list with = and \n
        res = list(map("=".join, myresult))
        res.reverse()
        #result = '\n'.join(str(myresult))
        res1=str('\n\n'.join(res))
        res_nume.text=res1
        mydb.commit()
        mydb.close()
#clear History of scientific calculator
    def history2_clear(self):
        mydb = sqlite3.connect('history.db')
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM history2")
        res_nume=self.root.ids.sci_his
        mydb.commit()
        mydb.close()
        res_nume.text="no history"
#help words
    def help(self):
        a=self.root.ids.sm_sub.current
        b=self.root.ids.help_text
        if a=='normal':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click the clock button to see the history, before you calculated.
            """
        if a=='scientific':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click the clock button to see the history, before you calculated.\n\n
            3) You should close the bracket for sin, cos, tan, sqrt and log.\n\n
            4) Do not use more than one thetas at the same time.\n\n
            5) Do not use thetas with sqrt() & log().\n\n
            6) If there is any value before \'(\' you should use any signs (+, -, *, /, %) before \'(\'.\n\n
            7) If there is any value after \')\' you should use any signs (+, -, *, /, %) after \')\'.

            """
        if a=='lcm':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click \"CALCULATE LCM\" button to calculate LCM.\n\n
            3) Click \"CALCULATE GCD\" button to calculate GCD\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='hcf':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click \"CALCULATE HCF\" button to calculate HCF.\n\n
            3) Don't leave the textbox as empty.\n\n
            4) Don't use alphabets in textbox.
            """
        if a=='bmi':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Your should weight in kilograms.\n\n
            3) You should enter your height in centimeter.\n\n
            4) Click \"CALCULATE\" button to calculate BMI and Catagory.\n\n
            5) Catagory :\n
            i) Under Weight - You shoud gain weight.\n
            ii) Normal Weight - You are Healthy.\n
            iii) Obese - You should loss weight.\n\n
            6) Don't leave the textbox as empty.\n\n
            7) Don't use alphabets in textbox.
            """
        if a=='fraction':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter Numerator and Denominator in the correct boxes.\n\n
            3) Click the button as you want (+, -, *, /) to calculate.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='comp_fraction':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter Numerator and Denominator in the correct boxes.\n\n
            3) Click \"COMPARE\" button to compare the fractions.\n\n 
            4) Result :\n
            i) > - Greater than.\n
            ii) < - Less than.\n
            iii) = - Equal to.\n\n
            5) Don't leave the textbox as empty.\n\n
            6) Don't use alphabets in textbox.
            """
        if a=='matrix':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the matrix in the correct boxes.\n\n
            3) Click the button as you want (+, -, *, ) to calculate.\n\n
            4) Don't use alphabets in textbox.
            """
        if a=='type_matrix':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the matrix in the correct boxes.\n\n
            3) Click the \"FIND\" button to find type of matrix.\n\n
            4) Don't use alphabets in textbox.
            """
        if a=='ratio':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click \"FIND MISSING\" button to calculate ratio.\n\n
            3) We can also find the product value.\n
            Example :\n
                i)If we know cost of 2 apples then we can find the cost of multiple apples.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='percentage':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the mark/part and outof/whole in the correct boxes.\n\n
            3) Click the \"Calculate%\" button to find Percentage.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='tax':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the Part & Percentage in the correct boxes.\n\n
            3) Click the \"CALCULATE\" button to calculate the value for the percentage.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='si':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Click \"CALCULATE SI\" button to calculate Simple Interest.\n\n
            3) Click \"CALCULATE CI\" button to calculate Compound Interest.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='peri_2d':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the measurements in the correct boxes.\n\n
            3) Click the \"Calculate Perimeter of specified shapes\" button to find the perimeter of that shape.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='area_2d':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the measurements in the correct boxes.\n\n
            3) Click the \"Calculate Area of specified shapes\" button to find the area of that shape.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='area_3d':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the measurements in the correct boxes.\n\n
            3) Click the \"Calculate TSA of specified 3D shapes\" button to find the TSA of that 3D shape.\n\n
            4) Click the \"Calculate CSA of specified 3D shapes\" button to find the CSA of that 3D shape.\n\n
            5) Don't leave the textbox as empty.\n\n6) Don't use alphabets in textbox.
            """
        if a=='vol_3d':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the measurements in the correct boxes.\n\n
            3) Click the \"Volume of specified 3D shapes\" button to find the volume of that 3D shape.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) Don't use alphabets in textbox.
            """
        if a=='conversion':
            b.text="""
            1) Click the first \"Select\" button to pick the measurement.\n\n
            2) Click the second button to pick measurement.\n\n
            3) Click on the textbox to use your default mobile keyboard.\n\n
            4) Click the \"CONVERT\" button to see the result.\n\n
            5) Don't leave the textbox as empty.\n\n
            6) Don't use alphabets in textbox.
            """
        if a=='sudoku':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the given puzzle in correct boxes.\n\n
            3) Don't use same numbers in same column or row.\n\n
            4) Don't leave the textbox as empty.\n\n
            5) If value not given, that boxex should be \"0\".\n\n
            6) Click the \"SOLVE\" button to get result for puzzle.\n\n
            7) After completing the puzzle reset the texboxes using \"RESET\" button.\n\n
            8) Don't use alphabets in textbox.
            """
        if a=='flames':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the names in given boxes.\n\n
            3) Click the \"FIND\" button to find the flames.\n\n
            4) Don't use space or numeric between the name.\n\n
            5) Don't leave the textbox as empty.
            """
        if a=='age':
            b.text="""
            1) Click on the textbox to use your default mobile keyboard.\n\n
            2) Enter the day in DD box.\n\n
            3) Enter the month in MM box.\n\n
            4) Enter the year in YYYY box.\n\n
            5) Click the \"CALCULATE\" button to find the Age.\n\n
            6) Don't leave the textbox as empty.\n\n
            7) Don't use alphabets in textbox.
            """
        if a=='xo':
            b.text="""
            1) Click on the grey button to start the game.\n\n
            2) X is first.\n\n
            3) If any one wins the button's text colour will turn to red and also display on label.\n\n
            4) If match tie it will display on label.\n\n
            5) Click on the \"RESET\" button to reset the game.\n\n
            """
        if a=='note_pad':
            b.text="""
            1) Write the sums using your fingers or touch pen.\n\n
            2) Click on the \"CLEAR ALL\" button to erase all notes.\n\n
            """
        if a=='about':
            b.text="Contact us"

#To switch screen
    def change_screen(self,name):
        self.root.ids.sm_sub.current=name

#####################################################################################################
#To load app
    def build(self):
        self.theme_cls.theme_style = "Dark"

    #to avoid app crash
        #normal calculator history

        mydb = sqlite3.connect('history.db')
        #create curser
        mycursor =mydb.cursor()
        #crete table
        mycursor.execute("create table if not exists history (quest text,res text)")
        #insert into table
        mycursor.execute("insert into history values (0,0)")
        mydb.commit()

        #scientific calculator history
        #create table
        mycursor.execute("create table if not exists history2 (quest text,res text)")
        #insert into table
        mycursor.execute("insert into history2 values (0,0)")
        mydb.commit()
        mydb.close()
        
        
        return Builder.load_file('design.kv') 
    
    #screen load & switch
    def set_current_screen(self, name: str,switch: bool = True):
        screen_names = [screen.name for screen in self.root.ids.sm_sub.screens]
        name1=screen_names[-2]
        cm=name1+".kv"
        sm = self.root.ids.sm_sub
        if name in screen_names:
            screen = sm.get_screen(name1)
            if screen is not None:
                Builder.unload_file(cm)
                sm.remove_widget(screen)
        #self.root.ids.sm_sub.clear_widgets()
        if not self.root.has_screen(name):
            if name not in screen_names:
                Builder.load_file(screens[name]["kv"])
            self.root.ids.sm_sub.add_widget(screens[name]["view"]())
        if switch:
            self.root.ids.sm_sub.current=name
        


########################################################################################################
        
#Fraction input for all oreration


#To run the app
MainApp().run()