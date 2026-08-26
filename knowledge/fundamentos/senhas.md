# 🔑 Senhas e Credenciais

> Conhecimento de referência d'O Agente para compreensão, criação, proteção e investigação de situações relacionadas a senhas e credenciais de acesso.

## 1. Visão geral

Uma senha é uma informação utilizada para autenticar uma pessoa em um serviço, sistema ou dispositivo.

Ela funciona como uma barreira de acesso:

```text
Pessoa
   │
   ▼
Identificação
   │
   ▼
Senha / outro fator
   │
   ▼
Autenticação
   │
   ▼
Acesso
```

A segurança de uma conta não depende apenas da existência de uma senha.

Também são relevantes fatores como:

* Qualidade da senha;
* Exclusividade da senha;
* Proteção da credencial;
* Autenticação multifator;
* Segurança do serviço;
* Métodos de recuperação da conta;
* Segurança do dispositivo utilizado.

> **Uma senha forte não torna uma conta invulnerável.**

---

## 2. Senha, credencial e autenticação

Esses conceitos estão relacionados, mas não são sinônimos.

### Senha

Informação secreta utilizada como parte do processo de autenticação.

### Credencial

Informação ou elemento utilizado para comprovar uma identidade durante a autenticação.

Uma credencial pode incluir:

* Senha;
* PIN;
* Chave de segurança;
* Certificado;
* Token;
* Outros mecanismos de autenticação.

### Autenticação

Processo utilizado para verificar se uma pessoa é realmente quem afirma ser.

Portanto:

```text
Senha
   ↓
é uma forma de
   ↓
Credencial
   ↓
utilizada durante
   ↓
Autenticação
```

---

## 3. Características de uma senha mais resistente

Uma senha deve dificultar tentativas de adivinhação ou descoberta.

Características importantes incluem:

* Comprimento adequado;
* Unicidade;
* Baixa previsibilidade;
* Ausência de informações pessoais óbvias;
* Não utilização de padrões facilmente identificáveis.

O tamanho da senha é um fator importante, mas não deve ser analisado isoladamente.

Uma senha longa e previsível pode continuar sendo inadequada.

---

## 4. Senhas únicas

Uma das práticas mais importantes é evitar reutilizar a mesma senha em diferentes serviços.

Considere:

```text
E-mail
   │
   ├── mesma senha ──► Rede social
   │
   ├── mesma senha ──► Loja
   │
   └── mesma senha ──► Banco
```

Se uma dessas contas for comprometida, a reutilização da senha pode aumentar o impacto sobre outras contas.

Por isso:

> **Uma senha comprometida não deve abrir portas para outras contas.**

---

## 5. Senhas previsíveis

Senhas baseadas em informações facilmente associadas à pessoa podem ser mais fáceis de adivinhar.

Exemplos de informações que podem ser previsíveis:

* Nome;
* Data de nascimento;
* Nome de familiares;
* Nome de animais;
* Time esportivo;
* Cidade;
* Sequências numéricas;
* Palavras muito comuns.

Informações públicas ou facilmente descobertas não devem ser consideradas segredos.

---

## 6. Gerenciadores de senhas

Gerenciadores de senhas são ferramentas desenvolvidas para armazenar e administrar credenciais.

Eles podem facilitar a utilização de senhas:

* Longas;
* Únicas;
* Diferentes para cada serviço.

Uma vantagem é reduzir a necessidade de memorizar várias senhas.

O uso de um gerenciador também exige proteção adequada da conta ou credencial principal utilizada para acessá-lo.

O Agente não deve afirmar que um gerenciador específico é absolutamente seguro.

Quando a pessoa perguntar sobre uma ferramenta específica, características e recursos devem ser verificadas antes de serem afirmados.

---

## 7. Senhas e autenticação multifator

MFA adiciona uma camada adicional de proteção além da senha.

Por exemplo:

```text
Senha
  +
Segundo fator
  ↓
Autenticação
```

Isso significa que o comprometimento da senha, isoladamente, pode não ser suficiente para obter acesso.

Porém:

> **MFA complementa a senha; não torna desnecessária a proteção da senha.**

As duas medidas devem ser consideradas partes de uma estratégia de proteção em camadas.

---

## 8. Não compartilhar senhas

Senhas são informações de autenticação e devem ser mantidas em sigilo.

O Agente nunca deve solicitar que a pessoa informe sua senha.

Isso também se aplica durante uma investigação.

Por exemplo, se uma pessoa disser:

> "Acho que minha senha foi descoberta."

O Agente pode perguntar sobre o contexto, mas não deve responder:

> "Qual é a sua senha?"

A orientação deve buscar informações sobre o ocorrido sem coletar a própria credencial.

---

## 9. Códigos de autenticação não são senhas comuns

Códigos temporários utilizados durante MFA também são informações de segurança.

Eles podem possuir validade curta, mas isso não significa que possam ser compartilhados.

O Agente deve tratar:

* Senhas;
* Códigos MFA;
* Tokens;
* Chaves privadas;

como informações sensíveis de autenticação.

> **O Agente não precisa conhecer uma credencial para ajudar a proteger a conta.**

---

## 10. Senhas em mensagens e e-mails

Uma pessoa pode receber mensagens solicitando sua senha.

Isso deve ser tratado com cautela.

Uma organização legítima pode utilizar diferentes mecanismos de autenticação, mas uma solicitação inesperada de senha por mensagem merece investigação.

O Agente deve evitar afirmar automaticamente que a mensagem é maliciosa.

Em vez disso, deve considerar:

* Quem enviou;
* Qual serviço está envolvido;
* Por qual canal a solicitação chegou;
* Qual justificativa foi apresentada;
* Se a pessoa esperava aquela comunicação;
* Se existe uma forma independente de verificar a solicitação.

---

## 11. Se a pessoa acredita que sua senha foi comprometida

O Agente deve primeiro compreender o contexto.

Perguntas úteis podem incluir:

* Qual conta pode ter sido afetada?
* O que levou à suspeita?
* Houve uma notificação de acesso?
* A senha foi reutilizada em outros serviços?
* Houve alguma interação com uma mensagem ou página suspeita?
* A conta possui MFA?
* A pessoa ainda consegue acessar a conta?

> **O Agente não deve solicitar a senha.**

### 11.1 Medidas gerais

Dependendo do contexto, podem ser consideradas:

* Alterar a senha pelo canal oficial do serviço;
* Encerrar sessões ou dispositivos desconhecidos, quando o serviço oferecer esse recurso;
* Ativar MFA;
* Verificar informações de recuperação da conta;
* Verificar atividades ou acessos recentes;
* Alterar senhas reutilizadas em outros serviços;
* Procurar suporte oficial quando necessário.

A ordem e a necessidade dessas ações dependem da situação.

---

## 12. Senha exposta x conta comprometida

Esses conceitos não devem ser tratados como equivalentes.

### Senha exposta

Existe alguma evidência de que a senha pode ter sido visualizada, compartilhada, capturada ou obtida por outra pessoa.

### Conta comprometida

Existem evidências de acesso ou controle indevido da conta.

Uma senha pode estar exposta sem que exista evidência de acesso indevido.

Da mesma forma, uma conta pode apresentar sinais de comprometimento sem que a causa seja conhecida.

O Agente deve evitar transformar uma suspeita sobre a senha em uma confirmação de comprometimento da conta.

---

## 13. Fatos, indícios e hipóteses

A análise deve diferenciar diferentes níveis de certeza.

### Fato

> "A pessoa recebeu uma notificação de login que não reconhece."

### Indício

> "Pode existir uma tentativa de acesso à conta."

### Hipótese

> "A senha pode ter sido obtida por terceiros."

### Conclusão

Uma conclusão exige evidências suficientes para sustentá-la.

O Agente deve evitar:

```text
Login desconhecido
       ↓
senha roubada
       ↓
conta invadida
```

como se cada etapa fosse automaticamente comprovada.

> **Cada hipótese precisa ser analisada separadamente.**

---

## 14. Situações relacionadas a senhas

### 📚 Explorar

O Agente pode explicar:

* O que é uma senha;
* O que é uma credencial;
* Como funciona a autenticação;
* Por que senhas únicas são importantes;
* Relação entre senha e MFA;
* Funcionamento geral de gerenciadores de senhas.

### 🛡️ Proteger

O Agente pode orientar sobre:

* Criação de senhas mais resistentes;
* Uso de senhas únicas;
* Utilização de gerenciadores;
* Ativação de MFA;
* Proteção de credenciais;
* Cuidados com solicitações de senha.

### 🔎 Investigar

O Agente pode ajudar a analisar:

* Suspeitas de exposição de senha;
* Notificações de acesso;
* Solicitações inesperadas de credenciais;
* Reutilização de senhas;
* Possíveis consequências de uma credencial comprometida.

---

## 15. O que O Agente NÃO deve fazer

O Agente não deve:

* Solicitar senhas;
* Solicitar códigos MFA;
* Solicitar tokens;
* Solicitar chaves privadas;
* Armazenar credenciais fornecidas pela pessoa;
* Repetir credenciais compartilhadas durante uma conversa;
* Afirmar que uma senha foi descoberta sem evidências;
* Afirmar que uma conta foi comprometida apenas porque existe uma suspeita;
* Prometer que uma senha é impossível de descobrir;
* Afirmar que determinado gerenciador ou método é absolutamente seguro;
* Inventar requisitos de senha de um serviço específico.

Quando a orientação depender de regras de uma plataforma específica, O Agente deve reconhecer a limitação e recomendar a consulta aos canais oficiais.

---

## 16. Privacidade durante a investigação

A investigação de uma possível exposição de credenciais deve buscar o máximo de contexto necessário com o mínimo de informação sensível possível.

O Agente deve preferir perguntas como:

> "Você recebeu alguma notificação de acesso que não reconhece?"

em vez de:

> "Qual é seu usuário e sua senha?"

Sempre que possível, dados pessoais devem ser removidos ou ocultados antes de serem compartilhados para análise.

---

## 17. Limitações do conhecimento

As políticas de senha e os métodos de autenticação variam entre serviços.

Um serviço pode exigir determinados critérios de senha, enquanto outro pode possuir regras diferentes.

O Agente não deve inventar requisitos específicos.

Quando uma recomendação depender de uma plataforma determinada, deve indicar essa dependência.

> **Boas práticas gerais orientam. Regras específicas devem ser verificadas no serviço correspondente.**

---

## 18. Regra de ouro

> 🔑 **Uma credencial não deve ser necessária para pedir ajuda sobre uma credencial.**

O Agente deve conseguir orientar uma pessoa sobre proteção, exposição ou comprometimento de senhas sem jamais precisar conhecer a senha em questão.

> **Proteja a credencial. Investigue o contexto.**
