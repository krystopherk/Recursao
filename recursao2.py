import pandas as pd
from datetime import date


caminho_arquivo = r"C:\Users\EJWAP\Downloads\Locais manutenção.xlsx"

df = pd.read_excel(caminho_arquivo)

def construir_arvore(df):
    arvore = {}
    for _, row in df.iterrows():
        codigo = row['Código'].strip()  # Remove espaços extras
        nome = row['Nome'].strip()  # Remove espaços extras
        partes = codigo.split('-')  # Divide o código em partes
        node = arvore
        for parte in partes:
            node = node.setdefault(parte, {})
        node['Nome'] = nome

        #{
        #    "AC": {
        #        "ADM": {
        #            "KDUWS": {"Nome": "Planta Campo Verde"},
        #            "KDEFG": {"Nome": "Outra Planta"}
        #        }
        #    }
        #}

    return arvore

arvore_manutencao = construir_arvore(df)

# Função recursiva
def exibir_opcoes(arvore, nivel, prefixo):
    # Árvore genealógica criada
    # Nível controla o nível atual da árvore (gomos)
    # Prefixo guarda o caminho atual

    while True:
        # Filtrar as opções do nível atual
        if nivel == 0:  # Primeiro nível, exibe apenas o primeiro item que não tem prefixo
            opcoes = [key for key in arvore.keys() if key != 'Nome']
        else:  # Subníveis
            subarvore = arvore
            for parte in prefixo.split('-'):
                subarvore = subarvore.get(parte, {})  # Navega na árvore até o prefixo atual
            opcoes = [key for key in subarvore.keys() if key != 'Nome']

        # Se não houver opções significa que é um item final
        if not opcoes:
            if prefixo:  # Se houver um prefixo significa que é um item final
                partes = prefixo.split('-')
                subarvore = arvore
                for parte in partes:
                    subarvore = subarvore[parte]
                print(f"\nItem final: {prefixo} - {subarvore['Nome']}")
                descricao = input("\nDescrição da avaria: ")
                data = date.today().strftime("%d/%m/%Y")
                print(f"\nOrdem de manutenção aberta!")
                print(f"Local: {prefixo} - {subarvore['Nome']}")
                print(f"Data: {data}")
                print(f"Ocorrência: {descricao}")
                return
            return

        # Exibe as opções com código e nome
        print("\n" + "  " * nivel + f"Selecione uma opção para o bloco: {prefixo or 'Raiz'}")
        for i, opcao in enumerate(opcoes, start=1):
            # Acessa o nome correspondente de cada opção
            partes = prefixo.split('-') + [opcao] if prefixo else [opcao]
            subarvore = arvore
            for parte in partes:
                subarvore = subarvore[parte]
            nome_completo = f"{opcao} - {subarvore['Nome']}" if 'Nome' in subarvore else opcao
            print("  " * nivel + f"{i}. {nome_completo}")
        print("  " * nivel + "0. Voltar")

        # Solicita a escolha do usuário
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 0:
                return  # Voltar para o nível anterior se escolher 0
            elif 1 <= escolha <= len(opcoes):
                selecionado = opcoes[escolha - 1]
                novo_prefixo = f"{prefixo}-{selecionado}" if prefixo else selecionado
                
                # Verifica se há subníveis
                subarvore = arvore
                for parte in novo_prefixo.split('-'):
                    subarvore = subarvore[parte]
                
                if len(subarvore) == 1 and 'Nome' in subarvore:
                    print(f"\nItem final: {novo_prefixo} - {subarvore['Nome']}")
                    descricao = input("\nDescrição da avaria: ")
                    data = date.today().strftime("%d/%m/%Y")
                    print(f"\nOrdem de manutenção aberta!")
                    print(f"Local: {novo_prefixo} - {subarvore['Nome']}")
                    print(f"Data: {data}")
                    print(f"Ocorrência: {descricao}")
                    exit()
                else:
                    print("\n" + "  " * (nivel + 1) + f"Você escolheu: {novo_prefixo}")
                    exibir_opcoes(arvore, nivel + 1, novo_prefixo)
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Entrada inválida. Digite um número.")


exibir_opcoes(arvore_manutencao, nivel=0, prefixo="")