import wx
import visual

import clear

import planelatticeframe
import directionframefinal
import latticeframefinal,latticeframefinal1


# ***********************************************************************
# ***********************************************************************
def My_Main_Application ( My_Form ) :
  app = wx.PySimpleApp ()
  frame = My_Form ( )
  
  frame.Show ( True )
  app.MainLoop ()
# ***********************************************************************


# ***********************************************************************
# ***********************************************************************
class Simple_Test_Form ( wx.Frame ):
  def __init__ ( self, ini = None ) :
    x,y=wx.GetDisplaySize()
    wx.Frame.__init__ ( self, None,-1,'CrystoSim',size=(x,y) )
    
    self.Splitter=wx.SplitterWindow( self)
    self.p1=wx.Panel( self.Splitter)
    
    str1=" "
    str2=" "
    self.p2=wx.Panel( self.Splitter)
    self.p2.SetBackgroundColour('')

    #making changes to the part where things will be asked
    self.p2.lblhear = wx.StaticText(self.p2, label="CRYSTOSIM", pos=(20, 90))
    

    #the control button
    self.p2.button =wx.Button(self.p2, label="LATTICE ", pos=(30, 140))
    self.p2.Bind(wx.EVT_BUTTON, self.OnClick,self.p2.button)
    self.p2.button1=wx.Button(self.p2,label="PLANE ",pos=(30,170))
    self.p2.Bind(wx.EVT_BUTTON,self.OnClick1,self.p2.button1)
    self.p2.button2=wx.Button(self.p2,label="DIRECTION",pos=(30,200))
    self.p2.Bind(wx.EVT_BUTTON,self.OnClick2,self.p2.button2)
    self.p2.button3=wx.Button(self.p2,label="CLEAR ",pos=(30,230))
    self.p2.Bind(wx.EVT_BUTTON,self.OnClear,self.p2.button3)
    self.p2.button5=wx.Button(self.p2,label="STRUCTURES ",pos=(30,260))
    self.p2.Bind(wx.EVT_BUTTON,self.OnClick3,self.p2.button5)
    self.p2.button4=wx.Button(self.p2,label="EXIT ",pos=(30,290))
    self.p2.Bind(wx.EVT_BUTTON,self.OnClose,self.p2.button4)

    

    
    
    
      
    self.Splitter.SplitVertically ( self.p1, self.p2,sashPosition = x-200 )
    self.Splitter.SetMinimumPaneSize(50)
    Sizer = wx.BoxSizer ( )
    Sizer.Add ( self.Splitter, 1, wx.EXPAND )
    self.SetSizer ( Sizer )

    # create a VPython application, just an copy of the Ball-demo
    visual.text(text='CrystoSim',
     align='center', depth=-0.3, color=visual.color.green) 
    #self.ash()

    # initialize the State_Machine and start the timer
    self.VP_State = 0
    self.Old_Size = ( 0, 0 )
    self.Timer = wx.Timer ( self )
    # the third parameter is essential to allow other timers
    self.Bind ( wx.EVT_TIMER, self._On_Timer, self.Timer)
    self.Timer.Start ( 100 )
  
  
               

  def OnClick(self,event):
            
            
            latticeframefinal.main()
            
  def OnClick1(self,event):
          #print 'a'
            planelatticeframe.main()
  def OnClick2(self,event):
     # print 'a'
            directionframefinal.main()
  def OnClick3(self,event):
            latticeframefinal1.main()
            
            
  def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
  def OnClear(self,event):
       clear.main()
          
    

  # *****************************************************************
  # *****************************************************************
  def _On_Timer ( self, event ) :
    size = self.p1.GetSize ()

    # Rest, wait till a resize is detected
    if self.VP_State == 0 :
      if size != self.Old_Size :
        self.Old_Size = size
        self.VP_State = 1
        visual.scene.visible = False

    # wait in this state until size remains stable
    elif self.VP_State == 1 :
      if size != self.Old_Size :
        self.Old_Size = size
      else :
        self.VP_State = 2

    # do an extra test if size is still unchanged
    elif self.VP_State == 2 :
      if size != self.Old_Size :
        self.Old_Size = size
        self.VP_State = 1
      else :
        self.VP_State = 3

    # now the size is stable for at least 2 clock cycli
    # so it's time to recreate the VPython window
    elif self.VP_State == 3 :
      visual.scene.visible = True
      wx.CallLater ( 10, self.Fetch_VP )
      self.VP_State = 4

  # *****************************************************************
  # Recreate and Position the VPython window
  # *****************************************************************
  def Fetch_VP ( self ) :
    import win32gui, win32con

    # Try to find the newly created VPython window
    # which is now a main-application-window
    self.VP = win32gui.FindWindow ( None, 'VPython' )

    if self.VP:
      w = self.Old_Size[0]
      h = self.Old_Size[1]

      # get the handle of the dock container
      PP = self.p1.GetHandle ()

      # Set Position and Size of the VPython window,
      # Before Docking it !!
      #flags = win32con.SWP_ASYNCWINDOWPOS or \
      #        win32con.SWP_SHOWWINDOW     or \
      #        win32con.SWP_FRAMECHANGED
      flags = win32con.SWP_SHOWWINDOW or \
              win32con.SWP_FRAMECHANGED
      win32gui.SetWindowPos ( self.VP, win32con.HWND_TOPMOST,
                              -8, -44, w+56, h+66, flags )

      # Dock the VPython window
      win32gui.SetParent ( self.VP, PP )

      # reset the State Machine
      self.VP_State = 0
# ***********************************************************************


# ***********************************************************************
# demo program
# ***********************************************************************
if __name__ == '__main__':
  My_Main_Application ( Simple_Test_Form )
  
# ***********************************************************************
