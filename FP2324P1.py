def eh_territorio(argumento):
    """
     Verifica se um argumento corresponde a um território. Um territorio é um tuplo de tuplos,
    que contêm no mínimo 1 caminho vertical e 1 caminho horizontal e no máximo 26 caminhos veticais
    e 99 caminhos horizontais, sendo que as interseções desses caminhos estão ocupadas pelos inteiros
    1 ou 0.
        Exemplo de um território: ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))

    Parâmetros:
            argumento (arg): Qualquer argumento que será verificado se é um território
    Retorna:
            bool: True se o argumento for um território, False caso contrário.
    """
    # Verifica se o argumento é um tuplo e tem um tamanho válido
    if not (type(argumento) == tuple and 1 <= len(argumento) <= 26):
        return False

    # Verifica se o argumento é um tuplo de tuplos representando caminhos horizontais
    if not type(argumento[0]) == tuple:
        return False
    territorio_comprimento = len(argumento[0])
    if not (1 <= territorio_comprimento <= 99):
        return False

    # Verifica se o argumento é um tuplo de tuplos e se as interseções são 0 ou 1
    for linha in argumento:
        if not type(linha) == tuple or len(linha) != territorio_comprimento:
            return False

        for intersecao in linha:
            if type(intersecao) != int or intersecao not in (1, 0):
                return False
    return True


def obtem_ultima_intersecao(territorio):
    """
    A função recebe um território válido e devolve a interseção do canto superior direito do território.

    Parâmetros:
        territorio (tuple): Um território válido.

    Retorna:
        tuple: Um tuplo que representa a última interseção do território no formato ('Letra', número).
    """

    return (chr(ord("A") + len(territorio) - 1), len(territorio[0]))


def eh_intersecao(argumento):
    """
    Verifica se um argumento corresponde a uma interseção.

    Parâmetros:
        argumento (arg): Qualquer argumento que será verificado se é uma interseção.

    Retorna:
        bool: True se o argumento for uma interseção, False caso contrário.
    """
    # Verifica se o argumento é um tuplo de 2 elementos
    if not type(argumento) == tuple or len(argumento) != 2:
        return False

    # Verifica se o primeiro elemento do argumento é uma letra e se o segundo é um inteiro
    # positivo menor que 100
    if not (
        type(argumento[0]) == str and len(argumento[0]) == 1 and argumento[0].isupper()
    ) or not (type(argumento[1]) == int and 1 <= argumento[1] <= 99):
        return False
    return True


def eh_intersecao_valida(territorio, intersecao):
    """
    Verifica se uma interseção é válida num território.

    Parâmetros:
        territorio (tuple): Qualquer território válido.
        intersecao (tuple): A interseção a ser verificada.

    Retorna:
        bool: True se a interseção é válida no território, False caso contrário.
    """
    if not eh_intersecao(intersecao):
        return False
    ultima_intersecao = obtem_ultima_intersecao(territorio)
    # Verifica se as coordenadas da interseção são superiores às da última interseção
    if intersecao[0] > ultima_intersecao[0] or intersecao[1] > ultima_intersecao[1]:
        return False
    return True


def eh_intersecao_livre(territorio, intersecao):
    """
    Verifica se uma interseção corresponde a uma interseção livre (não ocupada por montanhas)
    dentro do território.

    Parâmetros:
        territorio (tuple): Qualquer território válido.
        intersecao (tuple): A interseção a ser verificada.

    Retorna:
        bool: True se a interseção é livre, False caso contrário.
    """
    linha = ord(intersecao[0]) - ord("A")
    coluna = intersecao[1] - 1
    # Uma interseção ocupada por uma montanha é igual a 1
    if territorio[linha][coluna]:
        return False
    return True


def obtem_intersecoes_adjacentes(territorio, intersecao):
    """
    Obtém as interseções válidas adjacentes à interseção dada.

    Parâmetros:
        territorio (tuple): Qualquer território válido.
        intersecao (tuple): A interseção que se quer obter as adjacentes.

    Retorna:
        tuple: Tuplo com as interseções adjacentes à interseção dada.
    """

    intersecoes_adjacentes = ()
    # Definição das possíveis das direções das interseções adjacentes
    direcoes = ((0, -1), (-1, 0), (1, 0), (0, 1))
    # Cria as interseções adjacentes e verifica se são válidas
    for x, y in direcoes:
        intersecao_adjacente = (chr(ord(intersecao[0]) + x), intersecao[1] + y)
        if eh_intersecao_valida(territorio, intersecao_adjacente):
            intersecoes_adjacentes += (intersecao_adjacente,)

    return intersecoes_adjacentes


def ordena_intersecoes(intersecoes):
    """
    Ordena um tuplo de interseções de acordo com a ordem de leitura do territorio.

    Parâmetros:
        intersecoes (tuple): Tuplo de interseções.

    Retorna:
        tuple: Tuplo com as interseções ordenadas.
    """

    return tuple(
        sorted(intersecoes, key=lambda intersecao: (intersecao[1], intersecao[0]))
    )


def territorio_para_str(territorio):
    """
    Converte um território para uma cadeia de caracteres que o representa.

    Parâmetros:
        territorio (tuple): Qualquer território válido.

    Retorna:
        str: O território representado como uma cadeia de caracteres.
    """

    if not eh_territorio(territorio):
        raise ValueError("territorio_para_str: argumento invalido")

    # Cria a cadeia de caracteres e adiciona os números correspondentes
    # aos caminhos horizontais e também adiciona as montanhas representadas
    # por "X" e o as intersções livres pelo "."
    territorio_string = ""
    for linha in reversed(range(len(territorio[0]))):
        territorio_string += f"{linha + 1:2d}"
        for coluna in range(len(territorio)):
            territorio_string += " X" if territorio[coluna][linha] else " ."
        territorio_string += f" {linha + 1:2d}\n"

    # Cria as letras que correspondem aos caminhos verticais
    letras = "  "
    for coluna in range(len(territorio)):
        letras += " " + chr(ord("A") + coluna)

    return letras + "\n" + territorio_string + letras


def obtem_cadeia(territorio, intersecao):
    """
    Obtém as interseções conectadas à interseção fornecida.

    Parâmetros:
        territorio (tuple): Qualquer território válido.
        intersecao (tuple):  A interseção que se quer obter as conectadas.
    Retorna:
        tuple: tuplo com todas as interseções conectadas à interseção fornecida (incluida ela própria),
               ordenadas de acordo com a leitura do território.
    """

    if not eh_territorio(territorio) or not eh_intersecao_valida(
        territorio, intersecao
    ):
        raise ValueError("obtem_cadeia: argumentos invalidos")

    # A variável tipo representa o tipo de cadeia que procuramos,
    # False - montanhas, True - interseções livres
    tipo = eh_intersecao_livre(territorio, intersecao)

    # Função recursiva que obtêm a cadeia de interseções, através da procura de interseções
    # do mesmo tipo que a original que sejam adjacentes umas às outras
    def cadeia(territorio, intersecao, tipo, res):
        if intersecao not in res:
            res += (intersecao,)
            for i in obtem_intersecoes_adjacentes(territorio, intersecao):
                if eh_intersecao_livre(territorio, i) == tipo:
                    res = cadeia(territorio, i, tipo, res)
        return res

    return ordena_intersecoes(cadeia(territorio, intersecao, tipo, ()))


def obtem_vale(territorio, intersecao):
    """
    Obtém as interseções que fazem parte do vale da montanha da interseção fornecida.

    Parâmetros:
        territorio (tuple): Um território válido.
        intersecao (tuple): Uma interseção ocupada por uma montanha.

    Retorna:
        tuple: Um tuplo contendo todas as interseções que fazem parte do vale da montanha,
               ordenadas de acordo com a leitura do território.
    """
    if (
        not eh_territorio(territorio)
        or not eh_intersecao_valida(territorio, intersecao)
        or eh_intersecao_livre(territorio, intersecao)
    ):
        raise ValueError("obtem_vale: argumentos invalidos")

    # Obter a cadeia de interseções da montanha
    intersecoes_cadeia = obtem_cadeia(territorio, intersecao)
    vale = ()
    # Adicionar todas as interserções livres adjacentes às montanhas
    # da cadeia de modo a se obter o vale da montanha
    for montanha in intersecoes_cadeia:
        adjacentes = obtem_intersecoes_adjacentes(territorio, montanha)
        for i in adjacentes:
            if eh_intersecao_livre(territorio, i) and i not in vale:
                vale += (i,)
    return ordena_intersecoes(vale)


def verifica_conexao(territorio, intersecao1, intersecao2):
    """
    Verifica se duas interseções estão conectadas no território.

    Parâmetros:
        territorio (tuple): Um território válido.
        intersecao1 (tuple): A primeira interseção.
        intersecao2 (tuple): A segunda interseção.

    Retorna:
        bool: True se as interseções estão conectadas, False caso contrário.
    """
    if (
        not eh_territorio(territorio)
        or not eh_intersecao_valida(territorio, intersecao1)
        or not eh_intersecao_valida(territorio, intersecao2)
    ):
        raise ValueError("verifica_conexao: argumentos invalidos")

    # Se uma interseção encontra-se na mesma cadeia que outra interseção, elas estão conectadas
    if intersecao1 in obtem_cadeia(territorio, intersecao2):
        return True
    return False


def calcula_numero_montanhas(territorio):
    """
    Calcula o número de interseções ocupadas por montanhas no território.

    Parâmetros:
        territorio (tuple): Um território válido.

    Retorna:
        int: O número de interseções ocupadas por montanhas.
    """
    if not eh_territorio(territorio):
        raise ValueError("calcula_numero_montanhas: argumento invalido")

    # iteração sobre as interseções do teritório para se contar o número de montanhas
    counter = 0
    for coluna in territorio:
        for intersecao in coluna:
            if intersecao:
                counter += 1
    return counter


def calcula_numero_cadeias_montanhas(territorio):
    """
    Calcula o número de cadeias de montanhas contidas no território.

    Parâmetros:
        territorio (tuple): Um território válido.

    Retorna:
        int: O número de cadeias de montanhas.
    """
    if not eh_territorio(territorio):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")

    counter = 0
    montanhas = ()
    # Iteração sobre as itersecões do território
    for i in range(len(territorio)):
        for j in range(len(territorio[0])):
            intersecao = (chr(ord("A") + i), j + 1)
            # Verifica se a interseção é uma montanha e se ainda não foi incluída nas montanhas
            if (
                not eh_intersecao_livre(territorio, intersecao)
                and intersecao not in montanhas
            ):
                # Adiciona a cadeia associada às montanhas, de modo a não se contar a mesma cadeia mais que
                # 1 vez e incrementa o contador
                montanhas += obtem_cadeia(territorio, intersecao)
                counter += 1
    return counter


def calcula_tamanho_vales(territorio):
    """
    Calcula o número total de interseções diferentes que formam todos os vales do território.

    Parâmetros:
        territorio (tuple): Um território válido.

    Retorna:
        int: O número total de interseções que formam os vales.
    """
    if not eh_territorio(territorio):
        raise ValueError("calcula_tamanho_vales: argumento invalido")

    vales = set()
    montanhas = ()
    # Iteração sobre as itersecões do território,
    for i in range(len(territorio)):
        for j in range(len(territorio[0])):
            intersecao = (chr(ord("A") + i), j + 1)
             # Verifica se a interseção é uma montanha e se ainda não foi incluída nas montanhas
            if (
                not eh_intersecao_livre(territorio, intersecao)
                and intersecao not in montanhas
            ):
                # Adiciona os vales encontrados e também as montanhas cujos vales já foram encontrados
                # às respetivas variáveis
                vales.update(obtem_vale(territorio, intersecao))
                montanhas += obtem_cadeia(territorio, intersecao)
    return len(vales)
