from .. import loader

class mfMod(loader.Module):
	strings = {"name": "Minfo"}
	
	async def watcher(self, message):
		me = (await message.client.get_me())
		if message.sender_id == me.id:
			if message.text.lower() == "minfo":
			    await message.edit("👀ВСЕ ДОСТУПНЫЕ МОДУЛИ СНИЗУ⬇️\n\n📟Модули от @CREATIVE_tg1 есть <a href=\"https://t.me/moduleFTG\">тут</a>\n\n📟Сторонние источники модулей⬇️\n(GitHub)\n50+ модулей: <a href=\"https://github.com/HitaloSama/FTG-modules-repo\">ссылка</a>\n20+ модулей: <a href=\"https://github.com/AivenGog/ftg-modules\">ссылка</a>\n\nБолее подробная инструкция по установке модулей <a href=\"https://github.com/byWizard/FTG/blob/main/README.md\">тут</a>")