from models.mesas import Mesas
from repositories.mesas_repository import MesasRepository

class MesasController:

    def __init__(self):
        print("Mesas controller ready...")
        self.mesas_repository = MesasRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("all mesas")
        return self.mesas_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Get mesa")
        return self.mesas_repository.find_by_id(id_)

    def create(self, mesa_: dict) -> dict:
        """

        :param mesa_:
        :return:
        """
        print("Insert mesa")
        mesa = Mesas(mesa_)
        return self.mesas_repository.save(mesa)

    def update(self, id_: str, mesa_: dict) -> dict:
        """

        :param id_:
        :param mesa_:
        :return:
        """
        print("Update mesa")
        mesa = Mesas(mesa_)
        return self.mesas_repository.update(id_, mesa)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete mesa")
        return self.mesas_repository.delete(id_)
