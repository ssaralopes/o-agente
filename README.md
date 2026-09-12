# 🕶️ O Agente

### Investigue antes de confiar.

**O Agente** é um assistente virtual de Segurança Digital com **IA Generativa**, desenvolvido para **educação, prevenção e triagem de riscos digitais**.

> Projeto originalmente desenvolvido como desafio final durante a jornada no **Bootcamp Bradesco – GenAI, Dados & Cyber, da DIO**, a partir do laboratório **“Construa seu Assistente Virtual com Inteligência Artificial”**, e posteriormente expandido como **projeto autoral**.

A proposta é simples:

> **Antes de concluir, investigue. Antes de confiar, verifique.**

O projeto busca combinar conhecimentos de **Segurança da Informação** com uma interação simples e acessível, evitando respostas alarmistas, conclusões precipitadas ou recomendações baseadas em informações que não possam ser sustentadas.

---

## 📌 Sobre o projeto

O Agente nasceu da ideia de criar um assistente que não trate toda situação suspeita como um ataque confirmado — mas também não ignore sinais importantes.

Em vez de simplesmente responder *“isso é um golpe”* ou *“sua conta foi invadida”*, O Agente deve ajudar a organizar o problema:

* O que sabemos?
* O que é apenas um indício?
* O que ainda precisa ser verificado?
* Qual é o próximo passo mais seguro?

A proposta é que a pessoa consiga **entender o problema enquanto investiga**, e não apenas receber uma resposta pronta.

---

## 🚧 Estado atual

> **Protótipo funcional em desenvolvimento.**

O Agente já possui uma estrutura inicial funcional, capaz de:

* receber uma pergunta da pessoa usuária;
* identificar a intenção da pergunta;
* carregar informações de uma Base de Conhecimento local;
* montar um contexto para o modelo;
* enviar esse contexto para um modelo de linguagem local;
* gerar uma resposta seguindo as regras definidas para O Agente.

Neste estágio, o projeto ainda está em construção. Algumas funcionalidades já funcionam, enquanto outras estão sendo desenvolvidas e refinadas.

A Base de Conhecimento, por exemplo, ainda está sendo formada e será ampliada gradualmente conforme o projeto evoluir.

---

## 🧠 Como O Agente pensa

O comportamento do projeto é baseado em alguns princípios fundamentais.

### 🔎 Evidência antes da conclusão

O Agente deve diferenciar:

**Fato → Indício → Hipótese → Conclusão**

Uma situação suspeita não deve automaticamente ser tratada como um incidente confirmado.

### 🛡️ Segurança antes da conveniência

Quando houver conflito entre facilitar uma ação e preservar a segurança da pessoa usuária, a segurança deve ser priorizada.

### 🔐 Privacidade por padrão

O Agente não deve solicitar informações desnecessárias ou sensíveis.

Nunca deve solicitar, por exemplo:

* senhas;
* códigos MFA;
* tokens;
* chaves privadas;
* dados bancários completos;
* outras credenciais que possam comprometer a segurança da pessoa.

### 📚 Não inventar

Quando não houver informações suficientes, O Agente deve reconhecer essa limitação.

Ele não deve inventar:

* fontes;
* vulnerabilidades;
* estatísticas;
* acontecimentos;
* evidências;
* conclusões sobre um possível ataque.

### 🧩 Reconhecer seus próprios limites

O Agente não precisa ter uma resposta para tudo.

Ele precisa saber **quando ainda não existem evidências suficientes para responder com segurança**.

---

## 🎯 Modos de atuação

O projeto possui três modos principais.

### 📚 Explorar

Voltado para aprendizado e compreensão de conceitos.

Exemplos:

* O que é phishing?
* O que é MFA?
* Como funciona uma senha segura?
* O que é engenharia social?

---

### 🛡️ Proteger

Voltado para prevenção e orientação prática.

Exemplos:

* Como proteger minha conta?
* Como configurar MFA?
* O que posso fazer para melhorar minha segurança?
* Como reduzir os riscos de um dispositivo?

---

### 🔎 Investigar

Voltado para situações suspeitas.

Nesse modo, O Agente deve organizar informações, identificar indícios e orientar a pessoa sobre quais informações podem ajudar a compreender melhor a situação.

Exemplo:

> "Recebi uma mensagem estranha e não sei se é golpe."

Em vez de concluir imediatamente que se trata de um golpe, O Agente pode buscar informações como:

* por qual canal a mensagem chegou;
* quem aparentemente enviou;
* qual era o conteúdo;
* se havia links ou anexos;
* se alguma ação já foi realizada;
* quais outros sinais podem ser relevantes.

A intenção é transformar uma situação confusa em uma investigação organizada.

---

## 🚦 Níveis de atenção

O projeto também trabalha com níveis de atenção:

| NívelSignificado     |                                                                  |
| -------------------- | ---------------------------------------------------------------- |
| 🟢 **Baixo indício** | Poucos elementos indicam um problema                             |
| 🟡 **Atenção**       | Existem sinais que merecem verificação                           |
| 🔴 **Alto risco**    | Existem diversos indícios relevantes que exigem atenção imediata |

Esses níveis representam o **grau de preocupação justificável pelas informações disponíveis**, e não uma confirmação automática de que um incidente aconteceu.

---

## 🏗️ Arquitetura atual

Neste primeiro estágio, a aplicação possui uma arquitetura simples:

```text
Pessoa usuária
      │
      ▼
    app.py
      │
      ├───────────────┐
      ▼               ▼
Identificação     Base de
  de intenção     Conhecimento
      │               │
      └───────┬───────┘
              ▼
            Prompt
              │
              ▼
          Ollama
              │
              ▼
          Llama 3.2
              │
              ▼
           Resposta

```

A simplicidade é intencional.

O objetivo atual é construir e compreender cada parte do sistema antes de adicionar camadas mais complexas.

---

## 📁 Estrutura do projeto

```text
o-agente/
│
├── docs/
│   ├── 01-identidade-do-agente.md
│   ├── 02-arquitetura.md
│   ├── 03-prompts.md
│   ├── 04-casos-de-teste.md
│   ├── 05-avaliacao-e-metricas.md
│   └── 06-pitch.md
│
├── knowledge/
│   ├── ameacas/
│   │   ├── engenharia-social.md
│   │   ├── golpes-digitais.md
│   │   └── phishing.md
│   │
│   ├── dispositivos/
│   │   └── dispositivos.md
│   │
│   ├── fundamentos/
│   │   ├── mfa.md
│   │   └── senhas.md
│   │
│   ├── investigacao/
│   │   └── temp.md
│   │
│   └── protecao/
│       └── temporary.md
│
├── src/
│   ├── app.py
│   │
│   ├── access/
│   │   ├── ollama.py
│   │   └── knowledge.py
│   │
│   └── core/
│       └── intent.py
│
└── README.md

```

A estrutura pode mudar conforme novas funcionalidades forem incorporadas.

---

## 📚 Base de Conhecimento

A Base de Conhecimento contém informações utilizadas como contexto para as respostas do modelo.

Atualmente, ela possui conteúdos relacionados a:

* phishing;
* golpes digitais;
* engenharia social;
* dispositivos;
* MFA;
* senhas.

A base ainda **não está completa**.

Novos conteúdos serão adicionados gradualmente, principalmente conforme novas necessidades forem identificadas durante os testes do projeto.

A ideia não é criar centenas de arquivos apenas para dizer que existem centenas de arquivos. Primeiro vem a utilidade; depois, a expansão.

---

## 🛠️ Tecnologias utilizadas

O protótipo atual utiliza:

* **Python 3.11**
* **Ollama**
* **Llama 3.2**
* **Requests**
* **Git / GitHub**
* Arquivos Markdown para a Base de Conhecimento

O modelo de linguagem é executado localmente através do Ollama.

---

## ▶️ Executando localmente

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd o-agente

```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv

```

No Windows:

```bash
.venv\Scripts\activate

```

### 3. Instalar as dependências

```bash
pip install requests

```

### 4. Garantir que o modelo esteja disponível no Ollama

```bash
ollama pull llama3.2

```

### 5. Executar O Agente

```bash
python -m src.app

```

---

## 🧪 Testes iniciais

Durante o desenvolvimento, algumas entradas já foram utilizadas para verificar a identificação de intenção:

```text
O que é phishing?
→ explorar

Como posso proteger minha conta?
→ proteger

Recebi uma mensagem estranha.
→ investigar

Meu computador foi hackeado.
→ investigar

Quero entender o que é MFA.
→ explorar

Não sei o que fazer.
→ indefinido

```

Esses testes ajudam a identificar comportamentos que precisam ser aprimorados antes de novas funcionalidades serem adicionadas.

---

## ⚠️ Limitações atuais

O Agente ainda é um protótipo.

Entre as limitações atuais estão:

* a Base de Conhecimento ainda está em formação;
* o modelo recebe, nesta primeira versão, todo o conteúdo disponível da base;
* a seleção de conhecimento ainda pode ser aprimorada;
* a conversa atualmente funciona de maneira pontual, e não como uma investigação contínua;
* o modo **Investigar** ainda precisa evoluir para permitir perguntas e respostas em várias etapas;
* a identificação de intenção ainda pode retornar `indefinido`;
* as respostas do modelo ainda precisam de refinamento para permanecer mais focadas na pergunta original.

Essas limitações fazem parte do estágio atual do projeto e serão tratadas conforme o desenvolvimento avançar.

---

## 🔭 Possíveis evoluções

O projeto foi pensado para crescer gradualmente.

Entre as possíveis próximas etapas estão:

### 💬 Conversação contínua

Permitir que O Agente faça perguntas, receba respostas e continue a investigação.

```text
Pessoa:
Recebi uma mensagem estranha.

O Agente:
Por qual canal você recebeu a mensagem?

Pessoa:
WhatsApp.

O Agente:
A mensagem contém algum link?

Pessoa:
Sim.

O Agente:
Certo. Vamos analisar os próximos indícios...

```

### 🧠 Seleção inteligente de conhecimento

Em vez de enviar toda a Base de Conhecimento ao modelo, selecionar apenas os conteúdos relacionados à situação apresentada.

### 🔎 Investigação estruturada

Organizar uma investigação em:

```text
Fatos conhecidos
      ↓
Indícios
      ↓
Informações ausentes
      ↓
Hipóteses
      ↓
Próximos passos

```

### 📊 Avaliação das respostas

Criar testes para avaliar se O Agente:

* segue suas próprias regras;
* evita conclusões precipitadas;
* utiliza corretamente a Base de Conhecimento;
* reconhece falta de evidências;
* protege informações sensíveis;
* mantém o comportamento esperado em cada modo.

### 🌐 Evolução da interface

Futuramente, o projeto poderá deixar o terminal e receber uma interface própria.

### 📚 Expansão da Base de Conhecimento

Novos temas poderão ser incorporados conforme a necessidade, como:

* segurança de dispositivos;
* redes;
* privacidade;
* autenticação;
* engenharia social;
* incidentes;
* segurança de aplicações;
* boas práticas de proteção digital.

---

## 🎯 Objetivo do projeto

O objetivo de O Agente não é simplesmente criar mais um chatbot que responde perguntas sobre tecnologia.

A proposta é estudar, na prática, como conceitos de **Segurança da Informação, privacidade, análise de evidências e inteligência artificial** podem ser combinados para construir uma ferramenta que ajude pessoas a tomar decisões digitais mais conscientes.

O projeto também funciona como um espaço de aprendizado e experimentação em desenvolvimento de software e Segurança da Informação.

---

## 🧭 Em desenvolvimento

Este projeto está sendo desenvolvido de forma incremental.

Nem todas as funcionalidades planejadas estão implementadas, e a documentação será atualizada conforme novas partes forem construídas, testadas e validadas.

Por enquanto, O Agente ainda está aprendendo a investigar.

E, convenhamos, seria um tanto contraditório construir um agente de segurança que fingisse já saber tudo. 😉

---

## 📄 Licença

*Licença a definir conforme a evolução e os objetivos de publicação do projeto.*
