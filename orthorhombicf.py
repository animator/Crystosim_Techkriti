from visual import *
import wx

import orthorhombic
import orthorhombicbc
import orthorhombicec
import orthorhombicfc

class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(400,500))

        panel=wx.Panel(self,-1)
        self.quote = wx.StaticText(panel, label="Enter the data", pos=(20, 30))
        
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(panel, label="Choose the subdivision", pos=(20,60))
        self.sampleList = ['primitive','bodycentered','face centered','end centered']
        self.edithear = wx.ComboBox(panel, pos=(20, 80), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        #self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)
        #self.lblhear = wx.StaticText(self, label="Choose the subdivision", pos=(20, 170))
        #self.sampleList = ['primitive','bodycentered','face centered']
        #self.edithear = wx.ComboBox(self, pos=(20, 190), size=(95, -1), style=wx.CB_DROPDOWN)
        self.lblname1 = wx.StaticText(panel, label="a", pos=(20,160))
        self.editname1 = wx.TextCtrl(panel, value="1", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        self.lblname2 = wx.StaticText(panel, label="b", pos=(20,190))
        self.editname2 = wx.TextCtrl(panel, value="1", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar2, self.editname2)
        self.lblname3 = wx.StaticText(panel, label="c", pos=(20,220))
        self.editname3 = wx.TextCtrl(panel, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.lblname3 = wx.StaticText(self, label="Your name :", pos=(20,320))
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar3, self.editname3)
        
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar4, self.editname4)
        self.lblname5 = wx.StaticText(panel, label="percentage :", pos=(20,250))
        self.editname5 = wx.TextCtrl(panel, value="50", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname6 = wx.StaticText(panel, label="l", pos=(20,280))
        self.editname6 = wx.TextCtrl(panel, value="1", pos=(150, 280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(panel, label="w", pos=(20,310))
        self.editname7 = wx.TextCtrl(panel, value="1", pos=(150,310), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(panel, label="h", pos=(20,340))
        self.editname8 = wx.TextCtrl(panel, value="1", pos=(150, 340), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(panel, label="OK", pos=(30, 385))
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
            a=float(self.editname1.GetValue())
            b=float(self.editname2.GetValue())
            c=float(self.editname3.GetValue())
            p=float(self.editname5.GetValue())
            p=p/100.0
            l=int(self.editname6.GetValue())
            w=int(self.editname7.GetValue())
            h=int(self.editname8.GetValue())
            #r=1
            #print self.str1
            #print self.str2
            if(self.str1=='primitive'):
                    orthorhombic.main(l,w,h,a,b,c,p)
            if(self.str1=='bodycentered'):
                    orthorhombicbc.main(l,w,h,a,b,c,p)
            if(self.str1=='face centered'):
                    orthorhombicfc.main(l,w,h,a,b,c,p)
            if(self.str1=='end centered'):
                    orthorhombicec.main(l,w,h,a,b,c,p)
            #self.Destroy()
            #self.Close()
                
            return
   
       

    

def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data')
    app.MainLoop()


#main()
