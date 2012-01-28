from visual import *
import wx
import cscl,batio3,caf2,nacl

class ExamplePanel(wx.Frame):
    def __init__(self, parent,id,title):
        wx.Frame.__init__(self, parent,id,title,size=(300,400))

        panel=wx.Panel(self,-1)
        
        self.quote = wx.StaticText(panel, label="Enter the data", pos=(20, 30))
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.lblhear = wx.StaticText(panel, label="Choose the type of lattice ?", pos=(20, 90))
        self.sampleList = ['CsCl','BaTiO3','CaF2','NaCl']
        self.edithear = wx.ComboBox(panel, pos=(80, 110), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
                #the control button
        self.button =wx.Button(panel,-1,label="Next", pos=(30, 295))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        

    
            
            
        
        
        self.Centre()
        self.Show(True)


    def EvtComboBox(self, event):
       # self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
        s=event.GetString()
        self.str1=s
        
   
    def OnClick(self,event):
        self.Close()   
        if self.str1=='CsCl':
            cscl.main()
        if self.str1=='BaTiO3':
            batio3.main()
        if self.str1=='CaF2':
            caf2.main()
        if self.str1=='NaCl':
            nacl.main()
        
            
             #print 'v'
        
        
        #self.Destroy()
        #return
    
def main():
    app = wx.App()
    ExamplePanel(None,-1,'Enter Data ')
    app.MainLoop()


#main()
