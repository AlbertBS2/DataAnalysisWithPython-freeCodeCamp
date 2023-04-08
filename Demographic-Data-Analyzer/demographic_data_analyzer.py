import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    dfrace = df.set_index("race")
    race_count = round(dfrace.index.value_counts(), 1)

    # What is the average age of men?
    dfage = df.set_index("sex")
    dfage.drop("Female", inplace=True)
    average_age_men = round(dfage["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    dfbach = df[df["education"] == "Bachelors"]
    percentage_bachelors = round((len(dfbach) / len(df))*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    dfmast = df[df["education"] == "Masters"]
    dfdoct = df[df["education"] == "Doctorate"]
    dfbm = dfbach.append(dfmast, sort=True)
    higher_education = dfbm.append(dfdoct, sort=True)
    dfadv50 = higher_education.loc[higher_education["salary"] == ">50K"]

    dfedu = df.set_index("education")
    lower_education = dfedu.drop("Bachelors")
    lower_education.drop("Masters", inplace=True)
    lower_education.drop("Doctorate", inplace=True)
    dfnoadv50 = lower_education.loc[lower_education["salary"] == ">50K"]

    # percentage with salary >50K
    higher_education_rich = round((len(dfadv50)/len(higher_education))*100, 1)
    lower_education_rich = round((len(dfnoadv50)/len(lower_education))*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df["hours-per-week"].min(), 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    dfminh = df[df["hours-per-week"] == df["hours-per-week"].min()]
    num_min_workers = len(dfminh)
    dfminh50 = dfminh.loc[dfminh["salary"] == ">50K"]
    rich_percentage = round((len(dfminh50)/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    df50 = df[df["salary"] == ">50K"]
    v50perc = (df50["native-country"].value_counts()/df["native-country"].value_counts())*100
    highest_earning_country = v50perc.idxmax()
    highest_earning_country_percentage = round(v50perc.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df50india = df50[df50["native-country"] == "India"]
    v50india = df50india["occupation"].value_counts()
    top_IN_occupation = v50india.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }