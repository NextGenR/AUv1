import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

raw_path = Path("Raw_questions_CAVA/MSME_all_questions.json")
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# The curated best question IDs (representing the cream of all 8 modules)
selected_ids = [
    # Module 1: Macro & Data
    "MSME_001", "MSME_002", "MSME_003", "MSME_004", "MSME_009", "MSME_014",
    # Module 2: Theoretical & Structural
    "MSME_026", "MSME_028", "MSME_032", "MSME_035", "MSME_038",
    # Module 3: Statutory & Classification
    "MSME_051", "MSME_053", "MSME_056", "MSME_058", "MSME_062", "MSME_065",
    # Module 4: Delayed Payments & 43B(h)
    "MSME_076", "MSME_077", "MSME_079", "MSME_082", "MSME_085", "MSME_087", "MSME_092",
    # Module 5: Budget 2025-26 & Credit
    "MSME_101", "MSME_103", "MSME_106", "MSME_110", "MSME_115", "MSME_118",
    # Module 6: PM Vishwakarma & Udyam
    "MSME_126", "MSME_128", "MSME_133", "MSME_138",
    # Module 7: Schemes & Procurement
    "MSME_151", "MSME_154", "MSME_158", "MSME_162", "MSME_166",
    # Module 8: Views & Case Studies
    "MSME_176", "MSME_180", "MSME_185", "MSME_192", "MSME_198"
]

all_questions_by_id = {q["id"]: q for q in raw_data["questions"]}

# Mapping to relevant flowcharts
flowchart_mapping = {
    "flowchart_msme_classification.svg": [
        "MSME_002", "MSME_004", "MSME_051", "MSME_053", "MSME_056", "MSME_058", "MSME_062"
    ],
    "flowchart_delayed_payments.svg": [
        "MSME_076", "MSME_077", "MSME_079", "MSME_082", "MSME_085", "MSME_087", "MSME_092"
    ],
    "flowchart_pm_vishwakarma.svg": [
        "MSME_126", "MSME_128", "MSME_133", "MSME_138"
    ],
    "flowchart_dwarfism_vs_mittelstand.svg": [
        "MSME_026", "MSME_028", "MSME_032", "MSME_035", "MSME_038", "MSME_176", "MSME_180", "MSME_185"
    ]
}

filtered_questions = []
for qid in selected_ids:
    if qid in all_questions_by_id:
        q_item = dict(all_questions_by_id[qid])
        
        # Attach matching flowchart
        matching_fc = None
        for fc_file, q_list in flowchart_mapping.items():
            if qid in q_list:
                matching_fc = fc_file
                break
        q_item["associated_flowchart"] = matching_fc
        filtered_questions.append(q_item)

output_data = {
    "title": "MSME Reforms, Framework & Policy Architecture - Curated Best Questions",
    "total_filtered_questions": len(filtered_questions),
    "description": "High-yield curated questions for UPSC Prelims & Mains from ForumIAS notes, Mindmap and Budget 2025-26, mapped to visual flowcharts.",
    "flowcharts": [
        {
            "filename": "flowchart_msme_classification.svg",
            "title": "Composite Classification Framework & 2.5x Multiplier",
            "description": "Visual breakdown of Investment & Turnover ceilings (1/5, 10/50, 50/250) and export turnover exclusion."
        },
        {
            "filename": "flowchart_delayed_payments.svg",
            "title": "Delayed Payments & Section 43B(h) Workflow",
            "description": "Sections 15-19 MSMED Act, 3x RBI Bank Rate compounding, MSEFC 90-day arbitrations, and 45-day tax deductibility."
        },
        {
            "filename": "flowchart_pm_vishwakarma.svg",
            "title": "PM Vishwakarma 5-Pillar Scheme Architecture",
            "description": "₹13,000 Cr outlay, 18 trades, ₹15k toolkit, and ₹1L + ₹2L collateral-free credit at 5% interest."
        },
        {
            "filename": "flowchart_dwarfism_vs_mittelstand.svg",
            "title": "Dwarfism & Missing Middle vs. German Mittelstand",
            "description": "Inverted pyramid vs. high-productivity Mittelstand model and structural transition pathways."
        }
    ],
    "questions": filtered_questions
}

# Write out to all 3 destination paths
destinations = [
    Path("Filtered_Questions/MSME_best_questions.json"),
    Path("Filtered Questions/MSME_best_questions.json"),
    Path("Raw_questions_CAVA/Filtered_questions/MSME_best_questions.json")
]

for d in destinations:
    d.parent.mkdir(parents=True, exist_ok=True)
    with open(d, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(filtered_questions)} best questions to {d}")

