from visual import *
import wx

import hcpdirection

class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,400))

        panel=wx.Panel(self,-1)
        
        self.quote = wx.StaticText(panel, label="Enter the data for the primitive case", pos=(20, 30))
        self.lblname1 = wx.StaticText(panel, label="s", pos=(20,100))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        
        
        self.lblname6 = wx.StaticText(panel, label="h", pos=(20,140))
        self.editname6 = wx.TextCtrl(panel, value="1", pos=(150, 140), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(panel, label="k", pos=(20,180))
        self.editname7 = wx.TextCtrl(panel, value="1", pos=(150, 180), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(panel, label="l", pos=(20,220))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
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
            s=int(self.editname1.GetValue())
            s=s*2
            
            h=int(self.editname6.GetValue())
            k=int(self.editname7.GetValue())
            l=int(self.editname8.GetValue())
            hcpdirection.drawhc(s,h,k,0,l)
                
            return
   
       

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data')
    app.MainLoop()


#main()
