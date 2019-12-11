# blocksworld-tile-ai
AI for agent in 4*4 blocksworld tile problem using multiple search algorithms and heuristics.  
The agent can move Up / Down / Left / Right.  
When interacting with a tile, the agent swaps places with it.



The problem:  

|    |    |    |    |
|---|---|---|---|
| X  | X  | X  | X  |
| X  | X  | X  | X  |    
| X  | X  | X  | X  |
| 1  | 2  | 3  | A  |
|    |    |    |    |

The solution:

|   |   |   |   |
|---|---|---|---|
| X  | X  | X  | X  |
| X  | 1  | X  | X  |
| X  | 2  | X  | X  |
| X  | 3  | X  | A  |
|    |    |    |    |

Each of the traversal algorithms within **Search** require a start **Node** loaded with a **State**.  
They return a 2-tuple containing:  
    **Node** - (containing all data about the depth and moves taken for the solution)  
    *t_complexity* - the time complexity of the algorithm (In terms of nodes generated, not execution time).