class SimpleReport:
    def generate(data):
        lista_fabr = []
        lista_valid = []
        dic_empres = {}

        for produto in data:
            lista_fabr.append(produto["data_de_fabricacao"])
            lista_valid.append(produto["data_de_validade"])
            if produto["nome_da_empresa"] not in dic_empres:
                dic_empres[produto["nome_da_empresa"]] = 1
            else:
                dic_empres[produto["nome_da_empresa"]] += 1

        return(
            f"Data de fabricação mais antiga: {min(lista_fabr)}\n"
            f"Data de validade mais próxima: {min(lista_valid)}\n"
            f"Empresa com mais produtos:"
            f"{max(dic_empres, key = dic_empres.get)}"
        )

        # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/#:~:text=Resultado%3A%20Copy%20key3-,Utilize%20max()%20e%20dict.,%C3%A9%20utilizado%20o%20m%C3%A9todo%20dict.
