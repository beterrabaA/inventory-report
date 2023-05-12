from datetime import datetime, date


class SimpleReport:
    @staticmethod
    def generate(data):
        return (
        f"Data de fabricação mais antiga: {SimpleReport.get_earliest_date(data)}\n"
        f"Data de validade mais próxima: {SimpleReport.get_nearest_date(data)}\n"
        f"Empresa com mais produtos: {SimpleReport.get_company_with_most_products(data)}"
        )

    def get_earliest_date(data):
        dates = []
        for item in data:
            dates.append(item["data_de_fabricacao"])
        return min(dates)

    def get_nearest_date(data):
        data_atual = date.today()
        data_proxima = None
        diferenca_minima = None
        for item in data:
            data_validade = datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
            diferenca = abs(data_atual - data_validade).days
            if diferenca_minima == None or diferenca < diferenca_minima:
                data_proxima = data_validade
                diferenca_minima = diferenca
        return data_proxima

    def get_company_with_most_products(data):
        companies = []
        for item in data:
            companies.append(item["nome_da_empresa"])
        return max(set(companies), key = companies.count)
    

