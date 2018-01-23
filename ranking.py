from rit_lib import *
from utils import *

"""
This is a new struct type meant to hold the greatest life expectancy for a country in a given year
"""
CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))

"""
This function puts all of the countries life expectancies for a specific year in order
from greatest to least
"""
def sorted_ranking_data(data, year):
    sortdata = []
    index1 = (year - 1960)
    for item in data[0]:
        list1 = item.values
        if list1[index1] == "":
            continue
        sortdata.append(CountryValue(item.name, float(list1[index1])))

    sortdata.sort(key=lambda b: b.value, reverse=True)
    return sortdata

"""
This calls all of the functions above and also provides the correct output providing 
the top 10 and bottom 10 life expectancies by country
"""
def main():
    data = read_data("worldbank_life_expectancy")
    year = int(input("Enter Year of interest:"))
    newdata = sorted_ranking_data(data, year)

    region = input("Enter region (type ’all’ to consider all):")
    filtered_reg = filter_region(data, region)
    income = input("Enter income (typer 'all' to consider all):")

    """
    These are all of the conditional statements for sorting the data
    """
    # this filters the data
    if region == "all" and income == "all":
        print("Top 10 Life expecancy for", year)
        count = 1
        for country in newdata:
            if count > 10:
                pass
            else:
                print(count, country.country, country.value)
                count += 1
        print("Bottom 10 Life expectancy for", year)
        if len(newdata) > 10:
            for i in range(len(newdata) - 1, len(newdata) - 11, -1):
                print(i + 1, newdata[i].country, newdata[i].value)
        else:
            for x in range(len(newdata) - 1, -1, -1):
                print(x + 1, newdata[x].country, newdata[x].value)


    elif region != "all" and income == "all":
        filterreg = filter_region(data, region)
        new_struct = []
        for elt in filterreg[0]:
            for thing in newdata:
                if elt.name == thing.country:
                    new_struct.append(thing)
        new_struct.sort(key=lambda b: b.value, reverse=True)
        count = 1

        print("Top 10 Life expectancy for", year)
        for country in new_struct:
            if count <= 10:
                print(count, country.country, country.value)
                count += 1
            else:
                continue
        print("Bottom 10 Life expectancy for", year)
        if len(new_struct) > 10:
            for i in range(len(new_struct) - 1, len(new_struct) - 11, -1):
                print(i + 1, new_struct[i].country, new_struct[i].value)
        else:
            for x in range(len(new_struct) - 1, -1, -1):
                print(x + 1, new_struct[x].country, new_struct[x].value)


    elif region == "all" and income != "all":
        incomefilter = filter_income(data, income)
        new_thing = []
        for item in incomefilter[0]:
            for county in newdata:
                if item.name == county.country:
                    new_thing.append(county)
        new_thing.sort(key=lambda b: b.value, reverse=True)
        count1 = 1
        print("Top 10 Life expectancy for", year)
        for county in new_thing:
            if count1 <= 10:
                print(count1, county.country, county.value)
                count1 += 1
            else:
                continue
        print("Bottom 10 Life expectancy for", year)
        if len(new_thing) > 10:
            for i in range(len(new_thing) - 1, len(new_thing) - 11, -1):
                print(i + 1, new_thing[i].country, new_thing[i].value)
        else:
            for x in range(len(new_thing) - 1, -1, -1):
                print(x + 1, new_thing[x].country, new_thing[x].value)


    elif region != "all" and income != "all":
        incomefilter = filter_income(data, income)
        filterreg = filter_region(data, region)
        final_sort = []
        new_list = []
        for item in incomefilter[0]:
            for thing in filterreg[0]:
                if item.name == thing.name:
                    new_list.append(item)
        for thingy in newdata:
            for item in new_list:
                if thingy.country == item.name:
                    final_sort.append(thingy)
        final_sort.sort(key=lambda b: b.value, reverse=True)
        count2 = 1
        print("Top 10 Life expectancy for", year)
        for county in final_sort:
            if count2 <= 10:
                print(count2, county.country, county.value)
                count2 += 1
            else:
                continue
        print("Bottom 10 Life expectancy for", year)
        if len(final_sort) > 10:
            for i in range(len(final_sort) - 1, len(final_sort) - 11, -1):
                print(i + 1, final_sort[i].country, final_sort[i].value)
        else:
            for x in range(len(final_sort) - 1, -1, -1):
                print(x + 1, final_sort[x].country, final_sort[x].value)


if __name__ == '__main__':
    main()
