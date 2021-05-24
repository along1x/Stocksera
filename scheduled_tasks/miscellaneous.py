import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

conn = sqlite3.connect("database.db", check_same_thread=False)
db = conn.cursor()


def get_high_short_interest():
    """Returns a high short interest DataFrame
    Returns
    -------
    DataFrame
        High short interest Dataframe with the following columns:
        Ticker, Company, Exchange, ShortInt, Float, Outstd, Industry
    """

    url_high_short_interested_stocks = "https://www.highshortinterest.com"

    text_soup_high_short_interested_stocks = BeautifulSoup(requests.get(url_high_short_interested_stocks,).text, "lxml")

    a_high_short_interest_header = list()
    for high_short_interest_header in text_soup_high_short_interested_stocks.findAll(
        "td", {"class": "tblhdr"}
    ):
        a_high_short_interest_header.append(
            high_short_interest_header.text.strip("\n").split("\n")[0]
        )
    df_high_short_interest = pd.DataFrame(columns=a_high_short_interest_header)

    stock_list_tr = text_soup_high_short_interested_stocks.find_all("tr")

    for a_stock in stock_list_tr:
        a_stock_txt = a_stock.text

        if a_stock_txt == "":
            continue

        shorted_stock_data = a_stock_txt.split("\n")

        if len(shorted_stock_data) == 8:
            df_high_short_interest.loc[
                len(df_high_short_interest.index)
            ] = shorted_stock_data[:-1]

    db.execute("DELETE FROM short_interest")
    for index, row in df_high_short_interest.iterrows():
        db.execute("INSERT INTO short_interest VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (row['Ticker'], row['Company'], row['Exchange'], row['ShortInt'], row['Float'],
                    row['Outstd'], row['Industry']))
        conn.commit()


def get_low_float():
    """Returns low float DataFrame
    Returns
    -------
    DataFrame
        Low float DataFrame with the following columns:
        Ticker, Company, Exchange, ShortInt, Float, Outstd, Industry
    """

    url_high_short_interested_stocks = "https://www.lowfloat.com"

    text_soup_low_float_stocks = BeautifulSoup(requests.get(url_high_short_interested_stocks).text, "lxml")

    a_low_float_header = list()
    for low_float_header in text_soup_low_float_stocks.findAll(
        "td", {"class": "tblhdr"}
    ):
        a_low_float_header.append(low_float_header.text.strip("\n").split("\n")[0])
    df_low_float = pd.DataFrame(columns=a_low_float_header)

    stock_list_tr = text_soup_low_float_stocks.find_all("tr")

    for a_stock in stock_list_tr:
        a_stock_txt = a_stock.text

        if a_stock_txt == "":
            continue

        low_float_data = a_stock_txt.split("\n")

        if len(low_float_data) == 8:
            df_low_float.loc[len(df_low_float.index)] = low_float_data[:-1]

    db.execute("DELETE FROM low_float")
    for index, row in df_low_float.iterrows():
        db.execute("INSERT INTO low_float VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (row['Ticker'], row['Company'], row['Exchange'], row['Float'], row['Outstd'],
                    row['Outstd'], row['Industry']))
        conn.commit()


if __name__ == '__main__':
    get_high_short_interest()
    get_low_float()