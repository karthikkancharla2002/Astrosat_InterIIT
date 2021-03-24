# from openpyxl import load_workbook
import csv
import pandas as pd
publications_txt = "./AS_publications2019-21.txt"
publications_csv = "./publication.csv"

Title = 'Title'
Authors = 'Authors'
Bibliographi = 'Bibliographi'
Keywords = 'Keywords'
Abstract = 'Abstract'
URL = 'URL'

title_data = []
auth_data = []
bibl_data = []
keyword_data = []
abs_data = []
url_data = []

with open(publications_csv, 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row)>0:
            header = row[0].split()[0][:-1]
            if header == Title:
                title_data.append(row[0].split(':')[1].strip())
            elif header == Authors:
                auth_data.append(row[0].split(':')[1].strip())
            elif header == Bibliographi:
                bibl_data.append(row[0].split(':')[1].strip())
            elif header == Keywords:
                keyword_data.append(row[0].split(':')[1].strip())
            elif header == Abstract:
                abs_data.append(row[0].split(':')[1].strip())
            elif header == URL:
                url_data.append(row[0][5:].strip())

df_publications = pd.DataFrame([title_data, auth_data, bibl_data, keyword_data, abs_data, url_data], index=[Title,Authors,Bibliographi,Keywords,Abstract,URL]).T
# print(df_publications.head())

def displayPublicationData(source_name):

    df_selected_source_publication = df_publications[df_publications.Title.str.replace(" ","").str.find(source_name.replace(" ","")) != -1]
    return df_selected_source_publication


# def publicationsAppletGUI(selected_source_name):




# displayPublicationData('J17091-3624')
