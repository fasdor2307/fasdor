import vk_api
import datetime
import time

while True:

	vk = vk_api.VkApi(token="cf1b50f4bd5e6454d7c34c1ca8268fdd3a95ed156f443f08dc0dface12769f40c7167f9398173b05d4481")
	
	delta = datetime.timedelta(hours=8, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
	t = (datetime.datetime.now(datetime.timezone.utc) + delta)

	nowtime = t.strftime("%H:%M")
	nowdate = t.strftime("%d.%m.%Y")

	on = vk.method("friends.getOnline") 
	counted = len(on)

	vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})

	time.sleep(30) 