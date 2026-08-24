def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'

    tablero = []

    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))

    f = open(nombre_fichero, 'w', encoding='utf-8')

    for i in tablero:
        f.write('\t'.join(i) + '\n')
        

    f.close()

    for i in tablero:
        print('\t'.join(i))

    movimiento = 0

    while True:
        continuar = input('Deseas hacer otro movimiento? (s/n): ')
        if continuar != 's':
            break
        else:
            fila_origen = int(input('Introduce la fila de la pieza a mover: '))
            columna_origen = int(input('Introducela columna de la ficha que desea mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destina: '))

            tablero[fila_destino-1][columna_destino-1] = tablero[fila_origen-1][columna_origen-1]
            tablero[fila_origen-1][columna_origen-1] = ''

            movimiento += 1

            f = open(nombre_fichero, 'a', encoding='utf-8')
            f.write('Movimiento' + str (movimiento) + '\n')

            for i in tablero:
                f.write('\t'.join(i) + '\n')

            f.close()

            for i in tablero:
                print('\t'.join(i))
    return

        
partida_ajedrez('partida1.txt')   

