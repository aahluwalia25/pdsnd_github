import time
import pandas as pd
# import numpy as np  Doesn't look like numpy is used at all
# load data files into a dataframe

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv', 'new york': 'new_york_city.csv', 'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }
#This function loads the data from a csv
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv('C:\\Users\\Anoop\\OneDrive\\Desktop\\' + CITY_DATA[city])
    
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
        # filter by month if applicable
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months:
            print('Sorry but data is only available for months January through June. Please select an appropriate month.')
            return None
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        weekday_nums= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        weekday_num = weekday_nums.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == weekday_num]
    return df

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('What city would you like to explore data for? Please enter Chicago, New York City, Washington.')
    city = input('City:\n')
    city = city.lower().strip()
    # TO DO: get user input for month (all, january, february, ... , june)
    print('What month would you like to explore data for? Please choose a month from January through June or All')
    month = input('Month:\n')
    month = month.lower().strip()
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('What day of the week would you like more information about? Please enter a day Sunday through Saturday or All')
    day = input('Day:\n')
    day = day.lower().strip()
    
    print('-'*40)
    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most popular month is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most popular day is:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    print('The most popular start station is ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most popular end station is ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most popular combination of start station and end station trip is', (df['Start Station'] + ' AND ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    
    start_time = time.time()
  
    # TO DO: display total travel time
    print('The total trip duration is ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average duration of each trip:\n', round(df['Trip Duration'].mean(), 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()

    print('Most popular user type is', user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
    except: 
        gender_count = 0
        
    print('Most bikes are rented by', gender_count)
    

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Your docstring here """
    i = 0

    pd.set_option('display.max_columns',200)

    while True:      
        raw = input("Would you like to see next five lines of raw data for your chosen city?. Please enter Yes or NO.\n")
        raw = raw.lower().strip()
        if raw == 'y' or raw =='ye' or raw == 'yes': 
            print(df[i:i+5]) 
            i += 5
        elif raw == 'no' or raw =='n':
            break
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day) 
        if df is None: 
            continue
        print(df)
        user_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        time_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y', 'ye']:
            break
    
if __name__ == "__main__":
	main()

