from .. import loader
from asyncio import sleep
@loader.tds
class SasaSmileMod(loader.Module):
	strings = {"name": "Sasa"}
	@loader.owner
	async def sasacmd(self, message):
		for _ in range(1):
			for sasa in ["С", "А", "Ш", "А", "ᅠ", "З", "А", "Б", "Ы", "Л", "ᅠ", "Л", "О", "Х", "ᅠ", "САША ЗАБЫЛ ТОП"]:
				await message.edit(sasa)
				await sleep(0.4)