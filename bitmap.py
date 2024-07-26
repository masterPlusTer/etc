import numpy as np
import matplotlib.pyplot as plt
import random

def hex_to_bin_array(hex_array):
    """Convert an array of hex values to a 2D binary array."""
    bin_array = []
    for hex_value in hex_array:
        # Convert hex to binary string, remove '0b' prefix, and pad with zeros to ensure 8 bits
        bin_str = bin(int(hex_value, 16))[2:].zfill(8)
        # Convert binary string to list of integers
        bin_list = [int(bit) for bit in bin_str]
        bin_array.append(bin_list)
    return np.array(bin_array)

def plot_bitmap(bin_array):
    """Plot the binary array as a bitmap."""
    plt.imshow(1 - bin_array, cmap='gray', interpolation='nearest')
    plt.axis('off')  # Hide the axes
    plt.show()


numero_aleatorio =  random.randint(0, 2 ** 64 - 1)
hexadecimal_aleatorio = hex(numero_aleatorio)[2:].zfill(16)


binary_number = bin(int(hexadecimal_aleatorio, 16))[2:].zfill(64)
print('valor binario')
print()
print(binary_number)


print()

print(binary_number[0:8])
print(binary_number[8:16])
print(binary_number[16:24])
print(binary_number[24:32])
print(binary_number[32:40])
print(binary_number[40:48])
print(binary_number[48:56])
print(binary_number[56:64])
print()

def distribuir(a,b):
    return(str(hexadecimal_aleatorio[a:b]))

print('valor hexadecimal')
print()
print(hexadecimal_aleatorio);
print()
print(distribuir(0,2));
print(distribuir(2,4));
print(distribuir(4,6));
print(distribuir(6,8));
print(distribuir(8,10));
print(distribuir(10,12));
print(distribuir(12,14));
print(distribuir(14,16));




# Example hex array (each hex value represents 8 bits)
hex_array = [
 distribuir(0,2), distribuir(2,4), distribuir(4,6), distribuir(6,8), distribuir(8,10), distribuir(10,12), distribuir(12,14), distribuir(14,16)
]

# Convert hex array to binary array
bin_array = hex_to_bin_array(hex_array)

# Plot the bitmap
plot_bitmap(bin_array)

print(bin_array)
