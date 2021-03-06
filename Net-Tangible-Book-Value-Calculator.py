from bs4 import BeautifulSoup
import requests

stock_ticker = ['TSLA', 'ATVI', 'AAPL']
for value in stock_ticker:
    URLS = 'https://finance.yahoo.com/quote/{}/balance-sheet?p={}'.format(value, value)
    page = requests.get(URLS)
    soup = BeautifulSoup(page.content, 'html.parser')
    numbers = []
    company_values = []
    table_div = soup.find('div', class_ = "D(tbrg)")
    row_divs = table_div.find_all('div', recursive = False)
    total_assests_row = row_divs[0]
    total_liabilities_row = row_divs[1]
    total_shares_row = row_divs[11]
    total_assests_col = (total_assests_row.find('div', class_ = "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg D(tbc)"))
    total_liabilities_col = (total_liabilities_row.find('div', class_ = "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg D(tbc)"))
    total_shares_col = (total_shares_row.find('div', class_ = "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg D(tbc)"))
    total_assests_price = total_assests_col.find('span')
    total_liabilities_price = total_liabilities_col.find('span')
    total_shares_number = total_shares_col.find('span')
    stock_price = soup.find('div', class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    net_tangible_book_value = float(total_assests_price) - float(total_liabilities_price) / float(total_shares_number) / float(stock_price)
    company_values.append(net_tangible_book_value)
company_values.sort(reverse=True)
print(company_values)
