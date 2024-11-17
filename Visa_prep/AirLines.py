import math
X,N=map(int,input().split())
required_aircraft=math.ceil(N/100)
additional_aircraft=max(0,required_aircraft-X)
print(additional_aircraft)
