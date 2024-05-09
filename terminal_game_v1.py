## JUEGO CRUZANDO EL SEMAFORO // JUEGO RNG
## V1. NETMASK
## camacho.omar.c@gmail.com

## IMPORTAR LIBRERIAS
import random

## VARIABLES DE JUEGO
puntos_persona = 0
niveles = 1
sm = 0

## BUCLE DE SEMAFORO
while True:
    nro_persona = int(input('INTRODUZCA UN NRO DEL 0 - 9: ')) ## PEDIR NRO. A USUARIO
    nro_pc = random.randint(0, 9) ## RANDOMIZAR NRO. PARA MAQUINA
    
    ## CONDICION PARA CRUZAR SEMAFORO
    if nro_pc != nro_persona:
        print('*****************************')
        print('NIVEL = ', niveles)
        print('*****************************') 
        
        sm += 1
        puntos_persona += random.randint(50, 150)
        
        print('NRO. JUGADOR = ', nro_persona)
        print('NRO. MAQUINA = ', nro_pc)
        print()
        print('*****************************')
        print('HAS CRUZADO EL SEMAFORO = ', sm)
        print('*****************************') 
    
    ## CONDICIONAL PARA PASAR DE NIVEL Y RESETEO DE SEMAFORO.
    if sm == 4:
        niveles += 1
        sm = 0
        puntos_persona += 200
        print('+++++++++++++++++++++++++++++++')
        print('HAS PASADO AL NIVEL', niveles)
        print('PUNTOS ACUMULADOS', puntos_persona)
        print('+++++++++++++++++++++++++++++++')
        print()
    
    ## CONDICIONAL PARA GANAR EL JUEGO.
    if niveles == 5:
        print()
        print('*****************************')
        print('*****************************')
        print('*****HAS GANADO EL JUEGO*****')
        print('*****************************')
        print('*****************************')
        print('****PUNTAJE TOTAL :',puntos_persona,'*****')
        print('*****************************')
        break
    
    ## CONDICIONAL SI MAQUINA ELIGE MISMO NRO. QUE USUARIO.
    if nro_pc == nro_persona:
        print('NRO. JUGADOR = ', nro_persona)
        print('NRO. MAQUINA = ', nro_pc)
        print('TE HAS MUERTO EN EL SEMAFORO', sm, 'DEL NIVEL ', niveles, 'SACASTE NRO ', nro_persona, 'y LA MAQUINA SACO NRO ', nro_pc)