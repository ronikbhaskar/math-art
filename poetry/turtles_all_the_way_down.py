from turtle import Turtle, title, done as turtled

title('turtles all the way down')

def turtle(turtles, turtle_c):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.turtlesize(*turtles)
    turtle.color(turtle_c)
    return [turtle - 0.49 for turtle in turtles], [turtle for turtle in turtle_c[1:]+turtle_c[:1]]

turtle(
    *turtle(
        *turtle(
            *turtle(
                *turtle(
                    *turtle(
                        *turtle(
                            *turtle(
                                *turtle(
                                    *turtle(
                                        *turtle(
                                            *turtle(
                                                *turtle(
                                                    *turtle(
                                                        *turtle(
                                                            *turtle(
                                                                *turtle(
                                                                    *turtle(
                                                                        *turtle(
                                                                            *turtle(
                                                                                *turtle(
                                                                                    *turtle(
                                                                                        *turtle(
                                                                                            *turtle(
                                                                                                *turtle(
                                                                                                    *turtle(
                                                                                                        *turtle(
                                                                                                            *turtle(
                                                                                                                *turtle(
                                                                                                                    *turtle(
                                                                                                                        *turtle(
                                                                                                                            *turtle(
                                                                                                                                *turtle(
                                                                                                                                    *turtle(
                                                                                                                                        *turtle(
                                                                                                                                            *turtle(
                                                                                                                                                *turtle(
                                                                                                                                                    *turtle(
                                                                                                                                                        *turtle(
                                                                                                                                                            *turtle(
                                                                                                                                                                *turtle(
                                                                                                                                                                    *turtle(
                                                                                                                                                                        (21,21,21),(0.5,0.5,1)
                                                                                                                                                                    )
                                                                                                                                                                )
                                                                                                                                                            )
                                                                                                                                                        )
                                                                                                                                                    )
                                                                                                                                                )
                                                                                                                                            )
                                                                                                                                        )
                                                                                                                                    )
                                                                                                                                )
                                                                                                                            )
                                                                                                                        )
                                                                                                                    )
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

turtled()