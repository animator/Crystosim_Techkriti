from visual import *
import wx

import cubicfp1
import tetragonalfp1
import orthorhombicfp1
import hexagonalfp1
#import trigonalf

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(self, label="Choose the type of lattice ?", pos=(20, 100))
        self.sampleList = ['cubic', 'tetragonal', 'orthorhombic', 'monoclinic','trigonal','hexagonal','triclinic']
        self.edithear = wx.ComboBox(self, pos=(80, 120), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
                #the control button
        self.button =wx.Button(self, label="NEXT", pos=(30, 335))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
       
               
    def OnClick(self,event):
        if self.str1=='cubic':
            print 'a'
            cubicfp1.main()
        if self.str1=='tetragonal':
            print 'a'
            tetragonalfp1.main()
        if self.str1=='orthorhombic':
            print 'a'
            orthorhombicfp1.main()
        if self.str1=='hexagonal':
            print 'a'
            hexagonalfp1.main()
        if self.str1=='triclinic':
            print 'a'
        if self.str1=='trigonal':
            #trigonalf.main()
            print 'a'
            
            
        
            
        if(self.str1=='monoclinic'):
            print 'ash'
                               
                
        return
    

def main():
    app = wx.App(False)
    x,y=wx.GetDisplaySize()
    sx, sy = 400,400
    frame = wx.Frame(None,-1,'Enter Data',wx.Point((x-sx)/2,(y-sy)/2), wx.Size(sx,sy))
    panel = ExamplePanel(frame)
    frame.Show()
    app.MainLoop()


#main()
