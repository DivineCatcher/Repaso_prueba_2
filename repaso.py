import os
os.system("cls")
import time


DESCUENTO_NINO = 0.50 #Menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30 #60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19

bandera_acceso_numericos = False
bandera_acceso_dia = False

nombre = input("Ingrese su nombre: \n")

try: 
    edad = int(input("Ingrese su edad: \n"))
    cantidad_entradas = int(input("Ingrese la cantidad de entradas deseadas: \n"))
    precio_base = float(input("Ingrese el precio unitario de la entrada: \n"))
    dia = input("Ingrese dia deseado: \n").lower()
    
    if edad > 0 and cantidad_entradas > 0 and precio_base > 0:
        bandera_acceso_numericos = True
    
    if dia != "miercoles" and dia != "jueves":
        bandera_acceso_dia = True
        
    if bandera_acceso_numericos and bandera_acceso_dia: 
        subtotal = cantidad_entradas * precio_base
        
        if edad < 12 :
            valor_dscto_edad = subtotal * DESCUENTO_NINO
            tipo_cliente = "niño(a)"
        elif edad >= 60 :
            valor_dscto_edad = subtotal * DESCUENTO_ADULTO_MAYOR
            tipo_cliente = "adulto mayor"
        else:
            valor_dscto_edad = 0
            tipo_cliente = "adulto"
        
        valor_provisorio = subtotal - valor_dscto_edad
        
        if dia == "martes":
            valor_dscto_dia = valor_provisorio * DESCUENTO_MARTES
            valor_provisorio2 = valor_provisorio - valor_dscto_dia
            
        elif dia == "sabado" or dia == "domingo":
            valor_recargo_dia = valor_provisorio * RECARGO_FIN_SEMANA
            valor_provisorio2 = valor_recargo_dia + valor_provisorio
            
        else: 
            valor_provisorio2 = valor_provisorio
            
        valor_iva = valor_provisorio2 * IVA
        valor_final = valor_provisorio2 + valor_iva
        
        valor_final_redondeado = round(valor_final, 2)
        
        if valor_final_redondeado <= 10000:
            clasificacion = "Compra economica"
        
        elif valor_final_redondeado < 10000 and valor_final_redondeado >= 30000:
            clasificacion = "Compra normal"
            
        else:
            clasificacion = "Compra alta"
            
        print(f"Nombre: {nombre} ")
        time.sleep(0.3)
        print(f"Edad: {edad}")
        time.sleep(0.3)
        print(f"Tipo de cliente: {tipo_cliente}")
        time.sleep(0.3)
        print(f"Total a pagar: ${valor_final_redondeado}")
        time.sleep(0.3)
        print(f"Clasificación: {clasificacion}")
        
    
    
except:
    print("El valor ingresado es invalido.")