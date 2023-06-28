from main import daily_update_winning_numbers, URL_MEGAMILLION, URL_POWERBALL, OUTPUT_FILE_MEGAMILLION,OUTPUT_FILE_POWERBALL
import schedule
import time

if __name__ == '__main__':
    daily_update_winning_numbers(URL_POWERBALL,OUTPUT_FILE_POWERBALL,['monday','wednesday','saturday'])
    daily_update_winning_numbers(URL_MEGAMILLION,OUTPUT_FILE_MEGAMILLION,['tuesday','friday'])

    # for job in schedule.jobs:
    #     print(job.next_run)
    
    while True:
        schedule.run_pending()
        time.sleep(1)