from growth import *

"""
new struct type to hold all of the information about the greatest drop in life 
expectancy for each country
"""
Range = struct_type("Range", (str, 'country'), (int, 'year1'), (int, 'year2'), (float, 'value1'), (float, 'value2'))

"""
sorts all of the countries by the largest drop in life excectancy between two dates
"""
def sorted_drop_data(data):
    finallist = []
    count=0
    for item in data[0]:
        curr = [100.0, 0, 0, 0.0, 0.0]
        maximum = [100.0, 0, 0, 0.0, 0.0]
        for i in range(1960, 2016):
            # temp.year1 = i + 1960
            # temp.value1 = float(item.values[i])
            for g in range(i, 2016):
                if item.values[g - 1960] == "" or item.values[i - 1960] == "":
                    continue
                current = drop(item, i, g)
                if current[0] < curr[0]:
                    curr = current
            if curr[0] < maximum[0]:
                maximum = curr
        finallist.append(Range(item.name, maximum[1], maximum[2], maximum[3], maximum[4]))

    finallist.sort(key=lambda b: b.value2 - b.value1, reverse=True)

    return finallist, count

"""
this is a helper function of sorted_drop that stores the data in strcut types
"""
def drop(cont, year1, year2):
    return [float(cont.values[year2 - 1960]) - float(cont.values[year1 - 1960]), \
            year1, year2, float(cont.values[year2 - 1960]), float(cont.values[year1 - 1960])]

"""
this calls all of the above functions and also lists the top 
ten greatest drops in life expectancy and the dates in which it happened

"""
def main():
    data = read_data("worldbank_life_expectancy")
    worst = sorted_drop_data(data)[0]

    print("Worst Countries drop in life expectancies:")

    count=0
    while count < 10:
        print(count + 1, ":", worst[count].country, worst[count].year1, \
              worst[count].value1, worst[count].year2, \
              worst[count].value2, worst[count].value2 - worst[count].value1)
        count+=1


if __name__ == '__main__':
    main()
