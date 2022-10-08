from dadata import Dadata


def find_firm_data(inn):
    token = "a6c55eaa1cc00d35296d73416d59090ac1d9645a"
    dadata = Dadata(token)
    firm_datas = dadata.find_by_id(name="party", query=inn, branch_type="MAIN")

    return {"name": firm_datas[0]["value"],
            "address": firm_datas[0]["data"]["address"]["value"],
            "ogrn": firm_datas[0]["data"]["ogrn"],
            "inn": inn}
