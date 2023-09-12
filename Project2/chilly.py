def windchill(temp, wind_speed):
    return round(35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * wind_speed ** 0.16)
