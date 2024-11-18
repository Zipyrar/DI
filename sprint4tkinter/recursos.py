import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox

def descargar_imagen(url: str, size=(100, 100)):
    try:
        #Realiza la solicitud GET para descargar la imagen desde la URL.
        response = requests.get(url)
        #Lanza una excepción si el código de estado no es 200 (OK).
        response.raise_for_status()
        
        #Validar si la respuesta es de tipo imagen.
        if 'image' in response.headers['Content-Type']:
            #Abre la imagen en memoria desde los datos binarios recibidos.
            image = Image.open(BytesIO(response.content))
            #Redimensiona la imagen a las dimensiones proporcionadas.
            image_resized = image.resize(size, Image.LANCZOS)
            #Convierte la imagen redimensionada a un formato compatible con Tkinter.
            image_tk = ImageTk.PhotoImage(image_resized)
            return image_tk  #Devuelve la imagen convertida para usarla en Tkinter.
        else:
            #Si el contenido descargado no es una imagen, muestra un mensaje de error.
            print(f"El contenido descargado no es una imagen. Tipo de contenido: {response.headers['Content-Type']}")
            return None  #Si no es una imagen, se retorna None
        
    except requests.exceptions.RequestException as e:
        #Captura errores relacionados con la solicitud HTTP y muestra un mensaje de error.
        messagebox.showerror("Error con la imagen", f"Error al descargar la imagen: {e}")
        return None  #Si ocurre un error en la descarga, se retorna None.
    except Exception as e:
        #Captura errores generales y muestra un mensaje de error.
        messagebox.showerror("Error inesperado", f"Ocurrió un error inesperado: {e}")
        return None  #Si ocurre un error inesperado, se retorna None.