import tkinter as tk
from db import ejecutar_consulta

def cargar_login(ventana):
    panel = tk.Frame(ventana, padx=0, pady=0)
    panel.pack()

    entrada = tk.Entry(panel, width=40)
    entrada.pack(pady=5)

    def consultar():
        filtro = entrada.get()
        consulta_sql = f"SELECT * FROM canciones WHERE nombre LIKE '%{filtro}%'"
        resultados = ejecutar_consulta(consulta_sql)

        texto_resultado.delete("1.0", tk.END)
        for fila in resultados:
            texto_resultado.insert(tk.END, str(fila) + "\n")

    boton = tk.Button(panel, text="Consultar", command=consultar)
    boton.pack(pady=5)

    global texto_resultado
    texto_resultado = tk.Text(panel, height=15, width=60)
    texto_resultado.pack()

ventana = tk.Tk()
ventana.title("Filtro de Canciones - Korn")
ventana.geometry("600x400")

cargar_login(ventana)
ventana.mainloop()
