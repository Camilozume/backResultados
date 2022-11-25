from models.partidos import Partidos
from repositories.partidos_repository import PartidosRepository

class PartidosController:
    # contructor
    def __init__(self):
        print("Partidos controller ready...")
        self.partidos_repository = PartidosRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("all partidos")
        return self.partidos_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Get partido")
        return self.partidos_repository.find_by_id(id_)

    def create(self, partido_: dict) -> dict:
        """

        :param partido_:
        :return:
        """
        print("Insert partido")
        partido = Partidos(partido_)
        return self.partidos_repository.save(partido)

    def update(self, id_: str, partido_: dict) -> dict:
        """

        :param id_:
        :param partido_:
        :return:
        """
        print("Update partido")
        partido = Partidos(partido_)
        return self.partidos_repository.update(id_, partido)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete partido")
        return self.partidos_repository.delete(id_)
