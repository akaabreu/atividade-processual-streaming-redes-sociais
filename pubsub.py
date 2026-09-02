"""Núcleo do padrão Publish/Subscribe usado pelo projeto."""

from collections import defaultdict
from collections.abc import Callable
from typing import Any


Callback = Callable[[str, Any], None]


class PubSub:
    """Broker em memória que gerencia tópicos, inscrições e publicações."""

    def __init__(self) -> None:
        self._topicos: dict[str, list[Callback]] = defaultdict(list)

    @staticmethod
    def _validar_topico(topico: str) -> str:
        topico = topico.strip()
        if not topico:
            raise ValueError("O tópico não pode ser vazio.")
        return topico

    def subscribe(self, topico: str, assinante: Callback) -> bool:
        """Inscreve um callback no tópico. Retorna False se já estiver inscrito."""
        topico = self._validar_topico(topico)
        if not callable(assinante):
            raise TypeError("O assinante deve ser uma função ou método chamável.")
        if assinante in self._topicos[topico]:
            return False
        self._topicos[topico].append(assinante)
        return True

    def unsubscribe(self, topico: str, assinante: Callback) -> bool:
        """Remove um callback do tópico. Retorna False se ele não estiver inscrito."""
        topico = self._validar_topico(topico)
        assinantes = self._topicos.get(topico)
        if not assinantes or assinante not in assinantes:
            return False

        assinantes.remove(assinante)
        if not assinantes:
            del self._topicos[topico]
        return True

    def publish(self, topico: str, mensagem: Any) -> int:
        """Notifica os inscritos e retorna a quantidade de notificações enviadas."""
        topico = self._validar_topico(topico)
        assinantes = tuple(self._topicos.get(topico, ()))
        for assinante in assinantes:
            assinante(topico, mensagem)
        return len(assinantes)

    def quantidade_assinantes(self, topico: str) -> int:
        """Informa quantos assinantes estão ativos em um tópico."""
        topico = self._validar_topico(topico)
        return len(self._topicos.get(topico, ()))
