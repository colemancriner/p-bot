import ezgmail
from bs4 import BeautifulSoup
import requests as r
from datetime import datetime, timedelta
import random


# Create a delay between 4 and 7 seconds
end_sleep_time = datetime.now()
def delay():
    global end_sleep_time
    base_delay = 5
    jitter = random.uniform(-1, 3)  # Adds up to -1 to +3 seconds
    delay = base_delay + jitter
    while datetime.now() < end_sleep_time:
        pass
    if datetime.now() > end_sleep_time:
        end_sleep_time = datetime.now() + timedelta(seconds=delay)


# User Agents
def get_user_agent():
    user_agents = [
    # Chrome on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",

    # Firefox on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",

    # Edge on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.67",

    # Chrome on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",

    # Safari on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    
    # Chrome on Android
    "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",

    # Safari on iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

# Check for add to cart button
def check_for_add_to_cart_button(url):
    headers = {"User-Agent": get_user_agent()}
    delay()
    response = r.get(url, headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    
    # if Out of stock is nowhere to be found, then find add to cart button
    out_of_stock_element = soup.find(string=lambda text: text and "out of stock" in text.lower())
    print(out_of_stock_element)
    
    if out_of_stock_element:
        print("Product is out of stock")
        return False
        
    else:
        # Find the button with exact text
        button = soup.find('button', string="Add to cart")
        if button:
            print("Button found")
            return True
        else:
            print("Out of stock")
            return False
        


def loop_notify():
    is_button = False
    while is_button == False:
        is_button = check_for_add_to_cart_button('https://www.target.com/p/2024-pok-scarlet-violet-s8-5-elite-trainer-box/-/A-93954435')
        is_button = True
    #ezgmail.send('colemanccriner@gmail.com', 'BuyBot Test 2', 'Buy Now: https://www.target.com/p/pokemon-sword-and-shield-evolving-skies-booster-display-box-36-packs-of-10-cards/-/A-1000940829#lnk=sametab')



#================================================================================
#================================================================================
#================================================================================

loop_notify()