import json
from pathlib import Path

CATEGORY_MAP = {
    'Title': '# {}',
    'Section-header': '## {}',
    'Text': '{}',
    'Formula': '{}',
}

def format_json_to_md(source_dir):
    source_path = Path(source_dir)
    json_files = list(source_path.glob("*.json"))

    current_md_file = None
    current_md_content = []

    for json_file in json_files:
        data = json.loads(json_file.read_text(encoding='utf-8'))

        for item in data:
            category = item['category']
            text = item['text']

            if category == 'Page-header':
                if current_md_file:
                    current_md_file.write_text('\n'.join(current_md_content), encoding='utf-8')
                safe_filename = "".join(c for c in text if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
                current_md_file = source_path / f"{safe_filename}.md"
                current_md_content = []
            elif category in CATEGORY_MAP:
                current_md_content.append(CATEGORY_MAP[category].format(text) + '\n')

    if current_md_file:
        current_md_file.write_text('\n'.join(current_md_content), encoding='utf-8')


if __name__ == "__main__":
    format_json_to_md(r"D:\Download\math.tar.gz\mocr\elliptic_eq")
