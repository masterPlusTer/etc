// Código básico para Arduino R4 WiFi con uso exclusivo de char arrays

// Define mensajes constantes como arrays de caracteres
const char mensajeFlash1[] = "Este mensaje está en memoria Flash y se imprime desde RAM.\n";
const char mensajeFlash2[] = "Un número entero: ";
const char mensajeFlash3[] = "Un número decimal: ";
const char mensajeFlash4[] = "Este mensaje se repite en el loop.\n";

void setup() {
  // Inicializar la comunicación Serial
  Serial.begin(115200);
  while (!Serial); // Esperar a que el puerto serie esté disponible

  // Imprimir mensajes almacenados en arrays constantes
  Serial.print(mensajeFlash1);

  // Variables para mostrar ejemplos
  int valor = 42;
  float decimal = 3.14159;

  // Imprimir valores formateados utilizando char arrays
  Serial.print(mensajeFlash2);
  Serial.println(valor);

  Serial.print(mensajeFlash3);
  char bufferDecimal[10]; // Buffer para almacenar el número formateado
  dtostrf(decimal, 5, 2, bufferDecimal); // Convertir float a char[]
  Serial.println(bufferDecimal);         // Imprimir el número formateado
}

void loop() {
  // Mensaje repetitivo almacenado como char array
  Serial.print(mensajeFlash4);
  delay(1000); // Esperar un segundo entre mensajes
}
