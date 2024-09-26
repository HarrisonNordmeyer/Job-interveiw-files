
def showDate(date, tweet_records):
    # Counter to track the number of tweets on the given date
    tweet_count = 0

    # Iterate through each tweet record
    for tweet_record in tweet_records:
        # Check if the tweet's date matches the given date
        if tweet_record['date (UCT)'] == date:
            # Print the text of the tweet
            print(tweet_record['tweet'])
            # Increment the tweet count
            tweet_count += 1

    # Print a blank line
    print()

    # Print the number of tweets on the given date
    print(f"There were {tweet_count} tweets on {date}")

def allHours(tweet_list):
    hour_counts = {hour: 0 for hour in range(24)}

    for tweet in tweet_list:
        hour = int(tweet['time (UCT)'].split(':')[0])  
        hour_counts[hour] += 1

    print("HOUR  # TWEETS")

    for hour, count in sorted(hour_counts.items()):
        print(f"{hour:02d}    {count}")
        
def numBetween_and_showYears(start_date, end_date, tweet_list):

    def lessThan(date1, date2):
        [month1, day1, year1] = [int(x) for x in date1.split("/")]
        [month2, day2, year2] = [int(x) for x in date2.split("/")]
        return year1 < year2 or \
               (year1 == year2 and month1 < month2) or \
               (year1 == year2 and month1 == month2 and day1 < day2)

    count = 0
    year_count = {}

    for tweet in tweet_list:
        if lessThan(start_date, tweet['date (UCT)']) and lessThan(tweet['date (UCT)'], end_date):
            count += 1

        year = tweet['date (UCT)'].split('/')[2]
        year_count[year] = year_count.get(year, 0) + 1

    total = sum(year_count.values())

    for year, year_tweet_count in sorted(year_count.items()):
        print(f"{year} : {year_tweet_count}")

    print("TOTAL :", total)

def mostFrequent(tweet_list):
    """
    Returns the word that appeared most often in the tweet list and its corresponding count.
    """
    word_counts = {}

    for tweet in tweet_list:
        # Split the tweet into words by whitespace
        words = tweet.lower().split()
        for word in words:
            # Remove non-alphanumeric characters from the word
            cleaned_word = ''.join(char for char in word if char.isalnum())
            if cleaned_word:  # Check if the word is not empty after cleaning
                word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    max_word = max(word_counts, key=word_counts.get)
    max_count = word_counts[max_word]
    
    return max_word, max_count


import csv


def read_csv(filename):
    """
    Reads CSV data from the specified file and returns a list of dictionaries.
    Assumes the first row contains column headers.
    """
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


tweet_records = read_csv('elonmusk.csv')

showDate("7/12/20", tweet_records)


start_date = "10/27/23"
end_date = "10/29/23"


numBetween_and_showYears(start_date, end_date, tweet_records)


allHours(tweet_records)


print(mostFrequent([tweet['tweet'] for tweet in tweet_records]))
