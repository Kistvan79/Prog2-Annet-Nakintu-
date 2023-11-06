def minimum_days_to_print_statues(n):
    current_printers = 1 
    current_day = 0  
    statues_printed = 0  

    while statues_printed < n:
        
        statues_printed_today = current_printers

        statues_printed += statues_printed_today
        current_day += 1

        
        current_printers += statues_printed_today

        if statues_printed < n:
            current_printers += 1

    return current_day

# Input parameter
n = 5  # Number of statues you want to print

# Calculate the minimum number of days needed to print at least "n" statues
min_days = minimum_days_to_print_statues(n)

print(f"Minimum number of days to print at least {n} statues: {min_days} days")
