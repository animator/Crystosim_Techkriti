from visual import *
import wx

import millerdirection
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        
        self.lblname1 = wx.StaticText(self, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(self, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        self.lblname2 = wx.StaticText(self, label="b", pos=(20,130))
        self.editname2 = wx.TextCtrl(self, value="1", pos=(150, 130), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar2, self.editname2)
        self.lblname3 = wx.StaticText(self, label="c", pos=(20,160))
        self.editname3 = wx.TextCtrl(self, value="1", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        
        self.lblname6 = wx.StaticText(self, label="h", pos=(20,200))
        self.editname6 = wx.TextCtrl(self, value="1", pos=(150, 200), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(self, label="k", pos=(20,230))
        self.editname7 = wx.TextCtrl(self, value="1", pos=(150, 230), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(self, label="l", pos=(20,260))
        self.editname8 = wx.TextCtrl(self, value="1", pos=(150, 260), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(self, label="OK", pos=(30, 330))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button)

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
       
   
    
    def OnClick(self,event):
            a=int(self.editname1.GetValue())
            b=int(self.editname2.GetValue())
            c=int(self.editname3.GetValue())
            
            h=int(self.editname6.GetValue())
            k=int(self.editname7.GetValue())
            l=int(self.editname8.GetValue())
            #r=1
            #print self.str1
            #print self.str2
            millerdirection.main(a,b,c,90,90,90,h,k,l)
            #self.Destroy()
            #self.Close()
                
            return
   
       

    

def main():
    app = wx.App(False)
    x,y=wx.GetDisplaySize()
    sx, sy = 400,400
    frame = wx.Frame(None,-1,'Enter Data',wx.Point((x-sx)/2,(y-sy)/2), wx.Size(sx,sy))
    panel = ExamplePanel(frame)
    
    frame.Show()
    
    app.MainLoop()
    frame.Destroy()


#main()
