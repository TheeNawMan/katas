intervals = (
    ('years', 31536000),
    ('days', 86400),
    ('hours', 3600),    
    ('minutes', 60),
    ('seconds', 1),
    )

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append("{} {}".format(value, name if value>1 else name.rstrip('s')))
    length = len(result)
    
    if length>1:
        return ', '.join(result[:-1])+" and "+result[-1]
    else:
        return result[0]