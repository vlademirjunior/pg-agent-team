# Como Contribuir para o AI Database Analyst

Ficamos muito felizes por você ter interesse em contribuir para este projeto! Toda contribuição é bem-vinda, seja ela um reporte de bug, uma sugestão de nova funcionalidade ou uma contribuição de código.

Para garantir um processo tranquilo e uma base de código de alta qualidade, pedimos que siga as diretrizes abaixo.

## Código de Conduta

Este projeto e todos que participam dele são regidos pelo nosso [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, você concorda em seguir os seus termos. Por favor, reporte comportamentos inaceitáveis.

## Como Posso Contribuir?

### Reportando Bugs

Se você encontrar um bug, por favor, siga estes passos:

1. **Verifique as Issues Existentes:** Antes de abrir uma nova issue, verifique se o bug já não foi reportado.
2. **Abra uma Nova Issue:** Se o bug não foi reportado, abra uma nova issue. Certifique-se de incluir um título claro e descritivo.
3. **Seja Detalhado:** No corpo da issue, forneça o máximo de detalhes possível:
    * Passos exatos para reproduzir o bug.
    * O que você esperava que acontecesse.
    * O que de facto aconteceu (incluindo logs de erro e tracebacks).
    * Detalhes do seu ambiente (embora o uso do Dev Container padronize isso, qualquer detalhe adicional é útil).

### Sugerindo Melhorias

1. **Abra uma Nova Issue:** Use um título claro que resuma a sua sugestão (ex: "Sugestão: Adicionar suporte para MySQL").
2. **Explique a Sua Ideia:** Detalhe a sua sugestão e explique por que ela seria útil para o projeto. Inclua exemplos de como a nova funcionalidade seria usada.

### Contribuindo com Código

1. **Faça o Fork do Repositório:** Clique no botão "Fork" no canto superior direito da página do GitHub.
2. **Clone o Seu Fork:** Clone o seu fork para a sua máquina local:

    ```bash
    git clone [https://github.com/SEU-USUARIO/pg-db-analyst-agent.git](https://github.com/SEU-USUARIO/pg-db-analyst-agent.git)
    ```

3. **Crie um Branch:** Crie um novo branch para as suas alterações a partir do branch `main`. Escolha um nome descritivo para o branch (ex: `feat/add-mysql-support` ou `fix/resolve-rag-bug`).

    ```bash
    git checkout -b nome-do-seu-branch
    ```

4. **Configure o Ambiente:** A forma mais recomendada é usar o nosso **Dev Container**. Simplesmente abra o projeto no VS Code e clique em "Reopen in Container". Isto irá configurar todo o ambiente necessário para você.
5. **Faça as Suas Alterações:** Escreva o seu código, seguindo os princípios de Clean Code e a arquitetura existente.
6. **Faça o Commit das Suas Alterações:** Siga as nossas diretrizes de mensagens de commit (veja abaixo).
7. **Faça o Push para o Seu Fork:**

    ```bash
    git push origin nome-do-seu-branch
    ```

8. **Abra um Pull Request (PR):** Vá para o repositório original no GitHub e abra um novo Pull Request.
    * Forneça um título claro e uma descrição detalhada das suas alterações.
    * Se o seu PR corrige uma issue existente, inclua `Closes #123` (substitua `123` pelo número da issue) na descrição do PR.

## Guia de Mensagens de Commit

Para manter o histórico do Git limpo e legível, utilizamos o padrão **Conventional Commits**. As suas mensagens de commit devem seguir este formato.

**Tipos Comuns:**

* **feat:** Uma nova funcionalidade.
* **fix:** Uma correção de bug.
* **docs:** Alterações na documentação.
* **style:** Alterações de formatação que não afetam o significado do código.
* **refactor:** Uma alteração de código que não corrige um bug nem adiciona uma funcionalidade.
* **test:** Adição ou correção de testes.
* **chore:** Alterações no processo de build, ferramentas auxiliares, etc.

**Exemplo:**

```
feat(agent): Adiciona suporte para o modelo Claude 3

Implementa a capacidade de usar os modelos da Anthropic no AgentFactory,
adicionando uma nova opção de configuração e ajustando o processo de
inicialização do cliente.
```

Obrigado mais uma vez pela sua contribuição!

---

# How to Contribute to the AI Database Analyst

We are very happy that you are interested in contributing to this project! All contributions are welcome, whether it's a bug report, a suggestion for a new feature, or a code contribution.

To ensure a smooth process and a high-quality codebase, we ask that you follow the guidelines below.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms. Please report unacceptable behavior.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please follow these steps:

1. **Check Existing Issues:** Before opening a new issue, please check if the bug has already been reported.
2. **Open a New Issue:** If the bug has not been reported, open a new issue. Be sure to include a clear and descriptive title.
3. **Be Detailed:** In the body of the issue, provide as much detail as possible:
    * Exact steps to reproduce the bug.
    * What you expected to happen.
    * What actually happened (including error logs and tracebacks).
    * Details about your environment (although using the Dev Container standardizes this, any additional details are helpful).

### Suggesting Enhancements

1. **Open a New Issue:** Use a clear title that summarizes your suggestion (e.g., "Suggestion: Add support for MySQL").
2. **Explain Your Idea:** Detail your suggestion and explain why it would be useful for the project. Include examples of how the new feature would be used.

### Contributing with Code

1. **Fork the Repository:** Click the "Fork" button in the top-right corner of the GitHub page.
2. **Clone Your Fork:** Clone your fork to your local machine:

    ```bash
    git clone [https://github.com/YOUR-USERNAME/pg-db-analyst-agent.git](https://github.com/YOUR-USERNAME/pg-db-analyst-agent.git)
    ```

3. **Create a Branch:** Create a new branch for your changes from the `main` branch. Choose a descriptive branch name (e.g., `feat/add-mysql-support` or `fix/resolve-rag-bug`).

    ```bash
    git checkout -b your-branch-name
    ```

4. **Set Up the Environment:** The most recommended way is to use our **Dev Container**. Simply open the project in VS Code and click "Reopen in Container". This will set up the entire necessary environment for you.
5. **Make Your Changes:** Write your code, following the principles of Clean Code and the existing architecture.
6. **Commit Your Changes:** Follow our commit message guidelines (see below).
7. **Push to Your Fork:**

    ```bash
    git push origin your-branch-name
    ```

8. **Open a Pull Request (PR):** Go to the original repository on GitHub and open a new Pull Request.
    * Provide a clear title and a detailed description of your changes.
    * If your PR fixes an existing issue, include `Closes #123` (replace `123` with the issue number) in the PR description.

## Commit Message Guide

To keep the Git history clean and readable, we use the **Conventional Commits** standard. Your commit messages should follow this format.

**Common Types:**

* **feat:** A new feature.
* **fix:** A bug fix.
* **docs:** Changes to documentation.
* **style:** Formatting changes that do not affect the meaning of the code.
* **refactor:** A code change that neither fixes a bug nor adds a feature.
* **test:** Adding or correcting tests.
* **chore:** Changes to the build process, auxiliary tools, etc.

**Example:**

```
feat(agent): Add support for the Claude 3 model

Implements the ability to use Anthropic models in the AgentFactory,
adding a new configuration option and adjusting the client
initialization process.
```

Thank you once again for your contribution!
