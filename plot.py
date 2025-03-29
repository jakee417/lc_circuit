import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from IPython.display import display, Markdown
A = 1
L = 1
C = 1
T = np.pi * 2
phi = np.pi / 2
omega = 1 / np.sqrt(L * C)
t = np.linspace(0, T)
q = A * np.sin(omega * t + phi)
i = omega * A * np.cos(omega * t + phi)
v = -np.pow(omega, 2) * L * A * np.sin(omega * t + phi)
fig = px.line(pd.DataFrame({"t": t, "q(t)": q, "i(t)": i, "v(t)": v}), x="t", y=["q(t)", "i(t)", "v(t)"])
for i, x in [("T / 4", T / 4), ("T / 2", T / 2), ("T * 3 / 4", T * 3 / 4)]:
    fig.add_vline(x=x, line_width=3, line_dash="dash", line_color="red", annotation_text=f"t={i}")
fig.add_hline(y=0)
fig.show()
