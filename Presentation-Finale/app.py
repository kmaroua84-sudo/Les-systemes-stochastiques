import random
from collections import deque
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

st.set_page_config(page_title="Laboratoire de percolation", page_icon="🧪", layout="wide")
st.title("🧪 Laboratoire de percolation")
st.caption("Modèle de percolation sur un réseau carré — simulation interactive")

with st.sidebar:
    st.header("Paramètres")
    p = st.slider("Probabilité d’ouverture (p)", 0.0, 1.0, 0.5, 0.05)
    n = st.select_slider("Taille du réseau", options=[10, 15, 20, 30], value=10)
    seed = st.number_input("Graine aléatoire (facultatif)", min_value=0, max_value=999999, value=42, step=1)
    run = st.button("▶ Lancer la simulation", type="primary", use_container_width=True)
    st.caption("Un site est ouvert avec probabilité p, fermé avec probabilité 1−p.")

def find_vertical_path(grid):
    rows, cols = grid.shape
    q = deque()
    parent = {}
    for c in range(cols):
        if grid[0, c] == 1:
            q.append((0, c))
            parent[(0, c)] = None
    while q:
        r, c = q.popleft()
        if r == rows - 1:
            path = []
            cur = (r, c)
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]
        for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc] == 1 and (nr,nc) not in parent:
                parent[(nr,nc)] = (r,c)
                q.append((nr,nc))
    return []

if "grid" not in st.session_state:
    st.session_state.grid = None
    st.session_state.path = []
    st.session_state.p = p

if run or st.session_state.grid is None:
    rng = np.random.default_rng(int(seed) if seed else None)
    st.session_state.grid = (rng.random((n,n)) < p).astype(int)
    st.session_state.path = find_vertical_path(st.session_state.grid)
    st.session_state.p = p
    st.session_state.n = n

grid = st.session_state.grid
path = st.session_state.path
path_set = set(path)
display = np.zeros_like(grid, dtype=int)
display[grid == 1] = 1
for r,c in path_set:
    display[r,c] = 2

left, right = st.columns([1.5, 1])
with left:
    st.subheader("Réseau simulé")
    fig, ax = plt.subplots(figsize=(6.2, 6.2))
    cmap = ListedColormap(["#20354c", "#67dcb5", "#ffbd59"])
    ax.imshow(display, cmap=cmap, vmin=0, vmax=2)
    ax.set_xticks(np.arange(-.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=.8, alpha=.75)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    ax.set_title(f"Réseau {n} × {n}  |  p = {st.session_state.p:.2f}", color="#26384a")
    st.pyplot(fig, use_container_width=False)
    plt.close(fig)
with right:
    st.subheader("Résultat")
    if path:
        st.success("PERcolation : OUI — un chemin relie le haut au bas.")
    else:
        st.error("Percolation : NON — aucun chemin traversant trouvé.")
    st.metric("Sites ouverts", f"{int(grid.sum())}/{n*n}")
    st.metric("Proportion ouverte", f"{grid.mean()*100:.1f}%")
    st.metric("Longueur du chemin", len(path) if path else "—")
    st.markdown("**Légende**")
    st.markdown("🟦 Site fermé  \n🟩 Site ouvert  \n🟨 Site appartenant au chemin")

st.divider()
st.subheader("Comparer plusieurs essais")
trials = st.slider("Nombre d’essais", 10, 300, 100, 10)
if st.button("Calculer la fréquence de percolation"):
    rng = np.random.default_rng()
    successes = 0
    for _ in range(trials):
        g = (rng.random((n,n)) < p).astype(int)
        successes += bool(find_vertical_path(g))
    freq = successes / trials
    st.metric("Fréquence observée de percolation", f"{freq*100:.1f}%")
    st.progress(freq)
    st.caption(f"{successes} essais avec percolation sur {trials}. Cette fréquence est une estimation expérimentale, pas une probabilité exacte.")
st.info("Astuce pour la présentation : testez successivement p = 0,30 ; 0,50 ; 0,70 et comparez les fréquences sur plusieurs essais.")
