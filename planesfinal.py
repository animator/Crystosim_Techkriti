from visual import *
import wx
import cubic
import cubicplane
import planesformonoclinic
import hcpplane
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(self, label="Choose the lattice ?", pos=(20, 90))
        self.sampleList = ['cubic', 'tetragonal', 'orthorhombic', 'monoclinic','trigonal','hexagonal','triclinic']
        self.edithear = wx.ComboBox(self, pos=(80, 110), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        #self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)
        self.lblname1 = wx.StaticText(self, label="a", pos=(20,260))
        self.editname1 = wx.TextCtrl(self, value="1", pos=(150, 260), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar1, self.editname1)
        self.lblname2 = wx.StaticText(self, label="b", pos=(20,280))
        self.editname2 = wx.TextCtrl(self, value="1", pos=(150, 280), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar2, self.editname2)
        self.lblname3 = wx.StaticText(self, label="c", pos=(20,300))
        self.editname3 = wx.TextCtrl(self, value="1", pos=(150, 300), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.lblname3 = wx.StaticText(self, label="Your name :", pos=(20,320))
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar3, self.editname3)
        self.lblname4 = wx.StaticText(self, label="alpha", pos=(20,320))
        self.editname4 = wx.TextCtrl(self, value="90", pos=(150, 320), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar4, self.editname4)
        self.lblname5 = wx.StaticText(self, label="beta", pos=(20,340))
        self.editname5 = wx.TextCtrl(self, value="90", pos=(150, 340), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT_ENTER, self.EvtChar5, self.editname5)
        self.lblname6 = wx.StaticText(self, label="gamma", pos=(20,360))
        self.editname6 = wx.TextCtrl(self, value="90", pos=(150, 360), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(self, label="miller index h", pos=(20,380))
        self.editname7 = wx.TextCtrl(self, value="1", pos=(150, 380), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(self, label="miller index k", pos=(20,400))
        self.editname8 = wx.TextCtrl(self, value="1", pos=(150, 400), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname9 = wx.StaticText(self, label="miller index l", pos=(20,420))
        self.editname9 = wx.TextCtrl(self, value="1", pos=(150, 420), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        

        #the control button
        self.button =wx.Button(self, label="Save", pos=(30, 435))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
        
         
    def OnClick(self,event):
            a=int(self.editname1.GetValue())
            b=int(self.editname2.GetValue())
            c=int(self.editname3.GetValue())
            alpha=int(self.editname4.GetValue())
            
            beta=int(self.editname5.GetValue())
            gamma=int(self.editname6.GetValue())
            h=int(self.editname7.GetValue())
            k=int(self.editname8.GetValue())
            l=int(self.editname9.GetValue())
            
            #print self.str1
            #print self.str2
            if(self.str1=='cubic' or self.str1=='tetragonal' or self.str1=='orthorhombic'):
                cubicplane.main(a,b,c,h,k,l)
                
            if(self.str1=='monoclinic' or self.str1=='trigonal' or self.str1=='triclinic'):
                planesformonoclinic.main(a,b,c,alpha,beta,gamma,h,k,l)
                
            if(self.str1=='hexagonal'):
                hcpplane.drawhc(a,h,k,0,l)
            return
    

def main():
    app = wx.App(False)
    x,y=wx.GetDisplaySize()
    sx, sy = 400,600
    frame = wx.Frame(None,-1,'Enter Data 1',wx.Point((x-sx)/2,(y-sy)/2), wx.Size(sx,sy))
    
    panel = ExamplePanel(frame)
    frame.Show()
    app.MainLoop()

#main()

