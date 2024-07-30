import qrcode
import qrcode.constants
from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, Label, Entry, Button
from itertools import cycle

# Crear la ventana de Tkinter
root = Tk()
root.title("Código QR Personalizado")

# Crear el label donde se mostrará el código QR
label = Label(root)
label.pack()

# Crear el campo de entrada de texto
entry = Entry(root, width=50)
entry.pack()

def generate_color_palette():
    # Genera una paleta de colores aleatorios más oscuros
    colors = [(128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0), (128, 0, 128), (0, 128, 128)]
    return colors

def flood_fill(matrix, x, y, color, colored_matrix):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < len(matrix[0]) and 0 <= cy < len(matrix) and matrix[cy][cx] and colored_matrix[cy][cx] is None:
            colored_matrix[cy][cx] = color
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

def assign_colors(matrix):
    colors = generate_color_palette()
    color_cycle = cycle(colors)

    # Crear una nueva matriz para almacenar los colores
    colored_matrix = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Asignar colores a los conjuntos de cuadraditos conectados
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] and colored_matrix[y][x] is None:
                color = next(color_cycle)
                flood_fill(matrix, x, y, color, colored_matrix)

    return colored_matrix

def generate_qr_code():
    # Obtener el texto del campo de entrada
    data = entry.get()
    if not data:
        return

    # Crear el objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    # Agregar datos al código QR
    qr.add_data(data)
    qr.make(fit=True)

    # Obtener la matriz de datos del código QR
    matrix = qr.get_matrix()

    # Asignar colores a la matriz del código QR
    colored_matrix = assign_colors(matrix)

    # Calcular el tamaño de la imagen
    img_size = len(colored_matrix) * qr.box_size

    # Crear una imagen en blanco con el tamaño del código QR
    img = Image.new('RGB', (img_size, img_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Dibujar las celdas del código QR con los colores asignados
    for y in range(len(colored_matrix)):
        for x in range(len(colored_matrix[0])):
            if colored_matrix[y][x]:
                draw.rectangle((x * qr.box_size, y * qr.box_size, (x + 1) * qr.box_size, (y + 1) * qr.box_size),
                               fill=tuple(colored_matrix[y][x]))

    # Convertir la imagen PIL a un objeto PhotoImage de Tkinter
    photo_image = ImageTk.PhotoImage(img)
    label.configure(image=photo_image)
    label.image = photo_image

# Crear el botón para generar el código QR
button = Button(root, text="Generar Código QR", command=generate_qr_code)
button.pack()

# Iniciar el bucle principal de Tkinter
root.mainloop()
