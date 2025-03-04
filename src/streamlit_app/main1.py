import random
import time

import streamlit as st

st.title("Rock Paper Scissors")
st.header("In this game, You will play rock paper scissors against an AI.")
time.sleep(2)
st.write("Please wait...")
time.sleep(3)

# Initialize session state variables if they don't exist
if "move" not in st.session_state:
    st.session_state.move = "choose"
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "opponent_score" not in st.session_state:
    st.session_state.opponent_score = 0

move = st.selectbox("Choose Your move", ["Choose", "Rock", "Paper", "Scissors"])
if move.lower() == "choose":
    time.sleep(2)
    st.write("Please choose a move to start the game.")
elif move.lower() == "rock" or move.lower() == "paper" or move.lower() == "scissors":
    st.subheader("ROCK")
    time.sleep(1)
    st.subheader("PAPER")
    time.sleep(1)
    st.subheader("SCISSORS")
    time.sleep(1)
    st.subheader("SHOOT")
    time.sleep(1)
    st.write(f"Your move: {move}")
    opponent = random.choice(["Rock", "Paper", "Scissors"])
    st.write(f"Opponent's move: {opponent}")
    time.sleep(2)
    if move.lower() == opponent.lower():
        st.write("It's a Tie")
        st.write(f"Your Score: {st.session_state.player_score}")
        st.write(f"Opponent's score: {st.session_state.opponent_score}")
    elif (
        (move.lower() == "rock" and opponent.lower() == "scissors")
        or (move.lower() == "scissors" and opponent.lower() == "paper")
        or (move.lower() == "paper" and opponent.lower() == "rock")
    ):
        st.write("You Win!")
        st.session_state.player_score += 1
        st.write(f"Your Score: {st.session_state.player_score}")
        st.write(f"Opponent's score: {st.session_state.opponent_score}")
    else:
        st.write("You Lose!")
        st.session_state.opponent_score += 1
        st.write(f"Your Score: {st.session_state.player_score}")
        st.write(f"Opponent's score: {st.session_state.opponent_score}")
    if st.session_state.player_score == 5 or st.session_state.opponent_score == 5:
        if st.session_state.player_score == 5:
            st.write(
                f"You Win this round by {st.session_state.player_score - st.session_state.opponent_score} points."
            )
        elif st.session_state.opponent_score == 5:
            st.write(
                f"You lose this round by {st.session_state.opponent_score - st.session_state.player_score} points."
            )
