import qrcode
import tkinter as tk
from PIL import Image, ImageTk

# Función para actualizar el código QR
def actualizar_qr():
    # Obtener el texto del cuadro de entrada
    texto = entrada.get()
    print("Texto del código QR:", texto)

    # Crear una instancia del objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    print("Instancia del objeto QRCode creada.")

    # Agregar el texto al objeto QRCode
    qr.add_data(texto)
    print("Texto agregado al objeto QRCode.")

    # Generar la imagen del código QR
    qr.make(fit=True)
    print("Imagen del código QR generada.")

    # Obtener la imagen del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    print("Imagen del código QR obtenida.")

    # Convertir la imagen PIL a un objeto PhotoImage de Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_qr)
    print("Imagen convertida a formato Tkinter.")

    # Actualizar la imagen en el widget Label
    etiqueta.configure(image=imagen_tk)
    etiqueta.image = imagen_tk
    print("Imagen del código QR actualizada en el widget Label.")

# Crear la ventana Tkinter
ventana = tk.Tk()
ventana.title("Código QR")

# Crear el cuadro de entrada con un valor por defecto
texto_por_defecto = "¡Hola, mundo!"
entrada = tk.Entry(ventana)
entrada.insert(0, texto_por_defecto)
entrada.pack()

# Crear un botón para actualizar el código QR
boton = tk.Button(ventana, text="Actualizar QR", command=actualizar_qr)
boton.pack()

# Crear un widget Label para mostrar el código QR
etiqueta = tk.Label(ventana)
etiqueta.pack()

# Actualizar el código QR con el valor por defecto
actualizar_qr()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
