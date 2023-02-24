from sinta import Sinta
import openpyxl
import re
import pandas as pd

kepala = ['Judul jurnal', 'Link jurnal', 'Affiliation', 'GoogleScholar', 'Website', 'Editor', 'P-ISSN', 'E-ISSN', 'Subject Area', 'Sinta', 'Scopus', 'Garuda', 'Garuda Link']
kepalaArtikel = ['Judul Artikel', 'Link Artikel', 'Affiliation', 'Publikasi', 'Tahun']

def main() :
    sinta = Sinta()
    # allJournal = sinta.getAllJournal()
    # # excel
    # try : 
    #     workbook = openpyxl.Workbook()
    #     worksheet = workbook.active
    #     worksheet.append(kepala)
    #     for data in allJournal:
    #         worksheet.append(data.get_all_attributes())
    #     workbook.save('result/SeluruhJurnal.xlsx')
    # except : print("Excel gagal")

    df = pd.read_excel("result/SeluruhJurnal.xlsx", sheet_name="Sheet")
    allJournal = df.iloc[0:, 0]
    for i in allJournal :
        article = sinta.getJournalArticle(re.sub(r"\([^)]*\)", '', i))
        # excel
        try : 
            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            worksheet.append(kepalaArtikel)
            for data in article:
                worksheet.append(data.get_all_attributes())
            workbook.save('result/jurnal/{}.xlsx'.format(i))
            print('{}.xlsx berhasil dibuat'.format(i))
        except : print("Excel gagal")

if __name__ == '__main__':
    main()





