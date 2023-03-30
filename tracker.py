import tkinter as tk
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG)

class CryptoTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Crypto Tracker")
        self.window.geometry("200x120")
        self.window.attributes('-alpha', 0.2)
        self.num_rows = 5
        self.bitcoin_prices = {"Bitcoin": 0, "Ethereum": 0, "Binance Coin": 0, "Cardano": 0, "Dogecoin": 0}
        self.create_widgets()
        self.update_prices()
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.mainloop()

    def create_widgets(self):
        self.price_labels = []
        for i, coin in enumerate(self.bitcoin_prices.keys()):
            bitcoin_label = tk.Label(self.window, text="", font=("Arial", 14), fg="black")
            bitcoin_label.pack()
            self.price_labels.append(bitcoin_label)

    def update_prices(self):
        response = requests.get("https://api.coingecko.com/api/v3/ping")
        if response.status_code == 200:
            logging.debug("API is up and running!")
        else:
            logging.error("API is down!")

        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cbinancecoin%2Ccardano%2Cdogecoin&vs_currencies=usd")
        if response.status_code == 200:
            logging.debug("API is up and running!")
            prices = response.json()
            for i, (coin, price) in enumerate(prices.items()):
                self.bitcoin_prices[coin] = price["usd"]
                self.price_labels[i].config(text=f"{coin}: ${price['usd']}")
        else:
            logging.error("API is down!")

        self.window.after(10000, self.update_prices)

if __name__ == "__main__":
    app = CryptoTracker()