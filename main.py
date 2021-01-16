import asyncio
from distance_vector.router import Router

if __name__ == '__main__':
    router0 = Router(
        node_id=0, node_count=4,
        connections={
            1: 1,
            2: 3,
            3: 7
        }
    )
    router1 = Router(
        node_id=1, node_count=4,
        connections={
            0: 1,
            2: 1,
        }
    )
    router2 = Router(
        node_id=2, node_count=4,
        connections={
            0: 3,
            1: 1,
            3: 2
        }
    )

    router3 = Router(
        node_id=3, node_count=4,
        connections={
            0: 7,
            2: 2
        }
    )

    router0.route_init()
    router1.route_init()
    router2.route_init()
    router3.route_init()

    router0.set_router_obj({
        1: router1,
        2: router2,
        3: router3
    })

    router1.set_router_obj({
        0: router0,
        2: router2
    })

    router2.set_router_obj({
        0: router0,
        1: router1,
        3: router3
    })

    router3.set_router_obj({
        0: router0,
        2: router2
    })

    asyncio.run(router0.to_node())
    asyncio.run(router1.to_node())
    asyncio.run(router2.to_node())
    asyncio.run(router3.to_node())

    print(f'router 0 distance vector: {router0.dv}')
    print(f'router 1 distance vector: {router1.dv}')
    print(f'router 2 distance vector: {router2.dv}')
    print(f'router 3 distance vector: {router3.dv}')

