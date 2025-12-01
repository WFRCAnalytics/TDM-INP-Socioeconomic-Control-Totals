# TDM-INP-Socioeconomic-Control-Totals

_Note: This repository contains code and data for estimating county level se atotals for the Wasatch Front Travel Demand Model (TDM). The current implementation applies to model version 10, while all previous calculations from version 8.3.2 and version 9x are stored in the \_archive folder for reference._

# GPI Socioeconomic Data Processing Workflow

### End-to-End Documentation for Employment, Population, County Splits, and Finalization

This repository contains the full workflow for processing socioeconomic (SE) inputs used for travel demand modeling.  
The workflow is organized into a sequence of Jupyter notebooks:

1. **1a-Process-GPI-Employment-Data.ipynb**
2. **1b-Apply-Home-Based-Jobs.ipynb**
3. **2a-Process-GPI-Population-Data-2025+.ipynb**
4. **2b-Process-GPI-Population-Data-2023.ipynb**
5. **3-Split-Box-Elder-And-Weber-Counties.ipynb**
6. **4-Finalize.ipynb**

Each notebook performs a distinct part of the workflow—from cleaning and aggregating raw GPI data to applying home-based jobs factors, splitting counties, and producing final model-ready datasets.

---

## 📌 Overview

The workflow produces standardized, validated, and model-ready employment and population datasets for all Utah counties and split-county model areas.  
All outputs feed into travel demand modeling, dashboards, and scenario planning.

---

# 1. Employment Data Processing (Notebook: **1a**)

### **Purpose**

Ingest raw GPI employment data and prepare consistent county-year-industry employment totals.

### **Key Steps**

- Load raw GPI employment data.
- Standardize columns, FIPS codes, and year formats.
- Join NAICS → TDM industry classification tables.
- Clean numeric fields and remove placeholder rows.
- Aggregate employment by:
  - **County**
  - **Year**
  - **TDM sector**
- Create validation summaries.
- Output:  
  `gpi_employment_by_county_df`

---

# 2. Apply Home-Based Jobs (HBJ) (Notebook: **1b**)

### **Purpose**

Allocate total employment into **HBJ**, **NONHBJ**, and validate totals against base data.

### **Key Steps**

- Load employment data from Notebook 1a.
- Load HBJ percent allocation table.
- Compute:
  - `HBJ = Employment × PercentHBJ`
  - `NONHBJ = Employment − HBJ`
- Validate:  
  Compare `EMPCOUNT_BEFORE_HBJ` vs. `TOTAL_AFTER_HBJ`
- Output:  
  `tdm_employment_by_county_df`

---

# 3. Process Population Data (2025+) (Notebook: **2a**)

### **Purpose**

Convert GPI population projections into a unified age-group format for years 2025 and beyond.

### **Key Steps**

- Load population data for 2025+.
- Normalize fields and formats.
- Reshape into long format.
- Create standard age groups:
  - **0–17**
  - **18–64**
  - **65+**
- Validate subtotals = totals.
- Output:  
  `gpi_population_2025plus_df`

---

# 4. Process 2023 Population Data (Notebook: **2b**)

### **Purpose**

Align the differently formatted 2023 GPI population data with the 2025+ schema.

### **Key Steps**

- Load 2023 population tables.
- Standardize fields.
- Compute same three age groups as in Notebook 2a.
- Produce fully compatible dataset for merging.
- Output:  
  `gpi_population_2023_df`

---

# 5. Split Box Elder & Weber Counties (Notebook: **3**)

### **Purpose**

Apply model-area split rules to counties that are subdivided for the travel demand model.

### **Key Steps**

- Load county split percentages (e.g., WFRC share of Weber County).
- Melt split tables into long form:
  - `COUNTY, YEAR, CATEGORY, MODEL, PERCENT`
- Join percentages to employment and population.
- For each value:
  - If split exists → `value × percent`
  - Else → full value.
- Validate:  
  Sum(model-area splits) = original county totals.
- Outputs:
  - `employment_split_df`
  - `population_split_df`

---

# 6. Finalize Combined SE Data (Notebook: **4**)

### **Purpose**

Merge all intermediate datasets and prepare final model-ready SE data.

### **Key Steps**

- Load all processed datasets:
  - Employment (with HBJ)
  - Split employment
  - Population 2023 + 2025+
  - Split population
  - County names/metadata
- Merge into a single long-format dataset:  
  **CO_FIPS × YEAR × VARIABLE × VALUE**
- Add derived metrics (HH size, per-capita values, etc.).
- Pivot and aggregate for dashboards and modeling.
- Run quality checks.
- Output:
  - `se_final_df`
  - Dashboard pivot tables
  - Modeling input files

---

# 📤 Final Outputs

### **Employment**

- `gpi_employment_by_county_df`
- `tdm_employment_by_county_df`
- `employment_split_df`

### **Population**

- `gpi_population_2023_df`
- `gpi_population_2025plus_df`
- `population_split_df`

### **Final Model Files**

- `se_final_df`
- Dashboard-ready pivot tables
- TDM socio-economic inputs

---

# 📊 Workflow Diagram (Text)
