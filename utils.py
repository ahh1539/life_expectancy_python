from rit_lib import *

"""
These are the 2 data structures that hold all of the data from the life expectancy files
"""
MainData = struct_type("MainData", (str, 'name'), (str, 'code'), (list, 'values'))
MetaData = struct_type("MetaData", (str, 'country'), (str, 'region'), (str, 'income'), (str, 'name'))

"""
This function reads the file data and returns them into two struct types that present the data in easily accesible way
"""

def read_data(filename):
    main = []
    meta = []
    codes = []
    pd = open(filename + "_data.txt")
    pd.readline()
    for line2 in pd:
        yeet = line2.strip().split(",")
        main.append(MainData(yeet[0], yeet[1], yeet[2:]))
        codes.append(yeet[0])
    pd.close
    fd = open(filename + "_metadata.txt")
    count = 0
    fd.readline()
    for line1 in fd:
        newlist = line1.strip().split(",")
        metaObject = MetaData(newlist[0], newlist[1], newlist[2], codes[count])
        meta.append(metaObject)
        count += 1

    fd.close()
    return main, meta

"""
This is a helper function that displays the data for the number of countries 
& territories that are in each income range
"""
def income(data):
    lowermiddle = 0
    uppermiddle = 0
    high = 0
    low = 0
    for item in data[1]:
        if item.income == "Upper middle income":
            uppermiddle += 1
        elif item.income == "Low income":
            low += 1
        elif item.income == "Lower middle income":
            lowermiddle += 1
        elif item.income == "High income":
            high += 1
    return high, low, uppermiddle, lowermiddle

"""
this is a helper function to tell how many countries are in each region
"""
def numcountries(data):
    middle_east = 0
    europe = 0
    northa = 0
    latina = 0
    southa = 0
    easta = 0
    sub_sahara = 0
    for item in data[1]:
        if item.region == "Middle East & North Africa":
            middle_east += 1
        elif item.region == "Europe & Central Asia":
            europe += 1
        elif item.region == "North America":
            northa += 1
        elif item.region == "Latin America & Caribbean":
            latina += 1
        elif item.region == "South Asia":
            southa += 1
        elif item.region == "East Asia & Pacific":
            easta += 1
        elif item.region == "Sub-Saharan Africa":
            sub_sahara += 1
    return middle_east, europe, northa, latina, southa, easta, sub_sahara

"""
This is a helper function that tells how many countries there are
and how many countries + territories ect. there are.
"""
def allcountries(filename):
    fd = open(filename + "_metadata.txt")
    fd.readline()
    all = 0
    noncountry = 0
    for line in fd:
        newlist = line.strip().split(",")
        all += 1
        if newlist[1] == "":
            noncountry += 1

    return all, (all - noncountry)


"""
this filters through the data only keeping items that are in the specific region
"""
def filter_region(data, region):
    newdata = []
    newdata_main= []
    for elt in data[1]:
        if elt.region == "":
            continue
        elif elt.region == region:
            newdata.append(elt)
    for item in newdata:
        for thing in data[0]:
            if item.name == thing.name:
                newdata_main.append(thing)

    return newdata_main, newdata


"""
This filters through the main data struct type only keeping struct types
that are in the specified income category
"""
def filter_income(data, income):
    incomelist = []
    newdata_main= []
    for elt in data[1]:
        if elt.region == "":
            continue
        elif elt.income == income:
            incomelist.append(elt)
    for item in incomelist:
        for thing in data[0]:
            if item.name == thing.name:
                newdata_main.append(thing)

    return newdata_main, incomelist

"""
This is the main function that calls all of the functions above and makes the output
"""
def main():
    filename = "worldbank_life_expectancy"
    data = read_data(filename)

    # country count
    allcount = allcountries(filename)  # makes the return statement a list
    print("total number of entities:", allcount[0])
    print("Number of countries:", allcount[1])

    # region count
    reg = numcountries(data)
    print("Region and their country count:")
    print("Middle East & North Africa:", reg[0])
    print("Europe & Central Asia:", reg[1])
    print("North America:", reg[2])
    print("Latin America & Caribbean:", reg[3])
    print("South Asia:", reg[4])
    print("East Asia & Pacific:", reg[5])
    print("Sub-Saharan Africa:", reg[6])

    # income
    inc = income(data)
    print("Income categories and their country count:")
    print("Lower middle income:", inc[3])
    print("Upper middle income", inc[2])
    print("High income:", inc[0])
    print("Low income:", inc[1])

    # region
    region = input("Enter a correct region name:")
    print("Countries in the", region, "region:")
    f_data = filter_region(data, region)
    for meta in f_data[1]:
        print(meta.name, "(", meta.country, ")")

    # user input income
    inc1 = input("Enter Income Category:")
    f_inc_data = filter_income(data, inc1)
    for thing in f_inc_data[1]:
        print(thing.name, "(", thing.country, ")")

    """
    this presents all of the life expectancy values for one country
    """
    # show user data
    while True:
        name = input("Enter a country name or code (To end enter 1):")
        if name == "1":
            break
        count = 1959
        count1 = 0
        for line in data[0]:
            if line.name == name or line.code == name:
                print("Data for", name)
                value = len(line.values)
                for life in line.values:
                    if count1 >= value - 1:
                        pass
                    elif life == "":
                        count += 1
                        count1 += 1
                        continue
                    elif count1 <= value:
                        count += 1
                        print("Year:", count, "Life expectancy:", line.values[count1])
                        count1 += 1


if __name__ == "__main__":
    main()
