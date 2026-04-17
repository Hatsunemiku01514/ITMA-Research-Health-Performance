import qrcode

# Tu enlace oficial
enlace = "https://docs.google.com/forms/d/e/1FAIpQLScCxfz56l5rwfWM8jEWhmOsNjmrboHjkVyHgvg2B9thPwRy4A/viewform"

# Generar el QR
img = qrcode.make(enlace)
img.save("QR_Investigacion_ITMA.png")
print("¡QR generado con éxito, Wilhelm!")