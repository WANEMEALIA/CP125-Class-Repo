def has_warming_trend(temps):
    for i in range (len(temps) - 1):
       if (temps[i] > temps[i+1]) and (temps[i] > temps[i-1]) :
           return True
    return False