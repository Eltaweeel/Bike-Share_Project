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
    while True:
            city = input("Which city would like to see data for? chicago, new york city or washington? ").lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print("invalid input. Please choose a city from list above!!")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would like to filter the data by month? (all, january, february, march, ... , june)").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("invalid input. Please choose a month from above!!")
            
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would like to filter the by day? EX.(all, monday, tuesday, ... sunday)").lower()
        if day in ['all', 'monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("invalid input. Please choose a day from list above!!")

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
    # load data file into our DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime in our DataFrame
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day from the Start Time column to create month column and weekday column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    # filter by all month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding integer    
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new DataFrame
        df = df[df['month'] == month]
    
    # filter by all days if applicable
    if day != 'all':
        
        # filter by day of the week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_common_month = df['month'].mode()[0]
    
    print("The most common month is: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    
    print("The most common day of the week is: ", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    most_common_hour = df['hour'].mode()[0]
    
    print("The most common start hour is: ", most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common used start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most common used end station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_freq_combination = df['Start Station'] + " & " + df['End Station'] 
    print("The most frequent combination of start station and end station trip is:  ", most_freq_combination.mode()[0])

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_time /(60*60*24), "Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: ", mean_travel_time / 60, "Minutes")

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types are: ", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("gender counts: ", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("The earliest year of birth is: ", df['Birth Year'].min())

        print("The most recent year of birth is: ", df['Birth Year'].max())

        print("The most common year of birth is: ", df['Birth Year'].mode()[0])

                        
                        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def display_raw_data(df):
    x = 1000
    user_ans = input("Would like to see 5 lines of raw data? yes or no  ").lower()
    
    #built in function to show the max number of columns with none attribute to show the max number
    pd.set_option('display.max_columns', None)
    
    # asking the user if needs to show the next 5 lines of raw data, if answer is yes then displays the data any other answer will stop the if statement
    while True:
        if user_ans == 'yes':
            print(df[x: x+5])
            user_ans = input("Would like to see the next 5 lines of raw data? Enter yes or no  ").lower()
            x +=5
        else:
            break
                        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
