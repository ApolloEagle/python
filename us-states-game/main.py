import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
states = data.state.tolist()

count = 0
while count < len(data):
    answer_state = screen.textinput(title=(f'Guess the State {count}/{len(data)}'), prompt="What is the state's name?").title()
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[answer_state == data.state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        count += 1
    
screen.exitonclick()
