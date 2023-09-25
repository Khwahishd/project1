
    input_time_hours = int(input("Enter current hour: "))
    input_alarm_hours = int(input("Enter alarm hours: "))
    
    total_alarm_hours = input_time_hours + input_alarm_hours
    
    alarm_days = total_alarm_hours // 24
    alarm_hours = total_alarm_hours % 24
    
    print(f"The alarm will sound in {alarm_days} day(s) at {alarm_hours} hours")
    
