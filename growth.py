from ranking import *
from rit_lib import *

"""
this function sorts the life expectancy growths of countries inbetween two
given years by the user. It sorts them from greatest to least.
"""


def sorted_growth_data(data, year1, year2):
    final = []
    for country in data[0]:
        if country.values[year2 - 1960] == "" or country.values[year1 - 1960] == "":
            continue
        else:
            count = (float(country.values[year2 - 1960]) - float(country.values[year1 - 1960]))
            final.append(CountryValue(country.name, count))
    final.sort(key=lambda b: b.value, reverse=True)
    return final


"""
This calls all of the previous functions and presents them in the
proper output format
"""


def main():
    data = read_data("worldbank_life_expectancy")
    year1 = int(input("Enter starting year of interest:"))
    year2 = int(input("Enter ending year of interest:"))

    newdata = sorted_growth_data(data, year1, year2)

    region = input("Enter region (type ’all’ to consider all):")
    income = input("Enter income category (type ’all’ to consider all):")

    """
    very similar to task 1 where this contains all of the conditionals
    """

    # this filters the data
    if region == "all" and income == "all":
        print("Top 10 Life Expectancy Growth:", year1, "to", year2)
        count = 1
        for country in newdata:
            if count > 10:
                pass
            else:
                print(count, country.country, country.value)
                count += 1
        print("Bottom 10 Life expectancy for", year1, "to", year2)
        if len(newdata) > 10:
            for i in range(len(newdata) - 1, len(newdata) - 11, -1):
                print(i + 1, newdata[i].country, newdata[i].value)
        else:
            for x in range(len(newdata) - 1, -1, -1):
                print(x + 1, newdata[x].country, newdata[x].value)


    elif region != "all" and income == "all":
        filterreg = filter_region(data, region)
        new_struct = []
        for elt in filterreg[1]:
            for thing in newdata:
                if elt.name == thing.country:
                    new_struct.append(thing)
        new_struct.sort(key=lambda b: b.value, reverse=True)
        count = 1

        print("Top 10 Life Expectancy Growth", year1, "to", year2)
        for country in new_struct:
            if count <= 10:
                print(count, country.country, country.value)
                count += 1
            else:
                continue
        print("Bottom 10 Life Expectancy Growth", year1, "to", year2)
        if len(new_struct) > 10:
            for i in range(len(new_struct) - 1, len(new_struct) - 11, -1):
                print(i + 1, new_struct[i].country, new_struct[i].value)
        else:
            for x in range(len(new_struct) - 1, -1, -1):
                print(x + 1, new_struct[x].country, new_struct[x].value)


    elif region == "all" and income != "all":
        incomefilter = filter_income(data, income)
        new_thing = []
        for item in incomefilter[1]:
            for county in newdata:
                if item.name == county.country:
                    new_thing.append(county)
        new_thing.sort(key=lambda b: b.value, reverse=True)
        count1 = 1
        print("Top 10 Life Expectancy Growth", year1, "to", year2)
        for county in new_thing:
            if count1 <= 10:
                print(count1, county.country, county.value)
                count1 += 1
            else:
                continue
        print("Bottom 10 Life Expectancy Growth", year1, "to", year2)
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
        for item in incomefilter[1]:
            for thing in filterreg[1]:
                if item.name == thing.name:
                    new_list.append(item)
        for thingy in newdata:
            for item in new_list:
                if thingy.country == item.name:
                    final_sort.append(thingy)
        final_sort.sort(key=lambda b: b.value, reverse=True)
        count2 = 1
        print("Top 10 Life Expectancy Growth", year1, "to", year2)
        for county in final_sort:
            if count2 <= 10:
                print(count2, county.country, county.value)
                count2 += 1
            else:
                continue
        print("Bottom 10 Life Expectancy Growth", year1, "to", year2)
        if len(final_sort) > 10:
            for i in range(len(final_sort) - 1, len(final_sort) - 11, -1):
                print(i + 1, final_sort[i].country, final_sort[i].value)
        else:
            for x in range(len(final_sort) - 1, -1, -1):
                print(x + 1, final_sort[x].country, final_sort[x].value)


if __name__ == '__main__':
    main()
