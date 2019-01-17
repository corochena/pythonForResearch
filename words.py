desde colecciones importación Contador
importación os
importar pandas como pd
importar matplotlib.pyplot como plt

def  read_book ( title_path ):
    con  open (title_path, " r " , encoding = " utf8 " ) como current_file:
        text = current_file.read ()
        text = text.replace ( " \ n " , " " ) .replace ( " \ r " , " " )
    volver texto

def  count_words ( texto ):
    texto = texto.lower ()
    skips = [ " . " , " , " , " ; " , " : " , " ' " , ' " ' ]
    para ch en saltos:
        text = text.replace (ch, " " )
        
    word_counts = {}
    para la palabra en text.split ( "  " ):
        si word en word_counts:
            word_counts [word] + =  1
        otra cosa :
            word_counts [word] =  1
    devolver word_counts
    
def  count_words_fast ( texto ):
    texto = texto.lower ()
    skips = [ " . " , " , " , " ; " , " : " , " ' " , ' " ' ]
    para ch en saltos:
        text = text.replace (ch, " " )
        
    word_counts = Contador (text.split ( " " ))
    devolver word_counts

def  word_stats ( word_counts ):
    num_unique =  len (word_counts)
    cuenta = word_counts.values ​​()
    retorno (num_unique, cuentas)

# permite comparar la salida de las dos funciones
text =  " Este es mi texto de prueba. Mantenemos este texto corto para que las cosas sean manejables " .
count_words (texto) == count_words_fast (texto) # debe devolver True

# encontremos un extracto de Romeo y Julieta
text = read_book ( " .Books / English / shakespeare / Romeo and Juliet.txt " )
len (texto)
ind = text.find ( " Qué hay en un nombre " )
sample_text = text [ind: ind + 1000 ]

# vamos a hacer algunas estadísticas
word_counts = count_words (texto)
(num_unique, cuenta) = word_stats (word_counts)
suma (cuentas)

# comparemos las versiones inglesas y alemanas de Romeo y Julieth
text = read_book ( " .Books / English / shakespeare / Romeo and Juliet.txt " )
word_counts = count_words (texto)
(num_unique, cuenta) = word_stats (word_counts)
imprimir (num_unique, suma (cuentas))

text = read_book ( " .Books / German / shakespeare / Romeo und Julia.txt " )
word_counts = count_words (texto)
(num_unique, cuenta) = word_stats (word_counts)
imprimir (num_unique, suma (cuentas))

# leyendo múltiples archivos y almacenando información en un marco de datos de pandas
stats = pd.DataFrame ( columns  = ( " idioma " , " autor " , " título " , " longitud " , " único " ))
title_num =  1

book_dir =  " ./Books "
para lang en os.listdir (book_dir):
    para el autor en os.listdir (book_dir +  " / "  + lang):
        para el título en os.listdir (book_dir +  " / "  + lang +  " / "  + autor):
            archivo_entrada = book_dir +  " / "  + lang +  " / "  + autor +  " / "  + título
            imprimir (archivo de entrada)
            text = read_book (input_file)
            (num_unique, cuenta) = word_stats (count_words_fast (texto))
            stats.loc [title_num] = lang, author.capitalize (), title.replace ( " .txt " , " " ), suma (cuentas), num_unique
            title_num + =  1

# muestra toda la mesa, cabeza o cola
estadísticas
stats.head ()
stats.tail ()

# permite trazar palabras únicas vs longitud total
plt.plot (stats.length, stats.unique, " bo " )
# ahora usando un loglog
plt.loglog (stats.length, stats.unique, " bo " )

# permite estratificar por idioma
plt.figure ( figsize  = ( 10 , 10 ))
subset = stats [stats.language ==  " English " ]
plt.loglog (subset.length, subset.unique, " o " , label = " English " , color = " carmesí " )
subconjunto = estadísticas [stats.language ==  " French " ]
plt.loglog (subset.length, subset.unique, " o " , label = " French " , color = " forestgreen " )
subset = stats [stats.language ==  " German " ]
plt.loglog (subset.length, subset.unique, " o " , label = " German " , color = " orange " )
subset = stats [stats.language ==  " Portuguese " ]
plt.loglog (subset.length, subset.unique, " o " , label = " Portuguese " , color = " blueviolet " )
leyenda ()
plt.xlabel ( " Longitud del libro " )
plt.ylabel ( " Número de palabras únicas " )
plt.savefig ( " lang_plot.pdf " )
