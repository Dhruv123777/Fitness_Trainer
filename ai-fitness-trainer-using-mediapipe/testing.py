import streamlit as st
import os

video_path  = "output_sample.mp4"

if os.path.isfile(video_path):
    st.video(video_path)
else:
    st.error(f"Video not found at: {video_path}")


st.title('AI Fitness Trainer: Squats Analysis')


    

    


