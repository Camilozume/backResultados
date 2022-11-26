from repositories.reports_repository import ReportsRepository


class ReportsController():
    def __init__(self):
        self.reports_repository = ReportsRepository()

    def get_sorted_candidato(self) -> list:
        print("Candidatos por mesa ordenado por inscritos")
        return self.reports_repository.get_sorted_candidato()

    def get_sorted_partido_by_mesa(self, mesa_id: str) -> list:
        return self.reports_repository.get_sorted_partido_by_mesa(mesa_id)

    def get_porcentual_partido(self) -> list:
        return self.reports_repository.get_porcentual_partidos()
