import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    @staticmethod
    def import_data(path: str):
        prod_data = []
        if path.endswith(".xml"):
            with open(path, mode="r") as file:
                file = file.read()
                file = xmltodict.parse(file)
                file = file['dataset']['record']

                for line in file:
                    prod_data.append(dict(line))
            return prod_data

        else:
            raise ValueError("Arquivo inválido")
