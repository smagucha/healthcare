import asyncio
from elarian import Elarian, Customer

client = Elarian(
	org_id='el_org_eu_6Wyo8s', 
	app_id='el_app_BvClas', 
	api_key='el_k_live_1a029a1f89ef3f7656eaacb39838c02ccb90835ff5b06eb3ae33697ae6b00766'
	)

def on_connected():
  print("App is running!")

async def start():
    client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
    client.set_on_connected(on_connected)
    await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()


def on_connected():
    print("App is running!")

    alice = Customer(
        client=client,
        number="+254724123456",
        provider="cellular",
        first_name= 'alice',
        last_name='Motende'


    )

    # data = {"name": "Alice"}
    # await alice.update_metadata(data)

    # resp = await alice.get_state()

    # await alice.add_reminder({
    #     'key': 'loaner',
    #     'payload': "USD 100",
    #     'remind_at': round(time() + 60) # Remind 1m from now
    # })

async def start():
    client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
    client.set_on_connected(on_connected)
    await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()