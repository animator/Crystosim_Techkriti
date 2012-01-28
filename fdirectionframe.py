from visual import *
import wx

import cubicfp
import tetragonalfp
import orthorhombicfp
import hexagonalfp
#import trigonalf
#import directionframe

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        str1=' '
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(self, label="Choose the type of lattice ?", pos=(20, 100))
        self.sampleList = ['cubic', 'tetragonal', 'orthorhombic', 'hexagonal']
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
            
            cubicfp.main()
        if self.str1=='tetragonal':
            
            tetragonalfp.main()
        if self.str1=='orthorhombic':
            
            orthorhombicfp.main()
        if self.str1=='hexagonal':
            
            hexagonalfp.main()
        if (self.str1=='triclinic' or self.str1=='trigonal' or self.str1=='monoclinic'):
            #directionframe.main()
            print 'a'
            
            
        
            
       
                               
                
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
