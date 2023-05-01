import requests


def get_info():
    # Api request; API запрос
    response = requests.get(url="https://yobit.net/api/3/info")
    # Write response; Пишем ответ в файл
    with open("info.txt", "w") as file:
        file.write(response.text)
    return response.text


def get_ticker(coin1="btc", coin2="usd"):
    # Requesting information on a couple; Запрашиваем информацию по паре
    # If you need several pairs, separate with a hyphen '-'; Если нужно несколько пар, разделяем дефисом '-'
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")
    with open("ticker.txt", "w") as file:
        file.write(response.text)
    return response.text


def get_depth(coin1="btc", coin2="usd", limit=150):
    # Get info by order; Получаем информацию по актуальным ордерам
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
    with open("depth.txt", "w") as file:
        file.write(response.text)
    # Parsing buy orders; Парсинг ордеров на покупку
    bids = response.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]
        # Multiply the price by the number of coins; Умножаем прайс на количество монет
        total_bids_amount += price * coin_amount

    return f"Total bids {total_bids_amount}$"


def main():
    # print(get_info())
    # print(get_ticker())
    print(get_depth())

if __name__ == "__main__":
    main()