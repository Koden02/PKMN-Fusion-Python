def onImmunity(datadic : dict):
	"""function (type, pokemon) {
			if (type === 'sandstorm' || type === 'hail' || type === 'powder') return false;
		}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (move.flags['powder'] && target !== source && this.getImmunity('powder', target)) {
				this.add('-immune', target, '[from] ability: Overcoat');
				return null;
			}
		}
	""" 
	pass
