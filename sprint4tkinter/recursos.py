import requests 
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox

def descargar_imagen(url:str, size:tuple):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            #Verificar si el contenido es una imagen antes de abrirla.
            image = Image.open(BytesIO(response.content))
            image_resized = image.resize(size, Image.LANCZOS) #Redimensionar la imagen si es necesario.
            image_tk = ImageTk.PhotoImage(image_resized)
            return image_tk
        else:
            print(f"Error al descargar la imagen, código de respuesta: {response.status_code}")
            return None
    except requests.exceptions.RequestException as image:
        messagebox.showerror("Error con las imágenes", f"Error al descargar la imagen {image}")
        return None