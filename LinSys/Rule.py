
ProductionRules = []
DrawingRules = []

def AddProduction(rule):
	ProductionRules.append(rule)
	ProductionRules.sort(key=lambda item: (-len(item[0]), item[0]))

def AddDrawing(rule):
	DrawingRules.append(rule)
	DrawingRules.sort(key=lambda item: (-len(item[0]), item[0]))

def getProductions():
	return ProductionRules

def getDrawings():
	return DrawingRules

def removeProd(idx):
	del ProductionRules[idx]

def removeDraw(idx):
	del DrawingRules[idx]

def wipe():
	global ProductionRules
	global DrawingRules
	ProductionRules = []
	DrawingRules = []
