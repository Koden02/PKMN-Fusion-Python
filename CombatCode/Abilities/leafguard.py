def onSetStatus(datadic : dict):
	"""function (status, target, source, effect) {
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				if (effect && effect.status) this.add('-immune', target, '[from] ability: Leaf Guard');
				return false;
			}
		}
	""" 
	pass

def onTryAddVolatile(datadic : dict):
	"""function (status, target) {
			if (status.id === 'yawn' && this.isWeather(['sunnyday', 'desolateland'])) {
				this.add('-immune', target, '[from] ability: Leaf Guard');
				return null;
			}
		}
	""" 
	pass
