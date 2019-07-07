import datetime
import matplotlib.dates
from pylab import *
from numpy import array, sin, pi
import sys


def sign_check(data_value):
    try:
        if data_value >= 0:
            return 1
        return 0
    except Exception as e:
        print (e)


def time_conversions(date_of_birth, target_date):
    t0 = 0
    t1 = 0
    t = []
    try:
        date_of_birth_obj = datetime.datetime.strptime(date_of_birth, '%d-%m-%Y')
        t0 = date_of_birth_obj.toordinal()

        target_date_obj = datetime.datetime.strptime(target_date, '%d-%m-%Y')
        t1 = target_date_obj.toordinal()

        t = array(range(t1 - 15, t1 + 15))  # dates range

    except ValueError:
        print ('Invaid Date / Date format (DD-MM-YYYY) ')
        sys.exit()
    except Exception as e:
        print(e)
    return t0, t1, t


def conversion(x):
    return 50. * (x + 1)


def graph_details(t0, t1, t):
    label = []
    try:
        y = (sin(2 * pi * (t - t0) / 23),  # Physical cycle
             sin(2 * pi * (t - t0) / 28),  # Emotional cycle
             sin(2 * pi * (t - t0) / 33))  # Intellectual cycle
        for p in t:
            label.append(datetime.datetime.fromordinal(p))

        fig = figure(figsize=(14, 7))
        ax = fig.gca()
        plot(label, y[0], color="r", linewidth=4, alpha=.7)
        plot(label, y[1], color="b", linewidth=4, alpha=.7)
        plot(label, y[2], color="g", linewidth=4, alpha=.7)

        for n in range(len(t) - 1):
            print ("%s %3.1f %3.1f %3.1f" % (label[n], conversion(y[0][n]), conversion(y[1][n]), conversion(y[2][n])))
            if (sign_check(y[0][n]) != sign_check(y[0][n + 1]) or
                sign_check(y[1][n]) != sign_check(y[1][n + 1]) or
                    sign_check(y[2][n]) != sign_check(y[2][n + 1])):
                print (label[n], "***")

        legend(['Physical', 'Emotional', 'Intellectual'])

        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
        axhline(0, color="black", linewidth=1.4)
        grid(True, linestyle="-", alpha=.3)
        xlim((t[0], t[-1]))
        show()
    except Exception as e:
        raise e


def main():
    try:
        date_of_birth = input('Enter Date of birth (DD-MM-YYYY) : ')
        target_date = input('Enter Target date (DD-MM-YYYY) : ')
        first_time, second_time, time_list = time_conversions(date_of_birth, target_date)
        graph_details(first_time, second_time, time_list)
    except Exception as e:
        raise e


main()
