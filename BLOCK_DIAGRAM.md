## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        BEDTIME STORY GENERATOR SYSTEM                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐     ┌───────────────────┐                                     │
│  │   User   │────▶│  Categorizer      │                                     │                 
│  └──────────┘     └─────────┬─────────┘                                     │
│       │                     │                                               │
│       │                     ▼                                               │
│       │           ┌───────────────────┐                                     │
│       │           │  Category-Based   │                                     │
│       │           │  Prompt Selector  │                                     │
│       │           └─────────┬─────────┘                                     │
│       │                     │                                               │
│       │                     ▼                                               │
│       │           ┌───────────────────┐                                     │
│       │           │   Storyteller     │◀──────────────────┐                 │             
│       │           └─────────┬─────────┘                   │                 │
│       │                     │                             │                 │
│       │                     ▼                             │                 │
│       │           ┌───────────────────┐          ┌────────┴────────┐        │
│       │           │   Story Output    │          │   Suggestions   │        │
│       │           └─────────┬─────────┘          └─────────────────┘        │
│       │                     │                             ▲                 │
│       │                     ▼                             │                 │
│       │           ┌───────────────────┐                   │                 │
│       │           │       Judge       │───────────────────┘                 │
│       │           │                   │                                     │
│       │           │  Evaluates:       │                                     │
│       │           │  - Age Suitability│        ┌─────────────────┐          │
│       │           │  - Engagement     │        │  Score >= 8?    │          │
│       │           │  - Story Arc      │───────▶│                 │          │
│       │           │  - Creativity     │        │  YES: Finalize  │          │
│       │           │  - Moral          │        │  NO: Re-iterate │          │
│       │           └───────────────────┘        └────────┬────────┘          │
│       │                                                 │                   │
│       │                     ┌─────────────────┬───────────────────┐         │
│       │                     ▼                 ▼                   │         │
│       │           ┌───────────────┐   ┌───────────────┐           │         │
│       │           │ Final Story   │   │  Feedback     │───────────┘         │
│       │           └───────┬───────┘   └───────────────┘                     │
│       │                   │                                                 │
│       ▼                   ▼                                                 │
│  ┌──────────┐     ┌───────────────┐                                         │
│  │   User   │◀────│   Display     │                                         │
│  │ feedback │     │   Story       │                                         │
│  └────┬─────┘     └───────────────┘                                         │
│       │                                                                     │
│       ▼                                                                     │
│  ┌──────────────────────────────────┐                                       │
│  │  User Modification Requests:     │                                       │
│  │  - Make it funnier               │                                       │
│  │  - Add more adventure            │                                       │
│  │  - Change the ending             │                                       │
│  │  - Make it shorter/longer        │                                       │
│  └──────────────────────────────────┘                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. **User Input Layer**
- Accepts natural language story requests

### 2. **Story Request Categorizer** (LLM Call #1)
Classifies requests into categories for tailored prompting:

| Category | Description | Tone |
|----------|-------------|------|
| Adventure | Journeys, quests, discoveries | Exciting and brave |
| Fantasy | Magic, mythical creatures | Magical and wondrous |
| Animal | Animal protagonists | Warm and playful |
| Friendship | Making friends, teamwork | Caring and heartfelt |

### 3. **Storyteller Agent** (LLM Call #2)
Generates stories using:
- **Category-specific prompts** with appropriate tone and elements
- **Story Arc Structure**:
  1. Opening 
  2. Rising Action
  3. Climax 
  4. Falling Action
  5. Ending 

### 4. **LLM Judge** (LLM Call #3)
Evaluates stories on 6 criteria (1-10 scale):
- Age Appropriateness
- Engagement Level
- Story Structure
- Creativity
- Moral Integration
- Bedtime Suitability

**Decision Logic:**
- Score ≥ 8: Story approved
- Score < 8: Generate improvement feedback → Re-iterate (max 3 times)

### 5. **User Feedback Loop**
After story delivery, users can request modifications:
- "Make it funnier"
- "Change the ending"

---


