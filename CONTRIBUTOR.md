# COMMITS

Los commits deben estar comentados con los cambios realizados, con una __tag__
sobre la versión que se realiza el commits y deben comenzar por una de los siguientes
elementos:
- fix: errores leves o arreglos de documentación
- feat: añadir código o carácteristicas
- BREAKING CHANGE: si genera cambios incompatibles con versiones anteriores

# REGLAS DE DOCUMENTACION

- Clases -> UpperCamelCase
- Constantes -> CAPITALIZED_WITH_UNDERSCORES
- Funciones y Variables -> lowercase_separated_by_underscores
- Elementos privados -> _nombre

# LEGIBILIDAD

- Utilizar un espacio antes y después de los operadores binarios (como +, -, *, /)
- No superar los 80 caracteres, para ello usar "barra invertida":

mi_variable = 10 + 20 + 30 + \
              40 + 50 + 60 + \
              70 + 80 + 90

- Comentarios; se realizan con '''comentario''' o # comentario
  - Con '''_''' se escribe como:
    '''
    comentario
    '''
  - Con # se escribe con dos espacio despues del la linea o todos en la 
  misma columna (mirar archivos como ejemplo) y uno despues de #, la primera 
  letra va con mayuscula: varible  # Comentario