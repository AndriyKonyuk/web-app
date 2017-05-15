import aiohttp, asyncio, re
from lxml import html

async def get_url(event_loop):
    async with aiohttp.ClientSession(loop=event_loop) as session:
        async with session.get('https://coinmarketcap.com/all/views/all/') as response:
            if response.status == 200:
                return await response.text()

l = asyncio.new_event_loop()
set_loop = asyncio.set_event_loop(l)
loop = asyncio.get_event_loop()
run = loop.run_until_complete(get_url(loop))

root = html.fromstring(run)
table = root.xpath("//table[@id='currencies-all']")

table_head_data = tuple(table[0].xpath('./thead/tr/th/text()'))
table_body_obj = table[0].xpath('./tbody/tr')
table_body_data = []

for i in table_body_obj:
    _ = [re.sub(r'\s+', '', i) for i in i.xpath('./td/descendant-or-self::text()')]
    v = [i for i in _ if i and i != '*' and i != '**']
    val = [z.replace('?', '0').replace('LowVol', '0') for z in v]
    table_body_data.append(val)

