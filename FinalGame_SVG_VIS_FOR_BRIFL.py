import svgwrite
import FinalGame

DEBUG = False

FONT = 'font-family:Arial'

W = 1000 # Width of Vis. region
H = 500 # Height of Vis. region
MIDDLE = (500,250)
INDEX_KEYS = ['CC','GDP','EF','HI']
BACKGROUND_COLOR = 'rgb(250,250,250)'
METRIC_COLORS = ['rgb(108, 189, 129)', 'rgb(97, 137, 171)', 'rgb(168, 91, 100)', 'rgb(184, 191, 103)']
METRIC_COLORS_SUB = ['rgb(172, 227, 187)', 'rgb(182, 205, 224)', 'rgb(217, 163, 163)', 'rgb(209, 161, 206)']
BUDGET_COLOR = 'rgb(184, 191, 103)'
BUDGET_COLOR_SUB = 'rgb(211, 214, 171)'

METRIC_WIDTH = '30px'
MAX_METRIC_LENGTH_INT = 150
MAX_METRIC_LENGTH = '150px'

    
session = None
def render_state(s, roles=None):
    global session

    session = FinalGame.get_session() # Need HOST and PORT info for accessing images.
    dwg = svgwrite.Drawing(filename = "state.svg",
                           id = "state_svg",  # Must match the id in the html template.
                           size = (str(W)+"px", str(H)+"px"),
                           debug=True)
    
    dwg.add(dwg.rect(insert = (0,0),
        size = (W,H),
        stroke_width = "1",
        stroke = "black",
        fill = BACKGROUND_COLOR))
    #AVATER PICK PHASE!!!
    if False:
        dwg.add(dwg.text('Please choose your avatar!!', insert = MIDDLE,
                text_anchor="start",
                font_size="60",
                stroke = "black",
                fill = "black",
                style = FONT))

    #GAME PHASE!!!
    if True:
        increment = 200
        temp_x = 150
        for key in INDEX_KEYS:
            dwg.add(dwg.text(key, insert = (temp_x, 100),
                        text_anchor="start",
                        font_size="40",
                        stroke = "black",
                        fill = "black",
                        style = FONT))
            temp_x += increment
            
        dwg.add(dwg.text('YOUR AVATAR:', insert = (25, 230),
                        text_anchor="start",
                        font_size="15",
                        stroke = "black",
                        fill = "black",
                        style = FONT))
        dwg.add(dwg.text('Place holder', insert = (25, 250), #Inster avatar here
                        text_anchor="start",
                        font_size="15",
                        stroke = "black",
                        fill = "black",
                        style = FONT))
        dwg.add(dwg.text('Budget', insert = (25, 350),
                        text_anchor="start",
                        font_size="30",
                        stroke = "black",
                        fill = "black",
                        style = FONT))
            #INDEX BACKGROUND
        temp_x = 150
        increment = 200
        for color in METRIC_COLORS_SUB:
            dwg.add(dwg.rect(insert = (temp_x,120),
            size = (MAX_METRIC_LENGTH,METRIC_WIDTH),
            stroke_width = "1",
            stroke = "black",
            fill = color))
            temp_x += increment
        dwg.add(dwg.rect(insert = (25, 370),
            size = (MAX_METRIC_LENGTH,METRIC_WIDTH),
            stroke_width = "1",
            stroke = "black",
            fill = BUDGET_COLOR_SUB))
            #THE INDEXES
            
        dwg.add(dwg.rect(insert = (150,120),
            size = (metric_length(s.indexes['CC']),METRIC_WIDTH),
            fill = METRIC_COLORS[0]))
        dwg.add(dwg.rect(insert = (350,120),
            size = (metric_length(s.indexes['GDP']),METRIC_WIDTH),
            fill = METRIC_COLORS[1]))
        dwg.add(dwg.rect(insert = (550,120),
            size = (metric_length(s.indexes['EF']),METRIC_WIDTH),
            fill = METRIC_COLORS[2]))
        dwg.add(dwg.rect(insert = (750,120),
            size = (metric_length(0),METRIC_WIDTH), # ADD HAPPINESS INDEX
            fill = METRIC_COLORS[3]))
        dwg.add(dwg.rect(insert = (25, 370),
            size = (metric_length(0),METRIC_WIDTH), # GET EACH PLAYER'S VALUE
            fill = BUDGET_COLOR))
        
        insert_card(dwg, ('t',1), 200,200)
        insert_card(dwg, ('t',1), 350,200)
        insert_card(dwg, ('t',1), 500,200)
        insert_card(dwg, ('t',1), 650,200)
        insert_card(dwg, ('t',1), 800,200)
    
    #GOAL PHASE!!!
    if False:
        dwg.add(dwg.text('The winner is:', insert = MIDDLE,
                text_anchor="start",
                font_size="60",
                stroke = "black",
                fill = "black",
                style = FONT))

    
    
    svg_string = dwg.tostring()
    return svg_string

def metric_length(n):
    return int(n * (MAX_METRIC_LENGTH_INT / 100))

def insert_card(dwg, card, x, y):
    dwg.add(dwg.rect(insert=(x, y), size=(140, 200), fill='rgb(0,0,0)'))
    filename = CARD_IMAGES[card]
    url = "http://"+session['HOST']+":"+str(session['PORT'])+"/get_image/"+filename
    image = dwg.image(url, insert=(x, y), size=(140, 200))
    dwg.add(image)

CARD_IMAGES = \
 {('t',1): "t_1.png"}
    
if __name__ == '__main__':
    DEBUG = True
    PLAYER_HAND = [[('p',0),('r',3),('r',6),('p',4)]]
    session = {'HOST': 'localhost', 'PORT':5000}
    INITIAL_STATE = State()
    print(INITIAL_STATE)
    svg_string = render_state(INITIAL_STATE, roles=[0])
    print("svg_string is: ")
    print(svg_string)
