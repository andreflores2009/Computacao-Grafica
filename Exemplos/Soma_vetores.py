def adicionar_vetores(vetor1, vetor2):
    # Verifica se os vetores possuem o mesmo tamanho
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo número de componentes.")
    
    # Realiza a soma dos vetores
    resultado = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]
    return resultado

# Exemplo de uso
vetor_a = [2, 1]
vetor_b = [-3, 3]

resultado = adicionar_vetores(vetor_a, vetor_b)

print(f"A soma dos vetores {vetor_a} e {vetor_b} é: {resultado}")
