import reversiGUI	
import functions

tablero = []
fichasNegras = []
fichasBlancas= []



functions.creaTab(tablero,8)

#posiciones iniciales#############

functions.insertar(tablero,1,4,5)
functions.insertar(tablero,2,4,4)
functions.insertar(tablero,1,5,4)
functions.insertar(tablero,2,5,5)
##################################
#functionsinsertar(tablero,c,x,y)
functions.insertar(tablero,1,6,3)
functions.insertar(tablero,2,5,3)





a = functions.comprobarMov(tablero,1)
reversiGUI.prinTab(tablero,1)



print(tablero)
print("movimientos:",a)
