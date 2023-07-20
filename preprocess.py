import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
def preprocessor_iphone(data,option1):
    pattern=r"\[\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{1,2}:\d{1,2} [AP]M\]" if option1=="12 hour" else r"\[\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{1,2}:\d{1,2}\]"

    messages = re.split(pattern,data)
    date_time = re.findall(pattern,data)
    df=pd.DataFrame({"messages":messages[1:],"date":date_time})
    pattern=r".*?:\s*"
    df["user"]=df["messages"].apply(lambda x:str(re.search(pattern,x).group()).rstrip(":") if re.search(pattern,x) else "group notification" )
    
    
    df["user"]=df["user"].str.strip()
    df["user"]=df["user"].str.strip(":")
    df["user"]=df["user"].str.strip("\u200e")

    df=df.drop(df[df['user'] == 'You'].index)
    df["messages"]=df["messages"].str.strip("\u200e")
    df["messages"]=df["messages"].apply(lambda x:re.split(pattern,x))
    df["messages"]=df["messages"].apply(lambda x:x[1])
    df["messages"]=df["messages"].apply(lambda x:x.replace("\n",""))
    df["date"]=df["date"].apply(lambda x:x.replace("[",""))
    df["date"]=df["date"].apply(lambda x:x.replace("]",""))
    df["message_Date"]=pd.to_datetime(df["date"],format="%d/%m/%y, %I:%M:%S %p" if option1=="12 hour" else "%d/%m/%y, %I:%M:%S" )
    df["hour"]=df.message_Date.dt.hour
    df["minute"]=df.message_Date.dt.minute
    df["second"]=df.message_Date.dt.second
    df["day"]=df.message_Date.dt.day_name()
    df["month"]=df.message_Date.dt.month_name()
    df["year"]=df.message_Date.dt.year
    return_df=df
    return return_df
def preprocessor_android(data,option1):
    pattern=r"\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{1,2} - " if option1=="24 hour" else r"\d{2}/\d{2}/\d{4}, \d{2}:\d{2}\s?[ap]m - "
    messages = re.split(pattern,data)
    date_time = re.findall(pattern,data)
    df=pd.DataFrame({"messages":messages[1:],"date":date_time})
    pattern=r".*?:\s*"
    df["user"]=df["messages"].apply(lambda x:str(re.search(pattern,x).group()).rstrip(":") if re.search(pattern,x) else "group notification" )
    
    
    df["user"]=df["user"].str.strip()
    df["user"]=df["user"].str.strip(":")
    df["user"]=df["user"].str.strip("\u200e")

    df=df.drop(df[df['user'] == 'You'].index)
    df["messages"]=df["messages"].str.strip("\u200e")
    df["messages"]=df["messages"].apply(lambda x:re.split(pattern,x))
    df["messages"]=df["messages"].apply(lambda x:x[0] if x[0] else x[1])
    df["messages"]=df["messages"].apply(lambda x:x.replace("\n",""))
    df["message_Date"]=pd.to_datetime(df["date"],format="%m/%d/%y, %H:%M - " if option1=="24 hour" else "%d/%m/%Y, %I:%M %p - " )
    df["hour"]=df.message_Date.dt.hour
    df["minute"]=df.message_Date.dt.minute
    df["second"]=df.message_Date.dt.second
    df["day"]=df.message_Date.dt.day_name()
    df["month"]=df.message_Date.dt.month_name()
    df["year"]=df.message_Date.dt.year
    return_df=df
    return return_df