import turtle
import math

ws = turtle.Screen()
t = turtle.Turtle()
# background
ws.bgcolor('black')
ws.title('Space Invaders')
ws.addshape("/Users/jayesh/Downloads/roc.gif")
ws.addshape("/Users/jayesh/Downloads/invader.gif")
ws.addshape("/Users/jayesh/Downloads/laser.gif")
ws.bgpic("/Users/jayesh/Downloads/bg.gif")
ws.tracer(0)
n_l = 0
while True:
    answer = ws.textinput("Star Wars game", "Do you want to play level {}?".format(n_l + 1))

    if answer is None or answer.lower().startswith('n'):
        print("Bye!")
        break

    else:
        while True:

            n_l = n_l + 1
            level_pen = turtle.Turtle()
            level_pen.speed(0)
            level_pen.color("white")
            level_pen.penup()
            level_pen.setposition(-450, 400)
            level_string = 'level: %s' % n_l
            level_pen.write(level_string, False, align='left', font=('Arial', 15, 'normal'))
            level_pen.hideturtle()

            # square
            t.speed(0)
            t.color('white')
            t.penup()
            t.setposition(-500, -500)
            t.pensize(3)
            t.pendown()
            for side in range(4):
                t.fd(1000)
                t.lt(90)
            t.hideturtle()

            # score keeping
            score = 0
            score_pen = turtle.Turtle()
            score_pen.speed(0)
            score_pen.color("orange")
            score_pen.penup()
            score_pen.setposition(-150, 400)
            score_string = 'Score: %s' % score
            score_pen.write(score_string, False, align='left', font=('Arial', 84, 'normal'))
            score_pen.hideturtle()

            # bullet set
            bullet = turtle.Turtle()
            bullet.color('yellow')
            bullet.shape("/Users/jayesh/Downloads/laser.gif")
            bullet.penup()
            bullet.speed(0)
            bullet.setheading(90)
            bullet.shapesize(0.5, 0.5)
            bullet.setposition(0, -5000)
            bullet.hideturtle()
            b_speed = 20
            bullet_state = 'ready'

            # enemy set
            e_speed = 10

            number_of_e = 20
            es = []

            for i in range(number_of_e):
                es.append(turtle.Turtle())

            enemy_start_x = -450
            enemy_start_y = 350
            enemy_number = 0

            for enemy in es:
                enemy.color('red')
                enemy.shape("/Users/jayesh/Downloads/invader.gif")
                enemy.penup()
                enemy.speed(0)
                x = enemy_start_x + (125 * enemy_number)
                y = enemy_start_y
                enemy.setposition(x, y)
                enemy_number += 1
                if enemy_number == 5:
                    enemy_start_y -= 100
                    enemy_number = 0

            # player set
            speed = 15

            number_of_p = 1
            ps = []

            for i in range(number_of_p):
                ps.append(turtle.Turtle())

            x = 0
            y = -400
            player_number = 0

            for player in ps:
                player.shape("/Users/jayesh/Downloads/roc.gif")
                player.penup()
                player.shapesize(5, 5, 5)
                player.speed(0)
                player.lt(90)
                player.setposition(x, y)
                player_number += 1


            # firing bullet
            def fire_bullet():
                global bullet_state
                if bullet_state == 'ready':
                    bullet_state = 'fire'
                    x = player.xcor()
                    y = player.ycor()
                    bullet.setposition(x, y + 10)
                    bullet.showturtle()


            # coalition
            def is_col(t1, t2):
                distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
                if distance < 100:
                    return True
                else:
                    return False


            # mainloop
            while True:
                ws.update()
                ws.onkey(fire_bullet, 'space')
                ws.listen()

                for enemy in es:
                    x = enemy.xcor()
                    x += e_speed
                    enemy.setx(x)
                    if enemy.xcor() > 450:
                        e_speed *= -1
                    if enemy.xcor() < -450:
                        e_speed *= -1
                    if is_col(bullet, enemy):
                        bullet.hideturtle()
                        bullet_state = 'ready'
                        bullet.setposition(0, -5000)
                        enemy.setposition(0, 10000)
                        score += 5
                        score_string = 'Score: %s' % score
                        score_pen.clear()
                        score_pen.write(score_string, False, align='left', font=('Arial', 84, 'normal'))

                for player in ps:
                    x = player.xcor()
                    x += speed
                    player.setx(x)
                    if player.xcor() > 450:
                        speed *= -1
                    if player.xcor() < -450:
                        speed *= -1
                    if bullet_state == 'fire':
                        y = bullet.ycor()
                        y += b_speed
                        bullet.sety(y)
                    if bullet_state == 'fire':
                        y = bullet.ycor()
                        y += b_speed
                        bullet.sety(y)
                    if bullet.ycor() > 475:
                        bullet.hideturtle()
                        bullet_state = 'ready'

                if score == 100:
                    player.hideturtle()
                    score_pen.clear()
                    level_pen.clear()
                    break
            break
