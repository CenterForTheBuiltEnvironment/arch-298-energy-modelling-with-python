# 🌍 Final Project – From Simulation to Machine Learning

### 🎯 Objective
In this final project, you will complete the **entire pipeline** from detailed EnergyPlus simulation to data-driven prediction.  
The goal is not only to build accurate models but also to **understand how physical simulation and machine learning differ** — in data source, scale, precision, and interpretation.

---

## 🧱 Step 1 – Generate Simulation Data
Use your simplified EnergyPlus model (`model_week4.idf`) to perform a **multi-parameter batch simulation**.  

| Parameter | Description | Levels |
|------------|--------------|---------|
| **Location** | Climate zones representing U.S. cities | San Francisco, Sacramento, Chicago, New York |
| **Wall R-value** | Wall insulation level (ft²·°F·hr/Btu) | 14.3, 21.9, 29.7 |
| **WWR** | Window-to-Wall Ratio | 0.25, 0.40, 0.60 |
| **SHGC** | Solar Heat Gain Coefficient | 0.25, 0.40, 0.60 |
| **Occupancy Density** | People per floor area | 0.04, 0.06, 0.08 |
| **Lighting Density** | Lighting power density (W/m²) | 7.5, 9 |
| **Cooling Setpoint** | Indoor cooling temperature (°C) | 24, 26, 28 |

> 🔢 **Total simulation cases:** 4 × 3 × 3 × 3 × 3 × 2 × 3 = 1944 (or more if you add optional parameters)

Save the outputs:
- `results.csv` → cooling energy results  
- `all_parameters.csv` → corresponding parameter combinations  

---

## ⚙️ Step 2 – Feature Engineering
In this stage, you will **define and construct your own features** that best describe the relationship between building configuration and energy performance.

You may consider — but are not limited to — the following feature types:

| Category | Possible Examples | Description |
|-----------|-------------------|--------------|
| **Climate Indicators** | Cooling/Heating Degree Days (CDD/HDD), average or extreme temperatures, solar radiation | Capture how external conditions drive cooling demand | Don't use location as feature
| **Design Variables** | R-value, WWR, SHGC, setpoint, lighting/occupancy density | Represent envelope and operation parameters |
| **Derived Features** | Ratios, interaction terms (e.g., WWR × SHGC), normalized indicators | Capture nonlinear or combined effects |

> 💡 There is **no single correct method** — you are encouraged to explore different feature definitions, transformations, or normalization strategies that improve model performance or interpretability.

> ✅ **Goal:** create a structured dataset linking simulation parameters and climate factors to building energy response.

---

## 🤖 Step 3 – Train Machine Learning Models
Using your combined dataset:
1. Define input (`X`) and target (`y`) variables.  
2. Split your data into training (San Francisco, NYC, Chicago) and testing (Sacramento) sets.  
3. Train and compare multiple regression models (including at least Linear, Decision Tree, Random Forest).  
4. Evaluate performance using MSE, RMSE, MAE, and R² metrics.

> ✅ **Goal:** test how well data-driven models can approximate simulation-based results.

---

## 🔍 Step 4 – Compare and Reflect
After completing your models, analyze and discuss the **differences between simulation and machine learning**.  
Your reflection should go beyond numeric accuracy — focus on conceptual distinctions:

| Aspect | Simulation (EnergyPlus) | Machine Learning |
|--------|--------------------------|------------------|
| **Data Source** | Physics-based, derived from model geometry and materials | Pattern-based, relies on data relationships |
| **Scale** | Hourly/sub-hourly, spatially detailed | Aggregated across samples and features |
| **Precision** | Controlled by physical fidelity | Limited by data quality and coverage |
| **Interpretability** | Physically explicit | Statistical or black-box, depends on algorithm |
| **Computation** | Intensive, per simulation run | Lightweight after training |
| **Use Case** | Design analysis, calibration, validation | Prediction, optimization, surrogate modeling |

> 🧠 **Reflection Question:**  
> How do the **data scale** and **precision** differ between simulation and ML?  
> What trade-offs arise when replacing physics-based detail with data-driven learning?

---

## 📝 Deliverables (required — slides only)

Submit a short slide deck (PDF or PPTX, 4–8 slides). The deck must be self-contained and clearly communicate your workflow, results, and interpretation. Required slide content:

1. Title slide — project title, authors, date (1 slide).  
2. Climate distributions — 1 slide with plots showing outdoor temperature distributions for each location (histogram/violin + short summary stats).  
3. ML evaluation — 1–2 slides that include:
   - Key metrics (MSE, RMSE, MAE, R²) for the models you report,
   - Predicted vs actual scatter (with 1:1 line) and a brief note on major errors,
   - One compact feature-importance or interpretability plot.
4. Reflection & conclusions — 1–2 slides that:
   - Compare data-driven (ML) results vs physics-based simulation (strengths, limitations, recommended use cases),
   - State key takeaways and 1–2 recommended next steps.

### 📤 Submission instructions
- Filename: final_slides.pdf or final_slides.pptx  
- Submit slides only; including data/notebooks/code is optional but encouraged (provide a link or archive if available).

Grading (slides-focused, 100 pts)
- Clarity & communication: 25 pts  
- Climate & data visualisation: 25 pts  
- ML evaluation (metrics + plots): 20 pts  
- Reflection & interpretation: 30 pts  

---

## Submission Deadline
Submit your final slide deck (final_slides.pdf or final_slides.pptx) via the course LMS by 28/11/2025, 23:59 local time.  
If you include links to data/code/notebooks, add them in an appendix slide and ensure the links are accessible.
