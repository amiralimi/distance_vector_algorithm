from typing import List


class RoutingPacket:
    def __init__(self, source_id: int, dest_id: int, dv: List[float]):
        self.source_id = source_id
        self.dest_id = dest_id
        self.dv = dv
