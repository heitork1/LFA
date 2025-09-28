### Contexto: A Definição da Máquina

Primeiro, relembramos a definição da sua Máquina de Mealy:
`M = ⟨Σ, Q, δ, q₀, F, Δ⟩`
onde a função `δ` já combina a transição de estado e a geração de saída:
`δ: Q × Σ → Q × Δ*`

### Definição da Função Estendida (δ̂)

A função estendida, que chamamos de **`δ̂`** (delta chapéu), descreve o comportamento da máquina para uma cadeia de entrada completa. Ela nos diz em qual estado a máquina termina e qual é a cadeia de saída total produzida.

*   **Assinatura:** `δ̂ : Q × Σ* → Q × Δ*`
    *   *Recebe:* Um estado inicial `q` e uma cadeia de entrada `w ∈ Σ*`.
    *   *Retorna:* Um par `(q_final, s_total)`, onde `q_final` é o estado em que a máquina para e `s_total` é a cadeia de saída completa `s_total ∈ Δ*`.

A definição formal é recursiva, dividida em um caso base e um passo indutivo.

---

**1. Caso Base: Cadeia de Entrada Vazia (w = ε)**

Se a entrada é a cadeia vazia, a máquina não realiza nenhuma transição. Ela permanece no estado em que estava e não produz nenhuma saída.

> **δ̂(q, ε) = (q, ε)**

---

**2. Passo Indutivo: Cadeia de Entrada Não Vazia (w = ax)**

Se a entrada `w` pode ser escrita como `ax`, onde `a` é o primeiro símbolo (`a ∈ Σ`) e `x` é o restante da cadeia (`x ∈ Σ*`), o cálculo é feito em duas etapas:

*   **Etapa 1: Processar o primeiro símbolo `a`**
    *   Usamos a função `δ` para determinar o próximo estado e a saída parcial.
    *   Seja `δ(q, a) = (q', s₁)`
        *   `q'` é o estado para onde a máquina vai.
        *   `s₁` é a cadeia de saída gerada nesta primeira transição.

*   **Etapa 2: Processar o resto da cadeia `x`**
    *   Usamos a função estendida `δ̂` recursivamente para processar o resto da cadeia `x`, começando do novo estado `q'`.
    *   Seja `δ̂(q', x) = (q'', s₂)`
        *   `q''` é o estado final após processar `x`.
        *   `s₂` é a cadeia de saída gerada durante o processamento de `x`.

*   **Resultado Final: Combinar os resultados**
    *   O estado final da máquina após processar toda a cadeia `ax` é `q''`.
    *   A saída total é a concatenação da saída da primeira etapa com a saída da segunda etapa (`s₁s₂`).

Formalmente:

> Se `δ(q, a) = (q', s₁)` e `δ̂(q', x) = (q'', s₂)`, então:
> **δ̂(q, ax) = (q'', s₁s₂) **

---

### Resposta Direta (Função Programa Estendida)

Se o seu enunciado pede estritamente a **função programa estendida**, que seria a `λ̂`, ela é definida como a função que extrai apenas a **parte da saída** do resultado de `δ̂`.

> **λ̂(q, w) = s**, onde `δ̂(q, w) = (q', s)` para algum `q' ∈ Q`.

No entanto, como pode ver, o cálculo de `λ̂` depende inteiramente da definição recursiva de `δ̂`, que processa tanto o estado quanto a saída simultaneamente. A definição de `δ̂` é, portanto, a mais completa e fundamental.
