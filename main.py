"""Demonstração executável do padrão Pub/Sub."""

from modelos import CriadorConteudo, Usuario
from pubsub import PubSub


def demonstrar() -> None:
    broker = PubSub()

    marcos_paulo = Usuario("Marcos Paulo")
    marcos_vinicius = Usuario("Marcos Vinicius")
    marcos = Usuario("Marcos")

    canal_codigo = CriadorConteudo("Canal Código Direto", broker)
    canal_games = CriadorConteudo("Arena Gamer", broker)

    print("=== INSCRIÇÕES ===")
    broker.subscribe("Tech", marcos_paulo.receber)
    broker.subscribe("Tech", marcos_vinicius.receber)
    broker.subscribe("Games", marcos_vinicius.receber)
    broker.subscribe("Games", marcos.receber)
    print("Marcos Paulo e Marcos Vinicius assinaram Tech.")
    print("Marcos Vinicius e Marcos assinaram Games.")

    print("\n=== PUBLICAÇÕES ===")
    canal_codigo.publicar("Tech", "Novo vídeo: Pub/Sub com Python")
    canal_games.publicar("Games", "Live de lançamento começa às 20h")

    print("\n=== CANCELAMENTO DE INSCRIÇÃO ===")
    broker.unsubscribe("Games", marcos_vinicius.receber)
    print("Marcos Vinicius cancelou a inscrição em Games.")

    print("\n=== NOVA PUBLICAÇÃO APÓS UNSUBSCRIBE ===")
    canal_games.publicar("Games", "Melhores momentos da live disponíveis")

    print("\n=== RESULTADO ===")
    print("Marcos Vinicius não recebeu a última publicação de Games.")
    print("A demonstração de subscribe, publish e unsubscribe foi concluída.")


if __name__ == "__main__":
    demonstrar()
