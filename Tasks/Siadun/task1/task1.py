#(d) deposit = 20000 BYN
#(t) term = 5 years or 60 months
#(p) percent = 15% (must be divided by 100)
#(fd) final deposit - ?

d = 20000
p = 0.15
t = 60

fd = d*(1+p/12)**t
 
print(fd)
