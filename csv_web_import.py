from urllib import request

goog_url="https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"

def download_data(url):
    response = request.urlopen(url)
    data = response.read()
    data_str = str(data)
    lines = data_str.split("\\n")
    stock_file = r"goog.csv"
    fx = open (stock_file, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_data(goog_url)