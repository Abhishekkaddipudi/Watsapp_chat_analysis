import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import emoji
from collections import Counter
from functools import lru_cache
def messages_analysis(df):

    
    members=df["user"].unique()
    name=[]
    number_of_messages=[]
    if len(members)>10:
        members=members[:10]
    
        for i in members:
            name.append(i)
            number_of_messages.append(len(df[df["user"]==i]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_messages})
        fig,ax=plt.subplots()
        h.sort_values(by=["number of messages"])
        ax.bar(h["name"],h["number of messages"])
        ax.tick_params(axis='x', rotation=90) 
        return df.shape[0],fig,h
    else:
        for i in members:
            name.append(i)
            number_of_messages.append(len(df[df["user"]==i]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_messages})
        fig,ax=plt.subplots()
        h.sort_values(by=["number of messages"])
        ax.bar(h["name"],h["number of messages"],color="purple")
        ax.tick_params(axis='x', rotation=90)
        return df.shape[0],fig,h
    
def deleted_messages(df):
   
    members=df["user"].unique()
    name=[]
    number_of_delmsg=[]
    if len(members)>10:
        members=members[:10]
    
        for i in members:
            name.append(i)
            number_of_delmsg.append(len(df[(df["user"]==i)&(df["messages"].str.contains("this message was deleted|You deleted this message.",case=False))]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_delmsg})
        fig,ax=plt.subplots()
        ax.bar(h["name"],h["number of messages"])
        ax.tick_params(axis='x', rotation=90)
        return sum(number_of_delmsg),fig,h
    else:
        for i in members:
            name.append(i)
            number_of_delmsg.append(len(df[(df["user"]==i)&(df["messages"].str.contains("this message was deleted|You deleted this message.",case=False))]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_delmsg})
        fig,ax=plt.subplots()
        h.sort_values(by=["number of messages"])
        ax.bar(h["name"],h["number of messages"],color="purple")
        ax.tick_params(axis='x', rotation=90)
        return sum(number_of_delmsg),fig,h
    

def media_sent(df):
   
    members=df["user"].unique()
    name=[]
    number_of_media=[]
    if len(members)>10:
        members=members[:10]
    
        for i in members:
            name.append(i)
            number_of_media.append(len(df[(df["user"]==i)&(df["messages"].str.contains("omitted",case=False))]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_media})
        fig,ax=plt.subplots()
        ax.bar(h["name"],h["number of messages"])
        ax.tick_params(axis='x', rotation=90)
        return sum(number_of_media),fig,h
    else:
        for i in members:
            name.append(i)
            number_of_media.append(len(df[(df["user"]==i)&(df["messages"].str.contains("omitted",case=False))]))
        h=pd.DataFrame({"name":name,"number of messages": number_of_media})
        fig,ax=plt.subplots()
        h.sort_values(by=["number of messages"])
        ax.bar(h["name"],h["number of messages"],color="purple")
        ax.tick_params(axis='x', rotation=90)
        return sum(number_of_media),fig,h


def words_analysis(df):
    words=[]
    for i in df["messages"]:
        words.extend(i.strip("\u200e").split())
    item=['sticker','omitted','image','This','message','was','deleted.','video','<Media','omitted>']
    words=list(filter(lambda x: x not in item and not emoji.is_emoji(x), words))

    word_string = ' '.join(words)
    wc=WordCloud(width=700,height=700,min_font_size=10,background_color="white")
    wc_gene=wc.generate(word_string)
    word_count=Counter(words)
    df_words=pd.DataFrame(word_count.most_common(10),columns=["words","count"])
    return len(word_count),wc_gene,df_words

def emoji_analysis(df):
    emojis=[]
    for i in df["messages"]:
        for c in i:
            if emoji.is_emoji(c):
                emojis.append(c)
    emoji_count=Counter(emojis)
    df_emoji=pd.DataFrame(emoji_count.most_common(5),columns=["emoji","count"])
    labels_with_names=[emoji.demojize(label)[1:] for label in df_emoji["emoji"]]
   
    return len(emojis),labels_with_names,df_emoji

def busiest_month(df):
    timeline=df.groupby(["year","month"]).count()["messages"].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i]+"-"+str(timeline["year"][i]))
    timeline["time"]=time
    day_timeline=df["day"].value_counts()
    fig,ax=plt.subplots()
    ax.barh(day_timeline.keys(),day_timeline,color="purple")

    for index, value in enumerate(day_timeline):
        ax.text(value, index,
                 str(value))
    return timeline,fig

        
  
