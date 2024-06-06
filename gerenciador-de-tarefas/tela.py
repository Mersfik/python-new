from customtkinter import*

#creating a new window:
tela = CTk()
tela.geometry("700x400")
tela.title("Projeto")
tela.config(background="grey")
tela.iconbitmap("favicon.ico")

#creating a new botton with tkinter:
botao_1 = CTkButton(tela, width=200, height=30, text="Clique aqui!", bg_color="grey")
botao_1.pack(pady= 10)


tela.mainloop()