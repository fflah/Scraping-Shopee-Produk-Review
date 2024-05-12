import requests
import csv
from datetime import datetime
import json


def load_cookie(cookies_json) -> dict:
    """This func is responsible to load cookie json to python dict"""
    cookies_data = None
    with open(cookies_json) as f:
        cookies_data = json.load(f)

    cookies_string = ""
    for index, data in enumerate(cookies_data):
        temp = f"{str(data['name'])}={data['value']}"

        if index < len(cookies_data) - 1:
            temp += ";"

        cookies_string += temp

    return cookies_string


def shopee(url, cookies_json):
    shop_url = url.split("/")
    cookies = load_cookie(cookies_json)

    if not cookies:
        print("Cookies not valid")
        return

    headers = {"content-type": "application/json", "cookie": cookies}

    user_id = shop_url[4]
    shop_id = shop_url[5].replace("rating?shop_id=", "")
    count = 0
    result = []
    while True:
        try:
            count += 6
            url = f"https://shopee.co.id/api/v4/seller_operation/get_shop_ratings_new?limit=6&offset={count}&replied=false&shopid={shop_id}&userid={user_id}"
            req = requests.request("GET", url, headers=headers, data={})
            data_req = req.json()
            data_review = []
            try:
                data_review = data_req["data"]["items"]
            except:
                break

            for value in data_review:
                data_result = {
                    "nama pengguna": value["author_username"],
                    "produk": value["product_items"][0]["name"],
                    "review": value["comment"],
                    "rating": value["rating_star"],
                    "waktu transaksi": datetime.fromtimestamp(value["ctime"]).strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                }
                result.append(data_result)
                print(f"Getting review from {data_result['nama pengguna']}")
        except KeyError:        
            break

    # save to csv
    keys = result[0].keys()
    with open(f"shoope_rating.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)
    print("Data saved at shoope_rating.csv")


if __name__ == '__main__':    
    # silakan ganti page rating toko jika ingin mengambil data review dan rating dari toko lain
    url_shop = "https://shopee.co.id/buyer/165232471/rating?shop_id=165230265"
    cookies_json = "cookies.json"
    shopee(url_shop, cookies_json)
