from visual import *
import wx
import millerdirection
import directionsforothers
import hcpplane
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Enter the data", pos=(20, 30))
        
        self.lblname1 = wx.StaticText(self, label="a", pos=(20,100))
        self.editname1 = wx.TextCtrl(self, value="1", pos=(150, 100), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname6 = wx.StaticText(self, label="h", pos=(20,140))
        self.editname6 = wx.TextCtrl(self, value="1", pos=(150, 140), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname7= wx.StaticText(self, label="k", pos=(20,180))
        self.editname7 = wx.TextCtrl(self, value="1", pos=(150,180), size=(140,-1),style=wx.TE_PROCESS_ENTER)
        self.lblname8 = wx.StaticText(self, label="l", pos=(20,220))
        self.editname8 = wx.TextCtrl(self, value="1", pos=(150, 220), size=(140,-1),style=wx.TE_PROCESS_ENTER)
                #the control button
        self.button =wx.Button(self, label="OK", pos=(30, 300))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button)

   
   
    
    def OnClick(self,event):
            a=int(self.editname1.GetValue())
                       
            h=int(self.editname6.GetValue())
            k=int(self.editname7.GetValue())
            l=int(self.editname8.GetValue())
            #r=1
            #print self.str1
            #print self.str2
            hcpplane.drawhc(a,h,k,0,l)
            #self.Destroy()
            #self.Close()
                
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
