from drop import *
import turtle as tt

"""
this function makes the first graph
"""
def graph(data):
    tt.up()
    tt.right(90)
    tt.fd(220)
    tt.rt(180)
    tt.lt(90)
    tt.fd(250)
    tt.rt(90)
    tt.fd(460)
    tt.rt(180)
    tt.down()
    tt.fd(460)
    tt.lt(90)
    tt.fd(500)
    tt.rt(90)
    tt.up()
    tt.fd(15)
    tt.lt(90)
    tt.write("2015")
    tt.lt(180)
    tt.fd(250)
    tt.write("Year")
    tt.fd(250)
    tt.write("1960")
    tt.rt(90)
    tt.fd(15)
    tt.lt(90)
    tt.fd(20)
    tt.write("0")
    tt.rt(90)
    tt.fd(50)
    tt.write("10")
    tt.fd(50)
    tt.write("20")
    tt.fd(50)
    tt.write("30")
    tt.fd(50)
    tt.write("40")
    tt.fd(50)
    tt.lt(90)
    tt.fd(45)
    tt.rt(90)
    tt.write("Life exp.")
    tt.rt(90)
    tt.fd(45)
    tt.lt(90)
    tt.write("50")
    tt.fd(50)
    tt.write("60")
    tt.fd(50)
    tt.write("70")
    tt.fd(50)
    tt.write("80")
    tt.fd(50)
    tt.write("90")
    tt.rt(90)
    tt.fd(20)
    tt.rt(90)
    tt.fd(460)
    tt.rt(180)
    income(data)


def graph1(data):
    tt.up()
    tt.right(90)
    tt.fd(220)
    tt.rt(180)
    tt.lt(90)
    tt.fd(250)
    tt.rt(90)
    tt.fd(460)
    tt.rt(180)
    tt.down()
    tt.fd(460)
    tt.lt(90)
    tt.fd(500)
    tt.rt(90)
    tt.up()
    tt.fd(15)
    tt.lt(90)
    tt.write("2015")
    tt.lt(180)
    tt.fd(250)
    tt.write("Year")
    tt.fd(250)
    tt.write("1960")
    tt.rt(90)
    tt.fd(15)
    tt.lt(90)
    tt.fd(20)
    tt.write("0")
    tt.rt(90)
    tt.fd(50)
    tt.write("10")
    tt.fd(50)
    tt.write("20")
    tt.fd(50)
    tt.write("30")
    tt.fd(50)
    tt.write("40")
    tt.fd(50)
    tt.lt(90)
    tt.fd(45)
    tt.rt(90)
    tt.write("Life exp.")
    tt.rt(90)
    tt.fd(45)
    tt.lt(90)
    tt.write("50")
    tt.fd(50)
    tt.write("60")
    tt.fd(50)
    tt.write("70")
    tt.fd(50)
    tt.write("80")
    tt.fd(50)
    tt.write("90")
    tt.rt(90)
    tt.fd(20)
    tt.rt(90)
    tt.fd(460)
    tt.rt(180)
    income1(data)


def income1(data):
    tt.fd(480)
    tt.rt(90)
    tt.fd(100)
    tt.color("blue")
    tt.down()
    tt.write("Sub-Saharan Africa")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("red")
    tt.write("South Asia")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("green")
    tt.write("Europe & Central Asia")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("orange")
    tt.write("Latin America & Caribbean")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("black")
    tt.write("Middle east & North Africa")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("yellow")
    tt.write("North America")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("purple")
    tt.write("East asia & Pacific ")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(180)
    tt.fd(70)
    tt.lt(90)
    tt.fd(100)
    tt.lt(90)
    tt.fd(480)
    tt.lt(180)


def income(data):
    tt.fd(480)
    tt.rt(90)
    tt.fd(100)
    tt.color("blue")
    tt.down()
    tt.write("low income")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("red")
    tt.write("upper middle income")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("green")
    tt.write("lower middle income")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(270)
    tt.color("orange")
    tt.write("High income")
    tt.up()
    tt.fd(100)
    tt.down()
    tt.fd(25)
    tt.up()
    tt.rt(180)
    tt.fd(125)
    tt.lt(90)
    tt.fd(15)

    tt.rt(180)
    tt.fd(70)
    tt.lt(90)
    tt.fd(100)
    tt.lt(90)
    tt.fd(480)
    tt.lt(180)

"""
This finds the median points for the region
"""
def reg1(data, newlow):
    low = filter_region(data, newlow)
    print("Filter region", low)
    new_med = []
    for i in range(1960, 2016):
        list1 = sorted_ranking_data(low, i)
        print("LIST ONE", list1)
        if len(list1) % 2 == 0:
            median = (((list1[len(list1) // 2].value) + ((list1[(len(list1) // 2) + 1].value))) / 2)
            new_med.append(median)
        else:
            median = list1[len(list1) // 2].value
            new_med.append(median)

    return new_med

"""
same thing as reg1
"""
def reg(data, newlow):
    low = filter_region(data, newlow)
    new_med = []
    for i in range(1960, 2016):
        list1 = sorted_ranking_data(low, i)
        if len(list1) % 2 == 0:
            median = (((list1[len(list1) // 2].value) + ((list1[(len(list1) // 2) + 1].value))) / 2)
            new_med.append(median)
        else:
            median = list1[len(list1) // 2].value
            new_med.append(median)

    return new_med

"""
draws lines from median values in reg
"""
def draw1(list1, color):
    tt.down()
    tt.color('black')
    for item in range(0, 55):
        tt.goto(-250 + (item * (500 / 55)), -220 + (float(list1[item])) * 5)
        tt.color(color)
    tt.penup()
    tt.goto(-250, -220)


"""
finds the median values for the income filtered data
"""
def low(data, low):
    low = filter_income(data, low)
    new_med = []
    for i in range(1960, 2016):
        list1 = sorted_ranking_data(low, i)
        if len(list1) % 2 == 0:
            median = (((list1[len(list1) // 2].value) + ((list1[(len(list1) // 2) + 1].value))) / 2)
            new_med.append(median)
        else:
            median = list1[len(list1) // 2].value
            new_med.append(median)

    return new_med

"""
this function draws the lines from the median values given from low
"""
def draw(list1, color):
    tt.down()
    tt.color('black')
    for item in range(0, 55):
        tt.goto(-250 + (item * (500 / 55)), -220 + (float(list1[item])) * 5)
        tt.color(color)
    tt.penup()
    tt.goto(-250, -220)


"""
this calls all of the functions above drawing the graph and choosing the color of the lines
"""
def main():
    tt.speed("fastest")
    data = read_data("worldbank_life_expectancy")
    graph(data)
    list1 = low(data, "Low income")
    list2 = low(data, "High income")
    list3 = low(data, "Upper middle income")
    list4 = low(data, "Lower middle income")
    draw(list1, 'blue')
    draw(list2, 'orange')
    draw(list3, "red")
    draw(list4, "green")
    x = input("Press 1 to see the next graph:")
    tt.color("black")
    tt.rt(90)
    tt.clear()
    tt.goto(0, 0)
    if x == "1":
        graph1(data)
        lista = reg(data, "Sub-Saharan Africa")
        listb = reg(data, "South Asia")
        listc = reg(data, "Europe & Central Asia")
        listd = reg(data, "Latin America & Caribbean")
        liste = reg(data, "Middle East & North Africa")
        # listf= reg1(data, "North America")
        listg = reg(data, "East Asia & Pacific")
        draw1(lista, "blue")
        draw1(listb, "red")
        draw1(listc, "green")
        draw1(listd, "orange")
        draw1(liste, "black")
        # draw1(listf, "yellow")
        draw1(listg, "purple")

    tt.done()


main()
