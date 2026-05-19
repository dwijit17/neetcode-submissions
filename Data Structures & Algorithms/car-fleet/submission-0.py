class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        hmap = {}
        n = len(speed)
        for i in range(n):
            hmap[position[i]] = speed[i]
        
        #sort the hmap by order of kyes
        dis = sorted(hmap,key = lambda x : x,reverse=True)
        #we got distances sorted in descending order
        #now calculate time
        time = [(target-d)/hmap[d] for d in dis]
        print(time)
        for i in range(n):
            if len(stack)>0:
                if time[i]<=stack[-1]:
                    continue
            stack.append(time[i])
        return len(stack)
        
        