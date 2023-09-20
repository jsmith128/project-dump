import json

f = open('chat_history.json', encoding='utf-8')

j = json.loads(f.read())

recv = j['Received Saved Chat History']
sent = j['Sent Saved Chat History']

export = recv #or sent
export_filename = 'messages.txt'


removed_count = 0
for msg in recv:
	for k,v in msg.items():
		if (k.lower() == 'text' and v == ''):
			recv.remove(msg)
			print(f'removed message from \t{msg["From"]}\t (no text)')
			removed_count += 1

with open(export_filename, 'w', encoding='utf-8') as out:
	for item in recv:
		from_ = item['From']
		created = item['Created']
		text = item['Text']
		out.write(f'\t{from_}\t{created}\n{text}\n\n')

#print(recv)
print(f'removed {removed_count}/{removed_count+len(recv)}, {len(recv)} left')

f.close()