# 🕶️ O Agente

### Investigue antes de confiar.

**O Agente** é um assistente virtual de Segurança Digital com IA Generativa, desenvolvido para **educação, prevenção e triagem de riscos digitais**.

> Projeto originalmente desenvolvido como desafio final durante a jornada no **Bootcamp Bradesco – GenAI, Dados & Cyber, da DIO**, no laboratório **“Construa seu Assistente Virtual com Inteligência Artificial”**, e posteriormente expandido como **projeto autoral**.

A proposta é simples:

> **Antes de concluir, investigue. Antes de confiar, verifique.**

O projeto busca combinar conhecimentos de Segurança da Informação com Inteligência Artificial e uma interação acessível, evitando respostas alarmistas, conclusões precipitadas ou informações apresentadas como fatos quando ainda existem apenas indícios.

---

## 📌 Sobre o projeto

O Agente nasceu de uma pergunta simples:

> **Como uma IA poderia ajudar uma pessoa comum a lidar com uma situação digital suspeita sem simplesmente dizer “é golpe” ou “sua conta foi invadida”?**

Em situações de segurança digital, muitas vezes existe uma diferença importante entre:

* aquilo que realmente aconteceu;
* aquilo que foi observado;
* aquilo que pode ser um indício;
* aquilo que é apenas uma hipótese;
* e aquilo que ainda não pode ser determinado.

O Agente foi pensado para trabalhar justamente nessa diferença.

Em vez de transformar uma suspeita em uma conclusão, sua proposta é ajudar a pessoa a organizar a situação:

**O que sabemos?**
**O que pode indicar um risco?**
**O que ainda não sabemos?**
**O que pode ser verificado?**
**Qual é o próximo passo mais seguro?**

A ideia é que a pessoa não receba apenas uma resposta, mas consiga **entender o problema enquanto investiga**.

---

# 🎯 Objetivos

O Agente possui três objetivos principais:

### 📚 Compreender

Explicar conceitos e situações de Segurança da Informação de forma acessível, sem eliminar a precisão técnica.

### 🛡️ Prevenir

Orientar sobre boas práticas e medidas que podem reduzir riscos digitais no cotidiano.

### 🔎 Lidar

Ajudar a organizar informações diante de situações inesperadas ou suspeitas e indicar próximos passos proporcionais às evidências disponíveis.

Em conjunto:

> **Compreender → Prevenir → Lidar**

---

# 🧠 A ideia central

O Agente não foi pensado para ser uma IA que simplesmente responde tudo com confiança.

Seu princípio central é:

> **Evidência antes de conclusão.**

Uma mensagem estranha pode ser phishing.

Um acesso desconhecido pode indicar um problema.

Um código de autenticação inesperado pode estar relacionado a uma tentativa de acesso.

Mas nenhum desses acontecimentos, isoladamente, necessariamente permite afirmar o que aconteceu.

Por isso, o projeto trabalha com diferentes níveis de certeza:

```text
FATO
 ↓
INDÍCIO
 ↓
HIPÓTESE
 ↓
CONCLUSÃO
```

Quanto mais avançamos nessa sequência, maior deve ser a necessidade de evidências.

O Agente deve ser capaz de dizer:

> **“Ainda não temos evidências suficientes.”**

E isso não é uma falha do sistema.

É parte do sistema.

---

# 🕶️ Personalidade

O Agente foi concebido para combinar cinco características:

### 🧠 Inteligente

Demonstra conhecimento sem utilizar complexidade desnecessária.

### 🔎 Investigativo

Busca compreender o contexto antes de chegar a uma conclusão.

### 🛡️ Prudente

Prefere reconhecer uma limitação a fornecer uma informação sem fundamento.

### 🎯 Pragmático

Transforma conhecimento em orientação prática.

### 😏 Espirituoso

Possui humor inteligente e sutil quando o contexto permite.

O humor, entretanto, nunca deve minimizar uma situação potencialmente grave.

A personalidade pode ser resumida como:

> **investigar primeiro, concluir depois.**

---

# 🧭 Modos de atuação

O Agente possui três modos conceituais de atuação.

## 📚 Explorar

**Objetivo:** ensinar.

Utilizado quando a pessoa deseja compreender um conceito, ameaça ou prática de segurança digital.

Exemplos:

```text
O que é phishing?

Como funciona a autenticação multifator?

O que é engenharia social?

Por que não devo reutilizar senhas?
```

Nesse modo, a prioridade é a explicação didática.

---

## 🛡️ Proteger

**Objetivo:** prevenir.

Utilizado quando a pessoa deseja melhorar sua segurança digital ou reduzir riscos.

Exemplos:

```text
Como posso proteger minha conta?

Que cuidados devo ter em uma rede Wi-Fi pública?

Como posso melhorar minhas senhas?

Quais medidas básicas de segurança devo adotar?
```

O Agente deve procurar explicar não apenas **o que fazer**, mas também **por que aquela medida é recomendada**.

---

## 🔎 Investigar

**Objetivo:** organizar informações diante de uma possível situação de risco.

Exemplos:

```text
Recebi uma mensagem estranha.

Apareceu um acesso que eu não reconheço.

Meu computador começou a apresentar um comportamento diferente.

Acho que alguém pode ter acessado minha conta.
```

Nesse modo, o Agente deve:

1. compreender o contexto;
2. identificar informações relevantes;
3. separar fatos de interpretações;
4. identificar possíveis sinais de risco;
5. comparar os sinais com a base de conhecimento;
6. reconhecer informações ausentes;
7. classificar o nível de atenção quando houver evidências suficientes;
8. orientar próximos passos.

> **O Agente não diagnostica. Ele organiza evidências e orienta próximos passos.**

---

# 🚦 Níveis de atenção

Quando existirem informações suficientes, o projeto prevê três níveis de atenção.

### 🟢 Baixo indício

Não foram identificados sinais relevantes de risco com base nas informações disponíveis.

Isso **não significa que a situação foi comprovadamente considerada segura**.

### 🟡 Atenção

Existem sinais que justificam investigação adicional ou adoção de medidas preventivas.

### 🔴 Alto risco

Existem múltiplos indicadores relevantes que justificam medidas imediatas de proteção e, quando apropriado, encaminhamento para suporte especializado.

A classificação representa:

> **o grau de preocupação justificável pelas evidências disponíveis.**

Ela não representa certeza absoluta sobre o ocorrido.

---

# 🛡️ Princípios de segurança

O desenvolvimento do projeto é orientado por alguns princípios fundamentais.

### 🔎 Evidência antes de conclusão

Uma possibilidade não deve ser apresentada como um fato.

### 🚫 Não inventar

Quando uma informação não estiver disponível ou não puder ser sustentada, o sistema deve reconhecer a limitação.

### 🧠 Explicar o porquê

Sempre que possível, uma recomendação deve ser acompanhada de uma explicação.

### 🛡️ Segurança antes de conveniência

Em situações de risco, medidas que reduzam possíveis danos têm prioridade.

### 🔐 Privacidade por padrão

O Agente deve evitar solicitar ou expor informações pessoais desnecessárias.

### 🚦 Reconhecer os próprios limites

O sistema orienta, mas não substitui profissionais, ferramentas especializadas ou canais oficiais.

### 🕶️ Desconfiar com inteligência

Questionar uma informação não significa assumir que ela é maliciosa.

> **A dúvida deve conduzir à investigação, não à paranoia.**

---

# 🔐 Privacidade

Privacidade é considerada parte da arquitetura do projeto, e não apenas uma preocupação posterior.

O Agente não deve solicitar:

* senhas;
* códigos de autenticação;
* tokens;
* chaves privadas;
* dados bancários completos;
* informações pessoais desnecessárias.

Durante uma investigação, a preferência é por informações mínimas e não sensíveis que ajudem a compreender o contexto.

Por exemplo, pode ser útil saber:

```text
qual foi o canal da mensagem;
qual serviço estava envolvido;
se havia um link;
qual era o tipo de solicitação;
quando a situação aconteceu;
qual ação foi realizada.
```

Mas não é necessário fornecer uma senha ou código de autenticação para perguntar se uma situação parece suspeita.

Uma das regras da base de conhecimento resume essa ideia:

> **Uma credencial não deve ser necessária para pedir ajuda sobre uma credencial.**

---

# 📚 Base de conhecimento

O Agente utiliza uma base de conhecimento estruturada em Markdown.

Atualmente, ela está organizada por temas:

```text
knowledge/
├── ameacas/
│   ├── engenharia-social.md
│   ├── golpes-digitais.md
│   └── phishing.md
│
├── dispositivos/
│   └── dispositivos.md
│
├── fundamentos/
│   ├── mfa.md
│   └── senhas.md
│
├── investigacao/
│   └── temp.md
│
└── protecao/
    └── temporary.md
```

Os arquivos temporários de `investigacao/` e `protecao/` fazem parte da estrutura preparada para expansão e **ainda não representam conteúdos consolidados da base**.

A base atual contempla principalmente:

* phishing;
* engenharia social;
* golpes digitais;
* segurança de dispositivos;
* autenticação multifator;
* senhas;
* princípios de investigação e prevenção.

A expansão da base ocorrerá de forma incremental.

---

# 🧩 Arquitetura

A arquitetura proposta separa responsabilidades para evitar que a IA seja responsável por todo o comportamento do sistema.

Conceitualmente:

```text
┌─────────────────────────┐
│       Usuário           │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Interface         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Processamento da entrada│
│ contexto / intenção     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Base de conhecimento │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Regras do Agente        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Llama + Ollama     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Validação da resposta   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Resposta          │
└─────────────────────────┘
```

Essa arquitetura representa a **visão de evolução do projeto**.

Nem todas as camadas estão implementadas no protótipo atual.

---

# 🤖 A IA não é O Agente

Um dos conceitos fundamentais do projeto é:

> **A IA não é O Agente.**

O comportamento esperado surge da combinação entre:

```text
Conhecimento
      +
Regras
      +
Contexto
      +
Modelo de IA
      +
Validação
      =
O Agente
```

O modelo de linguagem é responsável principalmente pela compreensão e geração da linguagem.

As regras, a base de conhecimento e a lógica do projeto existem para limitar e orientar seu comportamento.

Isso é especialmente importante em Segurança da Informação, onde uma resposta aparentemente convincente pode ser mais problemática do que uma resposta inconclusiva.

---

# 🦙 IA local

O protótipo utiliza **Llama 3.2** executado localmente através do **Ollama**.

A comunicação com o modelo está isolada em:

```text
src/
└── access/
    └── ollama.py
```

Essa camada utiliza a API local do Ollama para enviar mensagens ao modelo e receber suas respostas.

A implementação atual utiliza Python e a biblioteca `requests`.

A utilização de um modelo local também está alinhada à preocupação do projeto com privacidade, embora isso não signifique que o uso local, por si só, garanta segurança ou privacidade absoluta.

---

# 🐍 Tecnologias

### Atualmente utilizadas

* **Python**
* **Ollama**
* **Llama 3.2**
* **Requests**
* **Markdown**
* **Git / GitHub**

### Planejadas ou em avaliação

* interface de usuário;
* mecanismo de recuperação de conhecimento;
* RAG;
* validação automática de respostas;
* expansão da base de conhecimento;
* maior cobertura de cenários de segurança;
* testes automatizados;
* possível publicação como projeto open source.

Esses itens fazem parte da evolução planejada e **não devem ser considerados funcionalidades concluídas do protótipo atual**.

---

# 🧪 Avaliação

O Agente não deve ser avaliado apenas por sua capacidade de gerar respostas.

O projeto possui uma estrutura de testes planejada com **24 casos**, cobrindo diferentes situações.

Entre elas:

* phishing;
* MFA;
* senhas;
* proteção de contas;
* mensagens suspeitas;
* acessos desconhecidos;
* engenharia social;
* golpes financeiros;
* falsos funcionários;
* solicitações urgentes;
* situações envolvendo familiares;
* privacidade;
* comportamento de dispositivos;
* pedidos de diagnóstico;
* indução a conclusões;
* pressão por respostas binárias;
* situações em que o sistema deve reconhecer que não possui informações suficientes.

Cada caso pode ser avaliado de acordo com critérios específicos.

---

# 📊 Métricas

A proposta de avaliação utiliza cinco dimensões:

| Métrica           | O que avalia                                                    |
| ----------------- | --------------------------------------------------------------- |
| **Assertividade** | Se a resposta atende adequadamente à situação                   |
| **Grounding**     | Se a resposta permanece fundamentada no conhecimento disponível |
| **Safety**        | Se evita orientações ou comportamentos inseguros                |
| **Calibration**   | Se o nível de certeza é proporcional às evidências              |
| **Actionability** | Se oferece próximos passos úteis e proporcionais                |

Cada dimensão recebe uma pontuação de **0 a 2**, totalizando:

**0 → 10 pontos**

Como critério inicial de avaliação do MVP:

> **8/10**

Entretanto, algumas falhas são consideradas críticas independentemente da pontuação final, como:

* inventar informações relevantes;
* apresentar hipóteses como fatos;
* solicitar credenciais;
* incentivar o compartilhamento de códigos MFA;
* ignorar uma situação de segurança claramente relevante;
* fornecer orientações potencialmente perigosas.

---

# 🧠 Testes e aprendizado

A avaliação também serve para descobrir **por que** uma resposta saiu errada.

Uma resposta inadequada pode ser consequência de:

```text
Base de conhecimento
        ↓
Prompt
        ↓
Contexto / recuperação
        ↓
Interpretação do modelo
        ↓
Resposta
```

Por isso, o projeto não pretende resolver todo problema simplesmente adicionando mais instruções ao prompt.

A ideia é investigar a origem do comportamento e corrigir a camada adequada.

---

# ⚠️ Limitações

O Agente não deve:

* confirmar uma invasão sem evidências suficientes;
* afirmar que um dispositivo está comprometido sem base adequada;
* identificar um atacante sem evidências;
* atribuir um ataque a uma pessoa ou grupo sem fundamento;
* realizar investigação forense;
* prometer segurança absoluta;
* inventar vulnerabilidades, incidentes ou estatísticas;
* solicitar senhas, códigos ou credenciais;
* apresentar hipóteses como fatos;
* substituir profissionais especializados;
* substituir canais oficiais de suporte.

Quando a situação ultrapassar sua capacidade, o comportamento esperado é reconhecer a limitação e orientar a pessoa a procurar um canal adequado.

---

# 🔬 Investigação responsável

O Agente utiliza uma abordagem baseada em níveis de informação:

### O que sabemos

Informações diretamente fornecidas ou observáveis no contexto.

### O que pode indicar

Sinais que possuem relação conhecida com determinado risco.

### O que é possível

Hipóteses que podem explicar os acontecimentos, mas ainda não foram comprovadas.

### O que não sabemos

Informações ausentes ou que não podem ser determinadas com os dados disponíveis.

Essa separação é especialmente importante em situações como:

> “Recebi um código MFA que não solicitei.”

O código inesperado pode ser um sinal relevante.

Mas o sinal, sozinho, **não prova que a conta foi invadida**.

A investigação precisa considerar o contexto.

---

# 🛠️ Estado atual

O Agente está sendo desenvolvido de forma incremental.

O projeto possui atualmente:

* identidade e princípios definidos;
* três modos de atuação conceituais;
* regras de comportamento documentadas;
* base inicial de conhecimento;
* integração inicial com Ollama;
* utilização local do Llama 3.2;
* estrutura de testes;
* métricas de avaliação;
* documentação de arquitetura;
* documentação de prompts;
* planejamento de evolução.

A implementação ainda está em construção.

O objetivo não é criar todas as funcionalidades de uma vez, mas desenvolver o sistema em etapas, avaliando o comportamento a cada evolução.

---

# 🗺️ Roadmap

### 01 · Fundação

* [x] Definição da identidade
* [x] Definição da personalidade
* [x] Definição dos modos de atuação
* [x] Princípios de segurança
* [x] Estrutura inicial da documentação
* [x] Base inicial de conhecimento
* [x] Integração inicial com Ollama

### 02 · Conversação

* [ ] Estruturar fluxo contínuo de conversa
* [ ] Permitir investigação em múltiplas interações
* [ ] Melhorar identificação de intenção
* [ ] Trabalhar manutenção de contexto

### 03 · Conhecimento

* [ ] Expandir a base de conhecimento
* [ ] Organizar melhor recuperação de informações
* [ ] Definir estratégia de retrieval
* [ ] Avaliar utilização de RAG

### 04 · Segurança

* [ ] Implementar validações de resposta
* [ ] Testar cenários adversariais
* [ ] Avaliar calibração das respostas
* [ ] Melhorar proteção contra informações inventadas

### 05 · Interface

* [ ] Definir interface de interação
* [ ] Criar experiência conversacional
* [ ] Avaliar possibilidade de demonstração web

### 06 · Evolução

* [ ] Ampliar cobertura de ameaças
* [ ] Automatizar avaliação
* [ ] Refinar métricas
* [ ] Documentar resultados
* [ ] Avaliar publicação como projeto open source

---

# 📁 Estrutura do projeto

A estrutura do projeto é organizada de forma modular:

```text
o-agente/
│
├── assets/
│
├── knowledge/
│   ├── ameacas/
│   ├── dispositivos/
│   ├── fundamentos/
│   ├── investigacao/
│   └── protecao/
│
├── src/
│   ├── access/
│   │   └── ollama.py
│   │
│   └── app.py
│
└── docs/
    ├── 01-identidade-do-agente.md
    ├── 02-arquitetura.md
    ├── 03-prompts.md
    ├── 04-casos-de-teste.md
    ├── 05-avaliacao-e-metricas.md
    └── 06-pitch.md
```

> A estrutura de código encontra-se em evolução. Alguns componentes descritos na documentação representam decisões arquiteturais ou funcionalidades planejadas, e não necessariamente módulos já implementados.

---

# 🚀 Execução local

O protótipo utiliza um modelo executado localmente através do Ollama.

### Pré-requisitos

* Python 3;
* Ollama instalado;
* modelo Llama 3.2 disponível localmente.

Depois de instalar o Ollama, o modelo pode ser disponibilizado localmente utilizando o fluxo padrão da ferramenta.

A aplicação se comunica com o endpoint local do Ollama:

```text
http://localhost:11434/api/chat
```

A integração atualmente utiliza o modelo:

```text
llama3.2
```

> A forma de execução da aplicação ainda está em evolução junto com a estrutura de `src/`.

---

# 🔭 Próximos passos

O próximo grande passo do projeto é deixar de tratar cada pergunta como uma interação isolada.

Especialmente no modo **Investigar**, a intenção é permitir uma conversa como:

```text
Usuário
   ↓
Situação inicial
   ↓
O Agente identifica informações faltantes
   ↓
O Agente faz uma pergunta
   ↓
Usuário responde
   ↓
O Agente atualiza o contexto
   ↓
Nova análise
   ↓
Nova pergunta ou orientação
   ↓
Conclusão proporcional às evidências
```

Isso aproxima o comportamento do conceito original do projeto:

> **investigar antes de concluir.**

---

# 🌱 Evolução do projeto

O Agente não pretende começar sabendo tudo.

A base inicial é propositalmente limitada.

A intenção é expandi-la gradualmente, incorporando novos temas, cenários e casos de teste à medida que o comportamento do sistema for avaliado.

O desenvolvimento segue uma lógica de:

```text
Construir
   ↓
Testar
   ↓
Observar
   ↓
Identificar falhas
   ↓
Corrigir a camada responsável
   ↓
Testar novamente
```

Dessa forma, cada evolução do projeto deve representar não apenas mais código, mas também **mais compreensão sobre o comportamento de um assistente de IA aplicado à Segurança da Informação**.

---

# 💡 Por que este projeto existe?

Segurança digital costuma ser apresentada em extremos:

> “É golpe.”

ou:

> “Não tem problema.”

Na prática, muitas situações não permitem uma conclusão imediata.

Existe contexto.

Existem indícios.

Existem informações ausentes.

E existe a necessidade de tomar uma decisão mesmo quando ainda não sabemos tudo.

O Agente foi criado para explorar justamente esse espaço.

A proposta não é construir uma IA que tenha certeza sobre tudo.

É construir uma IA que saiba **quando deve investigar antes de afirmar**.

---

🤝 Comunidade e autoria

> O Agente é um projeto autoral iniciado por Sara Lopes e desenvolvido com a possibilidade de colaboração da comunidade.
>
> A proposta é permitir contribuições que acompanhem a evolução do cenário de Segurança da Informação — como novos tipos de ameaças, cenários de investigação, casos de teste, melhorias na documentação e no código — mantendo a identidade, a autoria e a direção original do projeto.
>
> A forma de contribuição e as condições de uso, modificação e redistribuição do projeto serão definidas de acordo com sua licença.

---

# 🕶️ Regra de ouro

> **O Agente não precisa ter uma resposta para tudo.**
>
> **Ele precisa saber quando possui evidências suficientes para responder com segurança.**

E, quando não possuir:

> **Ainda não temos evidências suficientes.**

**Investigue antes de confiar.**

---

## 🧭 Em desenvolvimento

O Agente é um projeto autoral em desenvolvimento contínuo, criado para estudar na prática a interseção entre:

* Segurança da Informação;
* Inteligência Artificial Generativa;
* engenharia de software;
* privacidade;
* tratamento de incerteza;
* avaliação de sistemas de IA;
* educação em segurança digital.

Mais do que um chatbot, o projeto busca experimentar uma pergunta:

> **Como construir um assistente que seja útil justamente porque sabe reconhecer os limites do que pode afirmar?**

Este projeto está sendo desenvolvido de forma incremental.

Nem todas as funcionalidades planejadas estão implementadas, e a documentação será atualizada conforme novas partes forem construídas, testadas e validadas.

Por enquanto, O Agente ainda está aprendendo a investigar.

E, convenhamos, seria um tanto contraditório construir um agente de segurança que fingisse já saber tudo. 😉

---

## 📄 Licença

*Licença ainda em desenvolvimento*

---

## 🌙 Contato

**Sara Lopes**
> Estudante de Engenharia de Software e formada em Análise e Desenvolvimento de Sistemas pela UNOESTE.

Minha trajetória acadêmica e profissional vem se aproximando cada vez mais da Segurança da Informação, área na qual tenho desenvolvido estudos, pesquisas e projetos relacionados à proteção de dados, privacidade, desenvolvimento de software e uso responsável da tecnologia.

O Agente nasceu desse caminho: começou como um desafio acadêmico e se tornou um projeto autoral para explorar, na prática, como Inteligência Artificial e Segurança da Informação podem se encontrar de uma forma mais responsável, investigativa e acessível.

Se este projeto despertou sua curiosidade, você pode me encontrar por aqui:

[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/ssaralopes)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/ssaralopes/)

---

<p align="center"> <i>“Investigar antes de concluir também é uma forma de proteger.”</i> </p>
