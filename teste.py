def parse_mealy_machine(file_path):
    machine = {
        'states': [],
        'initial_state': '',
        'final_states': [],
        'input_alphabet': [],
        'output_alphabet': [],
        'transitions': {}
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() != '']

    machine['states'] = lines[0].split()
    machine['initial_state'] = lines[1]
    machine['final_states'] = lines[2].split()
    machine['input_alphabet'] = lines[3].split()
    machine['output_alphabet'] = lines[4].split()

    for line in lines[5:]:
        parts = line.split()
        if len(parts) != 4:
            raise ValueError(f"Linha de transição inválida: '{line}'")
        current_state, input_symbol, next_state, output_symbol = parts

        # Converter '\n' literal para caractere nova linha
        if output_symbol == r'\n':  # note o raw string para comparar literalmente '\n'
            output_symbol = '\n'
        elif output_symbol == 'e':
            output_symbol = ''

        if current_state not in machine['transitions']:
            machine['transitions'][current_state] = {}
        machine['transitions'][current_state][input_symbol] = (next_state, output_symbol)

    return machine


def simulate(machine, input_word):
    current_state = machine['initial_state']
    output_word = ""

    for symbol in input_word:
        if symbol not in machine['input_alphabet']:
            raise ValueError(f"Símbolo de entrada '{symbol}' não pertence ao alfabeto de entrada.")

        if current_state in machine['transitions'] and symbol in machine['transitions'][current_state]:
            next_state, output_symbol = machine['transitions'][current_state][symbol]
            output_word += output_symbol
            current_state = next_state
        else:
            raise ValueError(f"Transição indefinida: estado '{current_state}' com símbolo '{symbol}'.")

    return output_word


def generate_ppm(output_matrix_str, output_file_path):
    lines = output_matrix_str.strip('\n').split('\n')
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        for line in lines:
            f.write(' '.join(line.strip()) + '\n')


def main():
    print("=== Simulador de Máquina de Mealy com saída PPM ===")
    machine_file = input("Digite o nome do arquivo da máquina (ex: m1.txt): ").strip()
    input_file = input("Digite o nome do arquivo de entrada (ex: w16.txt): ").strip()
    output_file = input("Digite o nome do arquivo de saída PPM (ex: saida.ppm): ").strip()

    try:
        mealy_machine = parse_mealy_machine(machine_file)
        with open(input_file, 'r', encoding='utf-8') as f:
            input_word = f.read().strip()
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler os arquivos: {e}")
        return

    try:
        output_string = simulate(mealy_machine, input_word)
        generate_ppm(output_string, output_file)
        print(f"\n✅ Imagem PPM gerada com sucesso em '{output_file}'.")
    except Exception as e:
        print(f"\n❌ Erro durante simulação ou geração da imagem: {e}")


if __name__ == "__main__":
    main()
