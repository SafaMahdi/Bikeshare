# Explore US Bikeshare Data (Python Project)
""""
# Overview : 

In this project, you will make use of Python to explore data related to bike share systems
for three major cities in the United States—Chicago, New York City, and Washington.
You will write code to import the data and answer interesting questions about it
by computing descriptive statistics. You will also write a script that takes in raw
input to create an interactive experience in the terminal to present these statistics. 
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Choose a city name (chicago, new york city, washington):').lower()
    while city not in CITY_DATA.keys():
        print('Dear User, Please Enter a Valid City:')
        city = input('Choose a city name (chicago, new york city, washington):').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Choose a Month (january,february,march,april,may,june,all):').lower()
        if month not in ('january', 'february', 'march' , 'april', 'may', 'june', 'all'):
              print('Dear User, Please Enter a Valid Month:')
              continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tusday','wednesday','thursday','friday', 'saturday', 'all']
    while True:
        day = input('Choose a Day (sunday,monday,tusday,wednesday,thursday,friday,saturday,all):').lower()
        if day in days:
            break
        else:
            print('Dear User, Please Enter a Valid Day:')

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time & End Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march' , 'april', 'may', 'june']
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

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:',  most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day)
  
     # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is:' ,most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is :' , most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is :' , most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent combination of start station and end station trip is :' ,most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time :',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types : ', user_types)

    # TO DO: Display counts of gender
    try:
        the_gender = df['Gender'].value_counts()
        print('The gender',the_gender)
    except KeyError:
        print('there is no gender data')

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
           earliest_year_of_birth = df['Birth Year'].min()
           print('The earliest year of birth is :',earliest_year_of_birth)
    except KeyError :
           print('There is no data for birth year')

    try:
           most_recent_year_of_birth = df['Birth Year'].max()
           print('The most recent year of birth is :',most_recent_year_of_birth)
    except KeyError :
           print('There is no data for birth year')

    try:
           most_common_year_of_birth = df['Birth Year'].mode().values[0]
           print('The most common year of birth is :',most_common_year_of_birth)
    except KeyError :
        print('There is no data for birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
