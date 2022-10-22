# STEP ONE

import asyncio
import time


async def main():
    start_time = time.time()

    print('Saving the output of extracted information')

    time_difference = time.time() - start_time
    print(f'Scraping time: %2f seconds.' % time_difference)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# STE TWO

import asyncio
import csv
import time


async def main():
    start_time = time.time()

    with open('urls.csv') as file:
        csv_reader = csv.DictReader(file)
        for csv_row in csv_reader:
            # the url from csv can be found in csv_row['url']
            print(csv_row['url'])

    time_difference = time.time() - start_time
    print(f'Scraping time: %2f seconds.' % time_difference)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# STEP THREE

