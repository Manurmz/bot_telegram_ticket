from fpdf import FPDF


def crear_pdf(info):
    nombre = "ticket.pdf"
    fuente = "Times"
    # Crear el PDF
    pdf = FPDF(orientation='P', unit='mm', format=(56, 100))  # Tamaño personalizado
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_margins(3, 4, 3)
    pdf.add_page()

    pdf.set_font(fuente, size=13, style="B")
    pdf.cell(0, 4, "Miscelanea Emmanuel", ln=True, align='C')
    pdf.ln(4)
    pdf.set_font(fuente, size=9)
    pdf.cell(0, 4, "CARGO EXITOSO", ln=True, align='C')
    pdf.cell(0, 4, f"{info['servicio']}", ln=True, align='C')
    pdf.multi_cell(0, 4, f'Referencia: {info["referencia"]}', align='L')
    pdf.ln(4)
    pdf.cell(0, 4, f"Monto: ${info['monto']}", ln=True, align='C')
    pdf.ln(1)
    pdf.cell(0, 4, f"Comisión: ${info['comision']}", ln=True, align='C')
    pdf.ln(1)
    pdf.cell(0, 4, "Total: ", ln=False, align='C')
    pdf.set_font(fuente, size=10, style="B")
    pdf.set_x(33)
    pdf.cell(0, 4, f"${info['total']}", ln=True, align='L')
    pdf.ln(1)
    pdf.set_font(fuente, size=9)
    pdf.cell(0, 4, f"Autorización {info['servicio']}:", ln=True, align='C')
    pdf.cell(0, 4, f"{info['folio']}", ln=True, align='C')
    pdf.ln(1)
    pdf.cell(0, 4, info['hora'], ln=True, align='C')
    pdf.ln(4)
    pdf.multi_cell(0, 4, "El periodo para la aplicacion de pago es de 24 a 36 horas.")
    pdf.ln(1)
    pdf.multi_cell(0, 4, "Conserve este comprobante para futuras aclaraciones.", align="C")
    pdf.ln(1)
    pdf.multi_cell(0, 4, "ESTE NO ES UN COMPROBANTE FISCAL", align="C")
    pdf.ln(4)

    pdf.output(nombre)
    return nombre


# data = {
#     "servicio": "CFE",
#     "referencia": "2934492229344922293449222934492",
#     "monto": 1564,
#     "comision": 15,
#     "total": 1579,
#     "folio": "440653",
#     "hora": "2024-10-20 13:20:04"
# }
# dir = crear_pdf(data)
# print(dir)