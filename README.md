# Large-system-MPG

Objetivo: Cria plano de medição para sistemas de grande porte.

medplan_gen -> programa principal e notebook para facilitar manipulação.

f-observability -> funções de observabilidade da rede.
f-meas-gen -> funções referentes a geração de planos de medição.

## 12/11/2022: Primeiro Commit. 

Leitura da topologia do sistema de 2224 barras da rede da inglaterra do panda power encontrada pelo Vinicius.

Gerado um plano de medição onde medidas foram distribuidas aleatóriamente pela rede. 
  
  -Primeiramente, foram adicionadas medidas até alcançar uam redundância mínima de 80%. 
  
  -Em seguida, foram adicionadas medidas até o sistema se tornar observável. Teste de observabilidade realizado a cada adição de medida.

O plano contendo 6784 medidas demorou 34 min e 44 seg para ser criado. Teste de observabilidade é a etapa mais onerosa do processo. 
