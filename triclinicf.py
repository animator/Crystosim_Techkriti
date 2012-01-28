from visual import *
import wx
import tricliniccorrect
class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,550))
        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the values", pos=(20, 20))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(panel, label="Choose the subdivision", pos=(20, 50))
        self.sampleList = ['primitive']
        self.edithear = wx.ComboBox(panel, pos=(20, 70), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        #self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)
        #self.lblhear = wx.StaticText(self, label="Choose the subdivision", pos=(20, 170))
        #self.sampleList = ['primitive','bodycentered','face centered']
        #self.edithear = wx.ComboBox(self, pos=(20, 190), size=(95, -1), style=wx.CB_DROPDOWN)
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        self.lblname2 = wx.StaticText(panel, label="b", pos=(20,130))
        self.editname2 = wx.TextCtrl(panel, value="1", pos=(150, 130), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname3 = wx.StaticText(panel, label="c", pos=(20,160))
        self.editname3 = wx.TextCtrl(panel, value="1", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname4 = wx.StaticText(panel, label="alpha", pos=(20,190))
        self.editname4 = wx.TextCtrl(panel, value="90", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname5 = wx.StaticText(panel, label="beta", pos=(20,220))
        self.editname5 = wx.TextCtrl(panel, value="90", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname6 = wx.StaticText(panel, label="gamma", pos=(20,250))
        self.editname6 = wx.TextCtrl(panel, value="90", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.lblname3 = wx.StaticText(self, label="Your name :", pos=(20,320))
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar3, self.editname3)
        
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar4, self.editname4)
        self.lblname7 = wx.StaticText(panel, label="percentage :", pos=(20,280))
        self.editname7 = wx.TextCtrl(panel, value="50", pos=(150, 280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname8 = wx.StaticText(panel, label="l", pos=(20,310))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 310), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname9= wx.StaticText(panel, label="w", pos=(20,340))
        self.editname9 = wx.TextCtrl(panel, value="1", pos=(150, 340), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname10 = wx.StaticText(panel, label="h", pos=(20,370))
        self.editname10 = wx.TextCtrl(panel, value="1", pos=(150, 370), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 435))
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
            b=float(self.editname2.GetValue())
            c=float(self.editname3.GetValue())
            alpha=float(self.editname4.GetValue())
            beta=float(self.editname5.GetValue())
            gamma=float(self.editname6.GetValue())
            
            p=float(self.editname7.GetValue())
            p=p/100.0
            l=int(self.editname8.GetValue())
            w=int(self.editname9.GetValue())
            h=int(self.editname10.GetValue())
            
            tricliniccorrect.main(a,b,c,alpha,beta,gamma,l,w,h,p)
            

            
            
                
            return
   
    

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data')
    app.MainLoop()



#main()
