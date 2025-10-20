## Tarefas restantes

---

 **1. Conectar o front ao backend**

- Fazer o JavaScript do frontend buscar as perguntas diretamente da API usando uma requisição GET para `/api/perguntas/<nivel>/`.
- Recomenda-se criar um arquivo JS para cada página de nível (ex: `facil.html`, `medio.html`, `dificil.html`).

---

 **2. Exibir perguntas no HTML**

- Renderizar dinamicamente no HTML as perguntas e alternativas que vêm da API, mantendo o layout já existente.
- Cada pergunta deve aparecer na estrutura prevista no template, sem modificar o design base.

---

**3. Lógica de pontuação**

- Implementar no JavaScript a verificação da resposta escolhida pelo usuário:
  - Checar se ela corresponde à resposta correta enviada pela API.
  - Somar os pontos conforme o nível (ex: fácil = 10, médio = 20, difícil = 30).
- Exibir a pontuação atual no rodapé, usando o elemento `.pontos-atuais`.

---

 **4. Enviar resultado para o backend**

- Quando o usuário finalizar o quiz, enviar uma requisição POST para `/api/resultado/` com a pontuação total.
- Até o login estar implementado, usar um “usuário genérico” ou campo temporário.

---

 **5. Ajustar depois da autenticação**

- Assim que Ju e Isa finalizarem o sistema de login:
  - O campo de usuário no resultado deve ser preenchido automaticamente pelo backend, usando o token JWT.
  - O JavaScript do frontend só precisa enviar o token de autenticação no cabeçalho da requisição.

---

**6. Testes e revisão**

- Testar o fluxo completo nos três níveis do quiz (fácil, médio, difícil):
  - Carregar perguntas → responder → somar pontos → enviar resultado.
- Garantir que todas as etapas funcionam corretamente e revisar possíveis melhorias.

---
