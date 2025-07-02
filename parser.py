import re

def acha_nodes(texto):
    nodes = [] # : (int, int)
    i = 0
    while (i := texto.find('[', i+1)) != -1:
        j = texto.find(')', i+1)
        nodes.append((i,j))
    return nodes

def expandir(texto, n):
    texto = texto.replace("<", "").replace(">", "")
    nodes = acha_nodes(texto)
    i,j = nodes[n] 
    pattern = r'\[[^]]*\]\((\d+)\)'
    candidatos = re.findall(pattern, texto)
    linha = int(candidatos[n]) # : str
    expansão = dados[linha-1]
    novo_texto = texto[:i] + "<" + expansão + ">" + texto[j+1:]
    return novo_texto

def limpa(texto):
    pattern = r'(?<=\])\((\d+)\)'
    return re.sub(pattern, "", texto)

def colore(texto):
    texto = re.sub(r"<[^>]*>", lambda s: f"\033[33m{s[0][1:-1]}\033[0m", texto) # amarelo
    return texto

path = 'exemplo.tree'
with open(path) as file:
    dados = file.read().splitlines()

texto = dados[0]
while (n := input(f"\n{colore(limpa(texto))}\nexpandir: ")) != "":
    try:
        n = int(n)
        texto = expandir(texto, n)
    except IndexError:
        pass