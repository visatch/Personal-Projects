from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import requests
import random
import time
from typing import List


OUTPUT_FILE_POWERBALL = "V:/Python Project/lottery_number_api/list_of_winning_numbers_powerball.txt"
OUTPUT_FILE_MEGAMILLION = "V:/Python Project/lottery_number_api/list_of_winning_numbers_megamillion.txt"
URL_MEGAMILLION = "https://www.calottery.com/draw-games/mega-millions#section-content-2-3"
URL_POWERBALL = "https://www.calottery.com/draw-games/powerball#section-content-2-3"

CHROME_DRIVER_PATH = "V:/Python Project/chromedriver.exe"

# newLine must be join by space before passing to this function
def prepend_line_to_beginning_of_a_file(FILE: str,newLine: str):
    with open(FILE,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(newLine.rstrip('r\n') + '\n' + content)

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

    for i in rows_data:
        # Retrive the winning from the webpage
        winning_numbers_as_string = i.find_element(By.CSS_SELECTOR,".col-12 > div > .sr-only").text
        
        # Clean the text and make it as a list of numbers
        winning_numbers = clean_the_winning_numbers(winning_numbers_as_string)
        
        # prepend the numbers into the destination file
        prepend_line_to_beginning_of_a_file(OUTPUT_FILE_MEGAMILLION,' '.join(winning_numbers))

        print(' '.join(winning_numbers))

# load the file and return a list
def load_the_file(FILE:str) -> List[int]:
    with open(FILE,'r') as file:
        result = []
        for line in file:
            numbers = list(map(int,line.split(' ')))
            result.append(numbers)

    return result

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

def update_win_number_list(URL: str, FILE: str):
    #set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")    

    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(URL)

    time.sleep(5)
    content = driver.find_elements(By.CSS_SELECTOR,"#winningNumbers{} > div.card-body.d-flex.justify-content-center > ul > li".format("15" if URL == URL_MEGAMILLION else "12"))

    numbers = []
    for i in content:
        numbers.append(i.find_element(By.TAG_NAME,"span").text)
        
    prepend_line_to_beginning_of_a_file(FILE,' '.join(str(num) for num in numbers))

if __name__ == "__main__":
    # scrap_past_powerball_winning_numbers("https://portalseven.com/lottery/megamillions_winning_numbers.jsp?fromDate=2022-06-23&toDate=2023-06-23&viewType=3"
    #                                      ,OUTPUT_FILE_MEGAMILLION, 1)
    
    # scrap_winning_number_from_calottery_website("https://www.calottery.com/draw-games/mega-millions#section-content-2-3")
    
    # print(generate_powerball())
    # print(' '.join(str(num) for num in generate_megamillions()))
    update_win_number_list(URL_MEGAMILLION,OUTPUT_FILE_MEGAMILLION)

    #! List 
    #todo: Powerball -> Monday, Wednesday, Saturday
    #todo: MegaMillion -> Tuesday and Friday

