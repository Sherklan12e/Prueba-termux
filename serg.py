
import pyfiglet




def palabra():
    escribir = input('Escriba su nombre: ')
    apellido = input('Escriba su apellido: ')
    edad = int(input('Escriba su : '))
    da = "  "
    
    formula = f"{escribir  + da +  apellido  + da+    str(edad)}"
    
    
    nombre = pyfiglet.figlet_format(formula, font = "banner3-D")
    print(nombre)
    
    
    
palabra()

