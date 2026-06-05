# Forecasting Under Regime Instability: Labor Market Signals After COVID-19

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project evaluates whether traditional labor-market tightness measures, especially the job-openings-to-unemployment ratio, retained stable predictive value for future inflation and wage growth after the COVID-19 shock.

The main finding is that labor-market tightness did not become useless after COVID-19, but it became less stable, more conditional, and more target-dependent. The job-openings-to-unemployment ratio remains most useful for wage-growth forecasting, especially around the 6-month horizon. It is not a reliable standalone predictor of CPI or PCE inflation after COVID-19. Inflation forecasting is more persistence-driven and more sensitive to regime shifts than wage forecasting.

---
## Overview

### Problem Statement
Labor-market indicators are widely used to assess inflation pressure, wage pressure, and broader macroeconomic risk. One common measure is the job-openings-to-unemployment ratio, which compares labor demand with available unemployed labor. When this ratio is high, employers are posting many jobs relative to the number of unemployed workers. This usually signals a tight labor market, stronger worker bargaining power, and possible wage pressure.

The COVID-19 shock created a serious forecasting problem. The U.S. economy moved from a long pre-pandemic expansion into a sudden labor-market collapse, then into a rapid reopening, historically high labor tightness, elevated wage growth, and the strongest inflation surge in decades. A model trained on pre-2020 relationships will not describe the post-2021 economy well.

This project asks whether labor-market tightness still predicts future wage growth and inflation after this regime shift, and if machine-learning models adapt better than traditional econometric models under structural instability.

### Research Question
Did the job-openings-to-unemployment ratio remain a stable forecasting signal for wage growth and inflation after COVID-19, or did its predictive value deteriorate, shift, or become conditional on macroeconomic regime?

### Key Findings
| Area | Specific Result | Interpretation |
|---|---:|---|
| Labor tightness shift | JOLTS-to-unemployment ratio rose from 0.56 pre-COVID to 1.38 post-June 2021 | The post-pandemic labor market was much tighter than the pre-pandemic baseline. |
| Wage growth shift | 12-month wage growth rose from 2.49% to 4.35% | Wage dynamics changed materially after COVID-19. |
| Inflation shift | 12-month CPI rose from 2.08% to 4.44%; 12-month PCE rose from 1.78% to 3.92% | The post-pandemic period was a very distinct inflation regime. |
| Strongest wage result | 6-month wage JOLTS coefficient rose from 0.4840 pre-COVID to 1.10 post-COVID | Labor tightness remained informative for intermediate-horizon wage forecasting. |
| Best post-COVID wage model | Ridge won 6-month wage forecasting with RMSE 0.37 and MAE 0.3  | Regularized linear models remained useful under instability. |
| Inflation reliability | CPI and PCE labor-market signals were unreliable in the final signal matrix | JOLTS tightness was not a stable standalone inflation predictor. |
| Machine learning result | Random Forest and Gradient Boosting didn't consistently beat linear models or persistence | Model complexity didn't solve regime instability. |

### Data Sources and Scope
The project uses monthly U.S. macroeconomic data from January 2000 through April 2026. The merged dataset contains 316 monthly observations and 135 raw variables before feature engineering. The data are pulled primarily from FRED and related public macroeconomic series. 

---

## Methodology

### Regime Design
The project separates the sample into pre-pandemic, pandemic-shock, and post-pandemic regimes. The pre-pandemic period is used as the historical baseline. The pandemic-shock period captures the immediate COVID-19 labor-market collapse and reopening disruption. The post-pandemic period captures the high-tightness, high-inflation, high-rate environment after June 2021. This prevents the model from treating the post-pandemic economy as a normal continuation of the 2000–2019 period.

### Limitations
The post-COVID evaluation sample is short, especially for 12-month horizons. The project is strongest as evidence of regime instability and signal reliability breakdown, not as a final long-run structural estimate of the post-pandemic economy. Also, average hourly earnings can also be distorted during COVID-19 because lower-wage workers were disproportionately affected by job losses, which can raise measured average wages.

### Feature Engineering
The central labor-market feature is the job-openings-to-unemployment ratio. The project also uses the log version of this ratio because the raw ratio became extremely high and highly skewed after the pandemic. The feature set includes labor-market tightness, unemployment, quits, monetary policy, consumer sentiment, credit spreads, lagged target values, changes, rolling volatility, and macroeconomic state flags. The state flags identify high-inflation, tight-labor, and credit-stress environments relative to the pre-pandemic distribution. These features were selected to test whether labor-market indicators add forecasting value after controlling for persistence, monetary conditions, and financial stress.

### Econometric Diagnostics
The econometric work includes stationarity checks, level-shift tests, Chow structural-break tests, sup-F break searches, CUSUM stability tests, rolling coefficient analysis, HAC-adjusted regressions, multicollinearity diagnostics, and out-of-sample forecast evaluation. CUSUM is used to check whether model residuals remain stable over time. In this project, CUSUM tests reject stability for the 12-month wage, CPI, and PCE equations, supporting the main claim that forecasting relationships changed after COVID-19.

### Forecasting Models
The forecasting models include persistence, autoregression, OLS, Ridge, Lasso, ElasticNet, Huber regression, Random Forest, and Gradient Boosting. Models are evaluated with RMSE, MAE, and out-of-sample R-squared using time-aware splits instead of random cross-validation.

This project includes macroeconomic data engineering, time-series feature construction, econometric testing, structural-break analysis, forecast validation, model comparison, regularized regression, ML benchmarking, and research communication.

---
## Results And Interpretation

### Labor-Market Tightness Changed After COVID-19
The job-openings-to-unemployment ratio increased from about 0.56 before COVID-19 to about 1.38 after June 2021. The tight-labor state flag was active in 25.00% of pre-pandemic observations but 89.83% of post-pandemic observations. This confirms that the post-pandemic labor market was not a normal continuation of the pre-2020 period.

### Wage Forecasting Retains The Strongest Labor-Market Signal
The strongest evidence is for wage growth, not inflation. The 6-month wage-growth model is the clearest result. The JOLTS coefficient remains positive before and after COVID-19, increasing from 0.4840 to 1.1030. Ridge regression wins the post-pandemic 6-month wage forecast with RMSE 0.3724 and MAE 0.3152.

The 3-month wage result is weaker but still partly supportive. The JOLTS coefficient remains positive but falls from 0.5547 before COVID-19 to 0.1549 after COVID-19. The final signal matrix classifies JOLTS as a partial signal for 3-month wage growth.

The 12-month wage result is not reliable. The JOLTS coefficient changes sign from 1.4272 before COVID-19 to -0.7801 after COVID-19, and persistence wins the post-pandemic 12-month wage comparison. This means the project does not support a strong long-horizon wage claim.

### Inflation Forecasting Is More Unstable
The JOLTS ratio is not a stable standalone predictor of CPI or PCE inflation. The final signal reliability matrix classifies all tested CPI and PCE labor-market signals as unreliable after COVID-19.

The best limited inflation result is the 6-month CPI forecast, where ElasticNet wins the post-pandemic comparison with RMSE 0.3287 and positive out-of-sample R-squared of 0.3228. This does not mean JOLTS itself is reliable for inflation. It means a regularized model with controls performs well in that specific target window.

For PCE inflation, persistence remains difficult to beat. In the final post-pandemic comparison, persistence wins 12-month PCE with RMSE 0.6006 and MAE 0.5916.

### Machine Learning Did Not Dominate
Random Forest and Gradient Boosting were tested directly, but they did not consistently outperform linear models or persistence. Before COVID-19, linear models had lower average RMSE than machine-learning models. The pre-pandemic mean RMSE was 0.3329 for linear models, 0.4159 for machine-learning models, and 0.4667 for baseline models.

After COVID-19, baseline models had the lowest average RMSE at 0.4188, while linear models averaged 1.1422 and machine-learning models averaged 1.1447. These post-COVID averages are affected by short samples and unstable target windows, but the conclusion is still important. More flexible models did not automatically adapt better to regime instability.

---
## Repository Structure
```
├── LICENSE          
├── Makefile       
├── README.md         
│
├── data
│   ├── external    
│   ├── interim        
│   ├── processed      <- Final model-ready datasets (wage, price, interaction panels)
│   └── raw            <- Raw FRED pulls and source files
│
├── docs            
│
├── models            
│
├── notebooks
│   ├── 01-eda.ipynb                   
│   ├── 02-feature-engineering.ipynb    
│   ├── 03-baseline-models.ipynb      
│   ├── 04-structural-analysis.ipynb  
│   ├── 05-forecast-benchmarks.ipynb     
│   └── 06-results-and-audit.ipynb       
│
├── pyproject.toml     
│
├── references   
│
├── reports       
│   └── figures     
│
├── requirements.txt   
│
├── setup.cfg      
│
└── regime_instability <- src for the project
    │
    ├── __init__.py       
    │
    ├── config.py              
    │
    ├── data.py                 <- Data loaders (FRED, file ingestion, API handling)
    │
    ├── preprocessing.py     
    │
    ├── features.py           
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── train.py            <- Model training (OLS, Ridge, RF, etc.)
    │   ├── predict.py          <- Forecast generation and evaluation
    │   └── evaluation.py       <- RMSE comparison, horizon analysis, regime splits
    │
    └── visualization.py      
```
