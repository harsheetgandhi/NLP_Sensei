#!/bin/bash

# 1. Create the root level files
touch README.md .gitignore requirements.txt setup_repo.sh

# 2. Create the 14-week folder structure

# Phase 1: Core Fundamentals
mkdir -p week01_embeddings/{day01_02_theory,day03_04_code,day05_06_test}
touch week01_embeddings/day07_summary_README.md

mkdir -p week02_lm/{day08_09_theory,day10_11_code,day12_13_test}
touch week02_lm/day14_summary_README.md

mkdir -p week03_attention/{day15_16_theory,day17_18_code,day19_20_test}
touch week03_attention/day21_summary_README.md

mkdir -p week04_transfer/{day22_23_theory,day24_25_code,day26_27_test}
touch week04_transfer/day28_summary_README.md

# Phase 2: The LLM Revolution
mkdir -p week05_llm/{day29_30_theory,day31_33_code_test}
touch week05_llm/day34_35_summary_README.md

mkdir -p week06_prompting/{day36_37_theory,day38_40_code_test}
touch week06_prompting/day41_42_summary_README.md

mkdir -p week07_finetuning/{day43_44_theory,day45_47_code_test}
touch week07_finetuning/day48_49_summary_README.md

mkdir -p week08_efficiency/{day50_51_theory,day52_54_code_test}
touch week08_efficiency/day55_56_summary_README.md

# Phase 3: Advanced Systems & Production
mkdir -p week09_retrieval/{day57_58_theory,day59_61_code_test}
touch week09_retrieval/day62_63_summary_README.md

mkdir -p week10_agents/{day64_65_theory,day66_68_code_test}
touch week10_agents/day69_70_summary_README.md

mkdir -p week11_interpretability/{day71_72_theory,day73_74_code_test}
touch week11_interpretability/day75_summary_README.md

mkdir -p week12_multimodal/{day76_77_theory,day78_79_code}
touch week12_multimodal/day80_summary_README.md

mkdir -p week13_llm_systems/{day81_82_theory,day83_84_code}
touch week13_llm_systems/day85_summary_README.md

mkdir -p week14_agents_production/{day86_87_theory,day88_89_project,day90_final_repo_polish}

# 3. Add .gitkeep to all empty directories so Git tracks them
find . -type d -empty -exec touch {}/.gitkeep \;

echo "✅ NLP_Sensei 90-Day folder structure with .gitkeep files created successfully!"