import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
 

def iphone(data,option1):
    df=preprocess.preprocessor_iphone(data,option1)
    st.dataframe(df)
  
    st.header("Analysis")
    #messages
    st.header("Total messages")
    num,fig,df_u=helper.messages_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)

    #messages deleted
    st.header("Total messages deleted")
    num,fig,df_u=helper.deleted_messages(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)
    #media
    st.header("Total Media Sent")
    num,fig,df_u=helper.media_sent(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)
    #words
    st.header("Number of Words used")
    num,wc_gene,df_u=helper.words_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:

        fig,ax=plt.subplots()
        ax.imshow(wc_gene)
        st.pyplot(fig)

    #Emoji
    st.header("Number of emoji sent")
    num,wedges,df_u=helper.emoji_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        fig,ax=plt.subplots()
        fig.patch.set_alpha(0.0)
  
        _, texts, autotexts=ax.pie(df_u["count"],labels=wedges,autopct='%1.1f%%', startangle=140)
        _=[text.set_color('purple') for text in texts]
        _=[autotext.set_color('white') for autotext in autotexts]
        ax.axis('equal')
        
        st.pyplot(fig) 
    #time analysis
    st.header("Time Analysis")
    timeline,fig_d=helper.busiest_month(df)
   
    col1,col2=st.columns(2)    
    with col1:
        fig,ax=plt.subplots()
        ax.plot(timeline["time"],timeline["messages"],)
        ax.set_xticks(timeline["time"])
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    with col2:

        st.pyplot(fig_d)
def android(data,option1):
    df=preprocess.preprocessor_android(data,option1)
    st.dataframe(df)
  
    st.header("Analysis")
    #messages
    st.header("Total messages")
    num,fig,df_u=helper.messages_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)

    #messages deleted
    st.header("Total messages deleted")
    num,fig,df_u=helper.deleted_messages(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)
    #media
    st.header("Total Media Sent")
    num,fig,df_u=helper.media_sent(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        st.pyplot(fig)
    #words
    st.header("Number of Words used")
    num,wc_gene,df_u=helper.words_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)
   
    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:

        fig,ax=plt.subplots()
        ax.imshow(wc_gene)
        st.pyplot(fig)

    #Emoji
    st.header("Number of emoji sent")
    num,wedges,df_u=helper.emoji_analysis(df)
    st.header(f"{num}")
    col1,col2=st.columns(2)    
    with col1:
        st.dataframe(df_u,hide_index=True)
    with col2:
        fig,ax=plt.subplots()
        fig.patch.set_alpha(0.0)
  
        _, texts, autotexts=ax.pie(df_u["count"],labels=wedges,autopct='%1.1f%%', startangle=140)
        _=[text.set_color('purple') for text in texts]
        _=[autotext.set_color('white') for autotext in autotexts]
        ax.axis('equal')
        
        st.pyplot(fig) 
    #time analysis
    st.header("Time Analysis")
    timeline,fig_d=helper.busiest_month(df)
   
    col1,col2=st.columns(2)    
    with col1:
        fig,ax=plt.subplots()
        ax.plot(timeline["time"],timeline["messages"],)
        ax.set_xticks(timeline["time"])
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    with col2:

        st.pyplot(fig_d)





def main():
     
    st.title("WhatsApp Chat Analysis")

    # Add boundary around the file uploader
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload a file", type=["txt"])

    # Add boundary around the option buttons
    st.markdown("---")
    option = st.radio("Select your device:", ("Android", "iPhone"))

    option1 = st.radio("Select your hour format:", ("24 hour", "12 hour"))
    # Display the uploaded image (if any)
    st.markdown("---")
    
    if st.button("Submit"):
        # Check the selected option and perform corresponding action
        
          
        
         
        if uploaded_file is not None:
            bytes_data=uploaded_file.getvalue()
            data=bytes_data.decode("utf-8")
            if option == "Android":
                
                android(data,option1)
            elif option == "iPhone":
                iphone(data,option1)
        st.markdown("---")











if __name__ == "__main__":
    main()
