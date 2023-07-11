import aiohttp
import asyncio
import time, json,datetime
import async_timeout

#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
open('peopleRes.json', 'w').close()
#open('peopleLog.txt', 'w').close()

# API URL
#URL = 'https://localhost:11504/insis/people-data/pp-people-type/'
#todos = list(range(6000037131, 6000037332))
results = []

with open("peopleRes.json", "a") as j:
        j.write('[\n')
        j.close()

with open(r'p_people100K.json', 'rb') as f:
        todos = json.load(f)
        registros = len(todos)

async def get_tasks(session, url,todo, headers):
    async with session.post(url,json=todo,auth=aiohttp.BasicAuth('biwares.api','biwares.api'), headers=headers,ssl=False) as resp:
        results = await resp.text()
        return results

async def main():
    timeout = aiohttp.ClientTimeout(sock_connect=100,total=None, sock_read=None)
    async with aiohttp.ClientSession(timeout=timeout) as session:

        tasks = []
        headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        for todo in todos:
            url = f'https://localhost:11504/insis/people-data/pp-people-type/'
            tasks.append(asyncio.ensure_future(get_tasks(session, url, todo, headers)))
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        for results in responses:
            with open("peopleRes.json", "a") as data:
                data.write(results + ',\n')
                data.close()   
                #print(results)
        
        await session.close()

#def get_tasks(session):
#    tasks = []
#    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
#    for todo in todos:
#        tasks.append(session.post(URL, json=todo,auth=aiohttp.BasicAuth('biwares.api','biwares.api'), headers=headers,ssl=False))
#    return tasks

#async def run_tasks():
#    session = aiohttp.ClientSession()
#    tasks = get_tasks(session)
#    responses = await asyncio.gather(*tasks)
#    for response in responses:
#        results.append(await response.text())
#        with open("peopleRes.json", "a") as data:
#            data.write(await response.text() + ',\n')
#            data.close()        
#    await session.close()

    
print("Timer started...")

with open(r'peopleLog.txt', 'a') as c:
    c.write('------------------------------------ \n')
    start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    c.write('Total de Registros POST ' + str(registros) + '\n')
    comienzo  = "Hora Comienzo " + start_time
    c.write(comienzo + '\n')

#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

with open("peopleRes.json", "a") as j:
        j.write('\n ]')
        j.close()

with open(r'peopleLog.txt', 'a') as c:
    end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    fin  = "Hora de Finalizacion " + end_time
    c.write(fin + '\n')
    total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
    c.write('Diferencia ' + str(total_time))
    c.write('\n')
    c.write('------------------------------------ \n')
    c.close()
    
#start = time.time()
#end = time.time()
#print(f"Time to make {len(todos)} API calls with tasks, it took: {total_time}")
