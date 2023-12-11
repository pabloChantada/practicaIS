# Bugs solucionados

- Cerrar el progama al cerrar la ventana
- Al cargar el mismo pkl varias veces se genera de nuevo los labels
- Cambiar la actualizacion de create para que no redimenasione las ventana
- Al cargar sin generar la descripcion se carga mal
- Corregir limites de muestra de puntos de la prediccion
- Si cargas un archivo y luego generas un grafico se sobreponen
- Tras dos generaciones la ventana se cierra automaticamente

# Bugs sin solucionar

# Preguntas

## Pasar de .py a .exe

py -3.11 -m PyInstaller --onefile --noconsole --icon=icono.ico lol.py -F -w 
