# 🧠 P-Reinforce: The Autonomous Gardener 🌿

> **"지식의 중력을 거스르는 자율형 지식 자동화 엔진"**
>
> P-Reinforce는 Andre Karpathy의 LLM-Wiki 아키텍처와 강화학습(RL) 이론을 결합한 지식 구조화 시스템입니다. 파편화된 데이터로부터 패턴을 추출하고, 스스로 지식의 정원을 가꾸며 거대한 '외부 뇌'를 형성합니다.

---

## 🚀 Key Features

| 기능 | 설명 |
| :--- | :--- |
| **🤖 자율 구조화** | LLM이 데이터의 맥락을 분석하여 스스로 최적의 폴더 트리를 설계하고 배치합니다. |
| **📈 강화학습(RL) 최적화** | 사용자 피드백을 보상(Reward)으로 삼아 지식 분류 정책을 지속적으로 정교화합니다. |
| **🔗 지식 그래프 구축** | 문서 간 쌍방향 링크를 자동 생성하여 파편화된 정보를 연결된 지식 체계로 변환합니다. |
| **🔄 GitHub 자동 동기화** | 모든 지식의 변화를 실시간으로 추적하고 GitHub 저장소에 안전하게 보존합니다. |

---

## 📂 System Architecture

### 📁 Folder Structure
에이전트가 관리하는 표준 위계 구조입니다.

- **`00_Raw/`** `[불변]`
  - 사용자로부터 입력된 가공되지 않은 모든 데이터 (Source of Truth)
- **`10_Wiki/`** `[자율 가드닝]`
  - **`🛠️ Projects`**: 목표 중심의 프로젝트별 요약 및 진행 상황
  - **`💡 Topics`**: 개념 중심 분류 (지능적으로 자동 확장)
  - **`⚖️ Decisions`**: 주요 판단 및 의사결정 기록
  - **`🚀 Skills`**: 반복 가능한 실행 패턴 및 워크플로우
- **`20_Meta/`** `[시스템 엔진]`
  - `Graph.json`: 지식 간의 연결망 데이터
  - `Policy.md`: RL 보상 기반의 분류 정책 가이드

---

## ⚙️ How It Works

1. **상태 분석 (State)**: `10_Wiki/` 구조와 `Graph.json`을 읽어 현재 지식 지형을 파악합니다.
2. **분류 및 폴더링 (Action)**: 유사도 분석을 통해 기존 폴더에 배치하거나 새로운 카테고리를 생성합니다.
3. **지식 합성 (Synthesis)**: Karpathy Style 템플릿에 맞춰 핵심 통찰을 추출하고 관련 지식을 링크합니다.
4. **보상 및 학습 (Reward)**: 사용자의 수정 사항을 학습하여 `Policy.md`의 분류 기준을 강화합니다.

---

## 🛠️ Usage Guide

### 1. 지식 투입 (Input)
새로운 메모, 스크랩, 데이터는 `00_Raw/` 폴더에 넣어주세요. 에이전트가 자동으로 감지합니다.

### 2. 엔진 실행 (Run)
```bash
python reinforce.py
```

### 3. 자율 관리 (Auto-Pilot)
에이전트(Antigravity)가 내용을 분석하여 Wiki를 생성하고 링크를 연결한 뒤, GitHub에 자동으로 커밋합니다.

---

## 📝 Wiki Document Protocol
모든 문서는 엄격한 규격을 준수하여 지식의 밀도를 유지합니다.

*   **The Karpathy Summary**: 핵심을 꿰뚫는 한 줄 통찰
*   **Synthesized Content**: 추출된 패턴과 세부 내용 정리
*   **Knowledge Graph**: 상위/연관 개념의 맵핑 (쌍방향 링크)
*   **Confidence Score**: RL 알고리즘 기반의 분류 확신도 기록

---

<p align="center">
  <i>Created and Reinforcing by <b>Antigravity</b>.</i><br>
  <b>Empowering your external brain.</b>
</p>
