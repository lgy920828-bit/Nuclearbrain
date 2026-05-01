import os
import json
import uuid
import datetime
import subprocess
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "00_Raw"
WIKI_DIR = BASE_DIR / "10_Wiki"
META_DIR = BASE_DIR / "20_Meta"
POLICY_FILE = META_DIR / "Policy.md"
GRAPH_FILE = META_DIR / "Graph.json"
INDEX_FILE = META_DIR / "Index.md"
GIT_PATH = r"C:\Program Files\Git\bin\git.exe"

class PReinforceEngine:
    def __init__(self):
        self.load_metadata()

    def load_metadata(self):
        with open(GRAPH_FILE, "r", encoding="utf-8-sig") as f:
            self.graph = json.load(f)
        
    def save_metadata(self):
        with open(GRAPH_FILE, "w", encoding="utf-8-sig") as f:
            json.dump(self.graph, f, indent=2, ensure_ascii=False)

    def git_sync(self, message):
        try:
            subprocess.run([GIT_PATH, "add", "."], cwd=BASE_DIR, check=True)
            subprocess.run([GIT_PATH, "commit", "-m", f"[P-Reinforce] {message}"], cwd=BASE_DIR, check=True)
            subprocess.run([GIT_PATH, "push", "origin", "main"], cwd=BASE_DIR, check=True)
            print(f"Git Sync Successful: {message}")
        except Exception as e:
            print(f"Git Sync Failed: {e}")

    def generate_wiki_template(self, data):
        template = f"""---
id: {data.get('id', uuid.uuid4())}
category: "[[{data.get('category_path', '10_Wiki/Topics')}]]"
confidence_score: {data.get('confidence', 0.9)}
tags: {data.get('tags', [])}
last_reinforced: {datetime.date.today().isoformat()}
github_commit: "TBD"
---

# [[{data.get('title', 'Untitled')}]]

## 📌 한 줄 통찰 (The Karpathy Summary)
> {data.get('summary', '핵심 요약이 필요합니다.')}

## 📖 구조화된 지식 (Synthesized Content)
- **추출된 패턴:** {data.get('pattern', '발견된 패턴이 없습니다.')}
- **세부 내용:** 
{data.get('content', '- 정보가 비어있습니다.')}

## ⚠️ 모순 및 업데이트 (Contradictions & RL Update)
- **과거 데이터와의 충돌:** {data.get('contradiction', '없음')}
- **정책 변화:** {data.get('policy_change', '기존 정책 유지')}

## 🔗 지식 연결 (Graph)
- **Parent:** [[{data.get('parent', '10_Wiki/Index')}]]
- **Related:** {', '.join([f'[[{r}]]' for r in data.get('related', [])])}
- **Raw Source:** [[{data.get('raw_source', '')}]]
"""
        return template

    def update_index(self):
        # basic index update logic (listing folders)
        content = "# P-Reinforce Knowledge Index\n\n## 🗺️ 지식 지형도 (ToC)\n\n"
        for folder in ["Projects", "Topics", "Decisions", "Skills"]:
            path = WIKI_DIR / folder
            content += f"### [{folder}](file:///{path.as_posix()})\n"
            files = list(path.glob("**/*.md"))
            if not files:
                content += "- (비어 있음)\n"
            for f in files:
                content += f"- [[{f.stem}]]\n"
            content += "\n"
        
        with open(INDEX_FILE, "w", encoding="utf-8-sig") as f:
            f.write(content)

    def process_new_raw_files(self):
        # Scan 00_Raw for .md files not already in Graph.json
        processed_sources = {node['raw_source'] for node in self.graph['nodes'] if 'raw_source' in node}
        
        raw_files = list(RAW_DIR.glob("**/*.md"))
        new_files = [f for f in raw_files if str(f.relative_to(BASE_DIR)) not in processed_sources]
        
        if not new_files:
            print("처리할 새로운 원시 데이터가 없습니다.")
            return

        print(f"SEARCH: {len(new_files)}개의 새로운 데이터 발견.")
        for rf in new_files:
            print(f"FILE: 처리 중: {rf.name}")
            # In a real scenario, this is where the LLM (Antigravity) would take over.
            # For this script, we'll mark them as "Pending AI Reinforcement"
            # Or Antigravity can call this script after manually processing.

if __name__ == "__main__":
    engine = PReinforceEngine()
    engine.process_new_raw_files()
    engine.update_index()
