# Place any imports you need here!
# Helpful packages may include pandas, numpy, or sklearn.
import numpy as np

class Trader:
    def __init__(self):
        """
        The Trader class is instantiated once for each round.
        """

        # You may want to keep track of history.
        self.symbols = ['A', 'B', 'C', 'D']
        self.px_history = {sym: [] for sym in self.symbols}
        self.pos_history = {sym: [] for sym in self.symbols}

        self.pnl_this_round = 0

        self.max_abs_volume = 0

        # Keep in mind these params.
        self.TIMESTEPS_PER_ROUND = 252
        self.POS_LIMIT_BY_SYMBOL = 600_000
        self.POS_LIMIT_TOTAL = 1_000_000

        # You may want your bot to remember if it won the auction.
        self.won_auctions = {
            sym: False for sym in self.symbols
        }

        # TODO: ADD ANY ADDITIONAL INFO YOU WANT

    def WonAuctions(self, wins):
        """
        Our grader will call this function once, after PlaceBid,
        to tell you if you won the auction.
        Args:
            wins: dict[sym -> bool] telling you if you won.
        """
        # self.won_auctions = wins

        # bad form, but effectively will only trade "D". No bids
        # are made at auction
        self.won_auctions["D"] = True
    
    def BuyInfo(self, time, stock_prices, fund_prices):
        """
        Grader will call this self.TIMESTEPS_PER_ROUND times to 
        determine which hedge fund info you buy for that step.
        Args: 
            time: int, current time_step
            stock_prices: dict[sym -> float] of px this time step.
            hedge_prices: dict[sym -> float] of hedge px this step.
        Returns: 
            dict[symbol -> bool] of which symbols you choose to buy.
        """
        to_buy = {}

        # TODO: PICK WHICH HEDGE FUND DATA YOU WANT TO BUY.
        for sym in self.won_auctions:
            to_buy[sym] = False
            if self.won_auctions[sym]:
                to_buy[sym] = True
                if abs(fund_prices[sym]) > self.max_abs_volume:
                    self.max_abs_volume = fund_prices[sym]

        return to_buy

    def MakeTrades(self, time, fund_info, stock_prices):
        """ 
        Grader will call this self.TIMESTEPS_PER_ROUND times to 
        determine your buys/sells for that step.
        Args: 
            time: int, current time_step
            fund_info: dict[symbol -> float] of hedge fund ps for
                data that you bought. Do not assume the dict has
                keys for data you did not buy.
            stock_prices: dict[sym -> float] of px this time step.
        Returns: 
            dict[symbol -> float] of your positions. Positive is buy/long
                and negative is sell/ short.
        """
        trades = {}
        
        #TODO: PICK HOW TO MAKE TRADES.
        for sym in stock_prices:
            if self.won_auctions[sym]:
                trades[sym] = fund_info[sym]/self.max_abs_volume
            else:
                trades[sym] = 0


        # Be sure you don't trade more than self.POS_LIMIT_BY_SYMBOL of each.
        for sym in trades:
            max_pos = self.POS_LIMIT_BY_SYMBOL / stock_prices[sym]
            trades[sym] = np.clip(trades[sym], -max_pos, max_pos)

        # Be sure you don't trade more than self.POS_LIMIT_TOTAL total.
        total = sum([abs(trades[sym]) * stock_prices[sym] for sym in stock_prices])
        if total > self.POS_LIMIT_TOTAL:
            multiplier = self.POS_LIMIT_TOTAL / total
            for sym in stock_prices:
                trades[sym] = trades[sym] * multiplier

        return trades