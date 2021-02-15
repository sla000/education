from pathlib import Path

username = 'sla000@yandex.ru'
password = Path('password.txt').read_text().strip()
#print (vk.wall.get()['items'][0])

import vk_api

vk_session = vk_api.VkApi(username, password)
vk_session.auth()

vk = vk_session.get_api()

#print(vk.wall.post(message='SLAVA SLAVA SLAVA'))


print(vk.wall.delete(post_id = 440))
print(vk.wall.delete(post_id = 441))
