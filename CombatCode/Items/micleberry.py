def onResidual (pokemon):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 4 || (pokemon.hp <= pokemon.maxhp / 2 && pokemon.hasAbility('gluttony'))) {
				pokemon.eatItem();
			}
		}
	""" 
	pass

def onEat (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('micleberry');
		}
	""" 
	pass

def onSourceModifyAccuracy (accuracy, target, source):
	"""function (accuracy, target, source) {
				this.add('-enditem', source, 'Micle Berry');
				source.removeVolatile('micleberry');
				if (typeof accuracy === 'number') {
					return accuracy * 1.2;
				}
			}
	""" 
	pass