import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame', size=(300,200))
        panel=wx.Panel(self)

        slider=wx.Slider(panel,-1, 50,1,100,pos=(10,10),size=(250,-1),style=wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider.SetTickFreq(5,1)



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
