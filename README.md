# avis-python-stock-lookup-tool
Program takes in user input stock ticker and saves a csv file and graph png to 'results' folder of previous day's prices

## Function overview:
main: takes in desired stock name and passes to verification function, prints statuses of data and file
downloads

take_in_stock_price(prompt): verifies validity of user input ticker, if invalid user is re-prompted, if valid ticker
data from last 24 hours is gathered. returns downloaded data as 'data' and user specified ticker as 'input_ticker' to
main

export_data_to_csv(dataframe, ticker): writes downloaded stock price data (dataframe) into a csv file and saves in
dedicated directory folder 'results' in 'cs50_final' directory under the relevant ticker name (ticker) gathered from
the user and called from main.

create_graph_as_png(dataframe, ticker): plots stock price data on line graph using stock price data (dataframe) and
saves the image as a .png file in dedicated directory folder 'results' in 'cs50_final' directory under relevant
ticker name (ticker) from main.

## Inputs and Outputs
Input: valid stock exchange ticker

Output: .csv of price data from previous day of user chosen ticker and .png line graph of
price data

## Demonstration
https://www.youtube.com/watch?v=-krfl6gwz4s
