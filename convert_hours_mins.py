def hours_mins(mins):
    ''' Convert minutes to hours and minutes '''
    if mins > 59:
        hrs = int(mins / 60)
        mins = int(mins % 60)
        return f"{hrs} hours and {mins} mins"
    else:
        return f"{mins} mins"

print(hours_mins(119))
