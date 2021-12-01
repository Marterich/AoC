with open("16.dat","rt") as f: t = f.read().strip() # input as string
d = [int(x) for x in t]; N = len(d) # input as numbers
v = d[:] # working copy of data
for _ in range(100):
  v = [abs(sum( (0,1,0,-1)[(i+1)//(k+1)%4]*v[i] for i in range(N) )) % 10 for k in range(N)]
print(''.join(str(x) for x in v[:8]))
v = (10000*d)[int(t[:7]):] # tail for part2
for _ in range(100):
  for i in range(len(v)-1,0,-1): # need to do calculations from the end!!! that's the key idea!
    v[i-1] = (v[i-1]+v[i]) % 10
print(''.join(str(x) for x in v[:8]))