
# Guia de Commits - Projeto de Revisão Python

Este guia segue uma convenção de nomes de commit para manter clareza, rastreabilidade e profissionalismo no repositório.

## Formato Geral

```
<tipo>: <descrição curta>
```

Ou, de forma mais detalhada:

```
<tipo>(contexto): <descrição específica>
```

---

## Prefixos recomendados

| Prefixo     | Uso                                         | Exemplo                                      |
|-------------|---------------------------------------------|----------------------------------------------|
| feat        | Nova funcionalidade ou aula                 | feat: adiciona aula 05 sobre listas          |
| fix         | Correção de erro                            | fix: corrige lógica de índice em tupla       |
| chore       | Organização, tarefas sem código executável  | chore: ajusta nomes de pastas                |
| refactor    | Refatoração sem mudar comportamento         | refactor: limpa função de rotação            |
| docs        | Atualizações em README ou anotações         | docs: melhora explicação sobre funções       |
| test        | Inclusão de testes ou verificações manuais  | test: cria função para testar exercícios     |

---

## Exemplos reais no projeto

- feat: adiciona resolução da aula 03 (condicionais)
- fix: corrige bug no loop de soma
- chore: reorganiza estrutura de diretórios
- docs: atualiza README com estrutura de estudos
- refactor: simplifica função de rotação de matriz
- feat(rotacao): resolve matriz 3x3 com lógica baseada em índice
- docs(notebook): adiciona comentários na aula 05

---

## Dicas

- Use verbos no infinitivo: "adiciona", "corrige", "refatora"
- Mantenha as mensagens curtas e objetivas
- Commits diários devem refletir claramente o que foi feito no Bloco 2

