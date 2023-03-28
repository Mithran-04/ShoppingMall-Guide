import sys

ShopOrder = []
d = {}



class Graph():
    def __init__(self, vertices, mall):
        self.V = vertices
        self.dlist = []
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.Mall = mall

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def OrderToBeVisisted(self, dist, trq):
        minDist = 1000000
        shopName = "Max"
        for i in range(len(trq)):
            name = trq[i]
            l = self.Mall.index(name)
            currDist = dist[l]
            if (currDist < minDist):
                minDist = currDist
                shopName = trq[i]
        self.dlist.append(minDist)
        ShopOrder.append(shopName)

        return shopName
    def totaldist(self):
        td=0
        for i in range(len(self.dlist)):
            td+= self.dlist[i]
        print("----------------------------------------")
        print("aipuwebfpiuWEBFCI[WEbcvio")
        print(td)
        print("woiabfviuawb voin")
        return td

    def printdist(self, ShopList):
        print("---------------- DISTANCE NEEDED TO VISIT THE SHOPS -----------------------")
        print()
        for i in range(len(self.dlist)):
            if (i == 0):
                print("Entrance --> ", ShopList[i], " : ", self.dlist[i])
                d["Entrance  --> " + ShopList[i]] = self.dlist[i]
            else:
                print(ShopList[i - 1], "--> ", ShopList[i], " : ", self.dlist[i])
                d[ShopList[i - 1] + "--> " + ShopList[i]] = self.dlist[i]
        print("----------------------------------------")

        return d

    def dijkstra(self, src, trq):
        trq = trq
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for j in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        return (self.OrderToBeVisisted(dist, trq))


Mall = ["MAX", "NIKE", "TRENDS", "ALLEN SOLLY", "CASIO", "BATA", "ARROW", "PUMA", "CROMA", "DIESEL", "FUNCITY",
        "BURGER KING", "PUNJAB GRILL", "RADO", "DOMINOS", "HPWORLD"]
MallMap = {0: "HPworld", 1: "Dominos", 2: "Rado", 3: "Punjab Grill", 4: "Croma", 5: "Diesel", 6: "Funcity",
           7: "Burger King", 8: "Puma", 9: "Arrow", 10: "Bata", 11: "Casio", 12: "Max", 13: "Nike", 14: "Trends",
           15: "Allen Solly"}
print()
print("---------------------------------------------------MALL---------------------------------------------------")
j = 3
for i in range(1, 17):
    if ((i) % 4 == 1):
        print()
        print(f'floor{j}: ', end='')
        j -= 1
    print(MallMap[i - 1], end='')
    print('\t\t\t', end='')

ListToBeTraversed = []
print()
print()

OptimalShopTraversal = []
# for i in range(n):
#     s=input("Enter the name of the shop: ")
#     s=s.upper()
#     if(Mall.count(s)==0):
#         while(Mall.count(s)==0):
#               print("This shop is not currently available in the mall")
#               print()
#               s = input("Enter the name of the shop: ")
#               s=s.upper()
#         ListToBeTraversed.append(s)
#     elif(ListToBeTraversed.count(s)!=0):
#         while (ListToBeTraversed.count(s)!=0):
#             print("This shop is already present in the list !!. Enter a new shop to be visited.")
#             print()
#             s = input("Enter the name of the shop: ")
#             s=s.upper()
#         ListToBeTraversed.append(s)
#     else:
#         s=s.upper()
#         ListToBeTraversed.append(s)

g = Graph(16, Mall)
g.graph = [[0, 1, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 50, 0, 1, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [50, 0, 0, 0, 0, 0, 1, 0, 50, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 50, 0, 1, 0, 0, 0, 0, 0, 50],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 1, 0, 50, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 1, 0]]

ShopName = Mall[0]
ans = []
distance = []

print()
ShopOrder = []

def FirstOrder(ListToBeTraversed):
    ShopName = Mall[0]
    for i in range(len(ListToBeTraversed)):
        ShopName = g.dijkstra(Mall.index(ShopName), ListToBeTraversed)
        OptimalShopTraversal.append(ShopName)
        ListToBeTraversed.remove(ShopName)
    return ShopOrder
print("---------------- OPTIMAL ORDER TO VISIT THE SHOPS -----------------------")
for i in range(len(ShopOrder)):
    print(ShopOrder[i])
def OrderWithDistance():
    return(g.printdist(OptimalShopTraversal))
totalDistance = g.totaldist()


def totaldist():
    td = 0
    for i in range(len(g.dlist)):
        td += g.dlist[i]
    print("----------------------------------------")
    print("aipuwebfpiuWEBFCI[WEbcvio")
    print(td)
    print("woiabfviuawb voin")
    return td
print()
print("Total distance in units required to visit: ", totalDistance)
print()


















