from __future__ import annotations
from typing import Dict
from .routing_packet import RoutingPacket
import asyncio


class Router:
    def __init__(self, node_id: int, node_count: int, connections: Dict[int, int]):
        self.node_id = node_id
        self.connections = connections
        self.dv = [float('inf') for _ in range(node_count)]
        self.router_objs = dict()

    def route_init(self) -> None:
        self.dv[self.node_id] = 0
        for connection in self.connections:
            self.dv[connection] = self.connections[connection]

    def set_router_obj(self, router_objs: Dict[int, Router]) -> None:
        self.router_objs = router_objs

    async def to_node(self) -> None:
        for dest_id in self.connections:
            print(f'Node {self.node_id}: sending routing packet to: {dest_id}\n'
                  f'distance vector: {self.dv}')
            rp = RoutingPacket(self.node_id, dest_id, self.dv)
            await self.router_objs[dest_id].route_update(rp, self.connections[dest_id])

    async def route_update(self, routing_packet: RoutingPacket, delay: int) -> None:
        await asyncio.sleep(delay * 0.1)
        if self.node_id != routing_packet.dest_id:
            return
        print(f'Node {self.node_id}: received routing packet from: {routing_packet.source_id}\n'
              f'distance vector: {routing_packet.dv}')
        new_dv = routing_packet.dv
        flag = False
        for dest_id, distance in enumerate(new_dv):
            new_dest = distance + self.connections[routing_packet.source_id]
            if new_dest < self.dv[dest_id]:
                self.dv[dest_id] = new_dest
                flag = True
        if flag:
            await self.to_node()
