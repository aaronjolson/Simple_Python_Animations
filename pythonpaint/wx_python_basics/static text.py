import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'frame window',size=(300,200))
        panel=wx.Panel(self)

        wx.StaticText(panel, -1,"this is static text",(10,10))

        custom=wx.StaticText(panel, -1,"custom text",(10,30),(260,20),wx.ALIGN_CENTER)
        custom.SetForegroundColour('blue')
        custom.SetBackgroundColour('white')



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
