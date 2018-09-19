close all; clear all; clc %#ok<CLALL>
variaveis;
Amostras = dlmread('Amostras.csv');
disp(Amostras);
[tamLinha1, tamCol1] = size(Amostras);
target = Amostras(:,1);
amostras = Amostras;
amostras(:,1) = 0;
pesos = rand(1, tamCol1);
pesos(1) = 0;
taxaDeAprendizagem = (2*tamLinha1*tamCol1);
taxaDeAprendizagem = 1/taxaDeAprendizagem;
epocas = 0;
for i = 1:tamLinha1
    erro = 1;
    while (erro == 1)
        u = amostras .* pesos;
        if(sum(u(i,:)) >= 0)
            output = 1;
        else    
            output = -1;
        end
        if(output ~= target(i, 1))
            errox = target(i, 1) - output;
            variacao = taxaDeAprendizagem*errox*amostras(i,:);
            pesos = pesos + variacao;
        else
            erro = 0;  
        end
        epocas = epocas + 1;
    end
end
disp('O(s) peso(s) vale(m): ');
for k = 1:tamCol1-1
    disp(pesos(k+1));
end
disp('Qntidade de epocas: ');
disp(epocas);
if(erro == 0)
	fprintf('Não houve erro');
end
fprintf('\n\n');
dados = dlmread('Dados.csv');
[tamLinha2, tamCol2] = size(dados);
dado = ones(tamLinha2, tamCol2+1);
dado(:,2:end) = dados;
dado(:,1) = 0;
for i = 1:tamLinha2
    u = dado .* pesos;
    if(sum(u(i,:)) >= 0)
        output = 1;
    else
        output = -1;
    end
    fprintf('resultado %d: ', i);
    disp(output); 
end
fprintf('saidas: \n')
disp(target);
