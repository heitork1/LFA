def parse_mealy_maquina(file_path):
    maquina = {
        'estados': [],
        'initial_estado': '',
        'final_estados': [],
        'alfabeto_entrada': [],
        'output_alphabet': [],
        'transicoes': {}
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        linhas = [line.strip() for line in f if line.strip() != '']

    maquina['estados'] = linhas[0].split()
    maquina['initial_estado'] = linhas[1]
    maquina['final_estados'] = linhas[2].split()
    maquina['alfabeto_entrada'] = linhas[3].split()
    maquina['output_alphabet'] = linhas[4].split()

    for line in linhas[5:]:
        parts = line.split()
        if len(parts) != 4:
            raise ValueError(f"Linha de transição inválida: '{line}'")
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


def simulate(maquina, palavra_entrada):
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


def generate_ppm(output_matrix_str, arq_saida_path):
    linhas = output_matrix_str.strip('\n').split('\n')
    altura = len(linhas)
    larg = len(linhas[0]) if altura > 0 else 0

    with open(arq_saida_path, 'w', encoding='utf-8') as f:
        f.write("P1\n")
        f.write(f"{larg} {altura}\n")
        for line in linhas:
            f.write(' '.join(line.strip()) + '\n')


def main():
    print("=== Simulador de Máquina de Mealy com saída PPM ===")
    maquina_file = input("Digite o nome do arquivo da máquina (ex: m1.txt): ").strip()
    input_file = input("Digite o nome do arquivo de entrada (ex: w16.txt): ").strip()
    arq_saida = input("Digite o nome do arquivo de saída PPM (ex: saida.ppm): ").strip()

    try:
        mealy_maquina = parse_mealy_maquina(maquina_file)
        with open(input_file, 'r', encoding='utf-8') as f:
            palavra_entrada = f.read().strip()
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler os arquivos: {e}")
        return

    try:
        string_saida = simulate(mealy_maquina, palavra_entrada)
        generate_ppm(string_saida, arq_saida)
        print(f"\n✅ Imagem PPM gerada com sucesso em '{arq_saida}'.")
    except Exception as e:
        print(f"\n❌ Erro durante simulação ou geração da imagem: {e}")


if __name__ == "__main__":
    main()
