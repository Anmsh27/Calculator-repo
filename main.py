import os

from module_missing import no_module_error

try:
    import pygame
except ModuleNotFoundError:
    no_module_error()
import math
from datetime import date, datetime
from button_class import Button
from math_extras import cube_root
from exception_handler import FactorialException, value_error, zero_division_error, factorial_error, overflow_error
from sys import exit

pygame.init()
dir = os.getcwd()
path = dir
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Calculator")
bg = (0, 255, 255)
clock = pygame.time.Clock()
time = datetime.now()
time = time.strftime("%H:%M:%S")
today = date.today()
today = today.strftime("%B %d, %Y")

bg_for_main = pygame.Rect(0, 200, screen_width, screen_height)
butt1 = Button(0, 200, 100, 100, (235, 89, 52), 100, "1")
butt2 = Button(100, 200, 100, 100, (235, 89, 52), 100, "2")
butt3 = Button(200, 200, 100, 100, (235, 89, 52), 100, "3")
plus = Button(300, 200, 100, 100, (235, 89, 52), 100, "+")
butt4 = Button(0, 300, 100, 100, (235, 89, 52), 100, "4")
butt5 = Button(100, 300, 100, 100, (235, 89, 52), 100, "5")
butt6 = Button(200, 300, 100, 100, (235, 89, 52), 100, "6")
minus = Button(300, 300, 100, 100, (235, 89, 52), 100, "-")
butt7 = Button(0, 400, 100, 100, (235, 89, 52), 100, "7")
butt8 = Button(100, 400, 100, 100, (235, 89, 52), 100, "8")
butt9 = Button(200, 400, 100, 100, (235, 89, 52), 100, "9")
multi = Button(300, 400, 100, 100, (235, 89, 52), 100, "x")
dot = Button(0, 500, 100, 100, (235, 89, 52), 100, ".")
butt0 = Button(100, 500, 100, 100, (235, 89, 52), 100, "0")
equal = Button(200, 500, 100, 100, (235, 89, 52), 100, "=")
divid = Button(300, 500, 100, 100, (235, 89, 52), 100, "/")
clear = Button(325, 0, 75, 75, (235, 89, 52), 0, "C")
sin = Button(0, 240, 100, 100, (0, 0, 0), 100, "sin")
cos = Button(100, 240, 100, 100, (0, 0, 0), 100, "cos")
tan = Button(200, 240, 100, 100, (0, 0, 0), 100, "tan")
degtorad = Button(300, 240, 100, 100, (0, 0, 0), 100, "rad")
radtodeg = Button(300, 340, 100, 100, (0, 0, 0), 100, "deg")
asin = Button(0, 340, 100, 100, (0, 0, 0), 100, "asin")
acos = Button(100, 340, 100, 100, (0, 0, 0), 100, "acos")
atan = Button(200, 340, 100, 100, (0, 0, 0), 100, "atan")
cot = Button(0, 440, 100, 100, (0, 0, 0), 100, "cot")
sec = Button(100, 440, 100, 100, (0, 0, 0), 100, "sec")
csc = Button(200, 440, 100, 100, (0, 0, 0), 100, "csc")
fact = Button(300, 440, 100, 100, (0, 0, 0), 100, "!")
sqrt_butt = Button(0, 540, 100, 100, (0, 0, 0), 100, "sqrt")
cbrt_butt = Button(100, 540, 100, 100, (0, 0, 0), 100, "cbrt")
pow = Button(200, 540, 100, 100, (0, 0, 0), 100, "^")
history_butt = Button(300, 540, 100, 100, (0, 0, 0), 100, "H")
second_x = 0
second_y = 600
second_y_change = 0
more_butt = Button(0, second_y, screen_width, 40, (0, 0, 0), 0, None)
more_butt_text = pygame.font.Font(None, 64)
more_butt_text_rendered = more_butt_text.render("MORE OPTIONS", True, (255, 255, 255))

val1 = ""
op = ""
val2 = ""
result = 0
rendered = ""
result_is_ready = False
do_value_error = False
do_zero_division_error = False
do_factorial_error = False
do_overflow_error = False
clicked_color = (127, 129, 133)
second_gui_state = False


while True:
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.unicode == "1" and op != "!":
                if not op:
                    val1 += "1"
                elif op:
                    val2 += "1"
            if event.key == pygame.K_2 and op != "!":
                if not op:
                    val1 += "2"
                elif op:
                    val2 += "2"
            if event.key == pygame.K_3 and op != "!":
                if not op:
                    val1 += "3"
                elif op:
                    val2 += "3"
            if event.unicode == "+" and op != "!":
                op = "+"
            if event.key == pygame.K_4 and op != "!":
                if not op:
                    val1 += "4"
                elif op:
                    val2 += "4"
            if event.key == pygame.K_5 and op != "!":
                if not op:
                    val1 += "5"
                elif op:
                    val2 += "5"
            if event.key == pygame.K_6 and op != "!" and event.unicode != "^":
                if not op:
                    val1 += "6"
                elif op:
                    val2 += "6"
            if event.key == pygame.KSCAN_MINUS and op != "!":
                if val1:
                    op = "-"
                if not val1:
                    val1 += "-"
                if op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "asin" or op == "acos" or op == "atan":
                    val1 = ""
                    tmp = val2
                    val2 = "-"
                    val2 += tmp
            if event.key == pygame.K_7 and op != "!":
                if not op:
                    val1 += "7"
                elif op:
                    val2 += "7"
            if event.key == pygame.K_8 and event.unicode != "*" and op != "!":
                if not op:
                    val1 += "8"
                elif op:
                    val2 += "8"
            if event.key == pygame.K_9 and op != "!":
                if not op:
                    val1 += "9"
                elif op:
                    val2 += "9"
            if event.unicode == "*" and op != "!":
                op = "*"
            if event.key == pygame.K_PERIOD and op != "!":
                if not op:
                    val1 += "."
                elif op:
                    val2 += "."
            if event.key == pygame.K_0 and op != "!":
                if not op:
                    val1 += "0"
                elif op:
                    val2 += "0"
            if event.unicode == "/" and op != "!":
                op = "/"
            if event.key == pygame.K_BACKSPACE:
                if not op and val1:
                    val1 = val1[:-1]
                elif op and not val2:
                    op = op[:-1]
                elif op and val2:
                    val2 = val2[:-1]
            if event.unicode == "!":
                op = "!"
            if event.unicode == "^":
                op = "^"
            if event.key == pygame.K_m:
                if second_y > 200:
                    second_y_change = 50
                    second_gui_state = True
                if second_y <= 200:
                    second_y_change = -50
                    second_gui_state = False
            if event.key == pygame.K_EQUALS:
                if op:
                    if "!" in op:
                        try:
                            try:
                                int(val1)
                            except ValueError:
                                raise FactorialException
                            if val1 == 0:
                                result = 1
                            else:
                                try:
                                    result = math.factorial(int(val1))
                                except ValueError:
                                    raise FactorialException
                        except ValueError:
                            do_value_error = True
                        except FactorialException:
                            do_factorial_error = True
                        except ZeroDivisionError:
                            do_zero_division_error = True
                        except OverflowError:
                            do_overflow_error = True
                        font = pygame.font.Font(None, 100)
                        result = str(result)
                        rendered = font.render(result, True, (0, 0, 0))
                        result_is_ready = True
                    if val2:
                        if "sin" in op:
                            val1 = ""
                            try:
                                result = math.sin(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "cos" in op:
                            val1 = ""
                            try:
                                if val2 == "90" or val2 == "270":
                                    result = 0
                                else:
                                    result = math.cos(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "tan" in op:
                            val1 = ""
                            try:
                                if val2 == "90":
                                    result = "Not defined"
                                else:
                                    result = math.tan(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "cot" in op:
                            val1 = ""
                            try:
                                if val2 == "90":
                                    result = "Not defined"
                                else:
                                    result = 1/math.tan(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "sec" in op:
                            val1 = ""
                            try:
                                if val2 == "90" or val2 == "270":
                                    result = 0
                                else:
                                    result = 1/math.cos(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "csc" in op:
                            val1 = ""
                            try:
                                result = 1/math.sin(math.radians(float(val2)))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "rad" in op:
                            val1 = ""
                            try:
                                result = math.radians(float(val2))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "deg" in op:
                            val1 = ""
                            try:
                                result = math.degrees(float(val2))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "asin" in op:
                            val1 = ""
                            try:
                                result = math.degrees(math.asin(float(val2)))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "acos" in op:
                            val1 = ""
                            try:
                                result = math.degrees(math.acos(float(val2)))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "atan" in op:
                            val1 = ""
                            try:
                                result = math.degrees(math.atan(float(val2)))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "sqrt" in op:
                            val1 = ""
                            try:
                                result = math.sqrt(float(val2))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "cbrt" in op:
                            val1 = ""
                            try:
                                result = cube_root(float(val2))
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "/" in op:
                            try:
                                result = float(val1) / float(val2)
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "^" in op:
                            try:
                                result = math.pow(float(val1), float(val2))
                            except ValueError:
                                do_value_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            except OverflowError:
                                do_overflow_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "*" in op:
                            try:
                                result = float(val1) * float(val2)
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "+" in op:
                            try:
                                result = float(val1) + float(val2)
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if "-" in op:
                            try:
                                result = float(val1) - float(val2)
                            except ValueError:
                                do_value_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                history = open('history.txt', 'a')
                history.write(
                    today + " at " + time + ":\n" + str(val1) + " " + str(op) + " " + str(
                        val2) + " = " + str(result) + "\n" + "\n")
                history.close()
            if event.key == pygame.K_c:
                result_is_ready = False
                result = ""
                val1 = ""
                val2 = ""
                op = ""
                do_value_error = False
                do_zero_division_error = False
                do_factorial_error = False
                do_overflow_error = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if butt1.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "1"
                    elif op:
                        val2 += "1"
                if sin.clicked(mousex, mousey) and second_gui_state:
                    op = "sin"
                if butt2.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "2"
                    elif op:
                        val2 += "2"
                if cos.clicked(mousex, mousey) and second_gui_state:
                    op = "cos"
                if butt3.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "3"
                    elif op:
                        val2 += "3"
                if tan.clicked(mousex, mousey) and second_gui_state:
                    op = "tan"
                if degtorad.clicked(mousex, mousey) and second_gui_state:
                    op = "rad"
                if plus.clicked(mousex, mousey) and not second_gui_state:
                    op = "+"
                if butt4.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "4"
                    elif op:
                        val2 += "4"
                if asin.clicked(mousex, mousey) and second_gui_state:
                    op = "asin"
                if butt5.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "5"
                    elif op:
                        val2 += "5"
                if acos.clicked(mousex, mousey) and second_gui_state:
                    op = "acos"
                if butt6.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "6"
                    elif op:
                        val2 += "6"
                if atan.clicked(mousex, mousey) and second_gui_state:
                    op = "atan"
                if minus.clicked(mousex, mousey) and not second_gui_state:
                    if val1:
                        op = "-"
                    if not val1:
                        val1 += "-"
                    if op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "asin" or op == "acos" or op == "atan":
                        val1 = ""
                        tmp = val2
                        val2 = "-"
                        val2 += tmp
                if radtodeg.clicked(mousex, mousey) and second_gui_state:
                    op = "deg"
                if butt7.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "7"
                    elif op:
                        val2 += "7"
                if sqrt_butt.clicked(mousex, mousey) and second_gui_state:
                    op = "sqrt"
                if butt8.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "8"
                    elif op:
                        val2 += "8"
                if cbrt_butt.clicked(mousex, mousey) and second_gui_state:
                    op = "cbrt"
                if butt9.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "9"
                    elif op:
                        val2 += "9"
                if pow.clicked(mousex, mousey) and second_gui_state:
                    op = "^"
                if multi.clicked(mousex, mousey) and not second_gui_state:
                    op = "*"
                if history_butt.clicked(mousex, mousey) and second_gui_state:
                    try:
                        history.close()
                        os.system(f'cd {path}')
                        os.system('.\history.txt')
                        open('history.txt', 'a')
                    except:
                        pass
                if dot.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "."
                    elif op:
                        val2 += "."
                if butt0.clicked(mousex, mousey) and not second_gui_state:
                    if not op:
                        val1 += "0"
                    elif op:
                        val2 += "0"
                if divid.clicked(mousex, mousey) and not second_gui_state:
                    op = "/"
                if more_butt.clicked(mousex, mousey):
                    if second_y > 200:
                        second_y_change = 50
                        second_gui_state = True
                    if second_y <= 200:
                        second_y_change = -50
                        second_gui_state = False
                if fact.clicked(mousex, mousey) and second_gui_state:
                    op = "!"
                if cot.clicked(mousex, mousey) and second_gui_state:
                    op = "cot"
                if sec.clicked(mousex, mousey) and second_gui_state:
                    op = "sec"
                if csc.clicked(mousex, mousey) and second_gui_state:
                    op = "csc"
                if equal.clicked(mousex, mousey):
                    if op:
                        if "!" in op:
                            try:
                                try:
                                    int(val1)
                                except ValueError:
                                    raise FactorialException
                                if val1 == 0:
                                    result = 1
                                else:
                                    try:
                                        result = math.factorial(int(val1))
                                    except ValueError:
                                        raise FactorialException
                            except ValueError:
                                do_value_error = True
                            except FactorialException:
                                do_factorial_error = True
                            except ZeroDivisionError:
                                do_zero_division_error = True
                            except OverflowError:
                                do_overflow_error = True
                            font = pygame.font.Font(None, 100)
                            result = str(result)
                            rendered = font.render(result, True, (0, 0, 0))
                            result_is_ready = True
                        if val2:
                            if "sin" in op:
                                val1 = ""
                                try:
                                    result = math.sin(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "cos" in op:
                                val1 = ""
                                try:
                                    if val2 == "90" or val2 == "270":
                                        result = 0
                                    else:
                                        result = math.cos(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "tan" in op:
                                val1 = ""
                                try:
                                    if val2 == "90":
                                        result = "Not defined"
                                    else:
                                        result = math.tan(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "cot" in op:
                                val1 = ""
                                try:
                                    if val2 == "90":
                                        result = "Not defined"
                                    else:
                                        result = 1 / math.tan(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "sec" in op:
                                val1 = ""
                                try:
                                    if val2 == "90" or val2 == "270":
                                        result = 0
                                    else:
                                        result = 1 / math.cos(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "csc" in op:
                                val1 = ""
                                try:
                                    result = 1 / math.sin(math.radians(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "rad" in op:
                                val1 = ""
                                try:
                                    result = math.radians(float(val2))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "deg" in op:
                                val1 = ""
                                try:
                                    result = math.degrees(float(val2))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "asin" in op:
                                val1 = ""
                                try:
                                    result = math.degrees(math.asin(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "acos" in op:
                                val1 = ""
                                try:
                                    result = math.degrees(math.acos(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "atan" in op:
                                val1 = ""
                                try:
                                    result = math.degrees(math.atan(float(val2)))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "sqrt" in op:
                                val1 = ""
                                try:
                                    result = math.sqrt(float(val2))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "cbrt" in op:
                                val1 = ""
                                try:
                                    result = cube_root(float(val2))
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "/" in op:
                                try:
                                    result = float(val1) / float(val2)
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "^" in op:
                                try:
                                    result = math.pow(float(val1), float(val2))
                                except ValueError:
                                    do_value_error = True
                                except ZeroDivisionError:
                                    do_zero_division_error = True
                                except OverflowError:
                                    do_overflow_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "*" in op:
                                try:
                                    result = float(val1) * float(val2)
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "+" in op:
                                try:
                                    result = float(val1) + float(val2)
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                            if "-" in op:
                                try:
                                    result = float(val1) - float(val2)
                                except ValueError:
                                    do_value_error = True
                                font = pygame.font.Font(None, 100)
                                result = str(result)
                                rendered = font.render(result, True, (0, 0, 0))
                                result_is_ready = True
                    history = open('history.txt', 'a')
                    history.write(
                        today + " at " + time + ":\n" + str(val1) + " " + str(op) + " " + str(
                            val2) + " = " + str(result) + "\n" + "\n")
                    history.close()
                if clear.clicked(mousex, mousey):
                    result_is_ready = False
                    result = ""
                    val1 = ""
                    val2 = ""
                    op = ""
                    do_value_error = False
                    do_zero_division_error = False
                    do_factorial_error = False
                    do_overflow_error = False
    more_butt.y = second_y
    second_y -= second_y_change
    if second_y <= 200 or second_y >= 600:
        second_y_change = 0
    pygame.draw.rect(screen, (0, 0, 0), bg_for_main)
    butt1.draw_button(screen)
    butt2.draw_button(screen)
    butt3.draw_button(screen)
    plus.draw_button(screen)
    butt4.draw_button(screen)
    butt5.draw_button(screen)
    butt6.draw_button(screen)
    minus.draw_button(screen)
    butt7.draw_button(screen)
    butt8.draw_button(screen)
    butt9.draw_button(screen)
    multi.draw_button(screen)
    dot.draw_button(screen)
    butt0.draw_button(screen)
    equal.draw_button(screen)
    divid.draw_button(screen)
    clear.draw_button(screen)
    pygame.draw.rect(screen, (235, 89, 52), pygame.Rect(second_x, second_y, screen_width, screen_height))
    more_butt.draw_button(screen)
    screen.blit(more_butt_text_rendered, (25, second_y))
    if second_gui_state and second_y_change == 0:
        sin.draw_button(screen, 64, (235, 89, 52), 25, 270)
        cos.draw_button(screen, 64, (235, 89, 52), 115, 270)
        tan.draw_button(screen, 64, (235, 89, 52), 215, 270)
        degtorad.draw_button(screen, 64, (235, 89, 52), 315, 270)
        radtodeg.draw_button(screen, 64, (235, 89, 52), 310, 370)
        asin.draw_button(screen, 48, (235, 89, 52), 15, 370)
        acos.draw_button(screen, 48, (235, 89, 52), 115, 370)
        atan.draw_button(screen, 48, (235, 89, 52), 215, 370)
        cot.draw_button(screen, 64, (235, 89, 52), 15, 465)
        sec.draw_button(screen, 64, (235, 89, 52), 115, 465)
        csc.draw_button(screen, 64, (235, 89, 52), 215, 465)
        fact.draw_button(screen, 100, (235, 89, 52), 335, 460)
        sqrt_butt.draw_button(screen, 48, (235, 89, 52), 15, 570)
        cbrt_butt.draw_button(screen, 48, (235, 89, 52), 115, 570)
        pow.draw_button(screen, 100, (235, 89, 52), 230, 570)
        history_butt.draw_button(screen, 100, (235, 89, 52), 325, 560)
    if result_is_ready and not do_value_error and not do_zero_division_error and not do_factorial_error and not do_overflow_error:
        screen.blit(rendered, (0, 136))
    elif not result_is_ready and not do_value_error and not do_zero_division_error and not do_factorial_error and not do_overflow_error:
        combined = val1 + op + val2
        font1 = pygame.font.Font(None, 100)
        rendered1 = font1.render(combined, True, (0, 0, 0))
        screen.blit(rendered1, (0, 136))
    if do_value_error:
        value_error(screen)
    if do_zero_division_error:
        zero_division_error(screen)
    if do_factorial_error:
        factorial_error(screen)
    if do_overflow_error:
        overflow_error(screen)
    pygame.display.update()
    clock.tick(100)
