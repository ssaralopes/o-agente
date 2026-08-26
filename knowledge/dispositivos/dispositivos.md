# 💻 Segurança de Dispositivos

> Conhecimento de referência d'O Agente para compreensão, prevenção e investigação de situações relacionadas à segurança de computadores e dispositivos móveis.

---

## 1. Visão geral

Um dispositivo pode apresentar comportamentos inesperados por diversos motivos.

Entre eles:

- Problemas de configuração;
- Falhas de software;
- Aplicativos mal configurados;
- Atualizações pendentes;
- Extensões ou programas indesejados;
- Problemas de desempenho;
- Infecções por malware;
- Comprometimento de contas;
- Outros fatores.

Por isso:

> **Um comportamento estranho não significa automaticamente que o dispositivo foi invadido.**

O Agente deve investigar o contexto antes de apresentar qualquer conclusão.

---

# 2. Dispositivos no contexto de segurança digital

Computadores, smartphones e outros dispositivos armazenam ou processam informações que podem possuir valor para seus usuários.

Entre essas informações podem estar:

- Arquivos pessoais;
- Fotografias;
- Documentos;
- Mensagens;
- Credenciais;
- Dados de aplicativos;
- Informações de navegação;
- Dados financeiros.

A proteção do dispositivo contribui para reduzir a exposição dessas informações.

---

# 3. Atualizações

Atualizações de sistemas operacionais, aplicativos e outros componentes podem corrigir:

- Falhas de segurança;
- Problemas de funcionamento;
- Vulnerabilidades conhecidas;
- Erros de software.

Por isso, manter sistemas e aplicativos atualizados é uma prática importante de segurança.

O Agente deve evitar afirmar que uma atualização específica elimina determinado risco sem possuir informações suficientes sobre o software e a vulnerabilidade envolvida.

---

# 4. Aplicativos e programas

Aplicativos e programas devem ser obtidos preferencialmente por fontes confiáveis.

Sinais que justificam atenção incluem:

- Aplicativo desconhecido;
- Programa instalado sem conhecimento do usuário;
- Solicitações de permissões incompatíveis com sua finalidade;
- Downloads provenientes de fontes não confiáveis;
- Programas que solicitam privilégios inesperados.

A presença de um aplicativo desconhecido não comprova, sozinha, que ele seja malicioso.

O Agente deve considerar:

- Nome;
- Origem;
- Quando foi instalado;
- Permissões;
- Comportamento observado;
- Contexto da instalação.

---

# 5. Extensões de navegador

Extensões podem possuir acesso a determinadas informações ou funcionalidades do navegador.

Uma extensão desconhecida ou inesperada merece investigação.

O usuário pode verificar:

- Quais extensões estão instaladas;
- Quando foram adicionadas;
- Quem é o desenvolvedor;
- Quais permissões possuem;
- Se ainda são necessárias.

O Agente não deve classificar uma extensão como maliciosa apenas por não reconhecê-la.

---

# 6. Downloads e arquivos

Arquivos recebidos por e-mail, mensagens ou sites desconhecidos podem representar risco.

É necessário ter atenção especial quando:

- O arquivo não era esperado;
- A origem não foi confirmada;
- Existe pressão para abri-lo;
- O arquivo possui extensão inesperada;
- A mensagem apresenta outros sinais suspeitos.

O Agente deve evitar orientar a execução de arquivos desconhecidos como forma de investigação.

---

# 7. Links e páginas suspeitas

Links podem direcionar para páginas legítimas ou maliciosas.

Alguns sinais de atenção incluem:

- Domínio inesperado;
- Endereço diferente do serviço esperado;
- Erros ou alterações incomuns no endereço;
- Solicitação inesperada de login;
- Solicitação de informações sensíveis;
- Mensagem utilizando urgência ou ameaça.

Um endereço estranho não comprova automaticamente que uma página seja maliciosa.

Quando houver dúvida, a recomendação geral é acessar o serviço diretamente por um endereço conhecido ou aplicativo oficial.

---

# 8. Comportamentos inesperados

Alguns comportamentos podem justificar investigação.

Exemplos:

- Aplicativos abrindo sozinhos;
- Alterações inesperadas de configurações;
- Pop-ups recorrentes;
- Redirecionamentos inesperados;
- Novos aplicativos desconhecidos;
- Consumo incomum de recursos;
- Lentidão repentina;
- Mensagens de segurança inesperadas;
- Sessões ou acessos desconhecidos.

Esses sinais possuem múltiplas causas possíveis.

> **Sintoma não é diagnóstico.**

---

# 9. Malware

Malware é um termo utilizado para descrever software desenvolvido ou utilizado com finalidade maliciosa.

Existem diferentes categorias de malware, com comportamentos distintos.

Entre elas estão:

- Vírus;
- Worms;
- Trojans;
- Spyware;
- Ransomware;
- Outros tipos de software malicioso.

A presença de um sintoma isolado não é suficiente para identificar uma categoria específica de malware.

O Agente deve evitar afirmar:

> "Você está com um vírus."

quando não existem evidências suficientes.

Uma formulação mais adequada é:

> "Esse comportamento pode ter várias causas. Precisamos de mais informações para avaliar se existe algum indício de comprometimento."

---

# 10. Ransomware

Ransomware é um tipo de malware associado à indisponibilidade ou bloqueio de dados ou sistemas, frequentemente acompanhado de uma exigência de pagamento.

Situações envolvendo possível ransomware devem ser tratadas com atenção elevada.

O Agente deve priorizar:

- Evitar ações que possam agravar a situação;
- Preservar informações relevantes;
- Acionar suporte técnico ou equipe responsável;
- Seguir procedimentos oficiais de resposta a incidentes quando existentes.

O Agente não deve prometer recuperação dos dados.

---

# 11. Antivírus e ferramentas de segurança

Ferramentas de segurança podem auxiliar na identificação de ameaças.

Dependendo do sistema, podem existir:

- Antivírus;
- Antimalware;
- Firewall;
- Ferramentas de segurança integradas;
- Soluções de monitoramento.

Uma ferramenta não detectar uma ameaça não significa necessariamente que o dispositivo esteja absolutamente seguro.

Da mesma forma, um alerta de segurança deve ser interpretado considerando seu contexto.

> **Uma ferramenta de segurança fornece evidências; não uma garantia absoluta.**

---

# 12. Contas e dispositivos

A segurança de um dispositivo e a segurança das contas utilizadas nele estão relacionadas, mas não são a mesma coisa.

Por exemplo:

```text
Dispositivo comprometido
        ↓
Pode aumentar o risco
        ↓
Contas utilizadas no dispositivo
