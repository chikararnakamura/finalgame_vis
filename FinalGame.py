'''P3B-Game.py
'''
# <METADATA>
SOLUZION_VERSION = "4.0"
PROBLEM_NAME = "Crisis in C-attle"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['C. Nakamura, N. Belur, P. Bowers, R. Li']
PROBLEM_CREATION_DATE = "5-Sept-2024"
PROBLEM_DESC = \
    '''Player acts as a character in the city of C-attle to reach their own goals.
'''

# </METADATA>

# <COMMON_DATA>
#Player Creation
#Create Instances of the Player Class that the Players will be able to choose from
class Card():
    ''' Name: string for the name of the card
Stats: dictionary that represents the change of the indicators in the game.
It is in the order [CC: int, GDP: int, EF: int]
Cost: cost for the certain action, will also be a dictionary'''
    def __init__(self, name, stats, cost, pros, cons):
         self.name = name
         self.stats = stats
         self.cost = cost
         self.pros=pros
         self.cons=cons

    def __eq__(self, s2):
        if self.name != s2.name: return False
        for p in self.stats.keys():
            if self.stats[p] != s2.stats[p]: return False
        for p in self.cost.keys():
            if self.cost[p] != s2.cost[p]: return False
        if self.pros != s2.pros or self.cons != s2.cons: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        txt = self.name.capitalize() + "\n ------------------ \nChanges \n"
        for num in self.stats.keys():
            txt += num + ": " + str(self.stats[num]) + "\n"
        for num in self.cost.keys():
            txt += num + ": " + str(self.cost[num]) + "\n"
        txt += "Pro: " + self.pros + "\n" + "Con: " + self.cons + "\n"
        return txt + "\n"
    
    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        new = Card('', {}, {}, '', '')
        new.name = self.name
        for p in ['CC', 'GDP', 'EF']:
            new.stats[p] = self.stats[p] 
        for p in ['MONEY']:
            new.cost[p] = self.cost[p]
        new.pros = self.pros
        new.cons = self.cons
        return new
    
    def dict_access(self, string):
        return self.cost[string]
class Avatar():
    def __init__(self, name, cards, resources, *skills):
        '''name: name of the character (string)
p_id: Player id or Player number (int)
cards: an array of all the cards this player has
resources: dictionary displaying the remaining resources of the player (currently only $ exists)'''
        self.name = name
        self.cards = cards
        self.resources = resources
        self.skills = skills

    def __eq__(self, s2):
        if self.name != s2.name: return False
        for p in range(len(self.cards)):
            if self.cards[p] != s2.cards[p]: return False
        for p in self.resources.keys():
            if self.cost[p] != s2.cost[p]: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.

        # Not Done
        txt = self.name.capitalize() + "\n ------------------ \n Changes \n"
        for num in self.stats.keys():
            txt += num + ": " + self.stats[num] + "\n"
        for num in self.cost.keys():
            txt += num + ": " + self.cost[num] + "\n"
        return txt
    
    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        new = Avatar('', 0, [], {})
        new.name = self.name
        for p in range(len(self.cards)):
            new.cards[p] = self.cards[p] 
        for p in ['MONEY']:
            new.cost[p] = self.cost[p] 
        return new
GOOD_PLAYER_CARDS = [Card('Test_1',{'CC': 10, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_2',{'CC': 2, 'GDP': 0, 'EF': 0}, {'MONEY': 20}, 'a', 'b'),
Card('Test_3',{'CC': -10, 'GDP': 5, 'EF': 10}, {'MONEY': 5}, 'a', 'b'),
Card('Test_4',{'CC': 30, 'GDP': 20, 'EF': -20}, {'MONEY': 30}, 'a', 'b'),
Card('Test_5',{'CC': 0, 'GDP': -10, 'EF': 10}, {'MONEY': 0}, 'a', 'b'),
Card('Test_6',{'CC': 0, 'GDP': 0, 'EF': -5}, {'MONEY': 10}, 'a', 'b'),
Card('Test_7',{'CC': 0, 'GDP': -5, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_8',{'CC': -5, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_9',{'CC': 10, 'GDP': 10, 'EF': 10}, {'MONEY': 20}, 'a', 'b'),
Card('Test_10',{'CC': -10, 'GDP': -10, 'EF': -10}, {'MONEY': 20}, 'a', 'b'),
Card('Test_11',{'CC': 0, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_12',{'CC': 20, 'GDP': 0, 'EF': 0}, {'MONEY': 20}, 'a', 'b'),
Card('Test_13',{'CC': 10, 'GDP': 20, 'EF': -10}, {'MONEY': 30}, 'a', 'b'),
Card('Test_14',{'CC': 5, 'GDP': 0, 'EF': -50}, {'MONEY': 70}, 'a', 'b'),
Card('Test_15',{'CC': 0, 'GDP': -50, 'EF': 0}, {'MONEY': 70}, 'a', 'b'),
Card('Test_16',{'CC': -10, 'GDP': -20, 'EF': -20}, {'MONEY': 40}, 'a', 'b'),
Card('Test_17',{'CC': -10, 'GDP': 20, 'EF': 20}, {'MONEY': 40}, 'a', 'b'),
Card('Test_18',{'CC': 0, 'GDP': -15, 'EF': -10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_19',{'CC': 0, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_20',{'CC': -5, 'GDP': 10, 'EF': 20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_21',{'CC': 0, 'GDP': 30, 'EF': 0}, {'MONEY': 30}, 'a', 'b'),
Card('Test_22',{'CC': 20, 'GDP': 0, 'EF': -10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_23',{'CC': 10, 'GDP': -20, 'EF': 0}, {'MONEY': 20}, 'a', 'b'),
Card('Test_24',{'CC': 0, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_25',{'CC': -10, 'GDP': 10, 'EF': 10}, {'MONEY': 10}, 'a', 'b')]

GOOD_PLAYER_RESOURCES = {'MONEY': 100}

BAD_PLAYER_CARDS = [Card('Test_1',{'CC': 0, 'GDP': 10, 'EF': 10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_2',{'CC': 0, 'GDP': 10, 'EF': 0}, {'MONEY': 20}, 'a', 'b'),
Card('Test_3',{'CC': 0, 'GDP': 20, 'EF': 20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_4',{'CC': -10, 'GDP': 0, 'EF': 0}, {'MONEY': 30}, 'a', 'b'),
Card('Test_5',{'CC': 20, 'GDP': -30, 'EF': -20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_6',{'CC': 0, 'GDP': 0, 'EF': 30}, {'MONEY': 20}, 'a', 'b'),
Card('Test_7',{'CC': 0, 'GDP': 40, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_8',{'CC': -10, 'GDP': 20, 'EF': 30}, {'MONEY': 10}, 'a', 'b'),
Card('Test_9',{'CC': 0, 'GDP': 0, 'EF': 50}, {'MONEY': 30}, 'a', 'b'),
Card('Test_10',{'CC': 0, 'GDP': 10, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_11',{'CC': 10, 'GDP': 0, 'EF': 10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_12',{'CC': -20, 'GDP': 20, 'EF': 20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_13',{'CC': 0, 'GDP': 0, 'EF': 30}, {'MONEY': 20}, 'a', 'b'),
Card('Test_14',{'CC': 30, 'GDP': 30, 'EF': 30}, {'MONEY': 10}, 'a', 'b'),
Card('Test_15',{'CC': 0, 'GDP': 0, 'EF': 0}, {'MONEY': 30}, 'a', 'b'),
Card('Test_16',{'CC': 40, 'GDP': 10, 'EF': 30}, {'MONEY': 10}, 'a', 'b'),
Card('Test_17',{'CC': -20, 'GDP': 10, 'EF': 40}, {'MONEY': 10}, 'a', 'b'),
Card('Test_18',{'CC': 0, 'GDP': 0, 'EF': 0}, {'MONEY': 10}, 'a', 'b'),
Card('Test_19',{'CC': 20, 'GDP': 20, 'EF': 10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_20',{'CC': 10, 'GDP': 0, 'EF': 10}, {'MONEY': 20}, 'a', 'b'),
Card('Test_21',{'CC': 0, 'GDP': 20, 'EF': 20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_22',{'CC': -10, 'GDP': 0, 'EF': 30}, {'MONEY': 30}, 'a', 'b'),
Card('Test_23',{'CC': 0, 'GDP': 30, 'EF': 40}, {'MONEY': 10}, 'a', 'b'),
Card('Test_24',{'CC': 0, 'GDP': 30, 'EF': 10}, {'MONEY': 50}, 'a', 'b'),
Card('Test_25',{'CC': 20, 'GDP': 10, 'EF': 0}, {'MONEY': 10}, 'a', 'b')]
BAD_PLAYER_RESOURCES = {'MONEY': 100}

GOOD_PLAYER = Avatar("Player 1.0", GOOD_PLAYER_CARDS, GOOD_PLAYER_RESOURCES)
GOOD_PLAYER2 = Avatar("Player 3.0", GOOD_PLAYER_CARDS, GOOD_PLAYER_RESOURCES)
BAD_PLAYER = Avatar("Player 2.0", BAD_PLAYER_CARDS, BAD_PLAYER_RESOURCES)

ADD_PLAYER = True
USED = False

AVATARS = [GOOD_PLAYER, BAD_PLAYER, GOOD_PLAYER2]
UNPICKED_AVATARS = [GOOD_PLAYER, BAD_PLAYER, GOOD_PLAYER2]
MOVEMENT = [Card('Test_1',{'CC': 0, 'GDP': 10, 'EF': 10}, {'MONEY': 10}, 'a', 'b'),
Card('Test_2',{'CC': 0, 'GDP': 10, 'EF': 0}, {'MONEY': 20}, 'a', 'b'),
Card('Test_3',{'CC': 0, 'GDP': 20, 'EF': 20}, {'MONEY': 10}, 'a', 'b'),
Card('Test_4',{'CC': -10, 'GDP': 0, 'EF': 0}, {'MONEY': 30}, 'a', 'b'),
Card('Test_5',{'CC': 20, 'GDP': -30, 'EF': -20}, {'MONEY': 10}, 'a', 'b')]
PLAYERS = 2
CUR_PLAYER = 0

# </COMMON_DATA>

# <COMMON_CODE>
import random
class State:
    # Which Player is currently active (Player 1 is bad, Player 2 is good)
    cur_player = 0
    winner = -1
    def __init__(self, indexes = None, players = None):
        if indexes == None:
            #100 is max and 0 is min
            indexes = {'CC': 50, 'GDP': 50, 'EF': 50}
        if players == None:
            players = []    
        self.indexes = indexes
        self.players = players
        if len(players) != 0:
            global MOVEMENT
            MOVEMENT = self.drawCards()
            for i in range(len(MOVEMENT)):
                OPERATORS[i].change_arguments(MOVEMENT[i])
    def __eq__(self, s2):
        for p in ['CC', 'GDP', 'EF']:
            if self.indexes[p] != s2.indexes[p]: return False
        for p in range(len(self.players)):
            if self.players[p] != s2.players[p]: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
       
        txt = "It is Player " + str(self.cur_player + 1) + "'s turn\n"
        txt += "Current state of the city \n"
        for value in self.indexes.keys():
            txt += value + ": " + str(self.indexes[value]) + "\n"
        txt += str(self.players[self.cur_player])
        global MOVEMENT
        for i in MOVEMENT:
            txt += str(i)
        
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def __copy__(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        new = State()
        for side in new.indexes.keys():
            new.indexes[side] = self.indexes[side]
        global CUR_PLAYER
        for side in range(CUR_PLAYER):
            temp = self.players[side].copy()
            new.players.append(temp)
        new.cur_player = self.cur_player
        return new
    def drawCards(self):
        if len(self.players) != 0:
            copy = []
            rand_cards = []
            for i in self.players[self.cur_player].avatar.cards:
                copy.append(i)
            for i in range(5):
                rand_num = int(random.random()*len(copy))
                rand_cards.append(copy[rand_num])
                copy.remove(copy[rand_num])

            return rand_cards
        return []
    def can_move(self, role, card):
        global MOVEMENT
        if len(self.players) == 0 or len(MOVEMENT) == 0:
            return False
        global START_GAME
        return START_GAME and self.players[self.cur_player].can_move(card)

    def move(self, role, card): 
        '''Assuming it's legal to make the move, this computes
       the new state resulting from moving a certain animal.'''
        news = self.copy()  # start with a deep copy.
        for i in news.players[news.cur_player].resources.keys():
            news.players[news.cur_player].resources[i] -= card.cost[i]
        for j in news.indexes.keys():
            news.indexes[j] += card.stats[j]
        if self.cur_player == len(self.players)-1:
            news.cur_player = 0
        else: news.cur_player += 1
        news.players[news.cur_player].resources['MONEY'] += 20
        global MOVEMENT
        MOVEMENT = self.drawCards()
        for i in range(5):
            OPERATORS[i].change_arguments(MOVEMENT[i])
        return news  # return new state


    def is_goal(self):
        
        '''If the all things have passed the river.'''
        if self.indexes['CC'] > 80 or self.indexes['CC'] < 20 or self.indexes['EF'] > 80 or self.indexes['GDP'] < 20:
            return True
        elif self.indexes['GDP'] > 80 and self.indexes['EF'] < 20:
            self.winner = len(self.players)
            return True
        elif self.indexes['GDP'] > 80:
            self.winner = 0
        elif self.indexes['EF'] < 20:
            self.winner = 1
        return  False


    def goal_message(self):
        txt = "GAME OVER!!!!! \n"
        try:
            txt += "The Winner was " + self.players[self.winner].player_name
        except:
            if self.winner > 0:
                txt += "All Players Have won"
            else:
                txt += "no one"
        return txt
    '''def pick_avatar(self, role, player_name, avatar):
        news = self.copy()
        global CUR_PLAYER   
        global UNPICKED_AVATARS
        player = Player(player_name, avatar, CUR_PLAYER)
        news.players.append(player)
        UNPICKED_AVATARS.remove(avatar)
        CUR_PLAYER = len(news.players)
        return news

    def start(self, role):
        global START_GAME
        START_GAME = True
        global MOVEMENT
        MOVEMENT = self.drawCards()
        for i in range(5):
            OPERATORS[i+5].change_arguments(MOVEMENT[i])
        return self
    def add_player(self, role):
        global PLAYERS
        PLAYERS += 1
        return self'''
HOST = 'tempura.cs.washinngton.edu'
PORT = 5000
SESSION = None
def init_session():
    global SESSION
    SESSION = {\
           'USERNAMES': {},
           'NUMBER_OF_USERS': 0,
           'USER_NUMBERS': {},
           'SESSION_OWNER': None,
           'ROLES_MEMBERSHIP': None,
           'USERNAME': 'nobody now',
           'HOST': HOST,
           'PORT': PORT}
    SESSION['USE_ROLE_SPECIFIC_VISUALIZATIONS']=True
INACTIVE_PLAYERS = [] # Inactive after being sent to jail for doing illegal stuff
class Player():
    def __init__(self, player_name, avatar, order, resources = None):
        self.player_name = player_name
        self.avatar = avatar
        self.order = order
        if resources == None:
            resources = avatar.resources
        self.resources = resources

    def copy(self):
        new_resources = {}
        for r in ['MONEY']:
            new_resources[r] = self.resources[r]
        new = Player(self.player_name, self.avatar, self.order, new_resources)
        return new

    def __hash__(self):
        return (self.__str__()).__hash__()
    def __eq__(self, s2):
        if self.player_name != s2.player_name: return False
        if self.avatar != s2.avatar: return False
        if self.order != s2.order: return False
        for p in self.resources.keys():
            if self.cost[p] != s2.cost[p]: return False
        return True

    def __str__(self):
        txt = "Player " + str(self.order+1) + ": " + self.player_name + "\nAvatar: " + self.avatar.name + "\nResources Remaining \n"
        for i in self.resources.keys():
            txt += i + ": " + str(self.resources[i])
        return txt + "\n\n"
    def can_move(self, card):
        for i in self.resources.keys():
            if self.resources[i] < card.dict_access(i): return False
        return True
        
'''def can_pick_avatar(s, role, avatar):
    global CUR_PLAYER
    global PLAYERS
    global UNPICKED_AVATARS
    return CUR_PLAYER < PLAYERS and avatar in UNPICKED_AVATARS

def can_start(s, role):
    global START_GAME
    return CUR_PLAYER == PLAYERS and not START_GAME
def can_add_player(s, role):
    return not START_GAME and PLAYERS < 4'''
def get_session():
  return SESSION

# </COMMON_CODE>

# <OPERATORS>
class Operator:
    def __init__(self,
                 name,
                 precond=(lambda s: True),
                 transf=(lambda s: State(s)),
                 params=[]):
        self.name = name
        self.precond = precond
        self.transf = transf
        self.params = params
 
    def is_applicable(self, s, role_number=0):
        return self.precond(s, role_number)

    def apply(self, s, role):
        #if self.params:
            #args = GET_ARGS(self)
            #return self.transf(s, role, args)
        #else:
        return self.transf(s, role)
        
    def change_arguments(self, card):
        self.name = "Use the " + card.name + " card"
        self.precond = (lambda s, thing = card: s.can_move(thing))
        self.transf = (lambda s, thing = card: s.move(thing))

'''def GET_ARGS(op):
    return client.get_args(op)
import Int_Solv_Client5 as client'''

'''pick_avatar = [Operator("Pick the " + i.name + " avatar and add your player username", lambda s, avatar = i: can_pick_avatar(s, CUR_PLAYER, avatar),
                        lambda s, args, avatar = i:
                        s.pick_avatar(args[0], CUR_PLAYER, avatar), [{'name':'string', 'type':'str' }])
               for i in UNPICKED_AVATARS]
add_player = [Operator("Add a new player", lambda s: can_add_player(), lambda s: s.add_player())]
start_game = [Operator("Start the Game", lambda s: can_start(), lambda s: s.start())]'''
moving = [Operator("Use the " + i.name + " card",
                      lambda s, role = 0, thing = i: s.can_move(CUR_PLAYER, thing),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s, role = 0, thing = i: s.move(CUR_PLAYER, thing))
             for i in MOVEMENT]
#OPERATORS = pick_avatar + add_player + start_game + moving
OPERATORS = moving
# </OPERATORS>
# </Initial State>
INITIAL_STATE = None
def create_initial_state():
    global INITIAL_STATE
    INITIAL_STATE = State()
    print(INITIAL_STATE)
# </Initial State>
# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

#<ROLES>
ROLES = [ {'name': 'CEO', 'min': 1, 'max': 1},
          {'name': 'Environmentalist', 'min': 1, 'max': 1},
          {'name': 'Professor', 'min': 1, 'max': 1},
          {'name': 'Mayor', 'min': 1, 'max': 1},
          {'name': 'Observer', 'min': 0, 'max': 25}]
#</ROLES>

#<STATE_VIS>
BRIFL_SVG = True # The program FoxAndGeese_SVG_VIS_FOR_BRIFL.py is available
render_state = None
def use_BRIFL_SVG():
  global render_state
  from  FinalGame_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>



'''Testing Code: python3 Int_Solv_Client5.py P3B-Game '''
