# ------------------------------------------------ Barra de Progresso ------------------------------------------------ #

def progress_bar(percentagematual, total=100, tamanhobarra=30):
    """
    Função gera barra de progresso simples, para atualizar a barra, apenas chame a função novamente com a nova
    percentagem que deseja

    :param percentagematual: Percentagem atual da barra
    :type percentagematual: int
    :param total: Percentagemr Total da Barra
    :type total: int
    :param tamanhobarra: Tamanho da barra
    :type tamanhobarra: int
    :return:
    """
    # a percentagem é igual a percentagem da atual da barra definida pelo utilizador multiplicada por 100
    # e depois dividida pela percentagem total também definida pelo utilizador (ex. (80*100)/100 = 80;(80*100)/200 = 40,
    # para que o utilizador possa definir uma valor maior que 100% para a barra
    percentagem = int(float(percentagematual) * 100 / total)
    # a seta da barra  e progresso são multiplicadas pela percentagem(80/40) a dividir por cem (0.8/0.4) a multiplicar
    # pelo tamanho da barra que pode ser ou não definido pelo utilizador menos um (23/12) que será o quanto da
    # barra estará preenchida do tamanho total da barra(o valor predefinido é 30) mais uma sinal de maior que
    setas = "=" * int(percentagem / 100 * tamanhobarra - 1) + ">"
    # os espaços são o tamanho da barra menos o total de setas (30-23 = 7/30-12= 18)
    espacos = " " * (tamanhobarra - len(setas))
    # O print disso será (as setas, seguidos pelos espaços) com a percentagem no final, seguido depois então por
    # end="\r" o que fará com que o próximo print da barra tome o lugar do print anterior(na mesma linha no mesmo lugar)
    # dando então o efeito de uma barra de progresso
    print("\rProgress: [{0}{1}] {2} %".format(setas, espacos, percentagem), end="", flush=True)


# ---------------------------- Função para implementar barra de progresso que imprime algo --------------------------- #


def dinamic_bar(percentagemtotal=100, pararempercentagem=False,
                           pararem="", imprimir="", tempo=1200, mensagemconclusao="Done!"):
    """
    Funcão gera uma barra de progesso dinâmica que pode imprimir mensagens em certas percentagens

    :param percentagemtotal: Percentagem Total da barra
    :type percentagemtotal: int
    :param pararempercentagem: Se verdadeiro, em uma certa percentagem a função irá imprimir algo
    :type pararempercentagem: True / False
    :param pararem: Lista com percetagens que deseja parar, apenas números (Ex. [25, 50])
    :type pararem: list
    :param imprimir: Lista com mensagens que deseja imprimir, número de elementos deve ser igual à 'pararem'
    :type imprimir: list
    :param tempo: Tempo que a barra levará para completar 100% (1200 é aproximadamente 3s)
    :type tempo: int
    :param mensagemconclusao: Mensagem que irá ser mostrada após a barra atingir 100%
    :type mensagemconclusao: str
    """
    posicao_mensagem = 0
    numero_mensagens = len(pararem)
    # Percentagem total + 1 logo que o zero também conta
    for p in range(percentagemtotal + 1):
        for t in range(tempo):
            barradeprogresso(p, 100)
        if pararempercentagem is True:
            try:
                if p == pararem[posicao_mensagem]:
                    print(imprimir[posicao_mensagem])
                    # Adiciona mais 1 para posicao da mensagem até que seja igual ao número de elementos em pararem
                    if posicao_mensagem != numero_mensagens:
                        posicao_mensagem += 1
            except IndexError:
                continue
    print("\n" + mensagemconclusao)

# --------------------------------- Função para implementar carregamento com '...' ----------------------------------- #


def loading_info(info="Loading", tipo_de_ponto=".", numero_pontos=3, tipo_info="info", velocidade=1):
    """
    Função imprime um ponto a cada x segundos(EX.: Loading...)
    :param str info: Mensagem a ser impressa
    :param str tipo_de_ponto: Tipo de pontos(EX.: '.' , '-', etc) irão aparecer apos a info
    :param int numero_pontos: Número de pontos que serão colocados
    :param str tipo_info: Tipo da informação(pode ser 'info', 'error', 'warning') irá aparecer antes da info(Ex.:[INFO])
    :param int velocidade: Velocidade que os pontos irão aparecer, deve ser maior que zero, mas pode ser menor que 1
    """
    if tipo_info:
        tipo_info = "[{}]".format(tipo_info.upper())
    for loading in range(numero_pontos + 1):
        print("\r{0} {1}".format(tipo_info, info) + tipo_de_ponto * loading, end="")
        # Cria tempo para parecer que está carregando
        for t in range(10000000 * velocidade):
            t += 1
    print("\n")

