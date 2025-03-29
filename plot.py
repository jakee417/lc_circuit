import numpy as np
import plotly.express as px
import pandas as pd

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
H = 0.5 * C * np.power(v_C, 2) + 0.5 * L * np.power(i, 2)
df = pd.DataFrame(
    {"t": t, "q(t)": q, "i(t)": i, "v_L(t)": v_L, "v_C(t)": v_C, "H(t)": H}
)
fig = px.line(df, x="t", y=["q(t)", "i(t)", "v_L(t)", "v_C(t)", "H(t)"])
snapshots = [("T / 4", T / 4), ("T / 2", T / 2), ("T * 3 / 4", T * 3 / 4)]
for i, x in snapshots:
    fig.add_vline(
        x=x, line_width=3, line_dash="dash", line_color="red", annotation_text=f"t={i}"
    )
fig.add_hline(y=0)
fig.update_layout(
    legend=dict(
        orientation="h", entrywidth=70, yanchor="bottom", y=1.02, xanchor="right", x=1
    )
)
fig.show()
