from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import schedule
import requests
import random
import time
from typing import List
from enum import Enum

OUTPUT_FILE_POWERBALL = "V:\Personal Projects\Python Project\lottery_number_api\list_of_winning_numbers_powerball.txt"
OUTPUT_FILE_MEGAMILLION = "V:\Personal Projects\Python Project\lottery_number_api\list_of_winning_numbers_megamillion.txt"
URL_MEGAMILLION = "https://www.calottery.com/draw-games/mega-millions#section-content-2-3"
URL_POWERBALL = "https://www.calottery.com/draw-games/powerball#section-content-2-3"

CHROME_DRIVER_PATH = "V:/Python Project/chromedriver.exe"

class DayofWeek(Enum):
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'

# newLine must be join by space before passing to this function
def prepend_line_to_beginning_of_a_file(FILE: str,lt: List):
    if len(lt) == 0:
        return

    with open(FILE,'r+') as f:
        top_line = f.readline()
        content = top_line + f.read() 

        most_recent_winning_numbers = [int(num) for num in top_line.split()]

        result = ""
        for i in lt:
            if i == most_recent_winning_numbers:
                break
            result += ' '.join(str(num) for num in i) + '\n'

        f.seek(0,0)
        f.write(result.strip() + '\n' + content)

    # with open(FILE,'r+') as f:
    #     top_line = f.readline()
    #     content = top_line + f.read() 
    #     most_recent_winning_numbers = [int(num) for num in top_line.split()]
    #     f.seek(0)
    #     for i in lt:
    #         if i == most_recent_winning_numbers:
    #             break
    #         f.write(' '.join(str(num) for num in i) + '\n') 
    #     f.write(content)
    #     f.truncate()

# load the file and return a list
def load_the_file(FILE: str) -> List[int]:
    with open(FILE,'r') as file:
        result = []
        for line in file:
            numbers = list(map(int,line.split(' ')))
            result.append(numbers)
    return result

# URL= https://portalseven.com/lottery/megamillions_winning_numbers.jsp?fromDate=2022-06-23&toDate=2023-06-23&viewType=3
# FILE -> File to store, SKIP -> Number to skip from the right 'row_of_nums', for example [1,2,3,4,5] if skip = 1 => [1,2,3,4] otherwise, loop entire list
def scrap_past_powerball_winning_numbers(URL: str,FILE: str, SKIP: int):
    webpage = requests.get(URL)

    soup = BeautifulSoup(webpage.content,"html.parser")

    data_table = soup.find("table",{"class":"table table-bordered table-condensed table-striped text-center table-hover"})
    data_table = data_table.find_all('tr')

    with open(FILE,"a") as output:
        for row in data_table[1:]:
            list_nums = []
            date = row.find('td',{"class":"text-left"}).string
            row_of_nums = row.find_all('b')
            
            for i in row_of_nums[:-SKIP] if SKIP != 0 else row_of_nums:
                list_nums.append(i.string)

            print(list_nums)
            output.write(' '.join(list_nums) + '\n')

#Exactly only the numbers and return a list of number
def clean_the_winning_numbers(text: str) -> List[int]:
    import re
    return re.findall(r'\d+', text)


# https://www.calottery.com/draw-games/mega-millions#section-content-2-3
def scrap_winning_number_from_calottery_website(URL: str):
    #set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")    

    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(URL)

    time.sleep(5)

    # driver.find_element(By.ID,"section-title-2-3").click()

    content = driver.find_element(By.ID,"past-winners-accordion")
    rows_data = content.find_elements(By.CLASS_NAME,"card")

    winning_numbers_list = []
    for i in rows_data:
        # Retrive the winning from the webpage
        uncleaned_winning_numbers_as_string = i.find_element(By.CSS_SELECTOR,".col-12 > div > .sr-only").text
        
        # Clean the text and make it as a list of numbers
        winning_numbers = clean_the_winning_numbers(uncleaned_winning_numbers_as_string)

        # Append the list of numbers into the list
        winning_numbers_list.append(winning_numbers)

        print(' '.join(winning_numbers))

    # prepend the numbers into the destination file
    prepend_line_to_beginning_of_a_file(OUTPUT_FILE_MEGAMILLION,winning_numbers_list)

# Compare two lists if all same return true otherwise false
def compare_two_lists(l1: List[int], l2: List[int]) -> bool:
    pass

def generate_powerball() -> List[int]:
    white_balls = list(range(1, 70))
    red_ball = list(range(1, 27))
    
    past_winning_numbers = load_the_file(OUTPUT_FILE_POWERBALL)
    generated_numbers = []

    while True:
        generated_numbers = random.sample(white_balls, 5), random.choice(red_ball)
        generated_numbers = generated_numbers[0] + [generated_numbers[1]]

        if  generated_numbers not in past_winning_numbers:
            break

    return generated_numbers

def generate_megamillions() -> List[int]:
    white_balls = list(range(1, 71))
    red_ball = list(range(1, 26))

    past_winning_numbers = load_the_file(OUTPUT_FILE_MEGAMILLION)
    generated_numbers = []

    while True:
        generated_numbers = random.sample(white_balls, 5), random.choice(red_ball)
        generated_numbers = generated_numbers[0] + [generated_numbers[1]]

        if  generated_numbers not in past_winning_numbers:
            break

    return generated_numbers


#! To be implemented: Adjust the function to update the winning number list by comparing what is on the wesbiste to the most recent one in the file (the first line)
def update_win_number_list(URL: str, FILE: str):
    #set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")   
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating")
    chrome_options.add_argument("--disable-site-isolation-trials") 

    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.implicitly_wait(5)
    
    most_recent_winning_numbers = []
    with open(FILE,'r') as f:
        most_recent_winning_numbers = [int(num) for num in f.readline().split()]
        
    driver.get(URL)

    time.sleep(5)
    # content = driver.find_elements(By.CSS_SELECTOR,"#winningNumbers{} > div.card-body.d-flex.justify-content-center > ul > li".format("15" if URL == URL_MEGAMILLION else "12"))
    content = driver.find_elements(By.CSS_SELECTOR,"#past-winners-accordion > .card")

    #! fix this without use get_attribute 
    numbers = []
    for i in content:
        tmp = []
        winning_numbers = i.find_elements(By.CSS_SELECTOR,".row > div.col-12.col-md-4 > div > ul > li > span")
        
        for j in winning_numbers[:-1]:
            tmp.append(int(j.get_attribute("innerText")))
        
        if most_recent_winning_numbers != tmp:
            numbers.append(tmp) 
        else:
            break

    driver.quit()

    print(numbers)
    
    prepend_line_to_beginning_of_a_file(FILE,numbers)


def daily_update_winning_numbers(URL: str, FILE: str, listDaytoRun: List):
    def job():
        update_win_number_list(URL,FILE)
    
    for day in listDaytoRun:
        getattr(schedule.every(), day).at("23:00").do(job)

app = Flask(__name__)

@app.route('/api/get_lottery_numbers', methods=['GET'])
def get_both_lottery_numbers():
    powerball_number = generate_powerball()
    megamillio_number = generate_megamillions()
    return jsonify({'powerball':' '.join(str(num) for num in powerball_number),'mega_million':' '.join(str(num) for num in megamillio_number)})

@app.route('/api/get_powerball', methods=['GET'])
def get_powerball_numbers():
    return jsonify({'powerball':' '.join(str(num) for num in generate_powerball())})

@app.route('/api/get_megamillion', methods=['GET'])
def get_megamillion_numbers():
    return jsonify({'mega_million':' '.join(str(num) for num in generate_megamillions())})


if __name__ == "__main__":
    app.run(port=5000)

    # scrap_past_powerball_winning_numbers("https://portalseven.com/lottery/megamillions_winning_numbers.jsp?fromDate=2022-06-23&toDate=2023-06-23&viewType=3"
    #                                      ,OUTPUT_FILE_MEGAMILLION, 1)
    
    # scrap_winning_number_from_calottery_website(URL_MEGAMILLION)
    
    # print(generate_powerball())
    # print(' '.join(str(num) for num in generate_megamillions()))
    # #? MEGA MILLION
    # update_win_number_list(URL_MEGAMILLION,OUTPUT_FILE_MEGAMILLION)

    # #? POWERBALL
    # update_win_number_list(URL_POWERBALL,OUTPUT_FILE_POWERBALL)

    # print(generate_powerball())
    # print(generate_megamillions())

    # daily_update_winning_numbers(URL_POWERBALL,OUTPUT_FILE_POWERBALL,['monday','wednesday','saturday'])
    # daily_update_winning_numbers(URL_MEGAMILLION,OUTPUT_FILE_MEGAMILLION,['tuesday','friday'])

    # for job in schedule.jobs:
    #     print(job.next_run)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # lt = [
    #     [13, 62, 65, 67, 69, 14],
    #     [6, 37, 39, 45, 46, 21],
    #     [4, 24, 34, 45, 57, 19],
    #     [8, 10, 19, 44, 47, 4],
    #     [3, 19, 53, 60, 68, 13],
    #     [6, 12, 23, 29, 57, 4],
    #     [3, 16, 19, 36, 60, 25],
    #     [13, 16, 40, 64, 68, 21],
    #     [12, 20, 37, 41, 64, 1],
    #     [3, 10, 22, 65, 66, 19],
    #     [5, 11, 41, 44, 55, 14],
    #     [15, 34, 36, 69, 70, 17],
    #     [1, 2, 23, 40, 45, 15],
    #     [4, 37, 46, 48, 51, 19],
    #     [16, 18, 28, 42, 43, 11],
    #     [3, 15, 16, 32, 41, 9],
    #     [18, 38, 53, 62, 64, 20],
    #     [8, 29, 46, 47, 48, 12],
    #     [3, 21, 29, 46, 63, 9],
    #     [7, 9, 15, 19, 25, 4]
    # ]

    # prepend_line_to_beginning_of_a_file('V:/Personal Projects/Python Project/lottery_number_api/test.txt',lt)
    # with open(OUTPUT_FILE_MEGAMILLION,'r') as f:
    #     print(f.readline())
    #     print(content)
    #     # print([int(num) for num in content[0].split()])

    #     result = ""
    #     for i in lt:
    #         if i == most_recent_winning_numbers:
    #             break
    #         result += str(i) + "\n"


    #! List 
    #todo: Powerball -> Monday, Wednesday, Saturday
    #todo: MegaMillion -> Tuesday and Friday

