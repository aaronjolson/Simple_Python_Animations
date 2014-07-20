import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame Window',size=(300,200))
        panel =wx.Panel(self)

        box=wx.MessageDialog(None,'Is this the question?','Title',wx.YES_NO)#could be OK
        answer=box.ShowModal()
        box.Destroy



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
