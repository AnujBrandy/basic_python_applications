import turtle

def make_square( turtle_mover ) :
	
	# turtle_mover = turtle.Turtle( )
	# turtle_mover.shape( "turtle" )
	# turtle_mover.color( "red" )
	# turtle_mover.speed( 2 )

	square_count = 4
	break_square_count = 0
	while break_square_count < square_count :
		turtle_mover.forward( 100 )
		turtle_mover.right( 90 )
		break_square_count = break_square_count + 1
	

def make_circle( ) :
	turtle_mover_new = turtle.Turtle( )
	turtle_mover_new.shape( "arrow" )
	turtle_mover_new.color( "blue" )
	turtle_mover_new.speed( 2 )

	turtle_mover_new.circle( 100 )


def draw_circle_from_squares( ) :
	no_of_squares = 360
	break_square_count = 0

	turtle_mover = turtle.Turtle( )
	turtle_mover.shape( "turtle" )
	turtle_mover.color( "red" )
	turtle_mover.speed( 2 )

	while break_square_count < no_of_squares :
		make_square( turtle_mover )
		turtle_mover.right( 1 )
		break_square_count = break_square_count + 1

window = turtle.Screen( )
window.bgcolor( "yellow" )
draw_circle_from_squares( )
window.exitonclick( )


