import time
import sys
#esses label serao usados no lugar da função do goto da linguagem em c para retornar para o inicio assim q as perguntas acabarem
label = "carregar"
while label: 
    if label == "fim":
        label = "inicio"
    elif label == "carregar":
#um menu para escolher a pergunta de 1 milhão de reais em barras de ouro pq valem mais do q dinheiro hehe
        print("inicializando programa....")
        print("", end="")
        for i in range(101):
            #sys write para substituir o q ta escrito no ultimo print
            sys.stdout.write(f"{i}%")
            #flush para apagar o q foi escrito
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\r")
            #write para manter (usando o \r) na mesma linha a proxima palavra
        print("\n"*130)
        print("progama iniciado com sucesso!")
        label = "inicio"
    elif label == "inicio":
        escolha = int(input("\n1. programação estruturada" "\n2. programção orientada a objeto" "\n3. codigo fonte" "\n4. codigo objeto""\n5. codigo executavel""\n6. compilador""\n7. finalizar sistema""\nescolha entre as opções acima:"))
# variaveis auxiliares para serem usada no final coloque o tanto de aux igual ao numero de peguntas se for 5 perguntas ent serao 5 auxs
        aux = int
        aux2 = int
        aux3 = int
    #if para grantir q ngm vai bancar o espertinho
        if escolha==0 or escolha >=8:
         print("\nnumero invalido")
        elif escolha==1:
    #a primeira pergunta os seu modelo servira de base para todas as outras desde o int() ate o aux=0
            resp1QA = int(input("Qual é o principal objetivo da programação estruturada? \n1. Facilitar a criação de interfaces gráficas avançadas. \n2. Melhorar a legibilidade e a manutenção do código através de uma estrutura clara. \n3. Aumentar a velocidade de execução do código ao máximo possível. \n4. Permitir a programação em múltiplas linguagens simultaneamente" "\ndigite a resposta da primeira:"))
            if resp1QA== 2:
                print("\nvoce acertou!")
                aux=1
            else: 
                print("\nvoce errou!")
                aux=0 
#as perguntas podem ser estrturadas tanto na forma de cima quanto na de baixo fica a gosto do fregues        
            resp2QA = int(input("Qual das seguintes estruturas de controle é utilizada para repetir um bloco de código várias vezes na programação estruturada?\n1. Estrutura Condicional\n2. Estrutura de Repetição\n3. Estrutura de Seleção\n4. Estrutura de Exceção" "\ndigite a resposta da segunda:"))
            if resp2QA== 2:
                print("\nvoce acertou!")
                aux2=1
            else: 
                print("\nvoce errou!")
                aux2=0
            resp3QA = int(input("Em programação estruturada, qual é a função dos subprogramas (ou funções)?\n1. Armazenar dados de forma permanente no disco.\n2. Dividir um programa em blocos menores e reutilizáveis, facilitando a manutenção e a compreensão.\n3. Gerar gráficos e visualizações de dados.\n4. Criar e gerenciar bancos de dados relacionais.\ndigite a resposta da terceira:"))
            if resp3QA== 2:
                print("\nvoce acertou!")
                aux3=1
            else: 
                print("\nvoce errou!")
                aux3=0
    #as variaveis aux agr tem a função de contabilizar o tanto tanto de questoes acertadas quant mais questoes mais variaveis aux terao
            total = int(aux3)+int(aux)+int(aux2)
#as variaveis aux receberam um valo 0 para o erro e 1 para os acertos agora é so somar em uma nova variavel chamada total
            print(f"\nvoce acertou:{total} pergunta(s)")
#imprimir o numero de questoes acertadas e restar os valores das variaveis aux para zero para poderem ser usadas nas proximas perguntas do outro tema 
        label="fim"
#se lembra dos label do inicio? é aki q  eles agem apos a primeira rodada de questoes ele vai voltar la pro inicio

#e aki termina o codigo dps disso so copiar desde o resp1QA e repetir ate chegar no tema 6 e caso a pessoa escolha o "tema" 7 apenas faça um print("programa encerrado") caso queira pode melhorar as funções 
        if escolha==2:
            resp1QB = int(input("Questão 1: Conceitos Básicos Qual das seguintes afirmações é verdadeira sobre a herança na programação orientada a objetos?\n 1. A herança permite que uma classe herde métodos e atributos de uma classe que não está relacionada a ela.\n 2. A herança permite que uma classe herde métodos e atributos de uma classe base, também conhecida como classe pai.\n 3. A herança impede que uma classe base tenha atributos ou métodos próprios.\n 4. A herança é usada exclusivamente para criar interfaces entre classes.""\ndigite a resposta da primeira:"))
            if resp1QB==2:
             print("\nvoce acertou!")
             aux=1
            else:
             print("\nvoce errou!")
             aux=0
            resp2QB = int(input("Qual é a principal vantagem do encapsulamento em programação orientada a objetos?\n 1. Permitir que todas as variáveis e métodos sejam acessíveis de qualquer parte do código.\n 2. Proteger os dados internos de uma classe, expondo apenas uma interface pública controlada.\n 3. Garantir que os métodos de uma classe não possam ser sobrescritos por subclasses.\n 4. Facilitar a herança múltipla em linguagens que a suportam.""\ndigite a resposta da segunda:"))
    
            if resp2QB==2:
             print("\nvoce acertou!")
             aux2=1
            else:
             print("\nvoce errou!")
             aux2=0
 #aki ta sem pergunta ent quando voce colocar a pegunta dentro das aspas do input n esqueça de mudar o valor 0 do if resp3QB== 0 la embaixo        
            resp3QB = int(input("Pergunta: Qual dos seguintes conceitos não é um princípio fundamental da programação orientada a objetos (POO)?\n1. Encapsulamento\n2. Herança\n3. Polimorfismo\n4. Compilação""\ndigite a resposta da terceira:")) 
     #esse aki:
            if resp3QB==4:
             print("\nvoce acertou!")
             aux3=1
            else:
             print("\nvoce errou!")
             aux3=0
             total = int(aux3)+int(aux)+int(aux2)

             print(f"\nvoce acertou:{total}/3 pergunta(s)")
            label="fim"  
        if escolha==3:
            resp1QB = int(input("\nQual das seguintes práticas é recomendada para escrever código-fonte limpo? \n1. Usar nomes de variáveis genéricos\n2. Comentários excessivos em cada linha\n3. Manter funções pequenas e focadas\n4. Evitar a refatoração do código\ndigite a resposta da primeira:"))
            if resp1QB==3:
             print("\nvoce acertou!")
             aux=1
            else:
             print("\nvoce errou!")
             aux=0
            resp2QB = int(input("\nQual é o propósito principal dos comentários no código-fonte?\n1. Aumentar o tempo de compilação\n2. Melhorar a legibilidade e a manutenção\n3. Substituir a documentação técnica\n4. Esconder erros de sintaxe\ndigite a resposta da segunda:"))
            if resp2QB==2:
             print("\nvoce acertou!")
             aux2=1
            else:
             print("\nvoce errou!")
             aux2=0
            resp3QB = int(input("\nO que é um bug no contexto de desenvolvimento de software?\n1. Uma atualização de software\n2. Um erro ou falha no código-fonte\n3. Uma nova funcionalidade\n4. Um tipo de teste de unidade\ndigite a resposta da terceira:")) 
            if resp3QB==2:
             print("\nvoce acertou!")
             aux3=1
            else:
             print("\nvoce errou!")
             aux3=0
             total = int(aux3)+int(aux)+int(aux2)
             print(f"\nvoce acertou:{total}/3 pergunta(s)")
             label="fim"
        if escolha==4:
            resp1QB = int(input("\nO que é um código objeto?\n1. O código-fonte escrito em uma linguagem de programação de alto nível\n2. O código resultante após a compilação do código-fonte, antes da vinculação\n3. Um documento de design do sistema\n4. Um código usado apenas para fins de depuração\ndigite a resposta da primeira:"))
            if resp1QB==2:
             print("\nvoce acertou!")
             aux=1
            else:
             print("\nvoce errou!")
             aux=0
            resp2QB = int(input("\nQual é o papel do código objeto no processo de compilação?\n1. Ele é a versão final do programa executável\n2. Ele é utilizado para otimizar a execução do código em tempo de execução\n3. Ele serve como uma representação intermediária que ainda precisa ser vinculada para formar o executável\n4. Ele substitui o código-fonte durante a compilação\ndigite a resposta da segunda:"))
            if resp2QB==3:
             print("\nvoce acertou!")
             aux2=1
            else:
             print("\nvoce errou!")
             aux2=0
            resp3QB = int(input("\nQual dos seguintes arquivos geralmente contém código objeto?\n1. .png\n2. .obg\n3. .obj\n4. .ogg\ndigite a resposta da terceira:")) 
            if resp3QB==3:
             print("\nvoce acertou!")
             aux3=1
            else:
             print("\nvoce errou!")
             aux3=0
             total = int(aux3)+int(aux)+int(aux2)
             print(f"\nvoce acertou:{total}/3 pergunta(s)")
            label="fim"
        if escolha==5:
            resp1QB = int(input("\nO que é um código executável?\n1. O código-fonte que foi escrito em uma linguagem de programação de alto nível\n2. O código resultante após a compilação, pronto para ser executado pelo sistema operacional\n3. Um arquivo de texto contendo documentação sobre o software\n4. Um código intermediário que precisa ser convertido para código objeto\ndigite a resposta da primeira:"))
            if resp1QB==2:
             print("\nvoce acertou!")
             aux=1
            else:
             print("\nvoce errou!")
             aux=0
            resp2QB = int(input("\nQual é a principal função de um código executável?\n1. Armazenar dados temporários durante a execução de um programa\n2. Fornecer instruções que o processador pode executar diretamente\n3. Gerar código-fonte a partir de um arquivo objeto\n4. Facilitar a edição do código-fonte\ndigite a resposta da segunda:"))
            if resp2QB==2:
             print("\nvoce acertou!")
             aux2=1
            else:
             print("\nvoce errou!")
             aux2=0
            resp3QB = int(input("\nQual extensão de arquivo é comumente associada a arquivos executáveis em sistemas Windows?\n1. .c\n2. .exe\n3. .dll\n4. .bin\ndigite a resposta da terceira:")) 
            if resp3QB==2:
             print("\nvoce acertou!")
             aux3=1
            else:
             print("\nvoce errou!")
             aux3=0
             total = int(aux3)+int(aux)+int(aux2)

             print(f"\nvoce acertou:{total}/3 pergunta(s)")
            label="fim"
        if escolha==6:
            resp1QB = int(input("\nO que é um compilador?\n1. Um programa que interpreta e executa o código-fonte linha por linha\n2. Um software que traduz código-fonte de uma linguagem de programação para código objeto\n3. Um tipo de banco de dados para armazenar código-fonte\n4. Um editor de texto para escrever código-fonte\ndigite a resposta da primeira:"))
            if resp1QB==2:
             print("\nvoce acertou!")
             aux=1
            else:
             print("\nvoce errou!")
             aux=0
            resp2QB = int(input("\nQual das seguintes etapas faz parte do processo de compilação?\n1. Análise léxica do código-fonte\n2. Execução direta do código-fonte\n3. Conversão de código objeto em código-fonte\n4. Otimização do sistema operacional\ndigite a resposta da segunda:"))
            if resp2QB==1:
             print("\nvoce acertou!")
             aux2=1
            else:
             print("\nvoce errou!")
             aux2=0
            resp3QB = int(input("\nO que é a etapa de vinculação (linkagem) no processo de compilação?\n1. A conversão de código-fonte em código executável\n2. A combinação de código objeto e bibliotecas para criar um executável\n3. A execução de código-fonte em um ambiente de desenvolvimento\n4. A verificação de erros de sintaxe no código-fonte\ndigite a resposta da terceira:"))      
            if resp3QB==2:
             print("\nvoce acertou!")
             aux3=1
            else:
             print("\nvoce errou!")
             aux3=0
             total = int(aux3)+int(aux)+int(aux2)

             print(f"\nvoce acertou:{total}/3 pergunta(s)")
            label="fim"
        aux=0
        aux2=0
        aux3=0
        if escolha == 7:
            #caso a pessoa ecolha 7 vamos finalizar o programa
            print("Finalizando programa")
        print("····················", end="")
        for i in range(1, 21):
        # Adiciona pontos e usa \r para sobrescrever a linha
            sys.stdout.write("*" * i)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r")  # Retorna ao início da linha
          # Nova linha após a conclusão
#time.sleep para podermos dar um charme e fecharmos com um delay
        print("\n" * 130)
         #como o python n possue um comando q limpe o terminal vamos usar o print para empurrar toda a informação para longe dos olhos dos curiosos
        print("\nPrograma finalizado.")
            #time.sleep para podermos dar um charme e fecharmos com um delay
        label="fim"
           
