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
        lista = CompleteReport.get_stock(data)
        stock = ""
        for company, counter in lista.items():
            stock += f"- {company}: {counter}\n"
        return stock

    @staticmethod
    def get_stock(data):
        """Método que retorna a quantidade de produtos estocados por empresa"""
        stock = {}
        for item in data:
            if item["nome_da_empresa"] in stock:
                stock[item["nome_da_empresa"]] += 1
            else:
                stock[item["nome_da_empresa"]] = 1
        return stock
