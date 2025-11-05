# Merge Intervals & Insert Interval

## Descrição
Este arquivo contém duas funções para trabalhar com intervalos:

1. **Merge Intervals**: Recebe um array de intervalos e mescla todos os intervalos que se sobrepõem, retornando um array de intervalos não sobrepostos.

2. **Insert Interval**: Insere um novo intervalo em um array de intervalos ordenados e não sobrepostos, mesclando se necessário.

Ambos os algoritmos são comumente usados em problemas de agendamento e compressão de dados.

## Erros Presentes

1. **Erro de Sintaxe (Linha 49)**: Falta ponto e vírgula após incremento
   - **Código incorreto**: `i++`
   - **Código correto**: `i++;`
   - **Tipo**: Erro de sintaxe (tolerado pelo ASI do JavaScript, mas má prática)

2. **Erro de Sintaxe (Linha 61)**: Falta ponto e vírgula após return
   - **Código incorreto**: `return result`
   - **Código correto**: `return result;`
   - **Tipo**: Erro de sintaxe (tolerado pelo ASI do JavaScript, mas má prática)
