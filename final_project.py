"""

Program takes in user input stock ticker and saves a csv file and graph png to 'results' folder of previous day's
prices

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

Input: valid stock exchange ticker
Output: .csv of price data from previous day of user chosen ticker and .png line graph of
price data

"""

import pandas as pd
import yfinance as yf  # data source
import plotly.graph_objects as go


def main():
    data, user_input_ticker, status = take_in_stock_price('Enter stock ticker to gather price from last 1 days: ')
    # print('\n', data.head(2), '\n')
    # print(user_ticker)
    print(export_data_to_csv(dataframe=data, ticker=user_input_ticker)) # status message
    print(create_graph_as_png(dataframe=data, ticker=user_input_ticker)) # status message


def take_in_stock_price(prompt):  # if invalid ticker is passed, yahoo finance passes empty dataset
    while True:
        try:
            input_ticker = input(prompt)
            data = yf.download(tickers=input_ticker, period='1d',
                               interval='2m')  # tries to gather relevant data from Yahoo

            if data.empty:  # if invalid ticker is given, an empty dataframe is returned
                raise Exception
            break
        except Exception:  # if invalid ticker and empty dataframe returned, reprompt user
            print('Invalid ticker \n')
            pass

    return data, input_ticker, True


def export_data_to_csv(dataframe, ticker):
    df = pd.DataFrame(dataframe) # converts to pandas dataframe
    df.to_csv('/Users/avi_singh/cs50_final/results/' + ticker + '.csv') # pandas dataframe written to csv
    return 'Data written to file', True


def create_graph_as_png(dataframe, ticker): # plots graph
    figure = go.Figure(data=go.Scatter(
        x=dataframe.index,  # x axis should be datetime
        y=dataframe['Close'], # y axis should be final price
        mode='lines')) # joined lines

    figure.update_layout( # x and y axis titles
        title=ticker+' 24 Hour Stock Price',
        yaxis_title='Stock Price (USD per Shares)')

    figure.write_image('/Users/avi_singh/cs50_final/results/' + ticker + '.png')

    return 'Graph saved to file', True


if __name__ == '__main__':
    main()
