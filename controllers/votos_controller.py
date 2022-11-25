from models.votos import Votos
from models.candidatos import Candidatos
from models.mesas import Mesas
from repositories.votos_repository import VotosRepository
from repositories.candidatos_repository import CandidatosRepository
from repositories.mesas_repository import MesasRepository

class VotosController:
    # contructor
    def __init__(self):
        print("Votos controller ready...")
        self.votos_repository = VotosRepository()
        self.candidatos_repository = CandidatosRepository()
        self.mesas_repository = MesasRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("all votos")
        return self.votos_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Get voto")
        return self.votos_repository.find_by_id(id_)

    def create(self, voto_: dict, candidatos_id: str, mesas_id: str) -> dict:
        """

        :param candidatos_id:
        :param mesas_id:
        :param voto_:
        :return:
        """
        print("Insert voto")
        voto = Votos(voto_)
        candidatos_dict = self.candidatos_repository.find_by_id(candidatos_id)
        candidatos_obj = Candidatos(candidatos_dict)
        mesas_dict = self.mesas_repository.find_by_id(mesas_id)
        mesas_obj = MesasRepository(mesas_dict)
        voto.candidato= candidatos_obj
        voto.mesa = mesas_obj
        return self.votos_repository.save(voto)

    def update(self, id_: str, voto_: dict) -> dict:
        """

        :param id_:
        :param voto_:
        :return:
        """
        print("Update voto")
        voto = Votos(voto_)
        return self.votos_repository.update(id_, voto)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete voto")
        return self.votos_repository.delete(id_)
