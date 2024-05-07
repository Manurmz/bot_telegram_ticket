def json_actualizado(array):
  data = {
    "servicio": None,
    "referencia": None,
    "monto": None,
    "comision": 15,
    "total": None,
    "folio": None,
    "hora": None
    }
  data["servicio"] = array[0]
  data["referencia"] = array[1]
  data["monto"] = array[2]
  data["total"] = int(data["monto"]) + data["comision"]
  data["folio"] =  array[3]
  data["hora"] = array[4]
  return data