#primero vamos a importar las librerias basicas
import cv2 
import pytesseract


#leemos la imagen
img= cv2.imread('foto.png')

#la cosa es que pytesseract funciona con imganes rgb
# y cv2 con BGR ... entonces ahora lo vamos a transformar 
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#podemos utilizar la funcion imga_to_string para extraer todo el texto
print(pytesseract.image_to_string(img))

#pero como podemos saber la ubicacion exacta de los caracteres que estamos buscando?

#podemos utilizar la funcion image_to_boxes
#esto nos va a devolver el punto X, el Y, el width( el ancho) y el height (el alto)
print(pytesseract.image_to_boxes(img))
#una vez que ya tenemos la ubicacion es mas facil

#vamos a detectar los caracteres
#almacenamos las 3 variables que nos devuelve shape, la 3ra no nos interesa asi que la dejamos vacia
'''hImg,wImg,_ = img.shape
boxes=pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    #antes nos daba un resultado parecido a (i 618 157 640 188 0)
    #lo que vamos a buscar es dividirlo en una lista a ese string
    b=b.split(' ')
    #ya tenemos la letra, el x , el y , el ancho y el alto divididos
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    #por que lo quiero separar? ahora es facil crear un rectangulo en cada caracter
    #es facil saber que dibuja, primero tomamos el punto (x,y)en nuestro plano cartesiano
    #luego sumamos la altura, y el ancho para que trace estos rectangulos
    #pero ojo que y viene opuesto entonces vamos a restarle al alto total de la imagen nuestra y para que quede bien
    
    # manera incorrecta -> cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    #el uno del final es el grueso de las lineas, el (0,0,255 el color)
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)

    #vamos a ponerle un label al lado de cada box
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),1)
'''
#Pero imaginemos que no queremos una letra, sino palabras enteras
#veamos
hImg,wImg= img.shape
boxes=pytesseract.image_to_data(img)
print(boxes)
#ya ahora tenemos varios features, uno de ellos son las palabras
#vamos algo mejor, vamos a contar el numero que se repite una palabra
for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b=b.split()
        print(b)
        #vemos que algun tienen 11 columnas (las que no tiene palabras) y otras 12(las que tiene palabras)
        #las separamos
        if len(b)==12:
            print(b)
            #fijarese que solo la columna 6,7,8 y 9 nos dan las coordenadas
            x,y,w,h= int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            #vamos a escribir las palabras sobre la imagen, b[11] es la palabra
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),1)


cv2.imshow('resultados',img)
cv2.waitKey(33)