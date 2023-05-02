from binance import Binance
bot = Binance(
    API_KEY='pBqSe8dSaWrrY0U99LrTECkHg4pDXVfbvJqAx6SQL2RMmbcHxyzKk4az0D6OMSHT',
    API_SECRET='LxtnTxrVKHwqcORQInzVew2CDzVzEWeUPxFonkp4QBgtOQkFi39UpBZnJxFJqzS9'
)

print('debth', bot.depth(
    symbol="BTCUSDT",
    limit=500
))