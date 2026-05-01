# P-Reinforce RL Policy

## 🧠 Reward Function ($R$)
$$R = w_1(\text{Categorization Accuracy}) + w_2(\text{Graph Connectivity}) + w_3(\text{User Satisfaction})$$

### Current Weights
- **$w_1$ (Accuracy)**: 0.5
- **$w_2$ (Connectivity)**: 0.3
- **$w_3$ (Satisfaction)**: 0.2

## 📂 Classification Rules
- **Similarity Threshold**: 85%
  - > 85%: Place in existing category.
  - < 85%: Propose new category or place in top-level `Topics/`.
- **Refactoring Trigger**: 12 files in a single folder.
  - Action: Propose sub-categorization.

## 🤝 User Feedback Loop
- **Praise**: Increases $w_1$ and $w_3$ confidence for the specific path.
- **Manual Move**: Decreases $w_1$ for the previous path, updates semantic center for the new path.
- **Edit**: Updates the "extracted pattern" in the Wiki template.

## 🛠️ Update History
- 2026-04-21: Initial policy established.
