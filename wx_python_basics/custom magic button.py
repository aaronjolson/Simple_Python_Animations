import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame', size=(300,200))
        panel=wx.Panel(self)

        pic=wx.Image("pic.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button=wx.BitmapButton(panel,-1,pic,pos=(10,10))
        self.Bind(wx.EVT_BUTTON,self.magic, self.button)
        self.button.SetDefault()

    def magic(self,event):
        self.Destroy()



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent= None,id=-1)
    frame.Show()
    app.MainLoop()
