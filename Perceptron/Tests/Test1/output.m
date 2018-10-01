function outputx = outputx(vet1, vet2, pesos, aux)
    outputx = vet1(aux) * pesos(1) + vet2(aux) * pesos(2);
    if outputx > 0
        outputx = 1;
    else
        outputx = 0;
    end
end

