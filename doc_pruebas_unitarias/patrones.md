# PATRONES DE DISEÑO 

Librerias que usamos: Pandas, Pandastable, Tkinter, Dataclasses, Matplotlib, Sklearn.linear_model.

# PANDAS: 
- Singleton, patron creacional. Este patrón se utiliza para garantizar que ciertos objetos tengan una única instancia. Ejemplo:
pd.set_option() que sirve para configurar opciones específicas de Pandas, como el número máximo de filas o columnas a mostrar en una visualización.

- Facade, patron estructural. Pandas proporciona una interfaz simple y consistente para realizar operaciones complejas relacionadas al analisis
de datos, esta interfaz actúa como una fachada alrededor de estas complejidades, permitiendonos realizar operaciones avanzadas
de una manera más simple y fácil de entender.

# Tkinter:
- Composite, patron estructural que permite tratar tanto a los objetos individuales como a las composiciones de objetos
de manera uniforme. Tkinter permite la creación de interfaces gráficas complejas mediante la composición de widgets en estructuras 
más grandes.  

# Dataclasses:
- Decorador, patron estructural que al aplicarlo a una clase, se añade automáticamente funcionalidad como métodos __init__. 
