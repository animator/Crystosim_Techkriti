from visual import *
import wx
import cubic
import cubicfc
import tetragonal
import tetragonalbc
import orthorhombic
import orthorhombicbc
import orthorhombicec
import orthorhombicfc
import monoclinic
import trigonal
import hexagonal
import triclinic
import cubicbc
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the values", pos=(20, 30))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(self, label="Choose the subdivision", pos=(20, 80))
        self.sampleList = ['primitive','bodycentered','face centered']
        self.edithear = wx.ComboBox(self, pos=(20, 100), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        #self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)
        #self.lblhear = wx.StaticText(self, label="Choose the subdivision", pos=(20, 170))
        #self.sampleList = ['primitive','bodycentered','face centered']
        #self.edithear = wx.ComboBox(self, pos=(20, 190), size=(95, -1), style=wx.CB_DROPDOWN)
        self.lblname1 = wx.StaticText(self, label="a", pos=(20,160))
        self.editname1 = wx.TextCtrl(self, value="1", pos=(150, 160), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        
        #self.lblname3 = wx.StaticText(self, label="Your name :", pos=(20,320))
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar3, self.editname3)
        
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar4, self.editname4)
        self.lblname5 = wx.StaticText(self, label="percentage :", pos=(20,190))
        self.editname5 = wx.TextCtrl(self, value="50", pos=(150, 190), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname6 = wx.StaticText(self, label="l", pos=(20,220))
        self.editname6 = wx.TextCtrl(self, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(self, label="w", pos=(20,250))
        self.editname7 = wx.TextCtrl(self, value="1", pos=(150, 250), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(self, label="h", pos=(20,280))
        self.editname8 = wx.TextCtrl(self, value="1", pos=(150, 280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(self, label="OK", pos=(30, 335))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.button1=wx.Button(self,label="OK",pos=(30,515))
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button1)
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button)

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
       
   
    
    def OnClick(self,event):
            a=int(self.editname1.GetValue())
            
            p=int(self.editname5.GetValue())
            p=p/100.0
            l=int(self.editname6.GetValue())
            w=int(self.editname7.GetValue())
            h=int(self.editname8.GetValue())
            #r=1
            #print self.str1
            #print self.str2
            if(self.str1=='primitive'):
                cubic.main(a,l,w,h,p)
            if(self.str1=='bodycentered'):
                 cubicbc.main(l,w,h,a,p)
            if(self.str1=='face centered'):
                 cubicfc.main(l,w,h,a,p)
             # remove previous controls
             
            

            
            self.Close(True)
            self.Destroy()
                
            return
   
    

    

def main():
    app = wx.App(False)
    x,y=wx.GetDisplaySize()
    sx, sy = 400,450
    frame = wx.Frame(None,-1,'Enter Data',wx.Point((x-sx)/2,(y-sy)/2), wx.Size(sx,sy))
    panel = ExamplePanel(frame)
    
    frame.Show()
    
    app.MainLoop()


#main()
