# TDM-INP-Socioeconomic-Control-Totals

_Note: This repository contains code and data for estimating county level socio-economic totals for the Wasatch Front Travel Demand Model (TDM). The current implementation applies to model version 10, while all previous calculations from version 8.3.2 and version 9x are stored in the \_archive folder for reference._

## Updated Process Documentation

This repository contains the full, updated workflow for processing socioeconomic (SE) inputs for travel demand modeling.  
The workflow has been revised to reflect the latest notebook structure and updated GPI inputs.

The process now follows these notebooks:

1. **1-Process-GPI-Employment-Data.ipynb**
2. **2a-Process-GPI-Population-Data-2025+.ipynb**
3. **2b-Process-GPI-Population-Data-2023-2024.ipynb**
4. **3-Split-Box-Elder-And-Weber-Counties.ipynb**
5. **4-Apply-Home-Based-Jobs.ipynb**
6. **5-Finalize.ipynb**

---

# 📌 Overview

The goal is to produce a consistent, validated, model-ready SE dataset covering employment and population across all Utah counties (including split counties used by WFRC, MAG, UDOT, etc.).  
This updated workflow normalizes GPI inputs, applies model splits, and allocates home-based jobs (HBJ), producing final control totals by county, year, and variable.

---

# 1. Employment Processing

### Notebook: **1-Process-GPI-Employment-Data.ipynb**

### **Purpose**

Load, clean, and standardize GPI employment inputs for all available years.

### **Key Steps**

- Load GPI employment extract (industry × county × year).
- Standardize column names, FIPS codes, year fields.
- Convert wide format to long.
- Join NAICS-to-TDM-sector crosswalk.
- Aggregate employment by:
  - **County**
  - **Year**
  - **TDM sector**
- Validate totals and industry roll-ups.

### **Output**

`employment_raw_df` – cleaned, consistent employment table for all years.

---

# 2. Population Processing (2025 and later)

### Notebook: **2a-Process-GPI-Population-Data-2025+.ipynb**

### **Purpose**

Process GPI population files for 2025+ using the newer unified format.

### **Key Steps**

- Load GPI population data beginning in 2025.
- Standardize fields and geographic identifiers.
- Build long-format table (County × Year × Age Group).
- Group GPI age groups into:
  - **0–17**
  - **18–64**
  - **65+**
- Validate that age-group totals sum to GPI’s total population.

### **Output**

`population_2025plus_df`

---

# 3. Population Processing (2023–2024)

### Notebook: **2b-Process-GPI-Population-Data-2023-2024.ipynb**

### **Purpose**

Process 2023–2024 population data, which requires extra steps because GPI’s formatting for these years differs from the 2025+ structure.

### **Key Points**

- GPI **did provide age-breakdown data for all years**, including 2023 and 2024.
- But **GPI did not provide 2023 and 2024 total population in the same format as the 2025+ files**.
- Therefore:
  - The **total population** for 2023–2024 is sourced from earlier GPI base files.
  - The **age distribution** for 2023–2024 uses the later GPI age-breakdown extract.
  - We apply age shares to the base totals so totals remain consistent with GPI’s official values.

### **Key Steps**

- Load 2023–2024 population tables from both:
  - Base GPI “official totals” file
  - Updated GPI “age by year” file
- Apply age shares to total population.
- Produce long-format tables consistent with 2025+ outputs.
- Validate roll-ups.

### **Output**

`population_2023_2024_df`

---

# 4. County Splitting (Box Elder & Weber)

### Notebook: **3-Split-Box-Elder-And-Weber-Counties.ipynb**

### **Purpose**

Apply model-area split percentages so Box Elder and Weber counties are divided into model-specific subgeographies.

### **Key Steps**

- Load county-split percentages (by category × year).
- Melt and join splits to both population and employment.
- If a split exists → `value × percent`.  
  Otherwise → use original county value.
- Ensure:
  - Sum(model-area values) = original county total.

### **Outputs**

- `population_split_df`
- `employment_split_df`

---

# 5. Apply Home-Based Jobs (HBJ)

### Notebook: **4-Apply-Home-Based-Jobs.ipynb**

### **Purpose**

Allocate employment into **HBJ** and **Non-HBJ** using RSG’s latest factors.

### **Key Steps**

- Load split employment dataset.
- Load HBJ percentages (provided by RSG).
- Compute:
  - `HBJ = Employment × HBJ_pct`
  - `NONHBJ = Employment - HBJ`
- Validate totals pre- and post-HBJ.

### **Output**

`employment_hbj_df`

---

# 6. Finalize Combined SE Dataset

### Notebook: **5-Finalize.ipynb**

### **Purpose**

Merge all processed datasets into final model-ready control totals.

### **Key Steps**

- Merge:
  - Employment (with HBJ)
  - Population (2023–2024 + 2025+)
  - Split geographies
  - County metadata
- Produce:
  - County- and model-area–level SE tables
  - Long-format (Year × County × Variable × Value)
  - Pivot tables for dashboards
- Run QA/QC checks (subtotals, splits, HBJ balance).

### **Final Outputs**

- `ControlTotal_SE_AllCounties.csv`
- Dashboard-friendly pivot tables
- Model input files

---

# 📊 Updated Workflow Diagram
