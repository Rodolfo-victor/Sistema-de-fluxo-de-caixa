# MIT License
# Copyright (c) 2025 Rodolfo Victor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


import json
import datetime

def exibir_menu():
    print("\nXYZ Comercio de Produtos LTDA.")
    print("SISTEMA DE FLUXO DE CAIXA\n")
    print("1 - ENTRADA")
    print("2 - SAÍDA")
    print("3 - RALATORIOS")
    print("0 - FINALIZAR")
    return input("\nOPÇÃO")

movimentacao = {
    "documento": "123",
    "descricao": "Venda de produto",
    "valor": 150.00,
    "data": "2025-07-11",
    "tipo": "Entrada" # ou "saida"
}

def salvar_dados():
    try:
        with open("movimentacoes.json", "w", encoding="utf-8") as f:
            json.dump(movimentacoes, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        
def carregar_dados():
    global movimentacoes
    try:
        with open("movimentacoes.json", "r", encoding="utf-8") as f: movimentacoes = json.lond(f)
    except FileNotFoundError:
        movimentacoes = [] #se o arquivo ainda não existir 
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        movimentacoes = []        
        
movimentacoes = []

def exibir_submenu(tipo_operacao):
    while True:
        print(f"\nCadastro de {tipo_operacao}")
        print("1 - INCLUSÂO")
        print("2 - ALTERAÇÂO")
        print("3 - CONSULTA")
        print("4 - EXCLUSÃO")
        print("0 - RETONAR")
        opcao = input("\nOpção: ")
        
        if opcao == '1':
            incluir_movimentacao(tipo_operacao)
        elif opcao =='2':
            alterar_movimentacao(tipo_operacao)
        elif opcao =='3':
           consultar_movimentacao(tipo_operacao)
        elif opcao =='4':
            excluir_movimentacao(tipo_operacao)
        elif opcao =='0':
            break
        else:
            print("Opção Inválida. Tente Novamente.")
            
def exibir_menu_relatorios():
    while True:
        print("\nRELATÓRIOS")
        print("1 - FECHAMENTO DO CAIXA")
        print("2 - BALANÇO POR PERÍODO")
        print("0 - RETORNAR")
        opcao = input("\nOPCAO: ")
        
        if opcao == '1':
            relatorio_fechamento_caixa()
        elif opcao == '2':
            relatorio_balanco_periodo()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def relatorio_balanco_periodo():
    ano = input("informe o ano (ex: 2025): ").strip()
    if not ano.isdigit() or len(ano) != 4:
        print("Ano inválido.")
        return
    
    meses = {
        "01" : "JANEIRO",
        "02" : "FEVEREIRO",
        "03" : "MARCÇO",
        "04" : "ABRIL",
        "05" : "MAIO",
        "06" : "JUNHO",
        "07" : "JULHO",
        "08" : "AGOSTO",
        "09" : "SETEMBRO",
        "10" : "OUTUBRO",
        "11" : "NOVEMBRO",
        "12" : "DEZEMBRO"
    }            
    
    #aqui inicia a estrura de soma
    balanco = {mes: {"entrada": 0.0, "saidas":0.0} for mes in meses}
    
    #processa as movimentações
    for m in movimentacoes:
        data = m["data"] #formato da data YYYY/MM/DD
        if data.startswith(ano):
            mes = data[5:7]
            if m["tipo"] == "ENTRADA":
                balanco[mes]["entradas"] += m["valor"]
            elif m["tipo"] == "Saída":
                balanco[mes]["saídas"] += m["valor"]
                
    #mostra o relatório
    print(f"BALANÇO ANUL DE {ano}")
    print("-" * 50)
    print(f"{'MÊS':<15} {'ENTRADAS':>10} {'SAÍDAS':>10} {'SALDO':>10}")
    
    saldo_total = 0.0
    
    for mes in meses:
        ent = balanco[mes]["entradas"]
        sai = balanco[mes]["saidas"]
        saldo = ent - sai 
        saldo_total += saldo
        
        print(f"{meses[mes]:<15} R$ {ent:>8.2f} R$ {sai:>8.2f} R$ {saldo:>8.2f}")
        
    print("-" * 50)
    print(f"{'SALDO DO PERÍODO':<35} R$ {saldo_total:>8.2f}")
    
    
def incluir_movimentacao(tipo_operacao):
    while True:
        doc = input("Documento: ").strip()
        if not doc.isdigit():
            print("Documento deve conter apenas números.")
            continue
        
        desc = input("DESCRIÇÂO: ").strip()
        
        try:
            valor = float(input("Valor: ").replace(',', '.'))
        except ValueError:
            print("Valor inválido. Use apenas números.")
            continue 
        
        data = datetime.date.today().isoformat() #data de hoje
        
        print("\nConfirma inclusão (S/N)")
        confirma = input().strip().upper()
        if confirma == 'S':
            movimentacoes.append({
                "documento": doc,
                "descricao": desc,
                "valor": valor,
                "data": data,
                "tipo": tipo_operacao
            })
            print("Movimentação incluída com sucesso!")
        else:
            print("Inclusão cancelada.")
            
        nova = input("Nova inclusão (S/N)? ").strip().upper()
        if nova != 'S':
            break
    movimentacoes.append({...})
    salvar_dados()
        
def alterar_movimentacao(tipo_operacao):
    while True:
        doc = input("Informe o número do documento: ").strip()
        encontrado = False
        
        for m in movimentacoes:
            if m["documento"] == doc and m["tipo"] == tipo_operacao:
                encontrado = True
                print("\n DADOS ATUAIS:")
                print(f"DESCRIÇÃO: {m['descricao']}")
                print(f"VALOR: {m['valor']}")
                print(f"DATA: {m['data']}")
                
                nova_desc = input("Nova descrição: ").strip()
                try:
                    novo_valor = float(input("Novo valor: ").replace(',', '.'))
                except ValueError:
                    print("Valor inválido. Alteração cancelada")
                    break
                
                confirma = input("Confirma alteração (S/N)? ").strip().upper()
                if confirma == 'S':
                    m['descricao'] = nova_desc
                    m['valor'] = novo_valor
                    print("Alteração realizada com sucesso.")
                else:
                    print("Alteração cancelada.")
                    break
        if not encontrado:
            print("Documento não encontrado.")
            
        nova = input("Nova alteração (S/N)? ").strip().upper()
        if nova != 'S':
            break
    movimentacoes.append({...})
    salvar_dados()

def consultar_movimentacao(tipo_operacao):
    while True:
        doc = input("Informe o número do documento para consultar: ").strip()
        encontrado = False
        
        for m in movimentacoes:
            if m["documento"] == doc and m["tipo"] == tipo_operacao:
                encontrado = True
                print("\nDADOS DA MOVIMENTAÇÃO:")
                print(f"DESCRIÇÃO : {m['descricao']}")
                print(f"VALOR     : R$ {m['valor']:.2f}")
                print(f"DATA      : {m['data']}")
                print(f"TIPO      : {m['tipo']}")
                break
            
            if not encontrado:
                print("Documento não encontrado.")
                
        nova = input("Deseja fazer uma nova consulta (S/N)? ").strip().upper()
        if nova != 'S':
                break
            
            
def excluir_movimentacao(tipo_operacao):
    while True:
        doc = input("Informe o número do documento a ser excluido: ").strip()
        encontrada = False
        
        for i, m in enumerate(movimentacoes):
            if m["documento"] == doc and m["tipo"] == tipo_operacao:
                encontrada = True
                print("\nDADOS DA MOVIMENTAÇÃO:")
                print(f"DESCRIÇÃO : {m['descricao']}")
                print(f"VALOR     : R$ {m['valor']:.2f}")
                print(f"DATA      : {m['data']}")
                print(f"TIPO      : {m['tipo']}")
                
                confirma = input("Confirma exclusão (S/N)? ").strip().upper()
                if confirma == 'S':
                    movimentacoes.pop(i)
                    print("Movimentação excluida com sucesso.")
                else:
                    print("Exclusão cancelada.")
                break
            
        if not encontrada:
            print("Documento não encontrado.")
            
        nova = input("Nova exclusão (S/N)").strip().upper()
        if nova != 'S':
            break
    movimentacoes.append({...})
    salvar_dados()
    
def relatorio_fechamento_caixa():
    hoje = datetime.date.today().isoformat()
    entrada = []
    saidas = []
    
    for m in movimentacoes:
        if m["data"] == hoje:
            if m["tipo"] == "ENTRADA":
                entrada.append(m)
            elif m["tipo"] == "SAÍDA":
                saidas.append(m)
                
    total_entradas = sum(m["valor"] for m in entrada)
    total_saidas = sum(m["valor"] for m in saidas)
    saldo_inicial = 0.0 #pode ser ajustado depois 
    saldo_final = saldo_inicial + total_entradas - total_saidas
    
    print("\nXYZ COMÉRCIO DE PROFUTOS LTDA.")
    print("FECHAMENTO DO CAIXA -", hoje)
    print("-" * 40)
    
    print("\nENTRADAS")
    for e in entrada:
        print(f"{e['documento']:10} {e['descricao'][:20]:20} R$ {e['valor']:>8.2}")
     
    print("\nSAÍDAS")
    for s in saidas:
        print(f"{s['documento']:10} {s['descricao'][:20]:20} R$ {s['valor']:>8.2f}")   
        
    print("\nPOSIÇÃO DO DIA")
    print(f"SALDO INICIAL : R$ {saldo_inicial:,.2f}")
    print(f"ENTRADAS      : R$ {total_entradas:,.2f}")
    print(f"SAÍDAS        : R$ {total_saidas:,.2f}")
    print(f"TOTAL         : R$ {saldo_final:,.2f}")
    
    
def iniciar_sistema():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            exibir_submenu("Entrada")
            
        elif opcao == '2':
            exibir_submenu(" Saída.")
            
        elif opcao == '3':
            exibir_menu_relatorios()
            
        elif opcao == '0':
            print("Finalizando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
carregar_dados()
iniciar_sistema()

