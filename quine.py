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
grupoOrg=[]
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
grupoOrg = aux      
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
    traco='-'
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
            break
            
    if n == len(modelo):
        return " "
    if(palavra.count(traco)>0 and palavra.count(traco)< 2):
        return palavra
    return " "

#qqq = achaflips(grupo2[0],grupo3[0])
#print(qqq)
grupoSimp=[]
for x in range (0, len(grupo0)) : #grupo 01
    for y in range (0, len(grupo1)) :
        qqq = achaflips(grupo0[x],grupo1[y])
        if(qqq != " "):
            grupo01.append(qqq)
            grupoSimp.append(qqq)
            #print(grupo01[x])

for x in range (0, len(grupo1)) : #GRUPO 12
    for y in range (0, len(grupo2)) :
        qqq = achaflips(grupo1[x],grupo2[y])
        if(qqq != " "):
            grupo12.append(qqq)
            grupoSimp.append(qqq)
            #print(grupo12[x])

for x in range (0, len(grupo2)) :
    for y in range (0, len(grupo3)) :
        qqq = achaflips(grupo2[x],grupo3[y])
        if(qqq != " "):
            grupo23.append(qqq)
            grupoSimp.append(qqq)
            #print(grupo23[x])

for x in range (0, len(grupo3)) :
    for y in range (0, len(grupo4)) :
        qqq = achaflips(grupo3[x],grupo4[y])
        if(qqq != " "):
            grupo34.append(qqq)
            grupoSimp.append(qqq)
            #print(grupo34[x])

print("Grupo 01: {}\nGrupo 12: {}\nGrupo 23:{}\nGrupo 34: {}\n".format(grupo01, grupo12, grupo23, grupo34))   # PRINTA OS ELEMENTOS DOS GRUPOS


print("Grupo org: {}".format(grupoOrg))
print("Grupo Simp: {}".format(grupoSimp))
grupoFinal=[]
grupoFF=[]
for x in range (0, len(grupoSimp)) :
    for y in range (0, len(grupoOrg)) :
        qqq = achaflips(grupoSimp[x],grupoOrg[y])
        if(qqq != " "):
            grupoFinal.append(qqq)

grupoFF = sorted(set(grupoFinal))
print("Grupo Final: {}".format(grupoFF))

def transf(modelo):
    qqq=""

    if(modelo[0]== "1"):
        qqq+=str("A")
    elif(modelo[0]== "0"):
         qqq+=str("!A")
    elif(modelo[0]== "-"):
         qqq+=str("")

    if(modelo[1]== "1"):
        qqq+=str("B")
    elif(modelo[1]== "0"):
         qqq+=str("!B")
    elif(modelo[1]== "-"):
         qqq+=str("")

    if(modelo[2]== "1"):
        qqq+=str("C")
    elif(modelo[2]== "0"):
         qqq+=str("!C")
    elif(modelo[2]== "-"):
         qqq+=str("")

    if(modelo[3]== "1"):
        qqq+=str("D")
    elif(modelo[3]== "0"):
         qqq+=str("!D")
    elif(modelo[3]== "-"):
         qqq+=str("")

    return qqq

treta=""

treta += transf(grupoFF[0])
for x in range (1, len(grupoFF)) :
    treta += "+ " + transf(grupoFF[x])
        #treta = table1[1][1]*1
print(treta)
        #str((table1[l][0]*1)