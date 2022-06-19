from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data):
        dic_empres = {}
        empres_qtd = ""

        for produto in data:
            if produto["nome_da_empresa"] not in dic_empres:
                dic_empres[produto["nome_da_empresa"]] = 1
            else:
                dic_empres[produto["nome_da_empresa"]] += 1

        for key, value in dic_empres.items():
            empres_qtd += f"- {key}, Inc.: {value}\n"

        return SimpleReport.generate(data) + (
            f"Produtos estocados por empresa:"
            f"{ empres_qtd }"
        )
