function pesos = treino(vet1, vet2, pesos, taxaDeAprendizagem, erro, aux)
    pesos(1) = pesos(1) + (taxaDeAprendizagem * erro * vet1(aux));
    pesos(2) = pesos(2) + (taxaDeAprendizagem * erro * vet2(aux));
end

