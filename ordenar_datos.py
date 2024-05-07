def ordenar(array):
    array_corregido = []
    
    # Obtener el nombre del servicio
    servicio = ' '.join(array[4:6]) if not array[5].isdigit() else array[4]
    array_corregido.append(servicio)
    
    # Encontrar el índice del elemento que contiene la palabra "Folio"
    indice_folio = array.index("Folio")
    
    # Obtener la referencia
    if array[indice_folio-2].isdigit():
        referencia = array[indice_folio-2] + array[indice_folio-1]
    else:
        referencia = array[indice_folio-1]
    array_corregido.append(referencia)
    
    # Obtener el monto
    indice_dollar = array.index('$')
    monto = array[indice_dollar+1]
    array_corregido.append(monto)
    
    # Obtener el folio
    if array[indice_folio+1] == ':':
        folio = array[indice_folio+2]
        array_corregido.append(folio)
    
    # Obtener la fecha y hora
    fecha = array[0]
    hora_sin_corregir = array[1].split(':')[:2]
    hora = fecha + ' ' + ':'.join(hora_sin_corregir)
    array_corregido.append(hora)
    
    return(array_corregido)

# ordenar(array1)
# ordenar(array2)
# ordenar(array3)
