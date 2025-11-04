# Merge Intervals & Insert Interval

## Descrição
Este arquivo contém três funções para trabalhar com intervalos:

1. **merge**: Recebe uma lista de intervalos e mescla todos os intervalos que se sobrepõem, retornando uma lista de intervalos não sobrepostos.

2. **insert**: Insere um novo intervalo em uma lista de intervalos ordenados e não sobrepostos, mesclando se necessário.

3. **erase_overlap_intervals**: Calcula o número mínimo de intervalos que precisam ser removidos para que não haja sobreposições.

Estes algoritmos são comumente usados em problemas de agendamento e compressão de dados.

## Erros Presentes

1. **Erro Lógico Sutil (Linha 88 - função erase_overlap_intervals)**: Comparação incorreta para sobreposição
   - **Código incorreto**: `if intervals[i][0] < end:`
   - **Código correto**: `if intervals[i][0] >= end:` (com lógica invertida) ou ajustar a lógica
   - **Tipo**: Erro lógico sutil - a condição não cobre adequadamente todos os casos de sobreposição
   - **Consequência**: Pode contar incorretamente o número de intervalos a serem removidos em casos específicos
   - **Nota**: Dependendo da definição de sobreposição (se intervalos que se tocam contam como sobrepostos), este pode ou não ser um erro
