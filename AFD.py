import sys

def cargar_automata():
   
    Q = ['q1', 'q2', 'q3']
    
    Sigma = ['0', '1']
    
    q0 = 'q1'
    
    
    F = ['q2']
    
    delta = {
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q2', '1': 'q2'}, 
        'q3': {'0': 'q3', '1': 'q3'} 
    }
    
    return Q, Sigma, delta, q0, F

def procesar_cadena(cadena, delta, q0, F):

    estado_actual = q0
    
    for caracter in cadena:
        if caracter not in ['0', '1']:
            continue 
            
        if estado_actual in delta and caracter in delta[estado_actual]:
            estado_actual = delta[estado_actual][caracter]
        else:
            return False 

    if estado_actual in F:
        return "ACEPTA"
    else:
        return "NO ACEPTA"

def main():
    if len(sys.argv) < 2:
        sys.argv.append('entrada.txt')

    nombre_archivo = sys.argv[1]
    
    Q, Sigma, delta, q0, F = cargar_automata()

    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                cadena = linea.strip()
                
                if cadena:
                    resultado = procesar_cadena(cadena, delta, q0, F)
                    print(resultado)
                    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")

if __name__ == "__main__":
    main()