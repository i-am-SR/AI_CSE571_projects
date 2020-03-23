# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
        total_score = successorGameState.getScore()
 
    	#calculate the total manhattan distance of the ghosts from the current position
    	total_manh_dist_to_ghosts = 1 # to avoid division by zero
    	for ghostPos in successorGameState.getGhostPositions():
        	total_manh_dist_to_ghosts += manhattanDistance(newPos, ghostPos)

        #calculate the manhattan distance to the nearest food pallet
    	newFoodList = newFood.asList()
    	min_manh_dist_to_food = float('inf')
    	for foodPos in newFoodList:
        	dist = manhattanDistance(newPos, foodPos)
        	min_manh_dist_to_food = min(min_manh_dist_to_food, dist)

       	"""
        maxDist = 10
        for ghostPos in successorGameState.getGhostPositions():
            dist = manhattanDistance(newPos, ghostPos)
            total_score += max(dist, maxDist)
        newFood = newFood.asList()
        minDist = 10
        for foodPos in newFood:
            dist = manhattanDistance(newPos, foodPos)
            minDist = min(minDist, dist)
        total_score -= minDist
        """

        """These features affect the score:  
      	1) distance to the nearest food pallet => less is better so its inverse is added to the score
      	2) total manhattan distance to the ghosts => more is better so its inverse is subtracted from the score
      	"""
        total_score += (1/float(min_manh_dist_to_food)) - 5*(1/float(total_manh_dist_to_ghosts)) 

        return total_score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
          Here are some method calls that might be useful when implementing minimax.
          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1
          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action
          gameState.getNumAgents():
            Returns the total number of agents in the game
          gameState.isWin():
            Returns whether or not the game state is a winning state
          gameState.isLose():
            Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        

        def maxNode(gameState, ghost_index, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState) #Retrun the gameState if you specified depth is reached or the game ends

            legalMoves = gameState.getLegalActions()
            scores = [minNode(gameState.generateSuccessor(0, action), ghost_index, depth) for action in legalMoves]
            return max(scores) # Max node returns the maximum possible score

        def minNode(gameState, ghost_index, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            legalMoves = gameState.getLegalActions(ghost_index)
            if ghost_index == total_ghosts:
                scores = [maxNode(gameState.generateSuccessor(ghost_index, action), 1, depth - 1) for action in legalMoves]
            else:
                scores = [minNode(gameState.generateSuccessor(ghost_index, action), ghost_index + 1, depth) for action in legalMoves]

            return min(scores)	# Min node returns the minimum possible score

        total_ghosts = gameState.getNumAgents() - 1
        legalMoves = gameState.getLegalActions()
        ghost_index = 1
        scores = [minNode(gameState.generateSuccessor(0, action), ghost_index, self.depth) for action in legalMoves]
        best_action_index = scores.index(max(scores))
        return legalMoves[best_action_index] # return the best legal move

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def maxNode(gameState, ghost_index, depth, beta, alpha):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            legalMoves = gameState.getLegalActions()
            v = -float('inf')
            for action in legalMoves:
                successorState = gameState.generateSuccessor(self.index, action)
                v = max(v, minNode(successorState, ghost_index, depth, beta, alpha))
                if v > beta:
                    return v
                
                alpha = max(v, alpha)
            
            return v

        def minNode(gameState, ghost_index, depth, beta, alpha):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            current_index = total_ghosts - ghost_index + 1
            legalMoves = gameState.getLegalActions(current_index)
            v = float('inf')
            if current_index == total_ghosts:
                for action in legalMoves:
                    v = min(v, maxNode(gameState.generateSuccessor(current_index, action), total_ghosts, depth - 1, beta, alpha))
                    if v < alpha:
                        return v
                    
                    beta = min(v, beta)
            else:
            	for action in legalMoves:
                    v = min(v, minNode(gameState.generateSuccessor(current_index, action), ghost_index - 1, depth, beta, alpha))
                    if v < alpha:
                        return v
                    
                    beta = min(v, beta)                
            
            return v

        beta = float('inf')
        alpha = -float('inf')
        v = -float('inf')
        legalMoves = gameState.getLegalActions()
        scores = []

        for action in legalMoves:
            total_ghosts = gameState.getNumAgents() - 1
            successorState = gameState.generateSuccessor(self.index, action)
            v = max(v, minNode(successorState, total_ghosts, self.depth, beta, alpha))
            if v > beta:
                return v
            
            alpha = max(v, alpha)
            scores.append(v)

        best_action_index = scores.index(max(scores))
        return legalMoves[best_action_index]
    
        #util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        def maxNode(gameState, ghost_index, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            legalMoves = gameState.getLegalActions()
            scores = [minNode(gameState.generateSuccessor(0, action), ghost_index, depth) for action in legalMoves]
            return max(scores)

        def minNode(gameState, ghost_index, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            legalMoves = gameState.getLegalActions(ghost_index)
            normalizer = len(legalMoves)
            result = float(0)
            if ghost_index == total_ghosts:
                for action in legalMoves:
                    result += maxNode(gameState.generateSuccessor(ghost_index, action), 1, depth - 1)
            else:
                for action in legalMoves:
                    result += minNode(gameState.generateSuccessor(ghost_index, action), ghost_index + 1, depth)

            return result/normalizer

        total_ghosts = gameState.getNumAgents() - 1
        legalMoves = gameState.getLegalActions()
        ghost_index = 1
        scores = [minNode(gameState.generateSuccessor(0, action), ghost_index, self.depth) for action in legalMoves]
        best_action_index = scores.index(max(scores))
        return legalMoves[best_action_index]
        #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: I have chosen 3 important features that affect the score at the current state:  
      1) distance to the nearest food pallet => less is better so its inverse is added to the score
      2) total manhattan distance to the ghosts => more is better so its inverse is subtracted from the score
      3) number of power pallets remaining => it helps to use power pallets so it is subtracted from the score

    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()

    total_score = currentGameState.getScore()
 
    #calculate the total manhattan distance of the ghosts from the current position
    total_manh_dist_to_ghosts = 1 # to avoid division by zero
    for ghostPos in currentGameState.getGhostPositions():
        total_manh_dist_to_ghosts += manhattanDistance(newPos, ghostPos)

    #calculate the manhattan distance to the nearest food pallet
    newFoodList = newFood.asList()
    min_manh_dist_to_food = float('inf')
    for foodPos in newFoodList:
        dist = manhattanDistance(newPos, foodPos)
        min_manh_dist_to_food = min(min_manh_dist_to_food, dist)

    #calculate the number of power pallets remaining
    power = len(currentGameState.getCapsules())

    """
    #calculate the distance to the nearest power pallet
    min_manh_dist_to_capsule = float('inf')
    capsuleList = currentGameState.getCapsules()
    for capsulePos in capsuleList:
        dist = manhattanDistance(newPos, capsulePos)
        min_manh_dist_to_capsule = min(min_manh_dist_to_capsule, dist)
    """

    total_score += (1/float(min_manh_dist_to_food)) - (1/float(total_manh_dist_to_ghosts)) - 20 * power
    #total_score += (1/float(min_manh_dist_to_food)) + (1/float(min_manh_dist_to_capsule)) - .1*(1/float(total_manh_dist_to_ghosts))
    return total_score

    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

