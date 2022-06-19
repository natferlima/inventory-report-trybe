import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, report_type):
        data_list = []
        with open(path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                data_list.append(dict(row))

        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)
