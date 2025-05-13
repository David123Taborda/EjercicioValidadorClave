from validadorclave.modelo.validador import ReglaValidacionGanimedes, ReglaValidacionCalisto, Validador
from validadorclave.errores import ValidadorError

def validar_clave(clave, reglas):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la validación {type(regla).__name__}")
        except ValidadorError as e:
            print(f"Error: {type(regla).__name__}: {str(e)}")

if __name__ == "__main__":
    clave = input("Ingrese una clave: ")
    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    validar_clave(clave, reglas)