import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame aka window',size=(300,200))
        panel=wx.Panel(self)
        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        first=wx.Menu()
        second=wx.Menu()
        first.Append(wx.NewId(),"New Window","this is a new window")
        first.Append(wx.NewId(),"Open","this is a new window")
        menubar.Append(first,"File")
        menubar.Append(second,"Edit")
        self.SetMenuBar(menubar)

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
