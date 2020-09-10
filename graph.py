import copy
graph={
    'F':{'P':95,'W':217,'K':173},
    'P':{'X':80},
    'W':{'E':186,'N':170},
    'K':{'M':502},
    'N':{'M':167},
    'X':{'A':250},
    'A':{'M':94},
    
    }


heuristic={
            'F':0,
            'A':60,
            'E':1000,
            'K':340,
            'N':150,
            'P':400,
            'W':300,
            'X':340,
            'M':0,
            
    }
def get_cost(path):
    cost=0
    for i in range(1,len(path[0])):
        cost+=graph[path[0][i-1]][path[0][i]]
    return cost

def A_star(graph,heuristic,start,end):
    priority_queu=[]
    priority_queu.append([[start],heuristic[start]])
    
    while priority_queu:
        path=priority_queu.pop(0)
        node=path[0][-1]
        if node==end:
            return path
        for adjacent in graph.get(node,[]):
            new_path = copy.deepcopy(list(path))
            new_path[0].append(adjacent)
            H_value=heuristic[adjacent]
            G_value=get_cost(new_path)
            total=H_value+G_value
            new_path[1]=total
            priority_queu.append(new_path)
        priority_queu.sort(key=lambda x:x[1])
        
print(A_star(graph,heuristic,'F','M'))    
