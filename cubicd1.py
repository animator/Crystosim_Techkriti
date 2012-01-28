from visual import *
import wx
import millerdirecn


class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,350))
        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the values", pos=(20, 30))
        str1=' '
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname6 = wx.StaticText(panel, label="h", pos=(20,140))
        self.editname6 = wx.TextCtrl(panel, value="1", pos=(150, 140), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(panel, label="k", pos=(20,180))
        self.editname7 = wx.TextCtrl(panel, value="1", pos=(150, 180), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(panel, label="l", pos=(20,220))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 275))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.button1=wx.Button(self,label="OK",pos=(30,515))
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button1)
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
            
            
            h=int(self.editname6.GetValue())
            k=int(self.editname7.GetValue())
            l=int(self.editname8.GetValue())
            #r=1
            #print self.str1
            #print self.str2
            millerdirecn.main(a,a,a,90,90,90,h,k,l)
             # remove previous controls
             
            

            
            
                
            return
   
    

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data ')
    app.MainLoop()



#main()
