# Reverse String

## Descrição
Este algoritmo inverte uma string representada como um array de caracteres, fazendo a modificação in-place (sem usar espaço extra). A técnica utilizada é a abordagem de dois ponteiros, onde um ponteiro começa no início e outro no final do array, e eles se movem em direção ao centro trocando os elementos.

## Erros Presentes

1. **Erro Lógico (Linha 14)**: Incremento incorreto do ponteiro direito
   - **Código incorreto**: `right++;`
   - **Código correto**: `right--;`
   - **Tipo**: Erro de lógica que causará um loop infinito, pois ambos os ponteiros se movem na mesma direção
   - **Consequência**: O programa entrará em loop infinito e nunca terminará a execução
