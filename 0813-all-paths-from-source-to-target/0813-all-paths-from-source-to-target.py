class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(graph)
        def bfs():
            stack=[[0]]
            visite=set()
            while stack:
                vertex=stack.pop(0)
                if vertex[-1]==n-1:
                    res.append(vertex)
                else:
                    for adjvertex in graph[vertex[-1]]:
                        stack.append(vertex+[adjvertex])           
        bfs()
        return res
                
