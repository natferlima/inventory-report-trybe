import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path_file, report_type):
        data_list = []
        with open(path_file, 'r') as file:
            if path_file.endswith(".csv"):
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    data_list.append(dict(row))
            if path_file.endswith(".json"):
                data_list = json.load(file)

        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)
