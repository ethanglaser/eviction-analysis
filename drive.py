import requests
import pandas as pd

def req():
    #response = pd.read_csv('https://docs.google.com/spreadsheet/ccc?key=16uepDjfOVlVBqJyKFaPgwXDoyGGdnL23eEnZ73g4OeU&output=csv')
    response2 = pd.read_csv('https://docs.google.com/spreadsheet/ccc?key=16uepDjfOVlVBqJyKFaPgwXDoyGGdnL23eEnZ73g4OeU&output=csv&gid=1575276786')
    df = response2.dropna(subset=['Date Filed'])
    #response = response[response2.columns]
    #print(response)
    print(df)
    print(df.loc[int(df['Days Between Eviction and Leave Premises']) > 0])

    #print(response2.loc[response2['Case Number (Duplicate Highlights)'] == '79D04-2008-SC-001319'])
    #print(response.append9response2)
    #print(response2)
    #df = pd.concat([response, response2])

def new():
    response2019 = pd.read_csv('https://docs.google.com/spreadsheet/ccc?key=16uepDjfOVlVBqJyKFaPgwXDoyGGdnL23eEnZ73g4OeU&output=csv&gid=197192004')
    response2020 = pd.read_csv('https://docs.google.com/spreadsheet/ccc?key=16uepDjfOVlVBqJyKFaPgwXDoyGGdnL23eEnZ73g4OeU&output=csv&gid=1575276786')
    response2019[["Amount Owed (Excludes Court Cost)"]] = response2019[["Amount Owed (Excludes Court Cost)"]].apply(pd.to_numeric, errors='coerce')
    response2020[["Judgement Amount"]] = response2020[["Judgement Amount"]].apply(pd.to_numeric, errors='coerce')
    response2019 = response2019.dropna(subset=['Amount Owed (Excludes Court Cost)'])
    response2020 = response2020.dropna(subset=['Judgement Amount'])
    
    print(response2019["Amount Owed (Excludes Court Cost)"].mean(),len(response2019["Amount Owed (Excludes Court Cost)"]))
    print(response2020["Judgement Amount"].mean(), len(response2020["Judgement Amount"]))


if __name__ == '__main__':
    new()