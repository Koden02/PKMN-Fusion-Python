def onBasePower (basePower, user, target, move):
	"""function (basePower, user, target, move) {
			if (user.baseTemplate.num === 487 && (move.type === 'Ghost' || move.type === 'Dragon')) {
				return this.chainModify([0x1333, 0x1000]);
			}
		}
	""" 
	pass

def onTakeItem (item, pokemon, source):
	"""function (item, pokemon, source) {
			if ((source && source.baseTemplate.num === 487) || pokemon.baseTemplate.num === 487) {
				return False;
			}
			return True;
		}
	""" 
	pass