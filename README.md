# Fashion Product Adoption in a Consumer Social Network

**UWA — CITS4403 Computational Modelling Project**

## Research question

**How do influencer position and social influence strength affect the adoption of a new fashion product within a consumer social network?**

This project uses an **agent-based stochastic simulation** to study how a limited-edition fashion T-shirt spreads through a simulated consumer network. Consumers may purchase independently or be influenced by neighbours who have already adopted the product.

## Project objectives

- Compare a **central influencer** (a highly connected consumer) with a **less-central influencer** (a consumer with a more typical number of connections).
- Test how different values of **social influence strength** ($\alpha$) affect product adoption.
- Measure **final adoption rate** and **adoption speed** over a 28-day period.
- Visualise cumulative adoption and assess the reliability of results using repeated simulations.

## Model design

The model uses a **Barabási–Albert preferential-attachment network**, which contains a small number of highly connected nodes. This makes it suitable for studying the effect of influencer position.

| Setting                              | Value                                       |
| ------------------------------------ | ------------------------------------------- |
| Consumers (network nodes)            | 100                                         |
| Network model                        | Barabási–Albert                             |
| Edges per new node (`m`)             | 3                                           |
| Initial adopters                     | 1 selected influencer                       |
| Baseline purchase probability        | Sampled from `U(0.01, 0.10)`                |
| Social influence strengths (`alpha`) | `0.000`, `0.025`, `0.050`, `0.075`, `0.100` |
| Influencer strategies                | `central`, `less_central`                   |
| Simulation duration                  | 28 days                                     |
| Repetitions per condition            | 50                                          |
| Main experiment conditions           | 2 strategies × 5 alpha values = 10          |
| Main experiment runs                 | 500                                         |

A consumer who has purchased the product remains an adopter. The model is a simplified representation of social influence, **not a prediction of actual sales**.

## Experiments

### Baseline simulation and parameter checks

The notebook first inspects the network structure and influencer positions, runs a baseline simulation, checks candidate social-influence values, and examines whether 50 repetitions give reasonably stable estimates.

### Experiment 1 — Influencer strategy and social influence

Compares both influencer positions across five social-influence strengths. It measures:

- **Final adoption rate (%):** proportion of consumers who have adopted by Day 28.
- **Adoption speed (days):** first day when at least 50% of consumers have adopted. For averages of adoption speed, only runs that reach this threshold within 28 days are included.

Results include mean values, standard deviations, paired comparisons, and 95% confidence intervals.

### Experiment 2 — Social influence strength

Examines how cumulative adoption changes over time for different values of `alpha`, using repeated simulation runs and visual comparisons.

### Experiment 3 — Influencer position

Compares cumulative adoption trajectories for central and less-central influencers to illustrate how network position affects diffusion over time.

### Model validation

The notebook checks reproducibility with fixed random seeds, non-decreasing cumulative adoption, valid purchase probabilities, correct initial conditions, and adoption counts within the population size.

## Main findings

Within the simulated network:

- **Stronger social influence** generally increases final adoption and speeds up diffusion.
- **Central influencers** tend to produce slightly higher adoption and faster diffusion than less-central influencers.
- The effect of **social influence strength is substantially larger** than the effect of influencer position under the tested conditions.

For example, the notebook reports that, with a central influencer, mean final adoption increased from **71.82%** at `alpha = 0` to **94.64%** at `alpha = 0.10`, while the mean time to reach 50% adoption decreased from **14.56** to **9.64 days**. These are simulation results and depend on the chosen assumptions and random seeds.

## Repository structure

```text
UWA_computational_modelling_project/
├── notebooks/
│   └── experiments.ipynb    # Experiments, visualisations, analysis and validation
├── src/
│   └── model.py             # Network and simulation functions
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation and execution

### 1. Open the project

Open the repository folder in VS Code and open a terminal in its root directory.

### 2. Create a virtual environment (first time only)

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If `.venv` already exists and works, **reuse it** rather than recreating it.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
python -m pip install ipykernel
```

### 4. Run the notebook

1. Open `notebooks/experiments.ipynb` in VS Code.
2. Select the Python interpreter/kernel from `.venv`.
3. Select **Run All** to execute cells in order.
4. Review the figures, result tables, interpretations, and validation checks.

Run Jupyter from the repository root or its `notebooks/` directory so the notebook can locate `src/model.py`.

## Reproducibility

The main experiment uses 50 repetitions per condition, with seeds **0–49** for repeatable comparisons. Because the simulation is stochastic, results may vary if the model, parameter values, seed handling, or dependency versions change. Re-run the entire notebook after modifying the implementation to update its displayed results.

## Limitations

- The network is synthetic and fixed rather than based on observed consumer relationships.
- Purchase decisions are simplified into probabilistic rules.
- The simulation covers 100 consumers and 28 days, so results may not generalise to larger or evolving networks.
- The reported effects describe **model behaviour**, not verified real-world consumer purchasing patterns.

## Contributors

- Yu Ting Weng (`tammyweng0`) 24622994

## Further details

See [`notebooks/experiments.ipynb`](notebooks/experiments.ipynb) for the full model explanation, experimental methods, plots, statistical comparisons, validation tests, references, and conclusions.
