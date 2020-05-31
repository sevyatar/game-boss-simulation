# game_boss_simulation

Ever played a video game where you're fighting a boss and his minions? ever wonder if you should first attack the boss or the minions? (boos has higher health, inflicts more damage-per-second)
This is a simulation that tests different aspects of this problem.

# Assumptions:
1 Boss, N Minions
Player deals D Damage per time-unit

Health:
	Boss - H(B)
	Minions - H(M)
	H(B) > H(M)

Damage:
	Boss - D(B)
	Minions - D(M)
	D(B) > D(M)
	
	
Goal:
Kill Boss + all Minions, while minimizing their accumulated damage to player.
