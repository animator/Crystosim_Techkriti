from visual import *
import wx
import planesmonoclinic
class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,500))
        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the values", pos=(20, 20))
        str1=' '
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
        
        self.lblname8 = wx.StaticText(panel, label="h", pos=(20,280))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname9= wx.StaticText(panel, label="k", pos=(20,310))
        self.editname9 = wx.TextCtrl(panel, value="1", pos=(150, 310), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname10 = wx.StaticText(panel, label="l", pos=(20,340))
        self.editname10 = wx.TextCtrl(panel, value="1", pos=(150, 340), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 385))
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
            b=int(self.editname2.GetValue())
            c=int(self.editname3.GetValue())
            alpha=int(self.editname4.GetValue())
            beta=int(self.editname5.GetValue())
            gamma=int(self.editname6.GetValue())
            
            
            h=int(self.editname8.GetValue())
            k=int(self.editname9.GetValue())
            l=int(self.editname10.GetValue())
            
            planesmonoclinic.main(a,b,c,alpha,beta,gamma,h,k,l)
            

            
            
                
            return
   
    

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data')
    app.MainLoop()



#main()
