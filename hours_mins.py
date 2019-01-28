def hours_mins(mins):
    ''' Convert minutes to hours and minutes '''
    if mins > 59:
        hrs = int(mins / 60)
        mins = int(mins % 60)
        return("{} hours and {} mins".format(hrs, mins))
    else:
        return("{} mins".format(mins))

print(hours_mins(147))
