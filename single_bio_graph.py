
#!/usr/bin/env python
# from datetime import date
import datetime
import matplotlib.dates
from pylab import *
from numpy import array, sin, pi

date_of_birth = input('Enter Date of birth (DD-MM-YYYY) - ')
target_date = input('Enter Target date (DD-MM-YYYY) - ')


# def date_check(date_of_birth):
#     status = -1

#     ddd = 0
#     mmm = 0
#     yyy = 0
#     try:
#         if '-' in date_of_birth:
#             date_list = date_of_birth.strip().split('-')
#             if len(date_list) == 3:
#                 print (date_list)
#                 ddd = int(date_list[0])
#                 mmm = int(date_list[1])
#                 yyy = int(date_list[2])
#                 status = 0
#             else:
#                 print ("Invalid date")
#         else:
#             print ('Date format invalid')
#     except Exception as e:
#         print(e)
#     print (status)
#     print (ddd)
#     print (mmm)
#     print (yyy)
#     print ('##############################################')
#     return status, ddd, mmm, yyy


# if date_of_birth:
#     status, date, month, year = date_check(date_of_birth)
#     if status == 0:
#         dd = date
#         mm = month
#         yy = year
#     else:
#         print (" ")
# else:
#     print ("Date should not be empty")

# if target_date:
#     status, date_1, month_1, year_1 = date_check(target_date)
#     if status == 0:
#         dd1 = date_1
#         mm1 = month_1
#         yy1 = year_1
#     else:
#         print (" ")
# else:
#     print ("Date should not be empty")


# dd, mm, yy = 21, 1, 1995  # Guido van Rossum
# dd1, mm1, yy1 = 1, 1, 2019


def sig(q):
    if q >= 0:
        return 1
    return 0


# print (yy)
# print (dd)
# print (mm)
# print (yy1)
# print (dd1)
# print (mm1)


# print (type(yy))
# print (type(dd))
# print (type(mm))
# print (type(yy1))
# print (type(dd1))
# print (type(mm1))

try:
    date_of_birth_obj = datetime.datetime.strptime(date_of_birth, '%d-%m-%Y')
    t0 = date_of_birth_obj.toordinal()
    print (t0)

    target_date

    target_date_obj = datetime.datetime.strptime(target_date, '%d-%m-%Y')
    t1 = target_date_obj.toordinal()
    print (t1)
except ValueError:
    print ('Invaid Date / Date format (DD-MM-YYYY) ')
except Exception as e:
    raise e


# t0 = date(int(yy), mm, dd).toordinal()
# print (t0)
# t1 = date(yy1, mm1, dd1).toordinal()
# print (t1)
# t1 = date.today().toordinal()
# t = array(range(t1 - 3, t1 + 31))  # range of 31 days
t = array(range(t1 - 15, t1 + 15))  # range of 31 days

print (t)

#################################################################
# y = (sin(2 * pi * (t - t0) / 23),  # Physical
#      sin(2 * pi * (t - t0) / 28),  # Emotional
#      sin(2 * pi * (t - t0) / 33),  # Intellectual
#      sin(2 * pi * (t - t0) / 38),  # intuitive
#      sin(2 * pi * (t - t0) / 43),  # aesthetic
#      sin(2 * pi * (t - t0) / 48),  # awareness
#      sin(2 * pi * (t - t0) / 53))  # spiritual
#################################################################
y = (sin(2 * pi * (t - t0) / 23),  # Physical
     sin(2 * pi * (t - t0) / 28),  # Emotional
     sin(2 * pi * (t - t0) / 33))  # Intellectual
# sin(2 * pi * (t - t0) / 38),  # intuitive
# sin(2 * pi * (t - t0) / 43),  # aesthetic
# sin(2 * pi * (t - t0) / 48),  # awareness
# sin(2 * pi * (t - t0) / 53))  # spiritual


# av3 = (y[0] + y[1] + y[2]) / 3.
# av7 = (y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6]) / 7.

# converting ordinals to date
label = []
for p in t:
    # label.append(date.fromordinal(p))
    label.append(datetime.datetime.fromordinal(p))


# print (label)

fig = figure(figsize=(14, 7))
ax = fig.gca()
plot(label, y[0], color="r", linewidth=4, alpha=.7)
plot(label, y[1], color="b", linewidth=4, alpha=.7)
plot(label, y[2], color="g", linewidth=4, alpha=.7)
# plot(label, av3, linewidth=2, linestyle="--", color="black")
# plot(label, .5 * (y[0] + y[1]), label, .5 * (y[1] + y[2]), label, .5 * (y[2] + y[0]), linewidth=2, alpha=.65)
# plot(label, y[3], label, y[4], label, y[5], label, y[6], linewidth=2, alpha=.3)
# plot(label, .5 * (y[3] + y[1]), label, .5 * (y[3] + y[2]), label, .5 * (y[3] + y[0]), linewidth=4, alpha=.5, linestyle="dotted")
# plot(label, av7, linewidth=4, linestyle="--", color="black")


def f(x):
    return 50. * (x + 1)


for n in range(len(t) - 1):
    print ("%s %3.1f %3.1f %3.1f" % (label[n], f(y[0][n]), f(y[1][n]), f(y[2][n])))
    if (sig(y[0][n]) != sig(y[0][n + 1]) or
        sig(y[1][n]) != sig(y[1][n + 1]) or
            sig(y[2][n]) != sig(y[2][n + 1])):
        print (label[n], "***")

# # adding a legend
# legend(['Physical', 'Emotional', 'Intellectual', 'AVERAGE-3',
#         'Passion', 'Wisdom', 'Mastery',
#         'Intuitive', 'Aesthetic', 'Awareness', 'Spiritual',
#         'Psychic', 'Success', 'Perception', 'AVERAGE-7'])
legend(['Physical', 'Emotional', 'Intellectual'])

# formatting the dates on the x axis
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
axhline(0, color="black", linewidth=1.4)
grid(True, linestyle="-", alpha=.3)
xlim((t[0], t[-1]))
# a = date.today()
# a = date(yy1, mm1, dd1)
# title("%02u.%02u.%04u (Alter: %u Tage am %02u.%02u.%04u)" % (dd, mm, yy, t1 - t0, a.day, a.month, a.year))

# fn = "%04u-%02u-%02u.pdf" % (yy, mm, dd)
# savefig(fn)

show()
