import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

RISK_FREE_RATE = 0.05
MONTHS_IN_YEAR = 12

class CAPM:

    def __init__(self, stocks, start_date, end_date):
        self.data = None
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        data = {}
        for stock in self.stocks:
            ticker = yf.download(stock, self.start_date, self.end_date, multi_level_index=False, auto_adjust=False)
            data[stock] = ticker['Adj Close']

        return pd.DataFrame(data)

    def initialise(self):
        stock_data = self.download_data()
        stock_data = stock_data.resample('ME').last()
        self.data = pd.DataFrame({'s_adjclose': stock_data[self.stocks[0]],
                                  'm_adjclose': stock_data[self.stocks[1]]})
        self.data[['s_returns', 'm_returns']] = np.log(self.data[['s_adjclose', 'm_adjclose']]/self.data[['s_adjclose', 'm_adjclose']].shift(1))
        self.data = self.data[1:]

    def calculate_beta(self):
        covariance_matrix = np.cov(self.data['s_returns'], self.data['m_returns'])
        beta = covariance_matrix[0,1]/covariance_matrix[1,1]
        print('Beta from formula: ', beta)

    def regression(self):
        beta, alpha = np.polyfit(self.data['m_returns'], self.data['s_returns'], deg=1)
        print('Beta from regression: ', beta)
        expected_returns = RISK_FREE_RATE + beta*(self.data['m_returns'].mean()*MONTHS_IN_YEAR - RISK_FREE_RATE)
        print('Expected returns: ', expected_returns)
        self.plot_regressions(alpha, beta)

    def plot_regressions(self, alpha, beta):
        fig, axis = plt.subplots(1, figsize=(12,8))
        axis.scatter(self.data['m_returns'], self.data['s_returns'], label = 'Data Points')
        axis.plot(self.data['m_returns'], beta*self.data['m_returns']+alpha, label = 'CAPM Line', color = 'red')
        plt.title('Capital Asset Pricing Model Graph', fontsize = 16)
        plt.xlabel('Market Returns $R_m$', fontsize = 12)
        plt.ylabel('Stock Returns $R_a$', fontsize = 12)
        plt.text(0.07, 0.04, r'$R_a = \beta * R_m + \alpha$', fontsize = 12)
        plt.show()

if __name__ == '__main__':
    capm = CAPM(['BAJFINANCE.NS', '^NSEI'], '2010-01-01', '2017-01-01')
    capm.initialise()
    capm.calculate_beta()
    capm.regression()