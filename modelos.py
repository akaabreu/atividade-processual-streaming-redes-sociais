"""Participantes da plataforma fictícia de streaming e rede social."""

from typing import Any

from pubsub import PubSub


class Usuario:
    """Subscriber que recebe conteúdos dos tópicos assinados."""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notificacoes: list[tuple[str, Any]] = []

    def receber(self, topico: str, mensagem: Any) -> None:
        self.notificacoes.append((topico, mensagem))
        print(f"🔔 {self.nome} recebeu em [{topico}]: {mensagem}")


class CriadorConteudo:
    """Publisher que envia conteúdos ao broker sem conhecer os usuários."""

    def __init__(self, nome: str, broker: PubSub) -> None:
        self.nome = nome
        self._broker = broker

    def publicar(self, topico: str, conteudo: str) -> int:
        mensagem = f"{self.nome} publicou: {conteudo}"
        print(f"\n📢 Publicação no tópico [{topico}] — {mensagem}")
        return self._broker.publish(topico, mensagem)
