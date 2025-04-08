import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("data/governance_models.csv")

# Timeline Plot
plt.figure(figsize=(18, 12))
for i, row in df.iterrows():
    plt.plot([row["Start"], row["End"]], [i, i], linewidth=6)
    plt.text(row["End"] + 10, i,
             f"{row['System']} ({row['Region']})", va='center', fontsize=8)
plt.xlabel("Year")
plt.title("Global Governance Models Timeline")
plt.gca().invert_xaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.savefig("visuals/governance_timeline.png")
plt.show()

# Evolution Tree (Sankey)
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Greek Democracy", "Swiss Cantonal Democracy",
               "Kurultai", "Cossack Hetmanate"]
    ),
    link=dict(
        source=[0, 2],
        target=[1, 3],
        value=[1, 1]
    )
)])
fig.update_layout(title_text="Governance Evolution Tree", font_size=12)
fig.write_html("visuals/governance_evolution_tree.html")
