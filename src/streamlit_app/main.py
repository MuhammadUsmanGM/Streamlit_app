import random
import time

import streamlit as st

st.title("Adventure Game")
st.header("Welcome to the Adventure Game")
st.subheader("Enjoy the Endless Adventure")

st.write("Welcome...")
time.sleep(3)
if "inventory" not in st.session_state:
        st.session_state.inventory = []
if "health" not in st.session_state:
        st.session_state.health = 100
if "location" not in st.session_state:
        st.session_state.location = "Choose"    
user = st.selectbox(
            "Choose a Location",
            ["Choose", "Forest", "River", "Cave", "Quit"],
            key="location_radio",
        )
st.write(f"Health: {st.session_state.health}")
st.write(f"Inventory: {st.session_state.inventory}")

if user == "Forest":
            st.write(f"You selected {user}...")
            st.write(f"Waiting to enter in {user}...")
            time.sleep(3)
            st.write("You are in a Forest.")
            time.sleep(2)
            st.write("It seems quit in here.")
            time.sleep(2)
            st.write("You are in front of a lion.")
            time.sleep(2)
            if "lion" not in st.session_state:
                st.session_state.lion = "Choose"
            lion = st.radio(
                        "You wanna fight the lion",
                        ["Choose", "Yes", "No"],
                        key="lion_radio",
                    )

            if lion == "Yes":
                        st.write("You are having  a great fight.")
                        time.sleep(3)
                        damage = random.randint(0, 40)
                        st.session_state.health = st.session_state.health - damage

                        if st.session_state.health > 0:
                            st.write(f"You got a damage of {damage}")
                            st.write("You had a great fight.")
                            st.write(f"Your Health {st.session_state.health}")
                            st.write("After defeating lion,You found a Glowing Crystal")
                            if "crystal" not in st.session_state:
                                st.session_state.crystal = "Choose"
                            crystal = st.radio(
                                f"You wanna collect Glowing Crystal or not.",
                                ["Choose", "Yes", "No"],
                                key="crystal_radio",
                            )
                        
                        if crystal == "Yes":
                            st.session_state.inventory.append("Glowing Crystal")
                            st.write("Glowing Crystal added in your inventory.")
                            st.write(st.session_state.inventory)
                        elif crystal == "No":
                            st.write("You missed the treasure of your fate.")
                        elif st.session_state.health <= 0:
                            st.write("You died...")
                            st.write("you lost your inventory.")
                
            elif lion == "No":
                        st.write("You escaped from your fate.")
                        

elif user == "Cave":
                    st.write(f"You selected {user}...")
                    st.write(f"Waiting to enter in {user}...")
                    time.sleep(3)
                    st.write("You entered in a Cave.")
                    time.sleep(2)
                    st.write("It seem darkness rules in this cave")
                    time.sleep(2)
                    st.write("In this quite and dark,a bear is ready to have you in dinner.")
                    time.sleep(2)
                    if "bear" not in st.session_state:
                        st.session_state.bear = "Choose"
                    bear = st.radio(
                        "You wanna fight with bear.",
                        ["Choose", "Yes", "No"],
                        key="bear_radio",
                    )

                    if bear == "Yes":
                        st.write("You are having a fight with bear.")
                        time.sleep(3)
                        damage = random.randint(0, 40)
                        st.session_state.health = st.session_state.health - damage

                        if st.session_state.health > 0:
                            st.write(f"You got a damage of {damage}")
                            st.write("You had a great fight with the bear")
                            st.write(f"Your Health {st.session_state.health}")
                            st.write(
                                f"As expected after defeating bear,You found a Piece of valuable gold"
                            )
                            if "gold" not in st.session_state:
                                st.session_state.gold = "Choose"
                            gold = st.radio(
                                f"You wanna collect Piece of valuable gold or not.",
                                ["Choose", "Yes", "No"],
                                key="gold_radio",
                            )
                            
                            if gold == "Yes":
                                st.session_state.inventory.append("Piece of valuable gold")
                                st.write("Piece of valuable gold added to your inventory.")
                                st.write(st.session_state.inventory)
                            elif gold == "No":
                                st.write("You just missed a valuable Item")
                        elif st.session_state.health <= 0:
                            st.write("You Died...")
                            st.write("You lost your inventory")
                            
                    elif bear == "No":
                        st.write("You escaped from your fate.")
                        

elif user == "River":
                    st.write(f"You selected {user}...")
                    st.write(f"Waiting to enter in {user}...")
                    time.sleep(3)
                    st.write("You are in a river.Water is a little bit cold.")
                    time.sleep(2)
                    st.write("There's a crocodile in front of you.")
                    time.sleep(2)
                    if "crocodile" not in st.session_state:
                        st.session_state.crocodile = "Choose"
                    crocodile = st.radio(
                        "You wanna fight with the crocodile.",
                        ["Choose", "Yes", "No"],
                        key="crocodile_radio",
                    )

                    if crocodile == "Yes":
                        st.write("You are having a fight with Crocodile.")
                        time.sleep(3)
                        damage = random.randint(0, 40)
                        st.session_state.health = st.session_state.health - damage

                        if st.session_state.health > 0:
                            st.write(f"You got a damage of {damage}")
                            st.write(
                                "Fight with Crocodile was a little bit scary\n but it was an great experience."
                            )
                            st.write(f"Your Health {st.session_state.health}")
                            st.write(f"You found a Pearl in the water")
                            time.sleep(2)
                            if "pearl" not in st.session_state:
                                st.session_state.pearl = "Choose"
                            pearl = st.radio(
                                f"YOu wanna collect Pearl or not.",
                                ["Choose", "Yes", "No"],
                                key="pearl_radio",
                            )
                            if pearl == "Yes":
                                st.session_state.inventory.append("Pearl")
                                st.write("Pearl is added in your inventory.")
                                st.write(st.session_state.inventory)
                            elif pearl == "No":
                                st.write("You missed the reward of fight you have.")
                        elif st.session_state.health <= 0:
                            st.write("You Died")
                            st.write("You lost your inventory...")
                            
                    elif crocodile == "No":
                        st.write("You escaped from your fate.")
                        
elif user == "Quit":
                st.write("You are quitting the game...")
                st.write("You Escaped...")
                st.stop()
                st.rerun()
                

elif user == "Choose":
                st.write("Please select a location...")