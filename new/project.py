import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the City for which you want to see Data - Chicago, New York City, Washington:\n")

        if city.lower() == 'chicago' or city.lower() == 'new york city' or city.lower() == 'washington':
            print('\n')
            break
        else:
            print("Sorry wrong city. Kindly enter valid city name.")
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the Month which you want to filter Data for - january, february, march, etc." +
                      " Enter 'all' if you want no filter:\n")

        if month not in months and month != "all":
            print("Sorry wrong month. Kindly enter valid month name.")
            continue
        else:
            print('\n')
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of week in terms of integer like '1' for monday to filter data. Enter 'all' for no filters:\n")

        days_in_week = ['1', '2', '3', '4', '5', '6', '7']

        if day not in days_in_week and day != 'all':
            print("Sorry wrong day of week, Kindly enter valid integer value for day of week.")
            continue
        else:
            print('\n')
            break

    print('-' * 40)
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    # if month != 'all':
    #     # filter by month to create the new dataframe
    #     month = months.index(month) + 1
    #
    #     df = df[df['month'] == month]
    #
    # # filter by day of week if applicable
    # if day != 'all':
    #     # use the index of the months list to get the corresponding int
    #     # days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    #
    #     # filter by day of week to create the new dataframe
    #     day = int(day) - 1
    #
    #     df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # common_month = df['month'].value_counts().idxmax() - 1
    common_month = df['month'].mode()[0] - 1
    print("\nMost common month is {}\n".format(months[common_month]))

    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("\nMost common day of week is {} : {}\n".format(common_day, days[common_day]))

    # display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print("\nMost common hour of day is {}\n".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nMost common starting station is {}\n".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nMost common end station is {}\n".format(common_end_station))

    # display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().reset_index().max()
    print("\nMost Popular Trip\n{}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("\nTotal Travel Time is {}\n".format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("\nMean Travel Time is {}\n".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nVarious types of users are:\n{}".format(user_types))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nGender Ratio:\n{}".format(gender_count))
    else:
        print("\nNo data available for Gender\n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
        print("\nEarliest Year: {}\n".format(earliest_year))
        print("\nRecent Year: {}\n".format(recent_year))
        print("\nCommon Year: {}\n".format(common_year))
    else:
        print("\nNo data available for Birth Year\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, month, day)
        # print("\n")
        # print(df.head())

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
