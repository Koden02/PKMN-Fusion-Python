def onTryHit(datadic : dict):
	"""function (target, source) {
			if (source.volatiles['lockon']) return false;
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target, source) {
			source.addVolatile('lockon', target);
			this.add('-activate', source, 'move: Lock-On', '[of] ' + target);
		}
	""" 
	pass

def onSourceAccuracy(datadic : dict):
	"""function (accuracy, target, source, move) {
				if (move && source === this.effectData.target && target === this.effectData.source) return true;
			}
	""" 
	pass
