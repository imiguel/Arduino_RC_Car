# -*- coding: utf-8 -*-
import wx
import methods

class MainWindow(wx.Frame):
    def __init__( self, parent, size ):
        wx.Frame.__init__ ( self, parent, size = wx.Size(700,500) )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.menuBar = wx.MenuBar( 0 )
        self.fileMenu = wx.Menu()
        self.btnMenu_Sair = wx.MenuItem( self.fileMenu, wx.ID_ANY, "&Sair", wx.EmptyString, wx.ITEM_NORMAL )
        self.fileMenu.AppendItem( self.btnMenu_Sair )

        self.menuBar.Append( self.fileMenu, "&Ficheiro" )

        self.sobreMenu = wx.Menu()
        self.btnMenu_Sobre = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "S&obre", wx.EmptyString, wx.ITEM_NORMAL )
        self.sobreMenu.AppendItem( self.btnMenu_Sobre )

        self.btnMenu_Ajuda = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "F&AQ (Online)", wx.EmptyString, wx.ITEM_NORMAL )
        self.sobreMenu.AppendItem( self.btnMenu_Ajuda )

        self.menuBar.Append( self.sobreMenu, "&Sobre" )

        self.SetMenuBar( self.menuBar )


        self.Centre( wx.BOTH )
        ############################



        #adiciona metodos aos botões
       #self.Bind(wx.EVT_MENU, self.btnSair_onClick, btnSair)
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