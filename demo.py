import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(2)
def km(times,events,tmax=60):
    order=np.argsort(times); times=times[order]; events=events[order]
    n=len(times); surv=1.0; xs=[0]; ys=[1.0]; at=n
    for t,e in zip(times,events):
        if e: surv*= (1- 1/at)
        xs.append(t); ys.append(surv); at-=1
    return xs,ys
for grp,scale,c in [("high-risk",12,"firebrick"),("low-risk",30,"royalblue")]:
    t=rng.exponential(scale,120).clip(0,60); ev=(t<58).astype(int)
    xs,ys=km(t,ev); plt.step(xs,ys,where="post",label=grp,color=c)
plt.ylim(0,1); plt.xlabel("Time (months)"); plt.ylabel("Survival probability")
plt.title("Kaplan-Meier curves (demo data)"); plt.legend()
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("two risk groups, clear survival separation\n"); print("ok")