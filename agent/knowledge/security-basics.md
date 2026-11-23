# Fundamentos de segurança

## Vulnerabilidade

Fraqueza em software, configuração ou processo que pode ser explorada e causar dano.

## Ameaça

Pessoa, evento ou condição capaz de explorar uma vulnerabilidade e afetar um ativo.

## Risco

Combinação contextual da probabilidade de um evento e do impacto que ele causaria. Não é uma propriedade isolada do código.

## Confidencialidade

A informação só pode ser acessada por pessoas autorizadas.

## Integridade

Os dados e sistemas mantêm sua exatidão e completude; alterações indevidas são evitadas ou detectadas.

## Disponibilidade

Dados e serviços permanecem acessíveis de forma confiável e oportuna para quem tem autorização.

## Boas práticas

Aplique privilégio mínimo, configurações seguras por padrão, atualizações oportunas, validação de entradas, controles de autorização no servidor, proteção de segredos, registros úteis sem dados sensíveis, backups testados e defesa em profundidade. Teste apenas dentro do escopo autorizado. Avalie o risco no ambiente correspondente e não confunda um teste aprovado com prova de segurança completa.

## SQL parametrizado

Separe a instrução SQL dos valores fornecidos. Use placeholders e passe os valores em uma coleção separada, por exemplo: `cursor.execute("SELECT * FROM usuarios WHERE username = ?", (usuario,))`. O banco trata esses valores como dados, não como parte da sintaxe SQL, reduzindo o risco de injeção. A parametrização não substitui autorização, validação de regras de negócio ou armazenamento seguro de senhas.

## CWE e MITRE ATT&CK

- **CWE (Common Weakness Enumeration):** catálogo de tipos de fraqueza em software e hardware; ajuda a nomear e agrupar causas de vulnerabilidades.
- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas de adversários, organizada pelo comportamento observado durante ataques.

CWE descreve classes de fraqueza; ATT&CK descreve comportamentos de ataque. São referências com finalidades diferentes. Podem se complementar, mas não há correspondência obrigatória ou automática entre elas.