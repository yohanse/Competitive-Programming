class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Build graph
        graph = defaultdict(list)
        for bus in range(len(routes)):
            for bus_station in routes[bus]:
                graph[bus_station].append(bus)
        print(graph)

        queue = deque([(source, 0)])
        bus_visited = set()
        bus_station_visited = set()
        while queue:
            vertex, count = queue.popleft()
            if vertex == target:
                return count
            
            for bus in graph[vertex]:
                if bus not in bus_visited:
                    bus_visited.add(bus)
                    for bus_station in routes[bus]:
                        if bus_station not in bus_station_visited:
                            bus_station_visited.add(bus_station)
                            queue.append((bus_station, count + 1))
        return -1
            