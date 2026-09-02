"""Testes automatizados do broker Pub/Sub."""

import unittest

from pubsub import PubSub


class TestPubSub(unittest.TestCase):
    def setUp(self) -> None:
        self.broker = PubSub()
        self.recebidas: list[tuple[str, str]] = []

    def callback(self, topico: str, mensagem: str) -> None:
        self.recebidas.append((topico, mensagem))

    def test_subscribe_e_publish(self) -> None:
        self.assertTrue(self.broker.subscribe("Tech", self.callback))
        self.assertEqual(self.broker.publish("Tech", "Novo vídeo"), 1)
        self.assertEqual(self.recebidas, [("Tech", "Novo vídeo")])

    def test_topicos_sao_independentes(self) -> None:
        self.broker.subscribe("Tech", self.callback)
        self.broker.publish("Games", "Nova live")
        self.assertEqual(self.recebidas, [])

    def test_unsubscribe_interrompe_entrega(self) -> None:
        self.broker.subscribe("Tech", self.callback)
        self.assertTrue(self.broker.unsubscribe("Tech", self.callback))
        self.assertEqual(self.broker.publish("Tech", "Não entregar"), 0)
        self.assertEqual(self.recebidas, [])

    def test_inscricao_duplicada_e_ignorada(self) -> None:
        self.assertTrue(self.broker.subscribe("Tech", self.callback))
        self.assertFalse(self.broker.subscribe("Tech", self.callback))
        self.assertEqual(self.broker.quantidade_assinantes("Tech"), 1)

    def test_unsubscribe_inexistente_retorna_false(self) -> None:
        self.assertFalse(self.broker.unsubscribe("Tech", self.callback))

    def test_topico_vazio_e_invalido(self) -> None:
        with self.assertRaises(ValueError):
            self.broker.publish("   ", "Mensagem")


if __name__ == "__main__":
    unittest.main()
