"""importando as bibliotecas datetime e date para trabalhar com datas"""
from datetime import datetime, date


class SimpleReport:
    """Classe que gera o relatório simples"""
    @staticmethod
    def generate(data):
        """Método que gera o relatório simples"""
        return (
            f"Data de fabricação mais antiga: {SimpleReport.g_e_d(data)}\n"
            f"Data de validade mais próxima: {SimpleReport.g_n_d(data)}\n"
            f"Empresa com mais produtos: {SimpleReport.g_c_w_m_p(data)}"
        )

    # get_earliest_date
    @staticmethod
    def g_e_d(industry_data):
        """Método que retorna a data de fabricação mais antiga"""
        dates = []
        for item in industry_data:
            dates.append(item["data_de_fabricacao"])
        return min(dates)

    # get_nearest_date
    @staticmethod
    def g_n_d(date_data):
        """Método que retorna a data de validade mais próxima"""
        data_atual = date.today()
        data_proxima = None
        diferenca_minima = float('inf')
        for item in date_data:
            data_validade = datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            ).date()
            diferenca = abs(data_atual - data_validade).days
            if diferenca < diferenca_minima:
                data_proxima = data_validade
                diferenca_minima = diferenca
        return data_proxima

    # get_company_with_most_products
    @staticmethod
    def g_c_w_m_p(company_data):
        """Método que retorna a empresa com mais produtos"""
        companies = []
        for item in company_data:
            companies.append(item["nome_da_empresa"])
        return max(set(companies), key=companies.count)
