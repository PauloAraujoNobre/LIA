close all; clear all; clc % Limpa tela
variaveis;
Amostras = [classes; x; y];
Amostras = Amostras.';
[tamLinha1, tamCol1] = size(Amostras);
target = Amostras(:,1);
amostras = Amostras;
amostras(:,1) = -1;
pesos = rand(1, tamCol1);
taxaDeAprendizagem = (2*tamLinha1*tamCol1);
taxaDeAprendizagem = 1/taxaDeAprendizagem;
epocas = 0;
for i = 1:(tamCol1-1)
    erro = 1;
    while (erro == 1)
        u = amostras(:,(i+1)) .* pesos;
        if(sum(u) >= 0)
            output = 1;
        else 
            output = -1;
        end
        if(output ~= target(i, 1))
            errox = target(i, 1) - output;
            variacao = taxaDeAprendizagem*errox*amostras(i,2);

        else
            erro = 0;  
        end
        epocas = epocas + 1;
    end
    i = i + 1;
end
disp('O peso vale: ');
disp(pesos);
disp('Qntidade de epocas: ');
disp(epocas);
if(erro == 0)
	disp('Não houve erro');
end

dados = [classes; x; y];
dados = dados.';
[tamLinha2, tamCol2] = size(dados);
dado = dados;
dado(:,1) = -1;
for i = 1:tamCol2
    u = dado(:,(i+1)) .* pesos;
    if(sum(u) >= 0)
        output = 1;
    else
        output = -1;
    end
    i = i + 1;
end
