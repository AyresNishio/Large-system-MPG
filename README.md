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
Insere matriz de adjascências da rede Polonesa, os dados gerais desse caso são:
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


