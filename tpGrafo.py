import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def crearGrafoConExcel(path):
    global grafo
    global isGrafoCreado
    df = pd.read_excel(path)
    listaAux = df["Usuarios"].tolist()
    vertices = [x for x in listaAux if not pd.isna(x)]
    listaAux = df["Relaciones"].tolist()
    aristas = []
    for x in listaAux:
        if not pd.isna(x):
          aux = x.split(", ")
          aristas.append((aux[0], aux[1], int(aux[2])))
    grafo = nx.Graph()
    grafo.add_nodes_from(vertices)
    grafo.add_weighted_edges_from(aristas)
    isGrafoCreado = True
    return grafo

def mostrarGrafo(grafo):
    nx.draw(grafo, pos=nx.circular_layout(grafo), node_color='r', edge_color='b', with_labels=True)
    plt.show()

def distanciaMinimaAmistad(grafo, persona1, persona2):
    nx.dijkstra_path(grafo, persona1, persona2)
    return nx.dijkstra_path_length(grafo, persona1, persona2)

def bt1Call():
    path = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos de Excel", "*.xlsx *.xls")])
    if path:
        crearGrafoConExcel(path)
        messagebox.showinfo("Éxito", "Grafo creado exitosamente.")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")
    

def bt2Call(): 
    global grafo
    global isGrafoCreado
    if isGrafoCreado:
        mostrarGrafo(grafo)
    else:
        messagebox.showwarning("Advertencia", "No se ha creado ningun grafo.")

def bt3Call():
    global grafo
    global isGrafoCreado
    def sbCall(): 
        distancia = distanciaMinimaAmistad(grafo, input1.get(), input2.get())
        messagebox.showinfo("Encontrado", "La distancia minima entre "+ str(input1.get()) + " y " + str(input2.get()) + " es de: " + str(distancia))
    if isGrafoCreado:
        new_window = ctk.CTkToplevel()
        new_window.title("Distancia minima de amistad")
        new_window.geometry("350x250")
        frame = ctk.CTkFrame(master=new_window)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        input1 = ctk.CTkEntry(master=frame, placeholder_text="Usuario 1")
        input1.pack(pady=5)
        input2 = ctk.CTkEntry(master=frame, placeholder_text="Usuario 2")
        input2.pack(pady=5)
        subButton = ctk.CTkButton(master=frame, text="Buscar distancia minima de amistad", command=sbCall)
        subButton.pack(pady=10)
    else:
        messagebox.showwarning("Advertencia", "No se ha creado ningun grafo.")
    
def app():
    root = ctk.CTk()
    root.title("Mi Interfaz Gráfica con CustomTkinter")
    root.geometry("720x720")
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    titulo1 = ctk.CTkLabel(master=frame, text="TP 2-POO II", font=(ctk.CTkFont(family='Helvetica'), 50))
    titulo1.pack(pady=15, padx=10)
    subTitulo = ctk.CTkLabel(master=frame, text="FRASCINO JUAN PABLO, FRANCISCO ROY, FEDERICO LUNA Y GONZALO GARCIA")
    subTitulo.pack(pady=15, padx=10)
    titulo2 = ctk.CTkLabel(master=frame, text="Elija alguna de las siguientes opciones: ", font=(ctk.CTkFont(family='Helvetica'), 15))
    titulo2.pack(pady=15, padx=10)
    button1 = ctk.CTkButton(master=frame, text="Crear Grafo a partir de un Archivo Excel(.xlsx)", command=bt1Call, width=400, height=100)
    button1.pack(pady=15, padx=10)
    button2 = ctk.CTkButton(master=frame, text="Mostrar Grafo en pantalla", command=bt2Call, width=400, height=100)
    button2.pack(pady=15, padx=10)
    button3 = ctk.CTkButton(master=frame, text="Buscar distancia minima de amistad entre dos usuarios", command=bt3Call, width=400, height=100)
    button3.pack(pady=15, padx=10)
    root.mainloop()

def main():
    global isGrafoCreado
    isGrafoCreado = False
    app()

main()