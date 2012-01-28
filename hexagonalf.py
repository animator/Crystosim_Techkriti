from visual import *
import wx

import hexagonal

class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(300,400))

        panel=wx.Panel(self,-1)
        
        self.quote = wx.StaticText(panel, label="Enter the data for the primitive case", pos=(20, 30))
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
       
        self.lblname3 = wx.StaticText(panel, label="c", pos=(20,130))
        self.editname3 = wx.TextCtrl(panel, value="1", pos=(150, 130), size=(140,-1),style=wx.TE_PROCESS_ENTER)
       
        self.lblname5 = wx.StaticText(panel, label="percentage :", pos=(20,160))
        self.editname5 = wx.TextCtrl(panel, value="50", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname6 = wx.StaticText(panel, label="l", pos=(20,190))
        self.editname6 = wx.TextCtrl(panel, value="1", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(panel, label="w", pos=(20,220))
        self.editname7 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(panel, label="h", pos=(20,250))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 300))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.Centre()
        self.Show(True)                                                            
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button)

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
       
   
    
    def OnClick(self,event):

            self.Close()                                                          
            a=float(self.editname1.GetValue())
            
            c=float(self.editname3.GetValue())
            p=float(self.editname5.GetValue())
            p=p/100.0
            l=int(self.editname6.GetValue())
            w=int(self.editname7.GetValue())
            h=int(self.editname8.GetValue())
            
            hexagonal.main(a,c,l,w,h,p)
            
                
            return
   
       

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data ')
    app.MainLoop()


#main()
