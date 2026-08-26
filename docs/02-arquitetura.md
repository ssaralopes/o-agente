# 🕶️ O Agente — Arquitetura

> **Investigue antes de confiar.**

## 1. Visão geral

O Agente foi projetado como um assistente virtual de Segurança Digital capaz de compreender necessidades, consultar uma base de conhecimento, aplicar regras de segurança e utilizar Inteligência Artificial Generativa para construir respostas claras e contextualizadas.

A arquitetura foi pensada para separar **conhecimento, regras, processamento e interface**, permitindo que o comportamento do Agente seja controlado sem depender exclusivamente do modelo de linguagem.

O objetivo é que a IA seja responsável principalmente pela compreensão da linguagem e pela construção da resposta, enquanto as regras e a base de conhecimento estabelecem os limites dentro dos quais essa resposta deve ser produzida.

---

## 2. Princípios arquiteturais

A arquitetura do Agente segue os seguintes princípios:

### 🔎 Evidência antes de conclusão

Informações disponíveis na base de conhecimento e fornecidas pela pessoa usuária devem ter prioridade sobre suposições geradas pelo modelo.

### 🛡️ Segurança por padrão

O sistema deve priorizar comportamentos que reduzam riscos, principalmente quando houver informações insuficientes ou situações potencialmente críticas.

### 🔐 Privacidade

Sempre que tecnicamente possível, o processamento deve reduzir a exposição de informações da pessoa usuária a serviços externos.

### 🧠 Separação de responsabilidades

A IA generativa não deve ser responsável sozinha por todas as decisões do sistema.

### 🚦 Transparência

Quando não houver informação suficiente, O Agente deve reconhecer a limitação em vez de preencher lacunas com informações inventadas.

### 🧩 Modularidade

Os componentes devem ser organizados de maneira que possam ser substituídos ou evoluídos individualmente.

---

## 3. Visão conceitual

A arquitetura pode ser representada pelo seguinte fluxo:

```text
                    🕶️ O AGENTE
                         │
                         ▼
                ┌─────────────────┐
                │ Interface       │
                │ de conversa     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Processamento   │
                │ da solicitação  │
                └────────┬────────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
        Identificação  Contexto   Segurança
        da intenção
             │           │           │
             └───────────┼───────────┘
                         ▼
                ┌─────────────────┐
                │ Base de         │
                │ conhecimento    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Regras do       │
                │ Agente          │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Modelo de       │
                │ linguagem       │
                │ Llama / Ollama  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Validação da    │
                │ resposta        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Resposta para   │
                │ pessoa usuária  │
                └─────────────────┘
```

> O fluxo representa a arquitetura funcional do sistema. Ele não representa o processo de raciocínio interno do modelo de linguagem.

---

## 4. Componentes

### 💬 4.1 Interface

É o ponto de contato entre a pessoa usuária e O Agente.

Sua responsabilidade é:

* Receber mensagens;
* Apresentar respostas;
* Manter o contexto da conversa;
* Exibir orientações e níveis de atenção;
* Facilitar a interação.

A interface deve ser simples e priorizar a compreensão da informação.

A implementação poderá utilizar uma aplicação web leve, definida durante a etapa de desenvolvimento.

### 🧭 4.2 Processamento da solicitação

Responsável por organizar a entrada antes que ela seja enviada ao modelo.

Suas funções incluem:

* Identificar o objetivo da solicitação;
* Detectar informações relevantes;
* Determinar o modo de atuação;
* Organizar o contexto disponível;
* Encaminhar a solicitação para os componentes adequados.

Os modos definidos para O Agente são:

* 📚 **Explorar**
* 🛡️ **Proteger**
* 🔎 **Investigar**

### 📚 4.3 Base de conhecimento

A base de conhecimento contém as informações utilizadas pelo Agente para fundamentar suas respostas.

Inicialmente, ela poderá conter conteúdos sobre:

* Phishing;
* Engenharia social;
* Senhas;
* Autenticação multifator;
* Golpes digitais;
* Malware;
* Privacidade;
* Segurança de contas;
* Redes públicas;
* Boas práticas de segurança digital;
* Procedimentos de prevenção e resposta.

A base deverá ser organizada de forma estruturada e legível, permitindo sua expansão sem necessidade de alterar toda a aplicação.

O Agente utilizará a base de conhecimento como fonte prioritária para orientações relacionadas à Segurança Digital. O modelo Llama poderá utilizar conhecimento geral para explicações conceituais e educativas, mas não deverá utilizar esse conhecimento para preencher lacunas, inventar informações ou confirmar situações específicas sem evidências suficientes. Quando a informação disponível não for suficiente, O Agente deverá reconhecer a limitação e orientar a pessoa sobre como obter ou verificar informações adicionais.

### 🛡️ 4.4 Regras do Agente

As regras definem como O Agente deve utilizar o conhecimento disponível.

Entre elas estão:

* Não apresentar hipóteses como fatos;
* Não inventar informações;
* Não solicitar senhas ou credenciais;
* Não confirmar comprometimentos sem evidências;
* Reconhecer limitações;
* Priorizar medidas preventivas;
* Orientar encaminhamento quando necessário;
* Adaptar o tom de acordo com a gravidade da situação.

As regras são complementares ao conhecimento técnico da base.

Enquanto a base responde principalmente:

> **"O que sabemos?"**

As regras respondem:

> **"Como devemos agir com aquilo que sabemos?"**

### 🧠 4.5 Modelo de linguagem

O modelo de linguagem será responsável pela interpretação da linguagem natural e pela construção das respostas.

Como estratégia inicial, será avaliada a utilização de um modelo **Llama** executado localmente por meio do **Ollama**.

A execução local é especialmente relevante para o projeto por estar alinhada ao princípio de privacidade do Agente.

A escolha da versão específica do modelo será realizada durante a etapa de implementação, considerando:

* Recursos disponíveis no ambiente;
* Qualidade das respostas;
* Velocidade;
* Capacidade de seguir instruções;
* Comportamento diante de situações ambíguas.

A escolha do modelo não define a identidade do Agente. O modelo é um componente substituível da arquitetura.

### 📖 4.6 Recuperação de conhecimento

Quando necessário, O Agente poderá buscar informações relevantes na base de conhecimento antes de produzir uma resposta.

Esse mecanismo poderá evoluir para uma estratégia de **RAG (Retrieval-Augmented Generation)**.

A ideia é simples:

```text
Pergunta
   │
   ▼
Buscar informações relevantes
   │
   ▼
Selecionar conhecimento
   │
   ▼
Enviar contexto ao modelo
   │
   ▼
Gerar resposta fundamentada
```

A adoção de RAG será definida após a organização da base de conhecimento e dos primeiros testes.

### 🛡️ 4.7 Validação da resposta

Antes da resposta ser apresentada, o sistema deverá verificar se ela respeita as principais regras de segurança.

Entre os critérios de validação:

* A resposta está fundamentada nas informações disponíveis?
* O Agente apresentou uma hipótese como certeza?
* Foram inventadas informações?
* Foram solicitados dados sensíveis?
* A orientação é coerente com o contexto?
* O nível de atenção apresentado possui justificativa?
* A resposta reconhece limitações quando necessário?

Essa etapa representa uma das principais estratégias de prevenção contra alucinações.

---

## 5. Fluxo de uma interação

Uma interação típica pode seguir o fluxo:

```text
Pessoa usuária
      │
      ▼
"Recebi uma mensagem dizendo que minha conta
será bloqueada se eu não clicar em um link."
      │
      ▼
Identificação da intenção
      │
      ▼
🔎 INVESTIGAR
      │
      ▼
Coleta de contexto
      │
      ▼
Consulta à base de conhecimento
      │
      ▼
Identificação de sinais
      │
      ▼
Aplicação das regras
      │
      ▼
Classificação do nível de atenção
      │
      ▼
Llama / Ollama
      │
      ▼
Validação
      │
      ▼
Resposta
```

O Agente não deve concluir automaticamente que a mensagem é maliciosa apenas porque apresenta características associadas a phishing.

A classificação deve considerar as evidências disponíveis e comunicar incertezas quando elas existirem.

---

## 6. Estratégia contra alucinações

A prevenção contra alucinações não será baseada apenas em uma instrução no prompt.

O projeto pretende utilizar múltiplas camadas:

```text
┌──────────────────────────────┐
│ Base de conhecimento         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Regras e restrições          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Prompt do sistema            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Modelo de linguagem          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Validação da resposta        │
└──────────────┬───────────────┘
               │
               ▼
          Resposta final
```

Essa abordagem busca transformar o princípio de anti-alucinação em uma característica arquitetural testável.

---

## 7. Privacidade

A privacidade será considerada desde a arquitetura.

O protótipo priorizará:

* Não solicitar senhas;
* Não solicitar códigos de autenticação;
* Evitar coleta de dados pessoais desnecessários;
* Trabalhar preferencialmente com informações fornecidas de forma voluntária;
* Avaliar o processamento local do modelo de linguagem;
* Separar dados de demonstração da aplicação;
* Não utilizar dados bancários ou pessoais reais.

O projeto utilizará dados fictícios ou exemplos controlados durante o desenvolvimento.

---

## 8. Tecnologias previstas

A stack inicial considerada para o protótipo é:

| Componente                  | Tecnologia                      |
| --------------------------- | ------------------------------- |
| Linguagem                   | Python                          |
| Modelo de linguagem         | Llama                           |
| Execução local              | Ollama                          |
| Interface                   | A definir                       |
| Base de conhecimento        | Markdown / estrutura organizada |
| Recuperação de conhecimento | A definir                       |
| Versionamento               | Git + GitHub                    |

As tecnologias marcadas como **"A definir"** serão escolhidas após os primeiros testes do projeto.

A arquitetura deve permanecer independente de uma ferramenta específica sempre que possível.

---

## 9. Evolução da arquitetura

A arquitetura será desenvolvida de forma incremental.

### Fase 1 — Fundamentos

* Identidade do Agente;
* Base inicial de conhecimento;
* Regras de comportamento;
* System Prompt;
* Modelo local.

### Fase 2 — Conversação

* Interface;
* Contexto da conversa;
* Identificação dos modos de atuação;
* Integração com Ollama.

### Fase 3 — Conhecimento

* Organização da base;
* Busca de informações relevantes;
* Avaliação da necessidade de RAG.

### Fase 4 — Segurança

* Validação das respostas;
* Testes de alucinação;
* Testes de situações ambíguas;
* Testes de solicitações inadequadas.

### Fase 5 — Avaliação

* Definição das métricas;
* Cenários de teste;
* Comparação dos resultados;
* Identificação de limitações.

---

## 10. Decisões em aberto

Algumas decisões técnicas serão tomadas durante o desenvolvimento, evitando escolhas prematuras:

* Modelo Llama específico;
* Framework da interface;
* Estratégia definitiva de recuperação de conhecimento;
* Necessidade de implementação de RAG;
* Estratégia de validação automática;
* Forma de publicação do protótipo;
* Possível disponibilização de uma versão demonstrativa no GitHub Pages.

Essas decisões serão tomadas com base nos requisitos do projeto, nos recursos disponíveis e nos resultados dos testes.

---

## 11. Princípio arquitetural central

> **A IA não é O Agente.**

O modelo de linguagem é apenas um dos componentes da solução.

O Agente é formado pela combinação de:

**Conhecimento + Regras + Contexto + IA + Validação**

Essa separação permite que o sistema seja mais controlável, explicável e alinhado ao propósito de oferecer orientação de segurança digital sem transformar suposições em certezas.

---

## 12. Resumo

A arquitetura d'O Agente prioriza uma abordagem modular, local e orientada à segurança.

O sistema combina uma base de conhecimento estruturada, regras de comportamento, processamento de contexto, um modelo de linguagem executado localmente e uma camada de validação.

A arquitetura será implementada de forma incremental, permitindo que cada componente seja testado antes da construção da aplicação completa.

> **Investigue antes de confiar.**
