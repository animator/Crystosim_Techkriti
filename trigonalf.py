from visual import *
import wx
import tricliniccorrect
class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,500))
        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the values ", pos=(20, 30))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(panel, label="Choose the subdivision", pos=(20, 50))
        self.sampleList = ['primitive']
        self.edithear = wx.ComboBox(panel, pos=(20, 70), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        
        self.lblname4 = wx.StaticText(panel, label="alpha", pos=(20,130))
        self.editname4 = wx.TextCtrl(panel, value="90", pos=(150, 130), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        
        self.lblname7 = wx.StaticText(panel, label="percentage :", pos=(20,160))
        self.editname7 = wx.TextCtrl(panel, value="50", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname8 = wx.StaticText(panel, label="l", pos=(20,190))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname9= wx.StaticText(panel, label="w", pos=(20,220))
        self.editname9 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname10 = wx.StaticText(panel, label="h", pos=(20,250))
        self.editname10 = wx.TextCtrl(panel, value="1", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 355))
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
            
            a=float(self.editname1.GetValue())
           
            alpha=float(self.editname4.GetValue())
            
            
            p=float(self.editname7.GetValue())
            p=p/100.0
            l=int(self.editname8.GetValue())
            w=int(self.editname9.GetValue())
            h=int(self.editname10.GetValue())
            
            tricliniccorrect.main(a,a,a,alpha,alpha,alpha,l,w,h,p)
            

            
            
                
            return
   
    

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data ')
    app.MainLoop()



#main()
