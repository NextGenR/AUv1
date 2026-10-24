"""
Assembly and validation script to generate MSME_all_questions.json containing 200 questions
strictly derived from the provided MSME notes.
"""

import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

import msme_module_1
import msme_module_2
import msme_module_3
import msme_module_4
import msme_module_5
import msme_module_6
import msme_module_7
import msme_module_8

def main():
    modules = [
        ("Module 1: Macro Architecture & Data", msme_module_1.get_questions),
        ("Module 2: Core Economic Concepts & Theoretical Paradigms", msme_module_2.get_questions),
        ("Module 3: Statutory Framework & Classification Limits", msme_module_3.get_questions),
        ("Module 4: Delayed Payments & Dispute Resolution", msme_module_4.get_questions),
        ("Module 5: Union Budget 2025-26 & Credit Reforms", msme_module_5.get_questions),
        ("Module 6: PM Vishwakarma, Udyam & UAP", msme_module_6.get_questions),
        ("Module 7: PMEGP, SFURTI & Public Procurement Policy", msme_module_7.get_questions),
        ("Module 8: Expert Views, Academic Studies & Case Studies", msme_module_8.get_questions),
    ]

    all_questions = []
    seen_ids = set()

    for mod_name, get_fn in modules:
        qs = get_fn()
        print(f"Loaded {len(qs)} questions from {mod_name}")
        for q in qs:
            qid = q["id"]
            if qid in seen_ids:
                raise ValueError(f"Duplicate Question ID detected: {qid}")
            seen_ids.add(qid)

            # Validate options
            opts = q.get("options", {})
            for key in ["A", "B", "C", "D"]:
                if key not in opts or not opts[key]:
                    raise ValueError(f"Missing option {key} in question {qid}")

            # Validate correct option
            corr = q.get("correct_option")
            if corr not in ["A", "B", "C", "D"]:
                raise ValueError(f"Invalid correct_option '{corr}' in question {qid}")

            # Validate explanation
            if not q.get("explanation"):
                raise ValueError(f"Empty explanation in question {qid}")

            all_questions.append(q)

    total_count = len(all_questions)
    print(f"\nTotal Validated Questions: {total_count}")
    if total_count != 200:
        raise ValueError(f"Expected 200 questions, got {total_count}")

    output_data = {
        "chapter": "Micro, Small and Medium Enterprises (MSME)",
        "total_questions": total_count,
        "source_materials": [
            "ForumIAS Current Affairs Classes: MSMEs as catalysts (Ashok Chandra)",
            "Mindmap Notes: MSME Sector Framework, Concepts, Views, Studies & Case Studies",
            "PIB Delhi: Ministry of MSME - Budget 2025-26: Fuelling MSME Expansion"
        ],
        "modules_breakdown": {
            "Module 1 (Q1-Q25)": "Macro Architecture, Significance & Benchmark Data",
            "Module 2 (Q26-Q50)": "Core Economic Concepts & Theoretical Paradigms",
            "Module 3 (Q51-Q75)": "Statutory Framework, MSMED Act & Classification Limits",
            "Module 4 (Q76-Q100)": "Delayed Payments, Dispute Resolution & Section 43B(h)",
            "Module 5 (Q101-Q125)": "Union Budget 2025-26 & Credit Reforms",
            "Module 6 (Q126-Q150)": "PM Vishwakarma, Udyam Registration & UAP",
            "Module 7 (Q151-Q175)": "PMEGP, SFURTI, Public Procurement & RAMP",
            "Module 8 (Q176-Q200)": "Expert Views, Academic Studies, Case Studies & Strategic Roadmaps"
        },
        "questions": all_questions
    }

    output_path = r"d:\Anki_Upgraded\MSME_all_questions.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully generated: {output_path} ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    main()
