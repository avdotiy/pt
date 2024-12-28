def convert_time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        time_parts = time_str[:-2].strip().split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        
        if time_str.endswith('AM'):
            if hours == 12:
                hours = 0  
        elif time_str.endswith('PM'):
            if hours != 12:
                hours += 12 
        
        return f"{hours:02}:{minutes:02}"
    
    else:
        time_parts = time_str.strip().split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        
        if hours == 0:
            return f"12:{minutes:02} AM"  
        elif hours < 12:
            return f"{hours}:{minutes:02} AM"
        elif hours == 12:
            return f"{hours}:{minutes:02} PM"
        else:
            return f"{hours - 12}:{minutes:02} PM"


print(convert_time("03:52 PM"))