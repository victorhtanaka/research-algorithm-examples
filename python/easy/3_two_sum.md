# Two Sum

## Descrição
Este algoritmo resolve o problema clássico "Two Sum" do LeetCode. Dado um array de números inteiros e um valor target, o algoritmo deve encontrar dois números no array que somados resultem no target, retornando os índices desses números.

A solução utiliza um dicionário (HashMap) para armazenar os números já visitados e seus índices, permitindo uma solução em O(n) de complexidade temporal e O(n) de complexidade espacial.

## Erros Presentes

### Erro 1: Operação Matemática Incorreta (Linha 8)
**Problema:** O complemento está sendo calculado com adição (`target + nums[i]`) ao invés de subtração.

**Código Incorreto:**
```python
complement = target + nums[i]
```

**Código Correto:**
```python
complement = target - nums[i]
```

**Impacto:** Este erro faz com que o algoritmo procure pelo número errado no dicionário. Em vez de buscar o valor que, somado ao número atual, resulta no target, ele busca um valor que não tem relação matemática correta com a solução esperada.

**Exemplo:** Para `nums = [2, 7, 11, 15]` e `target = 9`:
- O complemento de 2 deveria ser 7 (9 - 2 = 7)
- Mas o código calcula 11 (9 + 2 = 11), procurando o valor errado

### Erro 2: Ordem Invertida dos Índices (Linha 11)
**Problema:** Os índices estão sendo retornados em ordem invertida: `[i, num_map[complement]]` ao invés de `[num_map[complement], i]`.

**Código Incorreto:**
```python
return [i, num_map[complement]]
```

**Código Correto:**
```python
return [num_map[complement], i]
```

**Impacto:** Mesmo que o algoritmo encontre os números corretos, ele retorna os índices na ordem errada. O problema Two Sum espera que os índices sejam retornados em ordem crescente (primeiro o menor índice, depois o maior). Como `num_map[complement]` sempre contém um índice de uma iteração anterior, ele é menor que `i`, e deveria vir primeiro no array de retorno.

**Exemplo:** Para `nums = [2, 7]` e `target = 9`:
- O correto seria retornar `[0, 1]`
- Mas o código retorna `[1, 0]`

