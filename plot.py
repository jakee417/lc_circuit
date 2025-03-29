import numpy as np
import plotly.express as px
import pandas as pd
import plotly.subplots as sp

A = 1
L = 1
C = 1
T = np.pi * 2
phi = np.pi / 2
omega = 1 / np.sqrt(L * C)
t = np.linspace(0, T)
q = A * np.sin(omega * t + phi)
i = omega * A * np.cos(omega * t + phi)
v_L = -np.pow(omega, 2) * L * A * np.sin(omega * t + phi)
v_C = q / C
fig1 = px.line(
    pd.DataFrame({"t": t, "q(t)": q, "i(t)": i, "v_L(t)": v_L, "v_C(t)": v_C}),
    x="t",
    y=["q(t)", "i(t)", "v_L(t)", "v_C(t)"],
)
E_C = 0.5 * C * np.power(v_C, 2)
E_L = 0.5 * L * np.power(i, 2)
H = E_C + E_L
fig2 = px.line(
    pd.DataFrame({"t": t, "E_C(t)": E_C, "E_L(t)": E_L, "H(t)": H}),
    x="t",
    y=["E_C(t)", "E_L(t)", "H(t)"],
)

# Create a 1x2 subplot
fig = sp.make_subplots(rows=2, cols=1)

# Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
for trace in range(len(fig1["data"])):
    fig.append_trace(fig1["data"][trace], row=1, col=1)

for trace in range(len(fig2["data"])):
    fig.append_trace(fig2["data"][trace], row=2, col=1)

snapshots = [("T / 4", T / 4), ("T / 2", T / 2), ("T * 3 / 4", T * 3 / 4)]
for l, x in snapshots:
    fig.add_vline(
        x=x, line_width=3, line_dash="dash", line_color="red", annotation_text=f"t={l}"
    )
fig.add_hline(y=0)
fig.show()
