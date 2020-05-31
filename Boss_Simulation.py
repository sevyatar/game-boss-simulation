BOSS_HEALTH = 100
BOSS_DAMAGE = 10

MINION_HEALTH = 20
MINION_DAMAGE = 2

MINION_COUNT = 11

PLAYER_DAMAGE = 5

class Monster:
	def __init__(self, health, damage):
		self.__health = health
		self.__damage = damage
		
	def GetHealth(self):
		return self.__health
		
	def GetDamage(self):
		return self.__damage
		
	# Returns True iff the monster was killed
	def DealDamage(self, damageDealt):
		self.__health -= damageDealt
		return (0 >= self.__health)

class Player:
	ATTACKS_BOSS_FIRST = 1
	ATTACKS_MINIONS_FIRST = 2

	def __init__(self, strategy, damage):
		self.__accumulatedDamage = 0
		self.__strategy = strategy
		self.__damage = damage
		
	def GetAccumulatedDamage(self):
		return self.__accumulatedDamage
		
	def GetStrategy(self):
		return self.__strategy
		
	def GetDamage(self):
		return self.__damage
		
	def DealDamage(self, damage):
		self.__accumulatedDamage += damage
		
########################################################################################
class Battle:
	def __init__(self, playerStrategy):
		self.__player = Player(playerStrategy, PLAYER_DAMAGE)
		self.__boss = Monster(BOSS_HEALTH, BOSS_DAMAGE)
		self.__minions = []
		
		# Create the minions
		for i in range(0, MINION_COUNT):
			self.__minions.append(Monster(MINION_HEALTH, MINION_DAMAGE))
	
	def AttackBoss(self):
		isBossDead = self.__boss.DealDamage(self.__player.GetDamage())
		if (True == isBossDead):
			self.__boss = None
	
	def AttackMinions(self):
		isMinionDead = self.__minions[0].DealDamage(self.__player.GetDamage())
		if (True == isMinionDead):
			self.__minions.pop(0)

	# Performs the battle until all monsters are dead.
	# Returns the player's accumulated damage.
	def PerformBattle(self):
		while ((len(self.__minions) > 0) or (self.__boss != None)):
			# Monsters do damage
			for monster in self.__minions:
				self.__player.DealDamage(monster.GetDamage())
				
			if (self.__boss != None):
				self.__player.DealDamage(self.__boss.GetDamage())
				
			# Player does damage
			if (Player.ATTACKS_BOSS_FIRST == self.__player.GetStrategy):
				if (self.__boss != None):
					self.AttackBoss()
				else:
					self.AttackMinions()
			else:
				if (len(self.__minions) > 0):
					self.AttackMinions()
				else:
					self.AttackBoss()
					
		return self.__player.GetAccumulatedDamage()
		

def Main():
	print "Minions first: " + str( Battle(Player.ATTACKS_MINIONS_FIRST).PerformBattle() )
	print "Boss first:    " + str( Battle(Player.ATTACKS_BOSS_FIRST).PerformBattle() )
	
Main()
