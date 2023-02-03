from abc import ABC


class Importer(ABC):

    @staticmethod
    def import_data(file: str):
        ...
