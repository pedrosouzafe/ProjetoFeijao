# Imports:
import calendar
import json
from datetime import datetime


# Função para traduzir os dias da semana:
def diaDaSemanaPT(dia):
    if dia == "Monday":
        return "Segunda-Feira"
    elif dia == "Tuesday":
        return "Terça-Feira"
    elif dia == "Wednesday":
        return "Quarta-Feira"
    elif dia == "Thursday":
        return "Quinta-Feira"
    elif dia == "Friday":
        return "Sexta-Feira"
    elif dia == "Saturday":
        return "Sábado"
    else:
        return "Domingo"
    
# Função para fazer o registro do crescimento do feijão:
def registroCrescimento():

    print("\n--- Registro do Crescimento do Feijão ---")
    data = input("Digite a data (dd/mm/aaaa): ")
    altura = float(input("Digite a altura do feijão (cm): "))
    obser = input("Digite uma observação sobre o feijão (opcional): ")

    # Data para DateTime
    try:
        dataObj = datetime.strptime(data, "%d/%m/%Y")
    except:
        print("Formato da data inválido! Use dd/mm/aaaa.")
        return None
    
    # Informações adicionais
    diaSemana = calendar.day_name[dataObj.weekday()]
    anoBissexto = calendar.isleap(dataObj.year)

     # Estrutura dos dados
    registro = {
        "data": data,
        "alturaCm": altura,
        "observação": obser,
        "dia_semana": diaDaSemanaPT(diaSemana),
        "ano_bissexto": anoBissexto
    }

    return registro

# Função para salvar os dados do feijão:
def salvarDados(arquivo, dados):
    try:
        with open(arquivo, "r") as f:
            registros = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        registros = []
    
    registros.append(dados)

    with open(arquivo, "w") as f:
        json.dump(registros, f, indent=4, ensure_ascii=False)

    print("Dados salvos com sucesso! ")

# Função principal
def main():
    arquivoJson = "crescimento_feijao.json"

    while True:
        print("\n1. Registrar Crescimento")
        print("2. Exibir Registros")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registro = registroCrescimento()

            if registro:
                salvarDados(arquivoJson, registro)
        elif opcao == "2":
            try:
                with open(arquivoJson, "r") as f:
                    registros = json.load(f)
                if registros:
                    print("\n--- Registro do Crescimento ---")
                    for reg in registros:
                        print(f"Data: {reg['data']}, Altura: {reg['alturaCm']} cm, "
                              f"Dia da Semana: {reg['dia_semana']}, "
                              f"Ano Bissexto: {reg['ano_bissexto']}, "
                              f"Observação: {reg['observação']}")
                else:
                    print("Nenhum registro encontrado.")
            
            except FileNotFoundError:
                print("Nenhum registro encontrado. ")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
