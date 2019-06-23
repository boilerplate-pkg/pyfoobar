#%%
import datetime
import pytz

def utcnow() :
    """
    use pytz, datetime, iso8601
    """
    return datetime.datetime.now(tz=pytz.utc)



#%%
def tostring() :
    """
    print timedate to ISO8601 format
    """
    return utcnow().isoformat()

#%%
import iso8601 
def todatetime(dt):
    return iso8601.parse_date(utcnow().isoformat())


#%%


#%%
