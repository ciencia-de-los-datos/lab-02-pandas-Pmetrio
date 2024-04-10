"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    
    return len(tbl0)

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    Cant_Column = len(tbl0.columns)
    
    return Cant_Column

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    Respuesta_03 = tbl0.groupby('_c1')['_c1'].count()
    
    return Respuesta_03

def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    Respuesta_04 = tbl0.groupby('_c1')['_c2'].mean()
    
    return Respuesta_04

def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    Respuesta_05 = tbl0.groupby('_c1')['_c2'].max()
    
    return Respuesta_05

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    
    tbl1['_c4'] = tbl1['_c4'].transform(str.upper)
    Respuesta_06 = list(tbl1.sort_values(by='_c4', ascending=True)['_c4'].unique())
    
    return Respuesta_06

def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    Respuesta_07 = tbl0.groupby('_c1')['_c2'].sum()
    
    return Respuesta_07

def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    Respuesta_08 = tbl0.assign(suma = tbl0['_c0']+tbl0['_c2'])
    
    return Respuesta_08

def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    # Resultado_09 = tbl0['year'] = tbl0['_c3'].str.split('-').str[0]
    Respuesta_09 = tbl0.copy()
    Respuesta_09['year'] = Respuesta_09['_c3'].str.split('-').str[0]
    
    return Respuesta_09

def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    Resultado = tbl0.copy()
    Resultado = Resultado.sort_values(['_c1', '_c2'], ascending=True)
    Respuesta_10 = Resultado.groupby('_c1')['_c2'].agg(lambda x: ':'.join(x.astype(str))).reset_index()    
    Respuesta_10.set_index('_c1', inplace=True)
    
    return Respuesta_10

def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    Df_Proof = tbl1.copy()
    Df_Proof_T = Df_Proof.sort_values(['_c4','_c0'], ascending=True)
    Df_Proof_T = Df_Proof_T.groupby('_c0')['_c4'].agg(lambda x: ','.join(x.astype(str))).reset_index()
    Df_Proof_T['_c4'] = Df_Proof_T['_c4'].apply(str.lower)
    
    return Df_Proof_T

def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    Respuesta_12 = tbl2.copy()
    Respuesta_12_T = Respuesta_12.sort_values(['_c5a','_c5b', '_c0'], ascending=True)
    Respuesta_To = Respuesta_12_T.assign( _c5 = Respuesta_12_T['_c5a']+":"+Respuesta_12_T['_c5b'].astype(str))
    Respuesta_Total = Respuesta_To.groupby('_c0')['_c5'].agg(','.join).reset_index()
    
    return Respuesta_Total

def pregunta_13():    
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    DF_Fusion = pd.merge(tbl2, tbl0, on='_c0')
    Respuesta_13 = DF_Fusion.groupby('_c1')['_c5b'].sum()
    
    return Respuesta_13
'''
respuesta_01 = pregunta_01()
print(f"La respuesta es: {respuesta_01}")
respuesta_02 = pregunta_02()
print(f"La respuesta es: {respuesta_02}")
respuesta_03 = pregunta_03()
print(f"La respuesta es: {respuesta_03}")
respuesta_04 = pregunta_04()
print(f"La respuesta es: {respuesta_04}")
respuesta_05 = pregunta_05()
print(f"La respuesta es: {respuesta_05}")
respuesta_06 = pregunta_06()
print(f"La respuesta es: {respuesta_06}")
respuesta_07 = pregunta_07()
print(f"La respuesta es: {respuesta_07}")
respuesta_08 = pregunta_08()
print(f"La respuesta es: {respuesta_08}")
respuesta_09 = pregunta_09()
print(f"La respuesta es: {respuesta_09}")
respuesta_10 = pregunta_10()
print(f"La respuesta es: {respuesta_10}")
respuesta_11 = pregunta_11()
print(f"La respuesta es: {respuesta_11}")
respuesta_12 = pregunta_12()
print(f"La respuesta es: {respuesta_12}")
respuesta_13 = pregunta_13()
print(f"La respuesta es: {respuesta_13}")
'''
