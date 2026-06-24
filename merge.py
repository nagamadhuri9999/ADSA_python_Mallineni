import pandas as pd
import os

base_dir = r"c:\Users\Venkatesh\Desktop\MalliNeni"
files_to_merge = [
    os.path.join(base_dir, "service_companies_greedy_prep.csv"),
    os.path.join(base_dir, "service_companies_greedy_100_more.csv"),
    os.path.join(base_dir, "service_companies_greedy_100_even_more.csv"),
    os.path.join(base_dir, "complete_dsa_curriculum_company_questions.csv"),
    os.path.join(base_dir, "Day18", "30_day_greedy_study_plan.csv"),
    os.path.join(base_dir, "Day18", "daywise_company_greedy_problems.csv"),
    os.path.join(base_dir, "Day18", "leetcode_greedy_company_questions.csv"),
    os.path.join(base_dir, "Day18", "leetcode_greedy_company_questions_part2.csv"),
]

# Write to Excel
excel_path = os.path.join(base_dir, "Master_Placement_Prep.xlsx")
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for f in files_to_merge:
        if os.path.exists(f):
            # some CSVs might have different encodings, handle it if needed
            df = pd.read_csv(f, encoding='utf-8', encoding_errors='ignore')
            # Create a short sheet name (max 31 chars)
            sheet_name = os.path.basename(f).replace('.csv', '')[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Added {sheet_name} to excel.")

# If successful, delete the old CSVs
if os.path.exists(excel_path):
    print("Excel created. Removing original CSVs...")
    for f in files_to_merge:
        if os.path.exists(f):
            os.remove(f)
            print(f"Removed {os.path.basename(f)}")
print("Done!")
