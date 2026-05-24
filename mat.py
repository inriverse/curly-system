import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit slider
prob = st.slider(
    "Probability",
    min_value=0.01,
    max_value=0.99,
    value=0.50,
    step=0.01
)

# Data
t = np.linspace(0, 10, 100)
y = 1 - (1 - prob) ** t

# Create figure
fig, ax = plt.subplots(figsize=(6, 5))

# Plot
ax.plot(t, y, lw=2)

# Axis settings
ax.set_ylim(0, 1.1)
ax.set_xlabel("t")
ax.set_ylabel("Probability")
ax.set_title("1 - (1 - p)^t")

# Display in Streamlit
st.pyplot(fig)
