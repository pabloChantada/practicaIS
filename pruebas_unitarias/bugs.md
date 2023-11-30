# Bugs solucionados

- Cerrar el progama al cerrar la ventana
- Al cargar el mismo pkl varias veces se genera de nuevo los labels
- Cambiar la actualizacion de create para que no redimenasione las ventana
- Al cargar sin generar la descripcion se carga mal

# Bugs sin solucionar

- Corregir limites de muestra de puntos de la prediccion
- Tras dos generaciones la ventana se cierra automaticamente
- Si cargas un archivo y luego generas un grafico se sobreponen

# Preguntas

- Preguntar si el archivo pkl se carga en open file o load file

## Pasar de .py a .exe
py -3.11 -m PyInstaller --onefile --noconsole --icon=icono.ico lol.py -F -w 
