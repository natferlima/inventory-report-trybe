import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data_csv(data_list, path_file, report_type):
        with open(path_file, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                data_list.append(dict(row))
        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)

    def import_data_json(data_list, path_file, report_type):
        with open(path_file, 'r') as file:
            data_list = json.load(file)
        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)

    def import_data_xml(data_list, path_file, report_type):
        # https://pythoniluminado.netlify.app/xml
        with open(path_file, 'r') as file:
            tree = ET.parse(file)
            root = tree.getroot()
            for elements in root.findall('record'):
                dic = {}
                for element in elements:
                    dic[element.tag] = element.text
                data_list.append(dic)
        if report_type == "simples":
            return SimpleReport.generate(data_list)
        if report_type == "completo":
            return CompleteReport.generate(data_list)

    def import_data(path_file, report_type):
        data_list = []
        # https://www.programiz.com/python-programming/methods/string/endswith
        if path_file.endswith(".csv"):
            return Inventory.import_data_csv(
                data_list,
                path_file,
                report_type
            )
        if path_file.endswith(".json"):
            return Inventory.import_data_json(
                data_list,
                path_file,
                report_type
            )
        if path_file.endswith(".xml"):
            return Inventory.import_data_xml(
                data_list,
                path_file,
                report_type
            )
