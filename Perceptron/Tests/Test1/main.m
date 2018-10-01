variaveis;
%figure; hold on;
%plot(vet1, vet2, 'o');
for i = 1:4
    output = outputx(vet1, vet2, pesos, aux);
    erro = errox(output, classes, aux);
    if erro ~= 0
        pesos = treino(vet1, vet2, pesos, taxaDeAprendizagem, erro, aux);
    end
    aux = aux + 1;
end
%Y = (vet1*pesos(1) + vet2*pesos(2));
%hold off;
