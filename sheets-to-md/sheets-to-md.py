#!/bin/env python3

import csv
import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

def clear_file(filename):
    with open(filename, 'w', encoding='utf-8') as x:
        x.write('')

def main():
    creds = ServiceAccountCredentials.from_json_keyfile_name("unity-sheets-key.json", SCOPE)
    client = gspread.authorize(creds)
    my_sheet = client.open("unity-docs-tables")

    # make list of worksheets, probably a better way to do this
    my_worksheets = []
    i = 0
    while True:
        try:
            i_worksheet = my_sheet.get_worksheet(i)
            my_worksheets.append(i_worksheet)
            i = i+1
        except gspread.WorksheetNotFound:
            break

    for my_worksheet in my_worksheets:
        i_data = my_worksheet.get_all_records()
        i_title = my_worksheet.title
        i_csv_name = f"output/{i_title}.csv"
        i_md_name = f"output/{i_title}.md"

        # each row is a dict {column header: value}
        try:
            column_headers = i_data[0].keys()
        # empty worksheet
        except IndexError:
            continue

        clear_file(i_csv_name)
        clear_file(i_md_name)

        with open(i_csv_name, 'a', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(column_headers)
            for row in i_data:
                writer.writerow(row.values())

        df = pd.read_csv(i_csv_name)
        df.fillna('', inplace=True) # remove NaN's
        with open(i_md_name, 'a') as md:
            df.to_markdown(buf=md, index=False)

        os.remove(i_csv_name)

if __name__=="__main__":
    main()
