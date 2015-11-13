# -*- coding: utf-8 -*-
import wx
import methods













































############################## GARBAGE ##############################################


'''class MainWindow(wx.Frame):
    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, title="RC Car Controller", size = wx.Size(700,500) )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        menuBar = wx.MenuBar( 0 )
        fileMenu = wx.Menu()
        btnMenu_Sair = wx.MenuItem( self.fileMenu, wx.ID_ANY, "&Sair", wx.EmptyString, wx.ITEM_NORMAL )
        fileMenu.AppendItem( self.btnMenu_Sair )

        menuBar.Append( self.fileMenu, "&Ficheiro" )

        sobreMenu = wx.Menu()
        btnMenu_Sobre = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "S&obre", wx.EmptyString, wx.ITEM_NORMAL )
        sobreMenu.AppendItem( self.btnMenu_Sobre )

        btnMenu_Ajuda = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "F&AQ (Online)", wx.EmptyString, wx.ITEM_NORMAL )
        sobreMenu.AppendItem( self.btnMenu_Ajuda )

        menuBar.Append( self.sobreMenu, "&Sobre" )



        self.SetMenuBar( self.menuBar )
        self.Centre( wx.BOTH )
        ############################



        #adiciona metodos aos botões
        self.Bind(wx.EVT_MENU, self.btnSair_onClick, btnMenu_Sair)
        #self.Bind(wx.EVT_MENU, self.btnSobre_onClick, btnSobre)


        self.Show(True)




    #------------- EVENTOS DE CLICKS NOS BOTOES, ETC ------------------------
    #Termina a aplicação
    def btnSair_onClick(self, event):
        self.Close()

    def btnSobre_onClick(self, event):
        dialog = wx.MessageDialog( self, "Programa para controlar o RC Car\n \nDesenvolvido por: Miguel Rosa");
        dialog.ShowModal() #mostra a caixa dialogo
        dialog.Destroy() #apos terminar, destroi



#Mostra no ecra
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "RC Car Controller")
    app.MainLoop()
'''