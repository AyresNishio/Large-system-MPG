%Conexao= readtable('Rede_Polonia.txt');
Conexao= dlmread('ieee-300-bus.txt');
[taml,tamc]=size(Conexao);
for i=1:tamc
    Conexao(i,i) = 1;
end
b=ones(tamc,1);
f=ones(tamc,1);
b=b*-1;
Conexao=Conexao*-1;
intcon=(1:tamc);
lb=zeros(tamc,1);
ub=ones(tamc,1);
y=intlinprog(f,intcon,Conexao,b,[],[],lb,ub);


for i=1:tamc
   y(i)=y(i)*i;
end
barras_alocadas = nonzeros(y);
dlmwrite('Initial_meas_plan.txt',barras_alocadas);