import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! and WELCOME!!, I am Ibrahim Let\'s explore some US bikeshare data!')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease select the city you would like to explore, the cities are: \nchicago \nnew york city \nwashington\n")
        city = city.lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("sorry invalid input please try again with a valid city name, the cities are:\nchicago \nnew york city \nwashington\n")
            continue
        else:
            break


        # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select the month you will like to filter by, the months are:\nJanuary \nFebruary \nMarch \nApril \nMay \nJune\n")
        month = month.lower()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print('please enter a valid month from january to june\n')
            continue
        else:
            break


        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Select the day you will like to filter by, the months are:\nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nSunday\n")
        day = day.lower()
        if day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('please enter a valid day of the week from monday to sunday')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from Start Time
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
    df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:  {}'.format(common_month))


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is:  {}'.format(common_day))


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:  {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:  {}'.format(common_start_station))


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:  {}'.format(common_end_station))


    # display most frequent combination of start station and end station trip
    start_end_comb = df.groupby(['Start Station', 'End Station'])
    most_frequent_trip_comb_count = start_end_comb['Trip Duration'].count().max()
    most_freq_start_end_trip = start_end_comb['Trip Duration'].count().idxmax()
    print('The most frequent combination of start and end station is:  {},  {}'.format(most_freq_start_end_trip[0], most_freq_start_end_trip[1]))
    print('With total trip of {}'.format(most_frequent_trip_comb_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is', total_travel_time/86400, "Days")


    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is ', average_travel_time/60, "munites")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('The user types and thier total number are:\n {}'.format(counts_of_user_types))


    # Display counts of gender
    try:
        print('Total gender count is:')
        counts_of_gender = df['Gender'].value_counts()
        print(counts_of_gender)
    except:
        print('There is no data available for this selection')

    # Display earliest, most recent, and most common year of birth
    try:
        print('Birth year statistics:')
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest year of birth is:' + str(earliest))
        print('The most recent year of birth:' + str(most_recent))
        print('The most common year of birth is:' + str(most_common))
    except:
        print('There is no data available for this selection')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Display raw data
def more_data(df):
    st = 0
    raw_data = input('Would you like to see raw data   yes or no?\n')
    while raw_data.lower() == 'yes':
        first_five_lines = df.iloc[st: st+5]
        print('The five lines of the raw data is:\n {}'.format(first_five_lines))
        st += 5
        raw_data = input('Would you like to see five more lines of the raw data  yes or no?\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)
          # ask if the user wishes to restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
