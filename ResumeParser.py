import json
from collections import defaultdict
from docx import Document

def parse_resume_to_json(doc_path):
    doc = Document(doc_path)
    resume_text = "\n".join([para.text for para in doc.paragraphs])
    resume_dict = defaultdict(list)
    sections = ["Education", "Experience", "Skills", "Projects", "Certifications", "Awards", "Languages", "Interests"]
    lines = resume_text.split('\n')

    current_section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if any(section in line for section in sections):
            current_section = line.strip()
        elif current_section:
            resume_dict[current_section].append(line)
    resume_json = dict(resume_dict)

    return resume_json
doc_path = 'John Doe.docx'
resume_json = parse_resume_to_json(doc_path)
print(json.dumps(resume_json, indent=4))
