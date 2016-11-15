class entitites(object):

	def __init__(self, strength,life,colour,position):
		self.strength = strength
		self.life = life
		self.colour = colour
		self.position = position
	def print_pos(self):
		print self.position
	def change_pos(self,i,n,size):
		if((self.position[i]==0 and n<0) or (self.position[i]==size and n>0)):
			print 'Operation is out of the matrix'
		else:
			self.position[i]=self.position[i]+n
	def strength_ret(self):
		return self.strength


class players(entitites):

	def __init__(self, p_id,strength,life,colour,position):
		self.p_id = p_id
		super(players, self).__init__(strength, life, colour,position)
	def fight(self,env,enemy):
		#print env.enemy_pos.values()
		if(self.position in env.enemy_pos.values()):
			key = env.enemy_pos.keys()[env.enemy_pos.values().index(self.position)]
			#print 'Key : ',key
			if (enemy[int(key)-1].strength_ret() >self.strength_ret()):
				self.life=self.life-1
				if(self.life==0):
					print 'You are doomed, Game Over'
					exit()
				else:
					print 'Enemy attacked you, Life Remaining: '+ str(self.life)
				

class enimies(entitites):
	"""docstring for players"""
	def __init__(self, e_id,strength,life,colour,position,env):
		self.e_id = e_id
		super(enimies, self).__init__(strength, life, colour,position)
		env.add_enemy(e_id,position)

class Environment():
	enemy_pos={}

	def __init__(self, matrix_size):
		self.matrix_size = matrix_size
		
	def add_enemy(self,e_id,position):
		self.enemy_pos[str(e_id)] = position


def title_display():
	#os.system('clear')
	x=raw_input('')
	return x

def list_player():
	print '1.Christy, strength:99, Colour:White'
	print '2.Tux, strength:90, Colour:White'		
	x=input('Enter the player no to Choose :')
	return x

#size = input('Enter the size of square matrix(n) :')
size=8
env = Environment(size)
player_no = list_player()
if(player_no==1):
	player = players(1,99,3,'White',[size/2,size/2])
elif (player_no==2):
	player = players(2,90,3,'White',[size/2,size/2])

enemy = []
enemy.append(enimies(1,100,3,'Red',[2,2],env))
enemy.append(enimies(2,100,3,'Red',[3,2],env))
print 'Enemy position : ',env.enemy_pos['1']
print 'Enemy position : ', env.enemy_pos['2']
print "Welcome to Python Game, Use 'i' 'j' 'k' 'l' for controls and 'q' to quit"
x=''
print 'Current Position = ',player.print_pos() 
while (x!='q'):
	x=title_display()
	if   x=='i':
		player.change_pos(1,-1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif x=='j':
		player.change_pos(0,-1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif x=='k':
		player.change_pos(1,1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif x=='l':
		player.change_pos(0,1,size)
		player.print_pos()
player.fight(env,enemy)
