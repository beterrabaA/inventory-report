"""importando a classe SimpleReport do arquivo simple_report.py"""
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    """criando a classe CompleteReport que herda da classe SimpleReport"""
    @staticmethod
    def generate(data):
        """Método que gera o relatório completo"""
        return (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.get_stock_by_company(data)}"
        )

    @staticmethod
    def get_stock_by_company(data):
        """Método que retorna os produtos estocados por empresa"""
        companies = []
        tupled_companies = []
        for item in data:
            companies.append(item["nome_da_empresa"])
        companies = set(companies)
        stock_by_company = ""
        for company in companies:
            stock = CompleteReport.get_stock(data, company)
            tupled_companies.append((company, stock))
        tupled_companies.sort(key=lambda x: x[0])
        for company in tupled_companies:
            stock_by_company += f"- {company[0]}: {company[1]}\n"
        return stock_by_company

    @staticmethod
    def get_stock(data, company):
        """Método que retorna a quantidade de produtos estocados por empresa"""
        stock = 0
        for item in data:
            if item["nome_da_empresa"] == company:
                stock += 1
        return stock
