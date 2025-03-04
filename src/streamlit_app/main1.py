import streamlit as st 
import random
import time

st.title("Rock Paper Scissors")
st.header("In this game, You will play rock paper scissors against an AI.")
time.sleep(2)
st.write("Please wait...")
time.sleep(3)

if "move" not in st.session_state:
    move="choose"

player_score=0
if "opponent_score" not in st.session_state:
    opponent_score=0
    
move=st.selectbox("Choose Your move",["Choose","Rock","Paper","Scissors"])
if move.lower()=="choose":
    time.sleep(2)
    st.write("Please choose a move to start the game.")
elif move.lower()=="rock" or move.lower()=="paper" or move.lower()=="scissors":
    st.subheader("ROCK")
    time.sleep(1)
    st.subheader("PAPER")
    time.sleep(1)
    st.subheader("SCISSORS")
    time.sleep(1)
    st.subheader("SHOOT")
    time.sleep(1)
    st.write(f"Your move: {move}")
    opponent=random.choice(["Rock","Paper","Scissors"])
    st.write(f"Opponent's move: {opponent}")
    time.sleep(2)
    if move.lower()==opponent.lower():
        st.write("It's a Tie")

        st.write(f"Your Score: {player_score}")
        st.write(f"Opponent's score: {opponent_score}")
    elif (move.lower()=="rock" and opponent.lower()=="scissors") or (move.lower()=="scissors" and opponent.lower()=="paper") or (move.lower()=="paper" and opponent.lower()=="rock"):
        st.write("You Win!")
        player_score+=1
        st.write(f"Your Score: {player_score}")
        st.write(f"Opponent's score: {opponent_score}")
    else:
        st.write("You Lose!")
        opponent_score+=1
        st.write(f"Your Score: {player_score}")
        st.write(f"Opponent's score: {opponent_score}")
    if player_score==5 or opponent_score==5:
        if player_score==5:
            st.write(f"You Win this round by {player_score-opponent_score} points.")
        elif opponent_score==5:
            st.write(f"You lose this round by {opponent_score-player_score} points.")
        st.rerun()