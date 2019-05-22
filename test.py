import vk_api
import datetime
import time

while True:

	vk = vk_api.VkApi(token="588a09fe546621880e553b027fa7b3f2f44ca3608728b3ab1451b3bc8015c27e789211eb08348befd9a16")
	
	delta = datetime.timedelta(hours=8, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
	t = (datetime.datetime.now(datetime.timezone.utc) + delta)

	nowtime = t.strftime("%H:%M")
	nowdate = t.strftime("%d.%m.%Y")

	on = vk.method("friends.getOnline") 
	counted = len(on)

	vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})

	time.sleep(30) 
