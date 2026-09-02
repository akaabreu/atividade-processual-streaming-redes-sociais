# Roteiro de apresentação — até 15 minutos

## 1. Marcos Paulo — cenário e conceito (3 a 4 minutos)

- Apresentar o problema: usuários querem receber apenas conteúdos de seu interesse.
- Explicar que Pub/Sub separa quem publica de quem recebe.
- Identificar Publisher, Broker, Topic e Subscriber no projeto.
- Mostrar rapidamente a arquitetura do README.

## 2. Marcos Vinicius — explicação do código (3 a 4 minutos)

- Abrir `pubsub.py` e explicar o dicionário de tópicos.
- Mostrar `subscribe`, destacando a prevenção de inscrições duplicadas.
- Mostrar `publish`, que percorre apenas os assinantes daquele tópico.
- Mostrar `unsubscribe`, que remove o assinante.

## 3. Marcos — demonstração prática (4 a 5 minutos)

- Executar `python main.py`.
- Apontar que Tech e Games possuem públicos diferentes.
- Destacar as duas primeiras publicações e seus destinatários.
- Mostrar o cancelamento de Marcos Vinicius em Games.
- Confirmar que ele não recebe a publicação seguinte.
- Se houver tempo, executar `python -m unittest -v`.

## 4. Encerramento e perguntas (2 a 3 minutos)

- Reforçar o desacoplamento: o criador conhece o broker, mas não conhece os usuários.
- Explicar que o exemplo é em memória e que Kafka seria uma alternativa em escala real.
- Abrir para perguntas.

## Perguntas prováveis

### Por que isso é Pub/Sub?

Porque publicadores enviam eventos para tópicos por meio de um broker, e somente os assinantes ativos nesses tópicos recebem as mensagens.

### Onde está o desacoplamento?

O `CriadorConteudo` publica no broker sem possuir referência direta aos usuários. Novos usuários podem entrar ou sair sem alterar o publicador.

### O processamento é realmente distribuído?

Esta implementação é uma simulação didática do padrão em um único processo. Em produção, broker, publishers e subscribers poderiam rodar em máquinas distintas.

### Por que não usar Kafka?

O objetivo é demonstrar o padrão arquitetural. Kafka é uma tecnologia que implementa mensageria distribuída, mas não é necessário para validar a mecânica solicitada.

### O que acontece sem assinantes?

O broker aceita a publicação e retorna zero notificações enviadas, sem gerar erro.
