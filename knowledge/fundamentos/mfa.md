# 🔐 Autenticação Multifator (MFA)

> Conhecimento de referência d'O Agente para compreensão, utilização e investigação de situações relacionadas à autenticação multifator.

## 1. Visão geral

Autenticação Multifator (MFA — Multi-Factor Authentication) é um mecanismo de autenticação que utiliza dois ou mais fatores de categorias diferentes para verificar a identidade de uma pessoa.

A ideia central é adicionar uma camada de proteção além da senha.

Quando uma conta utiliza apenas uma senha, o comprometimento dessa senha pode ser suficiente para permitir um acesso indevido.

Com MFA, um segundo fator pode ser exigido.

> **MFA não elimina o risco de comprometimento de uma conta, mas pode reduzir significativamente o impacto de uma senha comprometida.**

---

## 2. Fatores de autenticação

Os fatores de autenticação são geralmente agrupados em categorias.

### 🧠 Algo que você sabe

Informação que a pessoa conhece.

Exemplos:

* Senha;
* PIN;
* Resposta a um segredo previamente cadastrado.

### 📱 Algo que você possui

Um objeto ou dispositivo associado à pessoa.

Exemplos:

* Aplicativo autenticador;
* Chave de segurança;
* Dispositivo previamente registrado;
* Token de autenticação.

### 👤 Algo que você é

Uma característica biométrica da pessoa.

Exemplos:

* Impressão digital;
* Reconhecimento facial;
* Outros mecanismos biométricos.

---

## 3. MFA x 2FA

Os termos MFA e 2FA são relacionados, mas não são exatamente iguais.

**MFA** significa autenticação utilizando dois ou mais fatores de categorias diferentes.

**2FA** significa autenticação utilizando especificamente dois fatores.

Portanto:

```text id="2a6cvn"
2FA ⊂ MFA

Todo 2FA é uma forma de MFA, mas MFA pode utilizar mais de dois fatores.
```

---

## 4. O que caracteriza um segundo fator

Adicionar duas informações da mesma categoria não significa necessariamente utilizar MFA.

Por exemplo:

```text id="2jv7yb"
Senha + PIN

Ambos pertencem à categoria "algo que você sabe".

Isso não representa autenticação multifator no sentido tradicional.
```

Já uma combinação como:

```text id="f6q1zb"
Senha + código de aplicativo autenticador
```

utiliza categorias diferentes:

```text id="d4i0wx"
Algo que você sabe
        +
Algo que você possui
```

---

## 5. Métodos comuns de MFA

Existem diferentes formas de implementar autenticação multifator.

### Aplicativos autenticadores

Aplicativos podem gerar códigos temporários utilizados durante o processo de autenticação.

### Códigos enviados por SMS

Um código pode ser enviado para um número de telefone associado à conta.

Esse mecanismo adiciona uma camada adicional em relação à senha, mas possui limitações de segurança.

### Códigos enviados por e-mail

Alguns serviços utilizam códigos enviados para um endereço de e-mail associado à conta.

A segurança desse método depende também da proteção da própria conta de e-mail.

### Chaves de segurança

Dispositivos físicos podem ser utilizados como fator adicional de autenticação.

Esses mecanismos podem oferecer proteção mais forte contra determinados tipos de ataques de phishing.

### Biometria

Características biométricas podem ser utilizadas como fator de autenticação.

A disponibilidade e o funcionamento dependem do dispositivo e do serviço utilizado.

---

## 6. MFA não significa segurança absoluta

A utilização de MFA não torna uma conta invulnerável.

Ainda podem existir riscos relacionados a:

* Phishing;
* Engenharia social;
* Roubo de sessão;
* Comprometimento do dispositivo;
* Recuperação de conta;
* Fatores de autenticação comprometidos;
* Configurações inadequadas.

Portanto:

> **"A conta possui MFA" não significa "a conta está completamente protegida".**

O Agente deve evitar apresentar MFA como uma solução absoluta.

---

## 7. MFA e phishing

Algumas tentativas de phishing podem tentar obter não apenas a senha, mas também o segundo fator de autenticação.

Por exemplo, uma pessoa pode receber uma página falsa que solicita:

1. Usuário;
2. Senha;
3. Código de autenticação.

O fato de uma página solicitar MFA não significa que ela seja legítima.

O contexto e a autenticidade do serviço ainda precisam ser verificados.

---

## 8. Solicitações inesperadas de código

Uma situação importante ocorre quando a pessoa recebe um código de autenticação que não solicitou.

Isso pode indicar, entre outras possibilidades:

* Uma tentativa de acesso à conta;
* Uma tentativa de recuperação de conta;
* Uma autenticação iniciada pela própria pessoa em outro dispositivo;
* Um erro ou tentativa legítima não reconhecida.

O recebimento de um código, isoladamente, não comprova que uma conta foi invadida.

O Agente deve buscar contexto antes de apresentar uma conclusão.

### 8.1 Perguntas relevantes

Quando uma pessoa relata receber um código inesperado, O Agente pode perguntar:

* Você estava tentando entrar na conta?
* Qual serviço enviou o código?
* O código chegou por qual canal?
* Houve alguma outra notificação de acesso?
* Você recebeu alguma mensagem ou ligação relacionada ao código?
* Você informou o código para alguém?

> **O Agente nunca deve solicitar que a pessoa forneça o código recebido.**

---

## 9. Tentativas de obter códigos MFA

Códigos de autenticação são informações de segurança.

Uma pessoa ou serviço legítimo pode possuir processos próprios para autenticação, mas uma comunicação inesperada solicitando que a pessoa informe um código deve ser tratada com cautela.

Exemplos de abordagens suspeitas podem envolver:

> "Me informe o código que acabou de chegar."

> "Precisamos confirmar sua identidade."

> "Envie o código para cancelar a operação."

> "Passe o código para bloquear o acesso."

O contexto deve ser analisado antes de concluir que houve uma tentativa maliciosa.

> **Um código de autenticação deve ser tratado como informação de segurança, não como uma informação comum.**

---

## 10. O que fazer diante de um código inesperado

Quando a pessoa recebe um código que não solicitou:

* Não compartilhar o código;
* Não responder a mensagens suspeitas relacionadas ao código;
* Não fornecer o código para terceiros;
* Verificar a atividade da conta pelos canais oficiais;
* Considerar alterar a senha caso existam outros sinais de tentativa de acesso;
* Utilizar os mecanismos oficiais de segurança do serviço quando necessário.

A orientação deve considerar o contexto apresentado.

O recebimento isolado de um código não permite determinar exatamente o que aconteceu.

---

## 11. Recuperação de conta

Mecanismos de recuperação de conta são uma parte importante da segurança de autenticação.

Mesmo quando uma conta possui MFA, um processo de recuperação inadequadamente protegido pode representar um ponto de risco.

Por isso, a segurança de uma conta não deve ser avaliada apenas pela existência de MFA.

Também podem ser relevantes:

* Métodos de recuperação;
* E-mail associado;
* Número de telefone associado;
* Dispositivos confiáveis;
* Sessões ativas;
* Configurações de segurança.

---

## 12. Boas práticas

Para aumentar a segurança das contas:

* Ativar MFA sempre que o serviço oferecer o recurso;
* Preferir métodos de autenticação mais resistentes a phishing quando disponíveis;
* Não compartilhar códigos de autenticação;
* Não aprovar solicitações de login que não foram iniciadas pela própria pessoa;
* Verificar notificações de acesso;
* Manter métodos de recuperação atualizados;
* Utilizar senhas únicas para diferentes serviços;
* Manter dispositivos e aplicativos atualizados.

A melhor opção de MFA pode variar conforme o serviço, o dispositivo e o contexto de uso.

---

## 13. MFA e aprovação de login

Alguns serviços utilizam notificações no dispositivo para solicitar aprovação de uma tentativa de acesso.

Esse mecanismo pode ser conveniente, mas também pode ser alvo de engenharia social.

Uma pessoa pode receber várias solicitações de aprovação e ser induzida a aceitar uma delas por cansaço, confusão ou pressão.

Por isso:

> **Não aprove uma solicitação de login que você não iniciou.**

Se solicitações inesperadas continuarem acontecendo, a situação merece investigação adicional.

---

## 14. Fatos, indícios e conclusões

O Agente deve diferenciar o que foi observado do que pode ser inferido.

### Fato

> "Recebi um código de autenticação que não solicitei."

### Indício

> "Pode ter ocorrido uma tentativa de autenticação."

### Hipótese

> "Alguém pode estar tentando acessar minha conta."

### Conclusão

Uma conclusão exige evidências adicionais que sustentem a hipótese.

O Agente não deve transformar automaticamente:

```text id="1s7kqv"
código inesperado
       ↓
tentativa de acesso
       ↓
conta comprometida
```

em uma sequência de certezas.

Cada etapa exige evidências próprias.

---

## 15. Relação com os modos d'O Agente

### 📚 Explorar

Utilizar este conhecimento para:

* Explicar o que é MFA;
* Explicar fatores de autenticação;
* Diferenciar MFA e 2FA;
* Explicar métodos comuns;
* Explicar limitações.

### 🛡️ Proteger

Utilizar este conhecimento para:

* Orientar a ativação de MFA;
* Explicar boas práticas;
* Orientar sobre códigos de autenticação;
* Explicar cuidados com solicitações inesperadas.

### 🔎 Investigar

Utilizar este conhecimento para:

* Analisar códigos inesperados;
* Investigar solicitações de autenticação;
* Diferenciar fatos de hipóteses;
* Identificar informações adicionais necessárias;
* Orientar próximos passos.

---

## 16. O que O Agente NÃO deve fazer

O Agente não deve:

* Solicitar códigos de autenticação;
* Solicitar senhas;
* Solicitar tokens;
* Pedir que a pessoa aprove uma autenticação;
* Afirmar que uma conta foi invadida apenas porque um código inesperado foi recebido;
* Afirmar que MFA elimina completamente o risco;
* Declarar que determinado método é absolutamente seguro;
* Inventar recursos de segurança de um serviço;
* Presumir que todos os serviços oferecem os mesmos métodos de MFA.

Quando não souber quais mecanismos de autenticação ou recuperação um determinado serviço oferece, O Agente deve informar sua limitação.

---

## 17. Limitações do conhecimento

Os métodos de autenticação, recuperação e segurança podem variar entre serviços.

As recomendações apresentadas neste documento são princípios gerais e não substituem as instruções oficiais de cada serviço.

Quando uma orientação depender de uma característica específica de uma plataforma, O Agente deve reconhecer essa dependência e evitar inventar funcionalidades.

> **Conhecimento geral pode orientar. Informações específicas precisam ser verificadas.**

---

## 18. Regra de ouro

> 🔐 **MFA adiciona uma camada de proteção. Não adiciona imunidade.**

Uma conta protegida por MFA ainda pode estar sujeita a ataques.

O Agente deve incentivar a utilização de autenticação multifator, mas sem apresentar o mecanismo como uma garantia absoluta de segurança.

> **Proteção em camadas é mais importante do que uma única barreira.**

