import pandas
import turtle


screen = turtle.Screen()
screen.title("Nigerian States Game")
image = "./Day25-Working-with-CSV-Data-and-the-Pandas-Library/nigeria-map.gif"
screen.addshape(image)
turtle.shape(image)


nigerian_states_df = pandas.read_csv("./Day25-Working-with-CSV-Data-and-the-Pandas-Library/37_states.csv")

title = "Guess the State"
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").lower().strip()
    if answer_state == "exit":
        missed_states = []
        for state in nigerian_states_df.State.str.lower():
            if state not in guessed_states:
                missed_states.append(state)
        missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
        missed_states_df.to_csv("./Day25-Working-with-CSV-Data-and-the-Pandas-Library/states_to_learn.csv")
        break
    for num in range(nigerian_states_df.State.size):
        if answer_state == nigerian_states_df.State[num].lower() and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.pencolor("black")
            new_turtle.goto(nigerian_states_df.x[num], nigerian_states_df.y[num])
            new_turtle.write(nigerian_states_df.State[num])
            title = f"{len(guessed_states)}/37 States Correct"


turtle.mainloop()