import csv
from datetime import date

class CsvUtils:
    def montarCsv(self,textoString):
        data_atual = str(date.today())
        c = csv.writer(open("resposta.csv", "w",newline = ''))
        c.writerow(['delegacia','ano','numero','nAutor','nAutorAcaoFugir','nAutorAcaoAbordagem','nQtdeAutor','nAutorArma','nAutorAcaoCoação','nAutorSubtrair','nAutorAcaoAgressao','N° de Similares','data do teste'])
        for i in textoString:
            row = i.copy()
            row.append(data_atual)
            c.writerow(row)
        