import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.flipkart.com/cinthol-deo-stick-women-40g-pack-3-deodorant-women/p/itmf47n5wrfzyg68"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {"class": "_35KyD6"}).get_text()
    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    converted_price = price[1:4]

    if(converted_price <= 200 ):
        send_mail()

    print(converted_price)
    print(title)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('preethamkachhadiya@gmail.com', 'jobliohjfzazjjso')

    subject = "Price Fell Down Of Cinthol Deo Stick!"
    body = "Check the FlipKart link  https://www.flipkart.com/cinthol-deo-stick-women-40g-pack-3-deodorant-women/p/itmf47n5wrfzyg68"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'preethamkachhadiya@gmail.com',
        'preethamkachhadiya@gmail.com',
        msg
    )

    print("HEY!! EMAIL HAS BEEN SENT.")
