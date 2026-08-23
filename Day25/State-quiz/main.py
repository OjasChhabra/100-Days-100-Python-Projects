import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("India State Game")
screen.bgpic(r"Day25\State-quiz\blank_states_img.gif")


def mouse_click(x, y):
    print(x, y)
turtle.onscreenclick(mouse_click)



turtle.mainloop()