import json
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / "data" / "hbtu_data.json"


def load_data() -> dict:
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def build_context(data: dict) -> str:
    """
    Converts the HBTU JSON into plain text so the LLM can understand it.
    """
    lines = []

    u = data["university"]
    lines.append(f"University: {u['name']} ({u['short_name']}), {u['location']}")
    lines.append(f"Vice Chancellor: {u['vice_chancellor']}")
    lines.append(f"NAAC Grade: {u['naac_grade']}")
    lines.append(f"About: {u['about']}\n")

    lines.append("=== DEPARTMENTS ===")
    for dept in data["departments"]:
        lines.append(f"\nDepartment: {dept['name']} ({dept.get('short', '')})")
        lines.append(f"  School: {dept['school']}")
        lines.append(f"  Building: {dept['building']}, {dept['floor']}")
        lines.append(f"  Location: {dept.get('location_note', '')}")
        lines.append(f"  Programs: {', '.join(dept.get('programs', []))}")

        hod = dept.get("hod", {})
        lines.append(f"  HOD: {hod.get('name', 'N/A')} | Cabin: {hod.get('cabin', 'N/A')}")

        for f in dept.get("faculty", []):
            cabin = f.get("cabin", "N/A")
            role = f" ({f['role']})" if f.get("role") else ""
            lines.append(f"  Faculty: {f['name']} | {f['designation']}{role} | Cabin: {cabin}")

    lines.append("\n=== CAMPUS FACILITIES ===")
    for fac in data["facilities"]:
        lines.append(f"\n{fac['name']} [{fac['type']}]")
        lines.append(f"  Location: {fac['location']}")
        if fac.get("timings"):
            lines.append(f"  Timings: {fac['timings']}")
        if fac.get("services"):
            lines.append(f"  Services: {', '.join(fac['services'])}")
        if fac.get("note"):
            lines.append(f"  Note: {fac['note']}")

    lines.append("\n=== KEY OFFICES ===")
    for office in data["key_offices"]:
        lines.append(f"{office['name']}: {office['person']} — {office['location']}")

    lines.append("\n=== ADMISSIONS ===")
    adm = data["admissions"]
    lines.append(f"B.Tech: {adm['btech']}")
    lines.append(f"M.Tech/MBA/MCA: {adm['mtech_mba_mca']}")
    lines.append(f"Ph.D: {adm['phd']}")
    lines.append(f"Admission Portal: {adm['portal']}")

    lines.append("\n=== ERP PORTALS ===")
    erp = data["erp"]
    lines.append(f"Student Login: {erp['student_login']}")
    lines.append(f"Faculty Login: {erp['faculty_login']}")
    lines.append(f"Alumni Portal: {erp['alumni']}")

    return "\n".join(lines)
