import operator



dict = {} #creamos diccionario vacio

#contar las veces que esta cada letra y meterlas al diccionario
texto= "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
texto.upper
print(texto)

for l in texto:
    if l in dict:
        dict[l] = dict[l] + 1
    else:
        dict[l] = 1

print("Elementos:")
print(dict)

print("Elementos ordenados:")
dictOrdenado=sorted(dict.items(), reverse=True)
print(dictOrdenado)

#sustituir las 2 letras mas frecuentes (e, a) 
descifrado=""
for l in texto:
    if l=='X':
        descifrado= descifrado + 'e'
    elif l=='E':
        descifrado=descifrado + 'a'
    elif l=='T':
        descifrado=descifrado + 'l'
    elif l=='A':
        descifrado=descifrado + 'd'
    elif l=='N':
        descifrado=descifrado + 's'
    elif l=='I':
        descifrado=descifrado + 'o'
    elif l=='J':
        descifrado=descifrado + 'n'
    elif l=='R':
        descifrado=descifrado + 'c'
    elif l=='Z':
        descifrado=descifrado + 'u' 
    elif l=='K':
        descifrado=descifrado + 'r' 
    elif l=='D':
        descifrado=descifrado + 'p'
    elif l=='C':
        descifrado=descifrado + 'i' 
    elif l=='P':
        descifrado=descifrado + 'm' 
    elif l=='U':
        descifrado=descifrado + 'g'
    elif l=='H':
        descifrado=descifrado + 't'
    elif l=='S':
        descifrado=descifrado + 'q'
    elif l=='O':
        descifrado=descifrado + 'f'
    elif l=='Z':
        descifrado=descifrado + 'u'
    elif l=='Q':
        descifrado=descifrado + 'b'
    elif l=='G':
        descifrado=descifrado + 'j'
    elif l=='V':
        descifrado=descifrado + 'y'
    elif l=='M':
        descifrado=descifrado + 'h'
    else:
        descifrado=descifrado + l
print()
print(descifrado)

#recogemos las palabras de 2 y 3 letras para ver cuales pueden ser las terminaciones y el principio

palabra=""
lista=[]
for l in descifrado:
    if l==' ':
        if len(palabra)<4:
            lista.append(palabra)
        palabra=""
    else:
        palabra= palabra + l

print()
print(lista)

#nos damos cuenta de que la T podria ser una L
#tambien que la A puede ser una D
#hacemos el cambio en el for de arriba

#ahora parece que la N puede ser la S (palabra 'esa')

#vamos a sustituir la K que es bastante fercuente por la O, a ver si puede ser
#se han quedado dos 'o' juntas lo que me hace pensar que igual no es.
#probremos cambiando la I por la O

#en las letras de 2 parece que puede ser un 'no' gracias a esa nueva o
#con los cual cambiamos la J por una N

#ahora deducimos qeu la R es una C, y que la Z es una U

#poco a poco vamos deduciendo las demas palabras y al final obtenemos el texto

#con durruti moria el dirigente que, a su manera, mejor eFpresaba como combatir al fascismo desde un criterio de independencia de clase, a diferencia del colaboracionismo frentepopulista de la direccion anarquista. durruti fue un factor de primer orden en el papel de la clase obrera en catalunya en julio de 1936. pero durruti, como ocurre con las personalidades en la historia, no cayo del cielo. personificaba la tradicion revolucionaria de la clase obrera. su enorme popularidad entre la clase trabajadora, reflejada en el entierro multitudinario en barcelona el 22 de noviembre de 1936, muestra esa identificacion. su muerte fue sin duda un golpe objetivo al proceso revolucionario en marcha. sin durruti quedo mas libre el camino para que el estalinismo, con la complicidad del gobierno del frente popular y de la direccion anarquista, terminara en mayo de 1937 la tarea de liquidar la revolucion, desmoraliLando a la clase obrera y facilitando con ello el posterior triunfo franquista.