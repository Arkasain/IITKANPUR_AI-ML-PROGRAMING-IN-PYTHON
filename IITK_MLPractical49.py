import pandas as pd

df = pd.DataFrame({
    "A":[12,4,5,None,1],
    "B":[None,2,54,3,None],
    "C":[20,16,None,3,8],
    "D":[14,3,None,None,6]
}
)
print("\ndf=\n",df)

df2= df.interpolate(limit_direction='forward')
print("\n df2=\n",df2)

df3=df.interpolate(limit_direction='backward')
print("\ndf3=\n",df3)