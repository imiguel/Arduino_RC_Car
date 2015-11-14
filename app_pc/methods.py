# -*- coding: utf-8 -*-
import webbrowser
import wx




#Mostra a janela quando se clica no "Sobre"
def aboutDialogMessage(self):
    dialog = wx.MessageDialog(self, "Programa para controlar RC Car\n \n"
                                    "Desenvolvido por: Miguel Rosa\n \n \n \n"
                                    "Todos os direitos reservados\n \n"
                                    "Mértola 2016",
                                    "RC Car Controller - Sobre", wx.OK)
    dialog.ShowModal()#Mostra a caixa de dialogo
    dialog.Destroy() #destroi a caixa de dialogo



#Abre a pagina do projecto no github
def openWebPageFromGitHub():
    #linkToPage = "https://github.com/imiguel/Arduino_RC_Car/wiki"
    linkToPage = "https://imiguel.github.io/Arduino_RC_Car"

    webbrowser.open_new(linkToPage)