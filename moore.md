### Contexto: A Definição da Máquina de Moore

A sua definição de Máquina de Moore é `M = ⟨Σ, Q, δ, q₀, F, Δ, δ_S⟩`, onde:
*   `δ: Q × Σ → Q` é a função de transição (leva a um novo estado).
*   `δ_S: Q → Δ*` é a função de saída (associa uma cadeia de saída a cada estado).

A característica principal é que a saída depende **apenas do estado atual**, não da transição.

---

### 1. Função Programa Estendida (δ̂)

Neste contexto, a "Função Programa" refere-se à **função de transição estendida**. Seu objetivo é determinar em qual estado a máquina se encontrará após processar uma cadeia de entrada completa. É a extensão da função `δ` para cadeias.

*   **Assinatura:** `δ̂ : Q × Σ* → Q`
    *   *Recebe:* Um estado de partida `q` e uma cadeia de entrada `w`.
    *   *Retorna:* O estado final `q'` em que a máquina para.

A definição formal é recursiva:

**a) Caso Base (w = ε):** Se a cadeia de entrada é vazia, nenhuma transição ocorre. A máquina permanece no estado em que está.

> **δ̂(q, ε) = q**

**b) Passo Indutivo (w = ax):** Se a cadeia `w` pode ser escrita como `ax` (onde `a` é o primeiro símbolo e `x` é o resto da cadeia), o estado final é encontrado da seguinte forma:
1.  Primeiro, calcula-se o estado intermediário após processar o primeiro símbolo `a` a partir de `q`. Isso é `δ(q, a)`.
2.  Em seguida, calcula-se recursivamente o estado final processando o resto da cadeia `x` a partir desse estado intermediário.

> **δ̂(q, ax) = δ̂(δ(q, a), x)**

---

### 2. Função de Saída Estendida (δ̂_S)

Esta função descreve a **cadeia de saída total** que a Máquina de Moore gera ao processar uma cadeia de entrada. Ela é a extensão da função de saída `δ_S` para cadeias.

*   **Assinatura:** `δ̂_S : Q × Σ* → Δ*`
    *   *Recebe:* Um estado de partida `q` e uma cadeia de entrada `w`.
    *   *Retorna:* A cadeia de saída total `s` que foi produzida.

A definição formal também é recursiva e captura a essência da Máquina de Moore:

**a) Caso Base (w = ε):** Se a cadeia de entrada é vazia, a máquina está no estado `q` e não se move. No entanto, uma Máquina de Moore **sempre produz a saída associada ao seu estado atual**. Portanto, mesmo com entrada vazia, a saída do estado `q` é gerada.

> **δ̂_S(q, ε) = δ_S(q)**

**b) Passo Indutivo (w = ax):** Para uma cadeia não vazia `ax`, a saída total é a concatenação de duas partes:
1.  A saída do estado inicial `q`, que é `δ_S(q)`.
2.  A saída gerada pelo processamento do restante da cadeia `x`, começando do estado para o qual a máquina transita após ler `a` (ou seja, `δ(q, a)`).

> **δ̂_S(q, ax) = δ_S(q) ⋅ δ̂_S(δ(q, a), x)**

*(O símbolo `⋅` representa a concatenação de cadeias)*

### Resumo da Diferença

*   A **função programa estendida (`δ̂`)** rastreia a sequência de **estados**.
*   A **função de saída estendida (`δ̂_S`)** acumula a sequência de **saídas** geradas por cada estado visitado ao longo do caminho.
