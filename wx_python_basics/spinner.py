import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame', size=(300,200))
        panel=wx.Panel(self)

        spinner=wx.SpinCtrl(panel,-1,'',(40,40),(90,-1), style=wx.SP_WRAP)
        spinner.SetRange(1,100)
        spinner.SetValue(10)



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
