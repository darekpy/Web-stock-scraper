import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "user_scraper",
    "password": "Scr27td11",
    "database": "stockinfo_db"
}

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, args=["--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"])
    context = browser.new_context()
    page = context.new_page()

    product_symbol = input("Provide the product name: ") #Examples ap2151aw-7 ap21510fm-7 #ap2151dm8g-13

    while len(product_symbol) > 40:
        print("It's too long. A product name cannot have more than 40 characters.")
        product_symbol = input("Provide the product name: ")

    def scrape_tme():
        url = f"https://www.tme.eu/pl/details/{product_symbol}/"
        response = page.goto(url)
        
        if response.ok:
            page.locator(".c-buy-item-box__details")
            time.sleep(1)

            html_content = page.content()

            soup = BeautifulSoup(html_content, "html.parser")


            details_section = soup.find("div", class_="c-buy-item-box__details")
            current_stock = details_section.find("span", class_="o-in-stock__stock o-in-stock__stock--available")
                
            if current_stock != None:
                stock_amount = current_stock.get_text(strip=True)

                numbers_only = "".join(char for char in stock_amount if char.isdigit())

                return numbers_only
            else:
                return 0
        else:
            print("tme.eu: Invalid product name.")


    def scrape_digikey():
        url = "https://www.digikey.pl/"
        response = page.goto(url)

        search_box = page.get_by_placeholder("Wprowadź słowo kluczowe lub nr katalogowy")
        search_box.fill(product_symbol)
        search_box.press("Enter")
                
        if response.ok:
            try:
                page.locator(".tss-y10pf4-title")
                time.sleep(1)

                html_content = page.content()
                    
                soup = BeautifulSoup(html_content, "html.parser")


                current_stock = soup.find("div", attrs={"data-testid": "price-and-procure-title"}).find("span")
                    
                if current_stock != None:
                    stock_amount = current_stock.get_text(strip=True)

                    numbers_only = "".join(char for char in stock_amount if char.isdigit()) or "0" #Prints only the numbers without spaces or "0"

                    return numbers_only
                else:
                    return 0
            except Exception as e:
                print("digikey.pl: Invalid product name.")
        else: 
            print("Url adress is invalid.")


    tme_stock = scrape_tme()
    if tme_stock is not None:
        if int(tme_stock) > 0: print(f"Current stock at tme.eu is: {tme_stock}.")
        else: print("The product is not available at the moment.")

    digikey_stock = scrape_digikey()
    if digikey_stock is not None:
        if int(digikey_stock) > 0: print(f"Current stock at digikey.pl is: {digikey_stock}.")
        else: print("The product is not available at the moment.")

    #MySQL server connection
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        cursor = connection.cursor()
    
        
        insert_query1 = ("INSERT INTO tme_products (ProductName, ProductQuantity)"
                        "VALUES (%s, %s)"
                        "ON DUPLICATE KEY UPDATE ProductQuantity = VALUES(ProductQuantity)") #Only updates stock if symbol is the same
        data1 = (product_symbol, tme_stock)
        if tme_stock is not None:
            cursor.execute(insert_query1, data1)

        
        insert_query2 = ("INSERT INTO digikey_products (ProductName, ProductQuantity)"
                        "VALUES (%s, %s)"
                        "ON DUPLICATE KEY UPDATE ProductQuantity = VALUES(ProductQuantity)")
        data2 = (product_symbol, digikey_stock)
        if digikey_stock is not None:
            cursor.execute(insert_query2, data2)
        
        connection.commit()
        print("Records inserted/updated...\n")

        
        print("Updating values of records already added to the database.")
        #Extract data from column ProductName
        select_names_query1 = ("SELECT ProductName FROM tme_products")
        cursor.execute(select_names_query1)
        tme_products_items = cursor.fetchall()
        tme_items_extract = [item[0] for item in tme_products_items] #Extracts elements from tuples created by .fetchall()

        select_names_query2 = ("SELECT ProductName FROM digikey_products")
        cursor.execute(select_names_query2)
        digikey_products_items = cursor.fetchall()
        digikey_items_extract = [item[0] for item in digikey_products_items]

        #Extract data from column ProductQuantity
        select_quantity_query1 = ("SELECT ProductQuantity FROM tme_products")
        cursor.execute(select_quantity_query1)
        tme_products_values = cursor.fetchall()
        tme_values_extract = [item[0] for item in tme_products_values]

        select_quantity_query2 = ("SELECT ProductQuantity FROM digikey_products")
        cursor.execute(select_quantity_query2)
        digikey_products_values = cursor.fetchall()
        digikey_values_extract = [item[0] for item in digikey_products_values]

        print("At www.tme.eu:")
        for i, v in zip(tme_items_extract, tme_values_extract):
            product_symbol = i

            tme_stock = scrape_tme()
            
            data1 = (product_symbol, tme_stock)

            if tme_stock is not None:
                cursor.execute(insert_query1, data1)
            
            difference = abs(v - int(tme_stock))
            if int(tme_stock) != v:
                print(f"{product_symbol} - stock has changed by {difference}:\nFrom {v} to {int(tme_stock)}.")

            connection.commit()

        print("\nAt www.digikey.pl:")
        for i, v in zip(digikey_items_extract, digikey_values_extract):
            product_symbol = i

            digikey_stock = scrape_digikey()

            data2 = (product_symbol, digikey_stock)

            if digikey_stock is not None:
                cursor.execute(insert_query2, data2)

            difference = abs(v - int(digikey_stock))
            if int(digikey_stock) != v:
                print(f"{product_symbol} - stock has changed by {difference}:\nFrom {v} to {int(digikey_stock)}.")

            connection.commit()

        print("Update completed.")

        cursor.close()
    else:
        print("Connection to the server has failed.")

    connection.close()

    browser.close()