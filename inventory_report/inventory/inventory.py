import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data_csv(data_list, path_file):
        with open(path_file, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                data_list.append(dict(row))
            return data_list

    def import_data_json(data_list, path_file):
        with open(path_file, 'r') as file:
            data_list = json.load(file)
            return data_list

    def import_data(path_file, report_type):
        data_list = []
        # https://www.programiz.com/python-programming/methods/string/endswith
        if path_file.endswith(".csv"):
            data_list = Inventory.import_data_csv(data_list, path_file)
        if path_file.endswith(".json"):
            data_list = Inventory.import_data_json(data_list, path_file)

        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)
