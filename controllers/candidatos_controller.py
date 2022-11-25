from models.candidatos import Candidatos
from models.partidos import Partidos
from repositories.partidos_repository import PartidosRepository
from repositories.candidatos_repository import CandidatosRepository


class CandidatosController:

    def __init__(self):
        print("Candidates controller ready...")
        self.candidatos_repository = CandidatosRepository()
        self.partidos_repository = PartidosRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("all candidatos")
        return self.candidatos_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Get candidato")
        return self.candidatos_repository.find_by_id(id_)

    def create(self, candidato_: dict) -> dict:
        """

        :param candidato_:
        :return:
        """
        print("Insert candidato")
        candidato = Candidatos(candidato_)
        return self.candidatos_repository.save(candidato)

    def update(self, id_: str, candidato_:dict) -> dict:
        """

        :param id_:
        :param candidato_:
        :return:
        """
        print("Update candidato")
        candidato = Candidatos(candidato_)
        return self.candidatos_repository.update(id_,candidato)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete candidato")
        return self.candidatos_repository.delete(id_)

    def partidos_assign(self, candidatos_id: str, partidos_id: str) -> dict:
        """

        :param candidatos_id:
        :param partidos_id:
        :return:
        """
        cantidatos_dict = self.candidatos_repository.find_by_id(candidatos_id)
        cantidatos_obj = Candidatos(cantidatos_dict)
        partidos_dict = self.partidos_repository.find_by_id(partidos_id)
        partidos_obj = Partidos(partidos_dict)
        cantidatos_obj.partidos = partidos_obj
        return self.candidatos_repository.save(cantidatos_obj)


