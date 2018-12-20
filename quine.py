# -*- coding: utf-8 -*-
# ANDRÉ LUIZ GONÇALVES TEIXEIRA && PEDRO THIAGO ROQUE
# EXEMPLO DE ENTRADA: ABCD+!AB!CD+A!BC!D+ABC!D

table1=[[False,False,False,False, False, False, False, False, False],[True,False,False,False, False, False, False, False, False],[False,True,False,False, False, False, False, False, False],[True,True,False,False, False, False, False, False, False],[False,False,True,False, False, False, False, False, False],[True,False,True,False, False, False, False, False, False],[False,True,True,False, False, False, False, False, False],[True, True, True,False, False, False, False, False, False],[False,False,False,True, False, False, False, False, False],[True,False,False,True, False, False, False, False, False],[False,True,False,True, False, False, False, False, False],[True,True,False,True, False, False, False, False, False],[False,False,True, True, False, False, False, False, False],[True,False,True,True, False, False, False, False, False],[False,True, True, True, False, False, False, False, False],[True, True, True, True, False, False, False, False, False]]
cont=0
flagger=0
for l in range (0, 16) :
        table1[l][4]=not(table1[l][0]) 
        table1[l][5]=not(table1[l][1])     # GERA TABELA DOS INVERSORES
        table1[l][6]=not(table1[l][2])
        table1[l][7]=not(table1[l][3])
table1=table1*1  
entrada=input()
for l in range (0, 16) :
    aux2=entrada
    aux2=aux2.replace("!A", str(int(table1[l][4])))
    aux2=aux2.replace("!B", str(int(table1[l][5])))
    aux2=aux2.replace("!C", str(int(table1[l][6])))
    aux2=aux2.replace("!D", str(int(table1[l][7])))
    aux2=aux2.replace("A", str(int(table1[l][0])))
    aux2=aux2.replace("B", str(int(table1[l][1])))
    aux2=aux2.replace("C", str(int(table1[l][2])))
    aux2=aux2.replace("D", str(int(table1[l][3])))
    cont=aux2.count('+')
    aux2=aux2.split('+')
    flagger=0
    for j in range (0, cont+1) :
        if (flagger==1) :
            break
        if (aux2[j].count('0')!=0) :
            flagger=0
        elif (aux2[j].count('0')==0) :
            flagger=1
    table1[l][8]=flagger
    print(aux2)

aux=[]

grupo0=[]
grupo1=[]
grupo2=[]     # cria listas para os diferentes grupos
grupo3=[]
grupo4=[]
print('A  B  C  D !A !B !C !D  F')  
for l in range (0, 16) :
    for c in range (0,9):
        if (table1[l][c]==1) :
            print('1 ', end = ' ')       # PRINTA TABELA VERDADE PARA 4 VARIÁVEIS
        elif (table1[l][c]==0) :
            print('0 ', end = ' ')
    print()
#auxiliar tem que receber algo diferente
cont=0
for l in range (0, 16) :
    if ((table1[l][8]*1)==1) :
        aux.append(str((table1[l][0]*1)))
        aux[cont]+=str((table1[l][1]*1))
        aux[cont]+=str((table1[l][2]*1))
        aux[cont]+=str((table1[l][3]*1))
        cont+=1

#aux=entrada.split('+')      # GERA UMA LISTA COM OS MINTERMOS DA EXPRESSÃO
cont=entrada.count('+')         
print(aux)        
for c in range (0, cont+1) :
    if (aux[c].count('1') == 0) :
        grupo0.append(aux[c])
    elif (aux[c].count('1') == 1) :
        grupo1.append(aux[c])
    elif (aux[c].count('1') == 2) :           # DEPENDENDO DA QUANTIDDE DE 1'S NOS MINTERMOS ENQUADRA ELE EM UM GRUPO
        grupo2.append(aux[c])
    elif (aux[c].count('1') == 3) :
        grupo3.append(aux[c])
    elif (aux[c].count('1') == 4) :
        grupo4.append(aux[c])

print(aux, entrada.count('+'))
print("Grupo 0: {}\nGrupo 1: {}\nGrupo 2:{}\nGrupo 3: {}\nGrupo 4: {}\n".format(grupo0, grupo1, grupo2, grupo3, grupo4))   # PRINTA OS ELEMENTOS DOS GRUPOS
    
#   //vai percorrer cada um dos 5 grupos de agrupados
#     for(i=0;i<grupo0.size;i++){ // pega cada um do grupo0 e compara com todos os do grupo seguinte
#         for(j=0;j<grupo1.size;j++){
#             if(grupo0[i] for apenas um digito diferente de grupo1[j]){
#                 salva em novo grupo0+1
#                                 grupo1+2, grupo2+3, grupo3+4
#             }
#         }
# }

#COMPARAÇÃO DOS CONJUNTOS - TAL DA PARTE3
grupo01=[]
grupo12=[]
grupo23=[]     # cria listas para os diferentes grupos
grupo34=[]

def achaflips(modelo, palavra):
    i = 0 # Índice na palavra a ser testada
    n = 0 # Número de caracteres do modelo encontrados na palavra testada
    for letra in modelo:
        while i < len(palavra):
            if letra == palavra[i]:
                i += 1
                n += 1
                break
            list1 = list(palavra)
            list1[i] = '-'
            palavra = ''.join(list1)
            #print(palavra)
            i += 1
    if n == len(modelo):
        return modelo
    return palavra

qqq = achaflips(grupo3[0],grupo4[0])
print(qqq)
    # for x in range (0, grupo0.size) :
    #     if (grupo0[x]) :
    #         grupo0.append(aux[c])
