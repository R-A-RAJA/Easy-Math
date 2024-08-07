from kivy.uix.screenmanager import Screen

class XOView(Screen):
    turn="X"
    #winner variable for to find win or lose or tie
    winner=False
    #disable all btn
    def disable_all_btn(self):
        self.ids.xo1.disabled= True
        self.ids.xo2.disabled= True
        self.ids.xo3.disabled= True
        self.ids.xo4.disabled= True
        self.ids.xo5.disabled= True
        self.ids.xo6.disabled= True
        self.ids.xo7.disabled= True
        self.ids.xo8.disabled= True
        self.ids.xo9.disabled= True
  #End game and highlight
    def end_game(self,a,b,c):
        self.winner=True
        a.color="red"
        b.color="red"
        c.color="red"
        #disable all btn
        self.disable_all_btn()
        self.ids.res_xo.text= str(a.text)+" Wins!"
  #function to find match tie
    def no_winner(self):
        if self.winner==False and\
        self.ids.xo1.disabled== True and\
        self.ids.xo2.disabled== True and\
        self.ids.xo3.disabled== True and\
        self.ids.xo4.disabled== True and\
        self.ids.xo5.disabled== True and\
        self.ids.xo6.disabled== True and\
        self.ids.xo7.disabled== True and\
        self.ids.xo8.disabled== True and\
        self.ids.xo9.disabled== True:
            self.ids.res_xo.text="IT'S A TIE!"
  #Condition xo
    def win(self):
        #get all btn
        xo1=self.ids.xo1
        xo2=self.ids.xo2
        xo3=self.ids.xo3
        xo4=self.ids.xo4
        xo5=self.ids.xo5
        xo6=self.ids.xo6
        xo7=self.ids.xo7
        xo8=self.ids.xo8
        xo9=self.ids.xo9
        #Across
        if xo1.text !="" and xo1.text==xo2.text==xo3.text:
            self.end_game(xo1,xo2,xo3)
        if xo4.text !="" and xo4.text==xo5.text==xo6.text:
            self.end_game(xo4,xo5,xo6)
        if xo7.text !="" and xo7.text==xo8.text==xo9.text:
            self.end_game(xo7,xo8,xo9)
        #Down
        if xo1.text !="" and xo1.text==xo4.text==xo7.text:
            self.end_game(xo1,xo4,xo7)
        if xo2.text !="" and xo2.text==xo5.text==xo8.text:
            self.end_game(xo2,xo5,xo8)
        if xo3.text !="" and xo3.text==xo6.text==xo9.text:
            self.end_game(xo3,xo6,xo9)
        #diagonal
        if xo1.text !="" and xo1.text==xo5.text==xo9.text:
            self.end_game(xo1,xo5,xo9)
        if xo3.text !="" and xo3.text==xo5.text==xo7.text:
            self.end_game(xo3,xo5,xo7)
        #function for match tie
        self.no_winner()

  # X O select
    
    def xo(self,xo):
        self.ids.xo1.color= "white"
        self.ids.xo2.color= "white"
        self.ids.xo3.color= "white"
        self.ids.xo4.color= "white"
        self.ids.xo5.color= "white"
        self.ids.xo6.color= "white"
        self.ids.xo7.color= "white"
        self.ids.xo8.color= "white"
        self.ids.xo9.color= "white"
        if self.turn=="X":
            xo.text="X"
            xo.disabled=True
            xo.color="green"
            self.ids.res_xo.text="O's turn"
            self.turn="O"

        else:
            xo.text="O" 
            xo.disabled=True
            xo.color="green"
            self.ids.res_xo.text="X's turn"
            self.turn="X"
        
        self.win()
  #reset XO
    def reset_xo(self):
        self.turn="X"
        #make button active
        self.ids.xo1.disabled= False
        self.ids.xo2.disabled= False
        self.ids.xo3.disabled= False
        self.ids.xo4.disabled= False
        self.ids.xo5.disabled= False
        self.ids.xo6.disabled= False
        self.ids.xo7.disabled= False
        self.ids.xo8.disabled= False
        self.ids.xo9.disabled= False
        #text to empty
        self.ids.xo1.text= ""
        self.ids.xo2.text= ""
        self.ids.xo3.text= ""
        self.ids.xo4.text= ""
        self.ids.xo5.text= ""
        self.ids.xo6.text= ""
        self.ids.xo7.text= ""
        self.ids.xo8.text= ""
        self.ids.xo9.text= ""
        #text color

        #reset color
        self.ids.xo1.color= "white"
        self.ids.xo2.color= "white"
        self.ids.xo3.color= "white"
        self.ids.xo4.color= "white"
        self.ids.xo5.color= "white"
        self.ids.xo6.color= "white"
        self.ids.xo7.color= "white"
        self.ids.xo8.color= "white"
        self.ids.xo9.color= "white"
        #label reset
        self.ids.res_xo.text="X goes first!"
        #reset winner variable
        self.winner=False
