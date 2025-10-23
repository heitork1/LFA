def cria_mealy_maquina(file_path):
    maquina = {
        'estados': [],
        'initial_estado': '',
        'final_estados': [],
        'alfabeto_entrada': [],
        'saida__alfabeto': [],
        'transicoes': {}
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f if linha.strip() != '']

    maquina['estados'] = linhas[0].split()
    maquina['initial_estado'] = linhas[1]
    maquina['final_estados'] = linhas[2].split()
    maquina['alfabeto_entrada'] = linhas[3].split()
    maquina['saida__alfabeto'] = linhas[4].split()

    for linha in linhas[5:]:
        parts = linha.split()
        if len(parts) != 4:
            raise ValueError(f"Linha de transição inválida: '{linha}'")
        estado_atual, simbolo_entrada, prox_estado, simbolo_saida = parts

        # Converter '\n' literal para caractere nova linha
        if simbolo_saida == r'\n':  # note o raw string para comparar literalmente '\n'
            simbolo_saida = '\n'
        elif simbolo_saida == 'e':
            simbolo_saida = ''

        if estado_atual not in maquina['transicoes']:
            maquina['transicoes'][estado_atual] = {}
        maquina['transicoes'][estado_atual][simbolo_entrada] = (prox_estado, simbolo_saida)

    return maquina


def simula(maquina, palavra_entrada):
    estado_atual = maquina['initial_estado']
    palavra_saida = ""

    for symbol in palavra_entrada:
        if symbol not in maquina['alfabeto_entrada']:
            raise ValueError(f"Símbolo de entrada '{symbol}' não pertence ao alfabeto de entrada.")

        if estado_atual in maquina['transicoes'] and symbol in maquina['transicoes'][estado_atual]:
            prox_estado, simbolo_saida = maquina['transicoes'][estado_atual][symbol]
            palavra_saida += simbolo_saida
            estado_atual = prox_estado
        else:
            raise ValueError(f"Transição indefinida: estado '{estado_atual}' com símbolo '{symbol}'.")

    return palavra_saida


def gera_ppm(saida_matrix_str, arq_saida_path):
    linhas = saida_matrix_str.strip('\n').split('\n')
    altura = len(linhas)
    larg = len(linhas[0]) if altura > 0 else 0

    with open(arq_saida_path, 'w', encoding='utf-8') as f:
        f.write("P1\n")
        f.write(f"{larg} {altura}\n")
        for linha in linhas:
            f.write(' '.join(linha.strip()) + '\n')


def main():
    print("=== Simulador de Máquina de Mealy com saída PPM ===")
    maquina_arq = input("Digite o nome do arquivo da máquina (ex: m1.txt): ").strip()
    input_arq = input("Digite o nome do arquivo de entrada (ex: w16.txt): ").strip()
    arq_saida = input("Digite o nome do arquivo de saída PPM (ex: saida.ppm): ").strip()

    try:
        mealy_maquina = cria_mealy_maquina(maquina_arq)
        with open(input_arq, 'r', encoding='utf-8') as f:
            palavra_entrada = f.read().strip()
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler os arquivos: {e}")
        return

    try:
        string_saida = simula(mealy_maquina, palavra_entrada)
        gera_ppm(string_saida, arq_saida)
        print(f"\n✅ Imagem PPM gerada com sucesso em '{arq_saida}'.")
    except Exception as e:
        print(f"\n❌ Erro durante simulação ou geração da imagem: {e}")


if __name__ == "__main__":
    main()
