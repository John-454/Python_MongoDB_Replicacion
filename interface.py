import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Conexion base de datos
client = MongoClient('localhost', 27017)
db = client.clientes
collection = db.usuarios

def agregar_cliente():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()

    client = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    collection.insert_one(client)

    messagebox.showinfo("Cliente Agregado","Cliente Agregado Exitosamente")

root = tk.Tk()
root.title("Gestion de clientes")

tk.Label(root,text="ID: ").grid(row=0, column=0)
tk.Label(root,text="Nombre: ").grid(row=1, column=0)
tk.Label(root,text="Apellido: ").grid(row=2, column=0)
tk.Label(root,text="Telefono: ").grid(row=3, column=0)

entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

entry_apellido = tk.Entry(root)
entry_apellido.grid(row=2, column=1)

entry_telefono = tk.Entry(root)
entry_telefono.grid(row=3, column=1)

tk.Button(root,text="Agregar Cliente", command=agregar_cliente).grid(row=4,column=0,columnspan=2,pady=10)

root.mainloop()