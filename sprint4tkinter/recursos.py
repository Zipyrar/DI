import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox

def descargar_imagen(url: str, size=(100, 100)):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200.
        
        # Validar si la respuesta es de tipo imagen
        if 'image' in response.headers['Content-Type']:
            image = Image.open(BytesIO(response.content))
            # Redimensiona la imagen aquí
            image_resized = image.resize(size, Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(image_resized)
            return image_tk
        else:
            print(f"El contenido descargado no es una imagen. Tipo de contenido: {response.headers['Content-Type']}")
            return None
        
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error con la imagen", f"Error al descargar la imagen: {e}")
        return None
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un error inesperado: {e}")
        return None