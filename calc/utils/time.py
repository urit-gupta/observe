from datetime import date, time

def greenwich_sidereal_time(city : str, local_date : date, local_time : time):
  # function based on: https://pages.astro.umd.edu/~jpha/GST_eqn.pdf
  # adjust this function to account for which city is being observed from!
  G = 6.5988098 # year 2000, calculated successively for each year until we have one for the current observation year, potentially storable
  for i in range(2000, local_date.year):
    day = 365
    if i % 100 == 0:
      if i % 400 == 0:
        day = 366
    elif i % 4 == 0:
      day = 366
    G = (G + 0.0657098244 * day) % 24

  UD = local_date - (date(local_date.year, 1, 1)) # get around storing extra cumulative day information by using timedelta class

  # https://www.calculatoratoz.com/en/universal-time-calculator/Calc-12154
  UT = (local_time.hour + (local_time.minute / 60) + (local_time.second / 3600)) / 24

  return G + 0.0657098244 * UD.days + 1.00273791 * UT
