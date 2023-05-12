class Asset:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class Stock(Asset):
    def __init__(self, price, quantity, ticker):
        super().__init__(price, quantity)
        self.ticker = ticker

class Bond(Asset):
    def __init__(self, price, quantity, issuer, maturity_date):
        super().__init__(price, quantity)
        self.issuer = issuer
        self.maturity_date = maturity_date

class Currency(Asset):
    def __init__(self, price, quantity, currency_code):
        super().__init__(price, quantity)
        self.currency_code = currency_code

class Commodity(Asset):
    def __init__(self, price, quantity, commodity_type):
        super().__init__(price, quantity)
        self.commodity_type = commodity_type

class Cryptocurrency(Asset):
    def __init__(self, price, quantity, crypto_symbol):
        super().__init__(price, quantity)
        self.crypto_symbol = crypto_symbol

class Regulation:
    def __init__(self, capital_requirement, leverage_limit, transaction_tax):
        self.capital_requirement = capital_requirement
        self.leverage_limit = leverage_limit
        self.transaction_tax = transaction_tax

    def apply(self, agent):
        agent.capital -= self.transaction_tax * agent.trade_value
        agent.leverage = min(agent.leverage, self.leverage_limit)

class Agent:
    def __init__(self, capital, leverage, trade_value):
        self.capital = capital
        self.leverage = leverage
        self.trade_value = trade_value

    def trade(self, asset, quantity, regulation):
        self.trade_value = asset.price * quantity
        self.capital -= self.trade_value
        asset.quantity -= quantity

        # Примените регуляторные меры
        regulation.apply(self)
