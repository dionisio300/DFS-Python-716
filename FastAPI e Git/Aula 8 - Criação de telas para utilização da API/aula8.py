import tkinter as tk

# Verificar a versão do Tkinter
root = tk.Tk()
print(root.tk.call('info', 'patchlevel'))
root.mainloop()  # Para manter a janela aberta
