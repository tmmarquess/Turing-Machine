import json

fita = str()

movimento = {
    'D': 1,
    'E': -1,
    'P': 0
}

def reiniciar_fita(tam=100):
    global fita
    fita = 'b'*tam
    fita = list(fita)

def converter_para_dict(str : str) -> dict:
    str = str.replace("'", '"')
    str = str.replace('(',('[')).replace(')',(']'))
    str = str.replace('D',('"D"')).replace('E',('"E"'))
    str = str.replace('P',('"P"')).replace('b',('"b"'))

    try:
        return json.loads(str)
    except:
        return None

def computar(palavra : list, mt : dict) -> bool:
    global fita
    reiniciar_fita()
    for i in range(len(palavra)):
        fita[i] = palavra[i]
    
    cabecote = 0
    estado_atual = mt['inicial']
    estados = mt['delta']

    while True:
        refazer_loop = False
        for estado in estados:
            if estado[0] == estado_atual and str(estado[2]) == fita[cabecote]:
                    refazer_loop = True
                    fita[cabecote] = str(estado[3])
                    cabecote += movimento[estado[4]]
                    estado_atual = estado[1]
        if not refazer_loop:
            if estado_atual == mt['aceita']:
                return "ACEITA"
            else:
                return "REJEITA"


test_string = "{'inicial': 0, 'aceita': 1, 'rejeita': 2, 'delta': [(0,0,0,1,D),(0,0,1,0,D),(0,3,b,b,E), (3,1,0,0,P),(3,1,1,1,P)]}"

mt = converter_para_dict(test_string)

palavras = ['100', '10101', '000000000']

for palavra in palavras:
    res = computar(list(palavra), mt)

    palavra_modificada = []
    i = 0
    while(fita[i] != 'b'):
        print(f'{fita[i]}',end='')
        i += 1

    print(f' {res}')
    