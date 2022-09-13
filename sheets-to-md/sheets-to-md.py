#!/bin/env python3

import csv
import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

def main():
    creds = ServiceAccountCredentials.from_json_keyfile_name("unity-sheets-key.json", SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open("unity-docs-tables")

    # make list of worksheets, probably a better way to do this
    worksheets = []
    i = 0
    while True:
        try:
            worksheet = sheet.get_worksheet(i)
            worksheets.append(worksheet)
            i = i+1
        except gspread.WorksheetNotFound:
            break

    for worksheet in worksheets:
        data = worksheet.get_all_records()
        title = worksheet.title
        csv_name = f"output/{title}.csv"
        md_name = f"output/{title}.md"

        # each row is a dict {column_header:value , column_header2:value2 , ...}
        try:
            column_headers = data[0].keys()
        # empty worksheet
        except IndexError:
            continue

        with open(csv_name, 'w', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(column_headers)
            for row in data:
                writer.writerow(row.values())

        df = pd.read_csv(csv_name)
        df.fillna('', inplace=True) # remove NaN's
        with open(md_name, 'w', encoding="utf-8") as md:
            print(md_name)
            df.to_markdown(buf=md, index=False)

        os.remove(csv_name)

if __name__=="__main__":
    main()
