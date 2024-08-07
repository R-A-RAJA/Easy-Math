from kivy.uix.screenmanager import Screen

class FlamesView(Screen):
    def flames(self):
        try:
            s1=self.ids.flames1.text
            s2=self.ids.flames2.text
            if s1.isalpha() and s2.isalpha() and s1!=s2:
                name1=list(s1.lower())
                name2=list(s2.lower())
                for i,x in enumerate(name1):
                    j="".join(name2).find(name1[i])
                    if(j!=-1):
                        name1[i]='*'
                        name2[j]='*' 
        
                x=lambda x: True if x!='*' else False 
                a=[]
                a.extend(list(filter(x,name1)))
                a.extend(list(filter(x,name2)))
                n=len(a)

                flames=list("FLAMES")
                i=0
                c=0
                while len(list(filter(x,flames)))!=1:
                    if i==6:
                        i=0      
                    if flames[i]!='*':
                        c+=1      
                    if c==n:
                        flames[i]='*'
                        c=0       
                    i+=1
                result=''.join(list(filter(x,flames)))

                flamesDict={
                    'F':'Friend',
                    'L':'Love',
                    'A':'Affection',
                    'M':'Marriage',
                    'E':'Enemy',
                    'S':'Sibling',
                }
                res_flames=flamesDict[result]

                flames_res=self.ids.flames_res
                flames_res.text=res_flames
            else:
                flames_res=self.ids.flames_res
                flames_res.text="Error!"
        except:
            flames_res=self.ids.flames_res
            flames_res.text="Error!"