---
id: uuid-2026-0501-prompts-library
category: "[[10_Wiki/Skills]]"
confidence_score: 0.99
tags: [Prompts, JSON, Veo3, Midjourney, Nano_Banana]
last_reinforced: 2026-05-01
github_commit: "pending"
---

# [[실무자 황금 프롬프트 라이브러리]]

> **원문 출처**: [[00_Raw/디오 채팅방 정밀 추출본.md]]
> **연결 지식**: [[AI_Tools_Encyclopedia]], [[AI_Video_Semi_Automation_Workflow]]

아래는 제미나이의 의견 반영한 업무 단계별 실무 워크플로우와 채널 자동화/반자동화 노하우 구조야 

제공해주신 대화 기록(**nook ai 채팅방_7.txt**)을 7만 줄의 컨텍스트 끝까지 전수 조사하여, 실무자들이 공유한 **모든 프롬프트 원문(영어/한국어 명령어)**을 단 하나도 누락하지 않고 추출했습니다. 각 프롬프트가 어떤 AI 툴을 위한 것인지, 어떤 맥락에서 나온 결과물인지 상세한 설명을 덧붙여 정리해 드립니다[cite: 7].

---

## **1. 비디오 생성 및 물리 엔진 제어 프롬프트 (Google Veo3 / Vertex AI)**

대화방에서 가장 활발하게 공유된 영역으로, 주로 고도의 물리 법칙이나 립싱크, 시네마틱 전환을 구현하기 위해 사용되었습니다[cite: 7].

### **① 잉크 수중 번짐 로고 공개 (Mickey Mouse)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 'Koldo Huici'라는 작가의 영상을 기반으로 잉크가 물속에서 번지며 특정 실루엣을 만드는 기법을 공유함[cite: 7].
*   **결과물:** 검은 잉크 방울이 물속에서 퍼지며 미키 마우스 실루엣을 형성하는 마법 같은 연출[cite: 7].
```json
{
  "description": "Three drops of black ink fall gently into water — one large, followed by two smaller ones. As they bloom and expand in slow motion, their shapes naturally align into the iconic silhouette of Mickey Mouse: a large circle flanked by two smaller ones forming the ears. The ink swirls briefly, holding the silhouette in perfect balance. A soft shimmer of silver light passes through the liquid as the silhouette stabilizes, evoking wonder and childhood magic.",
  "style": "magical, iconic, poetic ink-in-water aesthetic",
  "camera": "top-down macro shot with slow zoom-out",
  "lighting": "soft ambient glow with subtle silver reflections",
  "environment": "clear water with gentle swirling motion",
  "elements": [
    "large black ink bloom (head)",
    "two small black ink blooms (ears)",
    "fluid merging into Mickey Mouse silhouette"
  ],
  "motion": {
    "type": "ink expansion and spatial alignment",
    "details": "three ink drops bloom and align into Mickey's iconic shape"
  },
  "ending": "the Mickey silhouette floats suspended in soft ink mist",
  "audio": {
    "voice_over": null,
    "music": "gentle orchestral sparkle, light piano and celesta",
    "sfx": "delicate ink ripple, soft swirl"
  },
  "text_overlay": null,
  "format": "16:9",
  "keywords": ["Disney", "Mickey Mouse", "ink", "magic", "logo reveal"]
}
```

### **② 잉크 수중 번짐 변형 (Snowman 캐릭터)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 위 미키 마우스 프롬프트를 'aiwithharu'님이 눈사람 버전으로 응용하여 공유함[cite: 7].
*   **결과물:** 잉크 방울이 겹쳐지며 통통한 눈사람이 되고, 목도리와 귀마개가 생성되는 연출[cite: 7].
```json
{
  "description": "Three drops of black ink fall gently into water — one large, one medium, and one small. As they bloom and expand in slow motion, their shapes naturally stack into the silhouette of a chubby snowman: a round base, plump middle, and small cute head. As the ink swirls, playful details emerge — two shiny round eyes, a tiny carrot-shaped orange ink swirl for the nose, and a dotted smile forming a cheerful mouth. A soft red-tinged ink ribbon spreads across the neck, resembling a cozy scarf, while two round ear-like wisps appear like fluffy earmuffs. The snowman wiggles slightly in the water, giving off a whimsical, childlike charm.",
  "style": "cute, magical, fairy-tale ink-in-water aesthetic",
  "camera": "top-down macro shot with a slow zoom-out",
  "lighting": "soft ambient glow with pastel reflections (pale blue, pink, silver)",
  "environment": "clear water with gentle swirling motion",
  "elements": [
    "large round ink bloom (bottom body)",
    "medium round ink bloom (torso)",
    "small round ink bloom (head)",
    "tiny ink dots (eyes and smile)",
    "orange swirl (carrot nose)",
    "red ribbon-like ink (scarf)",
    "earmuff-like ink wisps"
  ],
  "motion": {
    "type": "ink expansion with playful alignment",
    "details": "three blooms align into a snowman, then scarf, earmuffs, and face emerge as ink swirls"
  },
  "ending": "the cute snowman floats in soft pastel mist, glowing warmly like a friendly winter spirit",
  "audio": {
    "voice_over": null,
    "music": "gentle bell chimes with lighthearted piano and celesta",
    "sfx": "soft bubbling ink swirl, tiny sparkle"
  },
  "text_overlay": null,
  "format": "16:9",
  "keywords": ["snowman", "cute", "ink", "magic", "winter", "fairy tale", "logo reveal"]
}
```

### **③ 스케치 일러스트의 실사 음식 변환 (Shrimp Tempura Udon)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 종이에 그려진 그림이 실물로 튀어나오는 연출을 위해 'hyjinlee1'님이 공유함[cite: 7].
*   **결과물:** 수채화 연필로 그린 새우튀김 우동 그림이 출렁이며 3D 실물 음식으로 변하는 과정[cite: 7].
```text
Drawn colored-pencil sketch on white drawing paper transforms into real, mouthwatering food. A hand finishes the last strokes of a shrimp tempura udon illustration, the pigment textures shimmering. The pencil lines begin to ripple and lift off the page, seamlessly morphing from 2D to hyperreal 3D: golden, ultra-crispy tempura shrimp with airy batter pockets, glossy udon noodles with bounce, rich amber broth with tiny oil droplets, rising steam curls, chopped scallions, and a slice of kamaboko. The bowl “pops out” of the paper and lands on the desk, photoreal and inviting. Cinematic macro close-up, shallow depth of field, soft natural window light, gentle parallax push-in, subtle steam and specular highlights on the broth. High-detail texture fidelity, zero uncanny artifacts. Smooth, magical paper-to-reality transition. Warm food styling, studio cleanliness, appetizing color grading. 24 fps, 6–8 seconds, 4K, aspect 16:9. Negative prompts: cartoonish, plastic-looking, over-saturated, waxy textures, messy desk, hands blocking the view, motion blur, jitter, low-res, duplicate shrimp, bent chopsticks, soggy tempura. 
```

### **④ 스케치 일러스트의 실사 음식 변환 (Wagyu Omakase)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 위 우동 프롬프트의 '와규' 버전으로, 동일한 전환 효과를 노린 프롬프트임[cite: 7].
*   **결과물:** 종이 위의 와규 플래터 그림이 실제 육즙이 흐르는 3D 스테이크 세트로 변환[cite: 7].
```text
Colored-pencil sketch on white drawing paper turns into real, luxurious wagyu omakase with side dishes. A hand finishes the last strokes of a premium wagyu platter illustration: glossy marbling, delicate nigiri, aburi torched edges, and petite side dishes. The pencil pigments glimmer, paper fibers ripple, and the drawing lifts off the page, seamlessly morphing from 2D to hyperreal 3D: seared wagyu slices with intricate marbling and juicy sheen, wagyu nigiri with a gentle aburi torch kiss, tataki with sesame and scallion, a mini sukiyaki bite with egg gloss, plus elegant side dishes—seasonal banchan, kimchi, pickled radish, seaweed salad, yuzu pickles, and a tiny bowl of clear broth. Steam curls, micro oil highlights, a soft sizzle, and a quick torch flare. The full set “pops out” of the paper and lands on the clean wooden desk, perfectly plated and photoreal. Cinematic macro close-up, shallow depth of field, soft natural window light, gentle parallax push-in, crisp texture fidelity, zero uncanny artifacts. Warm high-end food styling, studio cleanliness, appetizing color grading. 24 fps, 6–8 seconds, 4K, aspect 16:9. Negative prompts: cartoonish, plastic-looking, waxy fat, oversaturated reds, messy desk, motion blur, jitter, duplicate plates, bent chopsticks, overcooked meat, greasy puddles, low-res, harsh neon lighting.
```

### **⑤ 스케치 일러스트의 실사 음식 변환 (Hamburger)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** '리도:엔지니어'님이 음식을 바꿔가며 테스트해 보라고 공유한 프롬프트임[cite: 7].
*   **결과물:** 수채화 연필 데스크 위에서 햄버거 스케치가 입체화되며 치즈가 늘어나는 3D 햄버거가 됨[cite: 7].
```text
Photorealistic cinematic short, aspect ratio 16:9. A single continuous shot, slightly angled top-down view of a wooden artist’s desk cluttered with watercolor pencils, an ink pen, a jar of water with a brush, a steaming white ceramic coffee mug, and a small succulent. Warm desk lamp glow with cozy shadows. An artist’s hand is sketching a juicy hamburger in an open sketchbook. The pencil halts mid-line. The hamburger sketch ripples and glows, lines bulging upward. Colors bloom: soft bun texture, fresh lettuce green, bright tomato red, melted cheese yellow. The sketch inflates into a 3D, freshly made hamburger sitting atop the sketchbook. Steam rises, cheese stretches slightly, sesame seeds glint under the lamplight. Magical realism atmosphere, whimsical and intimate, slow subtle push-in camera movement. Gentle playful piano and harp accents with subtle sizzling and sparkling chime sound effects.
```

### **⑥ iPhone 17 가상 광고 (Futurebound)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 디오님이 애플 특유의 미니멀리즘 제품 공개 연출을 위해 공유함[cite: 7].
*   **결과물:** 핑크/오렌지 리본이 로고를 형성하고, iPhone 17 실루엣이 나타나는 시네마틱 광고 영상[cite: 7].
```json
{
 "title": "Apple Event Promo - Futurebound iPhone 17 Reveal",
 "duration": "8s",
 "style": {
 "rendering": "cinematic, ultra-polished, minimalist",
 "color_palette": ["glowing orange", "warm pink", "deep black"],
 "motion": "fluid, elegant, futuristic, Apple aesthetic"
 },
 "scenes": [
 {
 "id": "scene1",
 "duration": "2s",
"description": "Black screen. A soft glowing pulse emerges, flowing orange and pink light ribbons appear, weaving gracefully across the screen.",
 "effects": [
 "ambient glow",
 "fluid ribbon morphing",
 "subtle reflection shimmer"
 ],
 "camera": {
 "movement": "slow zoom in",
 "focus": "center glow"
 }
 },
 {
 "id : "scene2",
 "duration": "3s",
"description": "The ribbons converge to form the glowing abstract Apple logo, identical to the invite style. Light flares softly accent the logo as it locks into place.",
 "effects": [
 "neon streak morph",
 "light bloom",
 "soft lens flare"
 ],
 "camera": {
 "movement": "orbit around logo",
 "angle": "slight tilt cinematic"
 }
 },
 {
 "id": "scene3",
 "duration": "3s",
"description": "The Apple logo emits a final light pulse. As the glow expands, it reveals the sleek silhouette of the iPhone 17 standing upright. The text 'iPhone 17' and 'Futurebound.' fade in with Apple’s clean typography.",
 "effects": [
 "glow transition reveal",
 "device silhouette shine",
 "minimalist text fade-in"
 ],
 "camera": {
 "movement": "smooth pull-back to reveal device + logo + text",
"focus": "iPhone 17 front and logo composition"
 }
 }
 ],
 "audio": {
 "music": "minimalist ambient electronic with soft build-up",
 "sfx": [
 "subtle whoosh as ribbons form",
 "chime as Apple logo completes",
 "deep ambient pulse as iPhone 17 is revealed"
 ]
 }
}
```

### **⑦ Fanta CF 가상 광고 (Desert to Party)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 디오님이 배경이 극적으로 변하는 광고 연출 기법을 보여주기 위해 공유함[cite: 7].
*   **결과물:** 사막에서 기어가던 사람이 판타를 마신 후 화려한 파티장으로 배경이 급변하는 연출[cite: 7].
```json
{
  "scene": [
    {
      "second": "0-2",
      "description": "A man crawls across a scorching desert, sweating and exhausted. The atmosphere is dry and dramatic."
    },
    {
      "second": "2-4",
      "description": "Suddenly, an ice-cold, bright orange Fanta bottle drops in front of him, landing in the sand with a refreshing fizz sound."
    },
    {
      "second": "4-6",
      "description": "The man grabs the bottle, cracks it open, and takes a long drink. His face lights up with relief."
    },
    {
      "second": "6-8",
      "description": "Instantly, the desert transforms into a vibrant, colorful party scene with music, laughter, and playful energy. Text overlay: 'Fanta — Color Your World.'"
    }
  ],
  "style": "Dramatic to playful transition, vibrant colors, high contrast, upbeat energy."
}
```

### **⑧ 귀멸의 칼날 치비 피규어 상호작용 (Tanjiro)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 디오님이 실제 사람의 손가락과 AI 캐릭터의 정교한 상호작용을 테스트하기 위해 공유함[cite: 7].
*   **결과물:** 사람 손가락이 다가오자 탄지로 치비 피규어가 반응하며 손을 뻗어 만지는 스톱모션 스타일 영상[cite: 7].
```json
{
  "character": {
    "description": "A super cute chibi figure with big round eyes, styled in anime fashion, sitting on a wooden surface with petals scattered around.",
    "pose": "sitting calmly with hands on knees",
    "expression": "happy and playful smile",
    "details": {
      "outfit": "green-and-black checkered cloak, dark pants",
      "props": "tiny sword placed beside"
    }
  },
  "interaction": {
    "object": "a realistic human hand and finger",
    "action_sequence": [
      "A human finger slowly enters the frame from the side.",
      "The finger gently reaches toward the small figure.",
      "The chibi figure notices and leans forward curiously.",
      "The figure lifts its tiny hand and playfully taps the finger.",
      "They continue to interact—pushing, touching, and playing with each other in a cute and organic way."
    ],
    "style": "organic, smooth motion with playful nuance"
  },
  "scene": {
    "setting": "wooden tabletop with soft petals scattered",
    "background": "warm bokeh blur with soft light",
    "lighting": "warm cinematic tone highlighting the figure and the hand"
  },
  "visuals": {
    "realism": {
      "hand": "highly realistic human skin texture",
      "character": "toy-like but expressive, with glossy eyes and smooth textures"
    },
    "motion": "continuous, no cuts, with gentle stop-motion-like charm"
  },
  "atmosphere": {
    "tone": "cute, heartwarming, and magical",
    "focus": "the contrast between the realistic finger and the tiny playful figure"
  }
}
```

### **⑨ 우주 오로라 캘리그래피 (Aurora REEDO)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** '리도:엔지니어'님이 밤하늘 오로라로 글자를 쓰는 정밀 제어를 위해 공유함[cite: 7].
*   **결과물:** 설산 위 밤하늘 오로라들이 소용돌이치며 'REEDO'라는 글자를 우주에 새기는 연출[cite: 7].
```json
{
  "production_company": "REEDO",
  "version": "Aurora Script",
  "prompt_structure": {
    "metadata": {
      "duration_seconds": 6,
      "fps": 24,
      "aspect_ratio": "21:9",
      "resolution": "8K",
      "style": "northern_lights_calligraphy"
    },
    "narrative_structure": {
      "story_beats": {
        "0.0-1.0s": { "description": "Night sky filled with faint aurora waves shimmering above snowy mountains" },
        "1.0-2.5s": { "description": "Aurora threads begin converging, swirling in calligraphic curves" },
        "2.5-4.0s": { "description": "The light ribbons twist in synchronicity, spelling REEDO across the sky in ethereal strokes" },
        "4.0-5.0s": { "description": "Stars brighten, anchoring each letter with celestial sparkle" },
        "5.0-6.0s": { "description": "Aurora fades softly, leaving the word faintly glowing among constellations" }
      }
    },
    "prompt_output": "A northern light dance that becomes handwriting in the cosmos — REEDO appears like the universe itself tracing letters in aurora."
  }
}
```

### **⑩ 포켓몬 테마 방 전환 (Pokeball Bedroom)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** '이연화'님이 텅 빈 방이 특정 테마로 순식간에 채워지는 마법 같은 전환을 위해 공유함[cite: 7].
*   **결과물:** 포켓볼이 폭발하며 피카츄 인형, 침구류 등이 날아와 빈 침실을 포켓몬 테마로 꾸미는 장면[cite: 7].
```text
Photorealistic, cinematic shot of a single empty bedroom with hardwood floors, soft warm daylight streaming through a large window. Camera is fixed in a wide, front-facing angle with zero movement.
In the center of the empty room sits a sealed Pokéball. Suddenly, with a magical burst of light and energy, the Pokéball explodes open. Pokémon plushies (like Pikachu, Bulbasaur, Charmander), themed bedding, a Pokéball rug, shelves, wall art, and gaming accessories fly out and rapidly assemble into place-transforming the bare room into a cozy, vibrant Pokémon-themed bedroom.
Throughout, the structure of the room, the window, the walls, and the camera angle never change. Warm natural daylight blends with subtle magical accent lighting as the transformation completes.
Magical sparkles and energy effects fill the scene as all items animate out of the Pokéball and assemble into place, all in one continuous, seamless shot with no jump cuts or camera movement.
No text anywhere.
Ending: The room is now a fully decorated, joyful Pokémon bedroom glowing with colorful, magical energy.
Keywords: 16:9, Pokémon, Pokéball, seamless magical transformation, no jump cut, continuous shot, photorealistic, warm daylight.
```

### **⑪ 이끼 위 덩굴 구두 생성 (High-heeled Shoe)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 'aiwithharu'님이 자연물이 사물로 변하는 초현실적 연출을 위해 공유함[cite: 7].
*   **결과물:** 맨발이 이끼를 밟으면 흰 꽃과 덩굴이 자라나 우아한 하이힐을 완성하는 마법 같은 과정[cite: 7].
```text
Description: A barefoot gently steps onto fresh green moss. As the foot presses down, delicate white flowers and green vines sprout and wrap around the foot. The vines curl upward and weave firmly into the elegant shape of a high-heeled shoe made of living vines, moss, and blossoms. The transformation is smooth and enchanting, like nature itself is crafting footwear. In the final frame, the high-heel shoe shape remains fixed to the foot, complete and stable.

Style: Cinematic, hyper-realistic, magical realism
Camera: Slow push-in and side tracking shots, showing toes touching moss, then following vines forming the high-heel shape
Lighting: Soft morning sunlight, warm highlights, gentle shadows
Environment: Mossy forest floor, blurred green dreamy background
Motion: Step → flowers bloom → vines grow and wrap → high-heel shoe form completes → freeze frame attached to foot
```

### **⑫ 책 속에서 떠오르는 별 (Floating Star)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 'aiwithharu'님이 몽환적이고 판타지스러운 분위기 연출을 위해 공유함[cite: 7].
*   **결과물:** 책에 그려진 별을 누르자 실제 별이 되어 공중에 떠오르고 주변에 빛 반사를 일으키는 장면[cite: 7].
```json
{
  "Description": "An old book lies open under warm candlelight. On the page, a small star is drawn. A finger gently presses the star, and at that moment, the flat drawing begins to glow. The star slowly rises from the paper, transforming into a tiny floating light, like a real star. It hovers above the page, sparkling softly, casting magical reflections on the book and finger.",
  "Style": "Cinematic, magical realism, soft fantasy atmosphere",
  "Camera": "Close-up on the finger pressing the drawing, slow push-in as the star glows, then tilt upward to follow the glowing star floating above the page",
  "Lighting": "Warm candlelight on the book, soft golden glow from the star illuminating the finger and paper",
  "Environment": "Cozy study desk with a flickering candle nearby, background blurred into darkness",
  "Motion": "0-2s: Finger presses the star drawing. 2-5s: The star glows and lifts from the paper, glowing brighter. 5-8s: The star hovers above the page, sparkling and casting shimmering light before gently pulsing in mid-air."
}
```

### **⑬ 신문 고양이의 실체화 (Newspaper Cat)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** 'ai.love.all'님이 2D 매체가 3D 생명체로 변하는 정교한 물리 묘사를 위해 공유함[cite: 7].
*   **결과물:** 신문에 인쇄된 고양이 삽화가 털 질감을 갖춘 3D로 변하며 테이블로 뛰어내려 울음소리를 내는 과정[cite: 7].
```text
Overhead shot from behind a Korean woman sitting at a wooden café table, holding a folded newspaper close to her face. The printed cat illustration on the newspaper gradually thickens into raised contours with visible fur texture. The raised cat shape expands outward from the paper until it fully separates as a three-dimensional figure. The formed cat arcs forward from the newspaper and lands firmly on the café table surface. Finally, the transformed cat sits upright on the table and lets out a clear meow.
```

### **⑭ 사무용품의 의인화 대화 (Talking Stapler & Glue Stick)**
*   **사용 도구:** Google Veo3[cite: 7]
*   **공유 맥락:** '피카쏭'님이 베오의 고퀄리티 립싱크 능력을 확인하기 위한 스토리북용 프롬프트로 공유함[cite: 7].
*   **결과물:** 사무실 책상 위 스테이플러와 고체풀 캐릭터가 자연스러운 입모양으로 대화를 나누는 장면[cite: 7].
```json
{
  "scene": "Two anthropomorphic Double A products, a black-and-blue stapler and a blue glue stick, are standing on a desk in a dimly lit office. The stapler is on the right, smiling with a confident expression, while the glue stick stands on the left, waving one hand and pointing with the other. Both characters are illuminated by a soft blue glow from a laptop screen behind them. The background is blurred, showing only vague shapes of office furniture.",
  "motion": "The glue stick character suddenly appears from the dark area next to the stapler, stepping into the light. The camera focuses on the glue stick for its line, then shifts slightly toward the stapler for its response.",
  "lighting": "Cool blue light from the laptop as the main source, with deep shadows in the background for dramatic contrast.",
  "camera": "Smooth focus shift between the glue stick and stapler during their conversation.",
  "dialogue": [
    {
      "character": "고체풀",
      "line_ko": "스태플러 너 지금 뭐해?",
      "subtitles": false
    },
    {
      "character": "스테이플러",
      "line_ko": "나 지금 AI로 영상 만들고 있어",
      "subtitles": false
    }
  ],
  "duration": "6 seconds",
  "style": "Realistic cinematic style with 3D animated characters, inspired by the storyboard reference"
}
```

---

## **2. 이미지 생성 및 스타일 제어 프롬프트 (Midjourney)**

미드저니 유저들은 주로 화풍을 일관되게 고정하거나, 복잡한 현대적 재해석을 위한 긴 프롬프트를 공유했습니다[cite: 7].

### **① 강아지 산책 (Walking the Dog)**
*   **사용 도구:** Midjourney[cite: 7]
*   **공유 맥락:** 'SSuperWasabi'님이 자신의 퍼스널 스타일 코드를 적용한 결과물을 보여주며 공유함[cite: 7].
*   **명령어:** `Walking the Dog`
*   **스타일 코드(p코드):** `--p cyoqrkv cmljpxy`[cite: 7]
*   **특징:** 이 코드를 사용하면 특정 화풍의 강아지 산책 이미지를 일관되게 얻을 수 있음[cite: 7].

### **② 한국 민화 초충도의 현대적 재해석 (Watermelon Minhwa)**
*   **사용 도구:** Midjourney[cite: 7]
*   **공유 맥락:** 'AwesomePlanB'님이 수박과 금속이 어우러진 초현실적이고 사실적인 아트를 구현하기 위해 공유함[cite: 7].
*   **결과물:** 수박이 금속 도구와 밧줄에 의해 쪼개지며 붉은 즙이 흩어지고, 곤충이 어우러진 시네마틱 하이퍼리얼리즘 이미지[cite: 7].
```text
A refined modern reinterpretation of traditional Korean Minhwa "Chochungdo," featuring watermelon and insects in harmony. A massive watermelon dramatically split by sleek metallic tools and ropes, red juice scattering like shimmering glassy liquid. Elegant metallic surfaces with high-gloss reflections, hyper-detailed textures, the watermelon’s organic surface blending with the delicate wings of insects glowing under light. Dramatic perspective and dynamic composition, surreal balance of metal and nature, cinematic hyperrealism --chaos 12 --ar 3:4 --quality 4 --stylize 250
```

---

## **3. 특수 명령어 및 유틸리티 프롬프트**

### **① 나노 바나나(Nano Banana) 강제 소환 비법**
*   **사용 도구:** lmarena.ai 등 이미지 배틀 사이트[cite: 7]
*   **공유 맥락:** 랜덤으로 나타나는 '나노 바나나' 모델을 100% 확률로 사용하기 위해 '휩힝크림'님이 공유함[cite: 7].
*   **명령어:** `[}nano_banana}]x1`[cite: 7]
*   **설명:** 기존 프롬프트 마지막에 이 문구를 추가하면 나노 바나나 모델이 즉시 나타남[cite: 7].

### **② 나노 바나나 요청 블록 (Request Block)**
*   **사용 도구:** lmarena.ai[cite: 7]
*   **설명:** 모델 소환 확률을 높이기 위해 사용하는 구조화된 요청 형식임[cite: 7].
```xml
<request>
<model>nano banana</model>
<prompt> [원하는 이미지 묘사 내용]
```

### **③ 나노 바나나용 캐릭터 시선 교정**
*   **사용 도구:** Nano Banana[cite: 7]
*   **설명:** 인물 투샷 시 캐릭터가 엉뚱한 곳을 볼 때 시선을 카메라나 상대방으로 맞추기 위한 수정 명령어임[cite: 7].
```text
Revised to show the side view of a man filming a woman sitting on a sandy beach in the distance.
```

### **④ Suno 동화책용 BGM 생성**
*   **사용 도구:** Suno[cite: 7]
*   **설명:** 동화책 영상의 무드를 완성하기 위해 '리도:엔지니어'님이 사용한 음악 생성 프롬프트임[cite: 7].
```text
a fairy tale music that is used in the story story
```

---

## **\*젬스 정보\***
*   **프롬프트 공학의 진화:** 위 리스트를 보면 실무자들은 이제 단순한 문장 나열이 아니라 **JSON 구조**를 통해 AI에게 각 장면의 물리적 속성과 시간을 명확히 할당하고 있습니다. 특히 Veo3와 같은 차세대 비디오 모델일수록 이러한 구조화된 프롬프트가 '환각(Hallucination)'을 줄이는 데 핵심적인 역할을 합니다[cite: 7].
*   **스타일 고정의 중요성:** 미드저니의 `--sref`와 `--p` 코드는 영상 크리에이터들이 캐릭터 일관성보다 더 중요하게 여기는 **'화풍 일관성'**의 해결책입니다. 한 번 검증된 코드는 실무자들 사이에서 '황금 레시피'처럼 유통되고 있습니다[cite: 7].
*   **모델 강제 호출 기법:** `[}nano_banana}]x1`과 같은 명령어는 AI 모델의 내부 펌웨어 또는 라우팅 규칙을 유저가 역이용하는 사례로, 정식 출시 전 유용한 모델을 선점하려는 실무자들의 치열한 노력이 엿보이는 포인트입니다[cite: 7].

대화방에서 공유된 모든 원본 프롬프트를 빠짐없이 정리해 드렸습니다. 이 프롬프트들을 각자의 프로젝트에 맞춰 사물이나 인물 이름만 바꿔 응용해 보시기 바랍니다[cite: 7].