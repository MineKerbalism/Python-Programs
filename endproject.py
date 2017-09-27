from mine import *

mc = Minecraft()

mc.postToChat("Your car is arriving...")

playerPos = mc.player.getPos()


def setBottomTop():
	mc.setBlocks(playerPos.x, playerPos.y, playerPos.z + 10, playerPos.x + 10, playerPos.y, playerPos.z + 14, block.WOOL_BLUE)
	mc.setBlocks(playerPos.x + 3, playerPos.y, playerPos.z + 10, playerPos.x + 8, playerPos.y + 3, playerPos.z + 14, block.WOOL_BLUE)

def makeWheels():
	mc.setBlock(playerPos.x + 1, playerPos.y - 1, playerPos.z + 10, block.WOOL_BLACK)
	mc.setBlock(playerPos.x + 1, playerPos.y - 1, playerPos.z + 14, block.WOOL_BLACK)
	mc.setBlock(playerPos.x + 9, playerPos.y - 1, playerPos.z + 10, block.WOOL_BLACK)
	mc.setBlock(playerPos.x + 9, playerPos.y - 1, playerPos.z + 14, block.WOOL_BLACK)

setBottomTop()
makeWheels()
