class Album:

    def __init__(self, artist, title, year_released, genre, stock_qty, purchase_price, sell_price, id = None):
        self.artist = artist
        self.title = title
        self.year_released = year_released
        self.genre = genre
        self.stock_qty = stock_qty
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.id = id

    def purchase_price_formatted(self):
        return f"£{self.purchase_price:.2f}"
    
    def sell_price_formatted(self):
        return f"£{self.sell_price:.2f}"
