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


def main():
    # print(get_info())
    print(get_ticker())


if __name__ == "__main__":
    main()