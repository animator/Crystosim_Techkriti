from visual import *
import wx

import cubicplane

class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,500))

        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the data", pos=(20, 30))
        
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,160))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        self.lblname2 = wx.StaticText(panel, label="b", pos=(20,190))
        self.editname2 = wx.TextCtrl(panel, value="1", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar2, self.editname2)
        self.lblname3 = wx.StaticText(panel, label="c", pos=(20,220))
        self.editname3 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        
        self.lblname6 = wx.StaticText(panel, label="h", pos=(20,250))
        self.editname6 = wx.TextCtrl(panel, value="1", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(panel, label="k", pos=(20,280))
        self.editname7 = wx.TextCtrl(panel, value="1", pos=(150,280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(panel, label="l", pos=(20,310))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 310), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 355))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button)
        self.Centre()
        self.Show(True)
    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
       
   
    
    def OnClick(self,event):
            self.Close()
            a=int(self.editname1.GetValue())
            b=int(self.editname2.GetValue())
            c=int(self.editname3.GetValue())
            
            l=int(self.editname6.GetValue())
            w=int(self.editname7.GetValue())
            h=int(self.editname8.GetValue())
            cubicplane.main(a,b,c,l,w,h)
           
                
            return
   
       

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data ')
    app.MainLoop()


#main()
