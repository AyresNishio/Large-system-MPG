# Large-system-MPG

Objetivo: Cria plano de medição para sistemas de grande porte.

medplan_gen -> programa principal e notebook para facilitar manipulação.

f-observability -> funções de observabilidade da rede.
f-meas-gen -> funções referentes a geração de planos de medição.

## 28/11/2022: Primeiro Commit. 

Leitura da topologia do sistema de 2224 barras da rede da inglaterra do panda power encontrada pelo Vinicius.

Gerado um plano de medição onde medidas foram distribuidas aleatóriamente pela rede. 
  
  -Primeiramente, foram adicionadas medidas até alcançar uam redundância mínima de 80%. 
  
  -Em seguida, foram adicionadas medidas até o sistema se tornar observável. Teste de observabilidade realizado a cada adição de medida.

O plano contendo 6784 medidas demorou 34 min e 44 seg para ser criado. Teste de observabilidade é a etapa mais onerosa do processo. 

## 06/12/2022: Segundo Commit. 
Insere matriz de adjascências da rede Polonesa com 2383 barras, os dados gerais desse caso são:
  CASE2383WP  Power flow data for Polish system - winter 1999-2000 peak.
   Please see CASEFORMAT for details on the case file format.

   This case represents the Polish 400, 220 and 110 kV networks during
   winter 1999-2000 peak conditions. It is part of the 7500+ bus
   Europen UCTE system. To decrease the number of buses, the tie lines
   to foreign networks were replaced by artificial load or generator
   buses (180-186). Multiple generators at a bus have been aggregated.
   Generators that are not centrally dispatchable in the Polish energy
   market are given a cost of zero.

   This data was graciously provided by, and is distributed with the
   permission of, Roman Korab <roman.korab@polsl.pl>.
   referencia: https://matpower.org/docs/ref/matpower5.0/case2383wp.html

## 06/12/2022: Terceiro Commit. 

Gerado um plano de medição para o sistema Polones

O plano contém 7148 medidas demorou 81 min e 38 seg para ser criado. Ao fim do processo um alerta da biblioteca lin alg apareceu, provavelmente o sistema encontra-se perto da falta de observabilidade. 

## 08/12/2022: Quarto Commit. 

Gerado um plano de medição otimizado para o sistema Polones

O plano contém 5673 medidas. Barras terminaais possuem UMs e restos das medidas foram sorteadas até observabilidade ser alcançada 

## 27/12/2022: Commit plano de medição incial ótimo

Gerado um plano de medição contendo 5846 medidas com 60% de redundância. Utilizando o programa do matlab Top_otimin aloc foi criado um plano inicial ótimo que garante a topologia mímima que garante a observabilidade topológica do sistema. Em sequencia, são adicionadas foram adicionadas medidas até a rede se tornar observável com mais de .6 de redundância

## 04/01/2023: Analise de Criticalidades plano de medição Polones

Construida a matriz de covariância do sistema polones de 5846 medidas, esta matriz mostrou-se pesada para leitura ocupando aproximadamente 800mb.
Realizada analise de Criticalidades via GPU do plano de medição do sistema polones  até k=3. Foram encontradas 12 C1s, 173 C2s e 560 C3s em aproximadamente meia hora. 
Será necessário avaliar 1000 vezes mais combinações para avaliar este plano de medição até k=4. Atravez da extrapolação do tempo requisitado para k=3, pode-se concluir que serão necessários aproximadamente 12 dias para realizar a análise até k=4.