from visual import *
import wx
import cubic
import cubicfc
import tetragonal
import tetragonalbc
import orthorhombicf
import orthorhombicbc
import orthorhombicec
import orthorhombicfc
import monoclinic
import trigonalf
import hexagonalf
import triclinic
import cubicbc
import cubicf
import tetragonalf

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(self, label="Choose the type of lattice ?", pos=(20, 90))
        self.sampleList = ['cubic', 'tetragonal', 'orthorhombic', 'monoclinic','trigonal','hexagonal','triclinic']
        self.edithear = wx.ComboBox(self, pos=(80, 110), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
                #the control button
        self.button =wx.Button(self,-1,label="Next", pos=(30, 295))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        

    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
        
   
    def OnClick(self,event):
        self.Close()   
        if self.str1=='cubic':
            cubicf.main()
        if self.str1=='tetragonal':
            tetragonalf.main()
        if self.str1=='orthorhombic':
            orthorhombicf.main()
        if self.str1=='hexagonal':
            hexagonalf.main()
        if self.str1=='triclinic':
            print 'a'
        if self.str1=='trigonal':
            trigonalf.main()
            
            
        
            
        #if(self.str1=='monoclinic'):
            
             #print 'v'
        
        
        #self.Destroy()
        return
    

def main():
    app = wx.App(False)
    x,y=wx.GetDisplaySize()
    sx, sy = 400,400
    frame = wx.Frame(None,-1,'Enter Data 1',wx.Point((x-sx)/2,(y-sy)/2), wx.Size(sx,sy))
    panel = ExamplePanel(frame)
    frame.Show()
    app.MainLoop()


main()
