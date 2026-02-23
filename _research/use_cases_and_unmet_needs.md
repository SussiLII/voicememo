# Use Cases & Unmet Needs: Wearable Audio Recording Devices

**Prepared for:** Product Team — Wearable Voice Recorder for Knowledge Workers
**Date:** February 2026
**Scope:** Creative, unexpected, and underserved use cases gathered from user reviews, Reddit, Substack, Product Hunt, tech blogs, and industry reporting

---

## Executive Summary

The market narrative for wearable audio recorders has been dominated by meeting transcription. But the most passionate users — and the most defensible market positions — exist in use cases that barely involve meetings at all.

**Key insight:** The most compelling use cases involve recording *yourself* (thinking out loud, idea capture, self-reflection), which completely sidesteps the consent problem — the single hardest challenge in this category. This could fundamentally shape product positioning.

---

## 1. Standard Use Cases (Brief)

These are well-known and well-served by existing products:

- Meeting notes / transcription
- Lecture recording
- Interview recording
- Phone call transcription

These are table stakes, not differentiators.

---

## 2. Creative & Unexpected Use Cases

### 2.1 Personal Knowledge Management & Thinking Out Loud

One Limitless Pendant reviewer found unexpected value in deliberate "thinking out loud" sessions, describing the experience as "a conversation with yourself" while preserving insights. Verbally processing thoughts while walking or driving created a searchable archive of decision-making. (jock.pl blog)

This user built Make.com automations to:
- Extract tasks from spoken thoughts and sync to todo apps
- Generate daily journaling summaries delivered via email
- Trigger Perplexity research based on detected question patterns

This transforms a recording device into a personal knowledge management system.

**Why this matters for product design:** This use case eliminates the consent problem entirely (you're recording yourself), aligns with knowledge-worker workflows, and creates high switching costs through accumulated personal archives. It suggests the product should support intentional recording sessions, not just passive ambient capture.

**Features needed:**
- Dedicated "thinking out loud" mode
- Task/insight extraction from stream-of-consciousness speech
- Daily digest summaries
- Searchable personal archive
- Integration with PKM tools (Notion, Obsidian, etc.)

---

### 2.2 ADHD & Executive Function Support

Fieldy, a product on Product Hunt, specifically targets ADHD users with a "wearable that listens to conversations and turns them into notes, summaries, and reminders." (Product Hunt)

One Product Hunt user titled their review: "Can this AI wearable help my ADHD brain remember tasks and save my marriage?" — highlighting both the executive function and relationship impact. (Product Hunt)

Use patterns in this population include:
- Managing executive dysfunction by externalizing memory to the device
- Idea capture during walks and commutes when thoughts are fleeting
- Students tracking lectures and study group conversations
- Entrepreneurs capturing rapid-fire ideas without breaking flow
- Reducing friction of "I'll remember that later" moments that ADHD brains consistently forget

**Why this matters:** ADHD affects an estimated 4.4% of U.S. adults (8.7 million people). This population has a specific, acute need for memory augmentation and is accustomed to using assistive technology. They may tolerate imperfect transcription if the capture-and-remind workflow is reliable.

**Features needed:**
- Proactive reminders based on captured commitments
- Ultra-low-friction recording (zero steps to start)
- Integration with task managers
- "Did I say I would do X?" searchability
- Gentle nudges, not overwhelming data dumps

---

### 2.3 Memory Support for Elderly & Caregiving

Several products and research projects target elderly memory support:

| Product/Project | Approach | Source |
|----------------|----------|--------|
| MemPal (MIT Media Lab) | Wearable voice assistant — reminders like "Did you remember to turn off the stove?" and "You already took your medicine" | MIT Media Lab |
| Senstone Scripter | Captures audio, auto-transcribes for seniors and caregivers | Senstone |
| Storii | Records life stories over any phone including landlines; AI generates well-crafted narratives | Storii |
| Remento | Speech-to-Story technology (Shark Tank) transforms voice into polished stories | Remento |

**Why this matters:** The elderly care market has different success criteria — simpler UX, caregiver-facing dashboards, and integration with health monitoring. It also has strong emotional appeal and less consent friction (caregivers and family members are typically aligned on the goal).

**Features needed:**
- Extremely simple operation (ideally zero-button)
- Caregiver dashboard with activity summaries
- Safety reminders (medication, stove, etc.)
- Integration with health monitoring
- Large text, simple app interface

---

### 2.4 Life Story Preservation

Recording elderly relatives' stories before they are lost emerged as a powerful emotional use case. Products like Storii (which works over landlines, removing the technology barrier) and Remento (which transforms voice into polished narratives) demonstrate real market demand. (Storii, Remento/Shark Tank)

Users in this category want:
- Simple, non-intimidating recording initiation
- Prompted storytelling (questions that elicit memories)
- Polished output suitable for sharing with family
- Long-term archival storage
- Beautiful presentation (book-like, shareable formats)

**Why this matters:** This is a deeply emotional use case with strong word-of-mouth potential. It's also time-sensitive — the stories are lost forever once the person is gone. This urgency drives purchase decisions.

---

### 2.5 Evidence & Legal Protection

Legal and evidentiary recording represents a high-stakes, high-reliability use case:

- **Legal depositions:** "I use Plaud for legal depositions. The physical switch for call recording is the only thing that works reliably. I don't care about AI friends; I need a transcript that is accurate." (Product review)
- **Workplace harassment documentation:** In one-party consent states, employees can legally record workplace interactions for evidence.
- **NLRB ruling (2023):** Affirmed employees' right to secretly record workplace conversations for protected activities. (NLRB)
- **Hacker News thread:** "Wearable device that records your voice for legal defense" generated significant discussion about always-on recording for personal protection. (Hacker News)

**Legal framework:**
- One-party consent states: recording is legal if you're a participant in the conversation
- Two-party consent states (including California): all parties must consent
- Federal NLRA may override state laws for protected workplace activities
- Secret recordings can be admissible but may complicate legal strategy

**Why this matters:** Legal users have extreme reliability requirements and are willing to pay premium prices for a device they can trust absolutely. They need physical recording indicators (for their own certainty), tamper-evident storage, and accurate timestamps.

**Features needed:**
- Rock-solid reliability (zero missed recordings)
- Physical on/off switch with clear state indicator
- Tamper-evident, timestamped, GPS-tagged recordings
- Encrypted local storage
- Easy export in forensically sound formats

---

### 2.6 Health & Wellness

| Use Case | Description | Source |
|----------|-------------|--------|
| Medical appointment recording | Patients record doctor instructions to review later — especially valuable for complex diagnoses, elderly patients, or high-stress medical conversations | Multiple |
| Therapy session recording | Patients review therapy sessions between appointments to reinforce insights | Product research |
| Alzheimer's/dementia caregiving | Documenting care interactions and tracking cognitive changes over time | MIT Media Lab, Senstone |
| Wellness & cognitive monitoring | Monitoring cognitive patterns through speech analysis (speech rate, vocabulary, coherence) | Academic research |

Use cases span "Alzheimer's, mental health, relationships, mental load, and education." (Product research)

**Why this matters:** Healthcare is a high-trust, high-value vertical. Patients already struggle to remember doctor's instructions — studies show patients forget 40-80% of medical information immediately. A reliable recorder positioned for this use case has clear product-market fit.

---

### 2.7 Networking & Professional Relationship Building

Silicon Valley adoption data reveals a specific professional use case:

- Nicholas Lopez uses a Plaud pin as a "second brain" for tracking his professional network. (SF Standard, Aug 2025)
- Founders use devices at networking events to "get it documented so you remember." (SF Standard)
- Investors use recorders to surface patterns in early-stage opportunities across dozens of founder meetings. (SF Standard)
- Sales teams get AI-generated transcripts of all interactions for coaching and CRM integration. (SF Standard)

**The core need:** After meeting 20 people at a conference, users want to remember who said what, what they cared about, and what follow-ups were promised.

**Features needed:**
- Automatic contact/speaker tagging
- Follow-up task extraction
- CRM integration (Salesforce, HubSpot)
- "Remind me what [person] said about [topic]" search
- Relationship timeline across multiple conversations

---

### 2.8 Creative & Content Creation

- Recording cooking classes for later reference (Product reviews)
- Narrating notes during chores about where items are stored — one user runs their recorder while doing chores to build a habit of narrating storage locations (Sacha Chua blog)
- One person takes a recorder to house parties "as a social experiment to relive nights out." (SF Standard)
- A founder uses their recorder in saunas; it works fine at 104°F. (SF Standard)
- Music/songwriting — capturing melody ideas and lyrical fragments on the go
- Podcast research — recording ambient conversations and experiences as source material
- Writers using verbal brainstorming to overcome writer's block

---

### 2.9 Self-Reflection & Personal Growth

Multiple sources converge on self-recording as a high-value use case:

- "The real value isn't in recording others, it's in recording yourself." (Product reviews)
- Self-awareness through searchable transcripts of own thinking patterns (jock.pl blog)
- Solo voice notes for self-reflection (multiple sources)
- Building a personal archive of decision-making rationale (jock.pl blog)
- Couples/relationship use: reviewing arguments objectively later (Bee Wearable trial noted partner banned it, but also acknowledged recording "deeply unflattering things you say in moments of weakness" — suggesting self-awareness value even when uncomfortable) (ekavc Substack)

**This use case is notable because it completely sidesteps consent friction — the most intractable problem in the category.**

---

### 2.10 Silicon Valley Power Users

Jeff Wilson (VC) observes: "AI wearables have become so ubiquitous [in Silicon Valley] that people rarely comment." (SF Standard, Aug 2025) This suggests that within a specific professional culture, normalization has already occurred.

Observed power-user behaviors:
- Wearing devices at all professional interactions as default behavior
- Using AI-generated transcripts to prepare for follow-up meetings
- Cross-referencing conversation transcripts to identify investment patterns
- Recording all sales interactions for coaching and CRM integration
- Building Make.com/Zapier automations to extract structured data from conversations
- Using Claude/ChatGPT with transcript exports for deeper analysis

However, normalization comes with tension:
- Workers self-censor, worried about offhand comments becoming permanent records
- Clara Brenner explicitly calls covert recording by VCs "an invasion of privacy" (SF Standard)
- "In 10 years, the majority of conversations will be recorded in some format" — Bee trial author prediction (ekavc Substack)

---

## 3. "I Wish I Could..." (Unmet Feature Requests)

Based on user complaints, workarounds, and explicit requests, these represent the strongest unmet needs:

| Unmet Need | Evidence | Source |
|------------|----------|--------|
| **Record what I'm listening to through earphones** | Knowledge workers consume hours of podcasts/calls daily; no product captures this | Product spec, user feedback |
| **Export raw audio as WAV/MP3** | Plaud lacks WAV export; users want to own their raw data | tldv.io review |
| **Integrate with task managers** (Todoist, Google Tasks, Notion) | Omi has no integrations; users build DIY automations | umevo.ai, jock.pl blog |
| **Transcribe offline with no cloud dependency** | Humane bricking fears; cloud privacy concerns | Multiple sources |
| **Build on a programmable/extensible platform** | Omi recommended "only for developers who want to write Python scripts" | geeky-gadgets.com |
| **Waterproof design** | Limitless not waterproof; sauna use case proves need | winstonfrancois.com, SF Standard |
| **Reliable physical on/off control** | Touch controls finicky; whole-device buttons accidental | Plaud, Omi reviews |
| **AI that learns from my corrections** | Plaud AI doesn't improve with repeated prompts | Reddit |
| **Handle multiple languages in single transcript** | Plaud mixes output languages incorrectly | Trustpilot |
| **Searchable long-term archive of all recordings** | Limitless "struggles with organization and recall" | jock.pl blog |
| **Built-in consent management framework** | Only 2/5 people consent; no product helps manage this | ekavc Substack |
| **Event-based organization (not files)** | Nobody organizes by event/context; all are linear file lists | Product spec insight |
| **Daily digest dashboard** (not meeting minutes) | Users want summary of day, not transcripts | Product spec insight |
| **Distinguish my commands from conversation** | "Mark this important," "new event" — no product supports this | Product spec insight |
| **Capture who I met and what we discussed** | Networking use case needs contact-level organization | SF Standard |

---

## 4. Product Opportunity Matrix

### Use Cases by Consent Friction

| Low Friction (Self-Recording) | Medium Friction (Known People) | High Friction (Strangers/Public) |
|-------------------------------|-------------------------------|----------------------------------|
| Thinking out loud / PKM | Team meetings | Networking events |
| ADHD idea capture | Medical appointments | Conferences |
| Self-reflection / journaling | Therapy sessions | Coffee chats |
| Creative brainstorming | Family story recording | Sales calls |
| Dictation / voice commands | Couples review | Street/ambient recording |

**Strategic implication:** A product that leads with low-friction, self-recording use cases can build a user base and brand trust before tackling the harder social acceptance challenges of recording others.

### Use Cases by Willingness to Pay

| High WTP (>$200) | Medium WTP ($100-200) | Lower WTP (<$100) |
|-------------------|----------------------|-------------------|
| Legal/evidence | Knowledge workers | Students |
| Medical professionals | ADHD adults | Casual journalers |
| Sales teams (enterprise) | Elderly caregiving | Hobbyist content creators |
| Executive coaching | Networking professionals | |

### Use Cases by Market Size vs. Passion

| Large Market, Moderate Passion | Small Market, High Passion |
|-------------------------------|---------------------------|
| Meeting transcription | Legal evidence recording |
| Lecture notes | ADHD support |
| General productivity | Elderly memory/caregiving |
| | Life story preservation |
| | Self-reflection/PKM |

**The most defensible strategy:** Start with small-but-passionate markets (ADHD, PKM, self-reflection) where users are highly motivated and consent is not an issue, then expand to larger markets as the product matures and social norms evolve.

---

## 5. Delighters (Features That Create Word-of-Mouth)

| Delighter | Description | Evidence of Demand |
|-----------|-------------|-------------------|
| **"Thinking Out Loud" mode** | Dedicated mode for verbal processing that extracts tasks, insights, and journal entries | jock.pl automations; PKM community interest |
| **Consent management UX** | Built-in prompts, scripts, and indicators that make asking permission natural | 2/5 consent rate in Bee trial |
| **Life Story interview templates** | Prompted storytelling for recording elderly relatives with polished output | Storii, Remento market validation |
| **ADHD-optimized reminders** | Proactive nudges based on captured tasks and commitments | Fieldy on Product Hunt; 8.7M U.S. adults with ADHD |
| **"Did I say that?" self-search** | Instant search across your own verbal history | Reflection use case; decision-making archive |
| **Waterproof design** | Enables sauna, shower, rain, exercise use | Founder uses in sauna at 104°F |
| **Physical switch with tactile state** | A switch you can feel to confirm recording state | Legal user's emphasis on physical reliability |

---

## 6. Selected User Quotes on Use Cases

1. "I use Plaud for legal depositions. The physical switch for call recording is the only thing that works reliably. I don't care about AI friends; I need a transcript that is accurate." — Legal professional (product review)

2. "The real value isn't in recording others, it's in recording yourself" — self-recording advocate (product reviews)

3. "A conversation with yourself" — describing thinking-out-loud sessions (jock.pl blog)

4. "Get it documented so you remember" — Silicon Valley founders on networking events (SF Standard)

5. "Did you remember to turn off the stove?" — MemPal voice assistant prompt for elderly users (MIT Media Lab)

6. "Wearable that listens to conversations and turns them into notes, summaries, and reminders" — Fieldy, targeting ADHD users (Product Hunt)

7. "Second brain" — Nicholas Lopez on using Plaud for professional network tracking (SF Standard)

8. "AI wearables have become so ubiquitous [in Silicon Valley] that people rarely comment" — Jeff Wilson, VC (SF Standard)

9. "In 10 years, the majority of conversations will be recorded in some format" — Bee trial author (ekavc Substack)

10. "Is fundamentally a different conversation" — Harvin Park on how recording changes behavior (SF Standard)

11. "Can this AI wearable help my ADHD brain remember tasks and save my marriage?" — Fieldy Product Hunt review title

12. Recording "deeply unflattering things you say in moments of weakness" — Bee trial on self-awareness (ekavc Substack)

13. Takes recorder to house parties "as a social experiment to relive nights out" — Silicon Valley user (SF Standard)

14. Uses recorder in saunas; works at 104°F — Silicon Valley founder (SF Standard)

15. "Speaking in prompts" — how recording changes the way people communicate (SF Standard)

---

## Sources

1. jock.pl blog — Limitless Pendant real-world review and automation experiments
2. Product Hunt — Fieldy ADHD wearable reviews
3. MIT Media Lab — MemPal research
4. Senstone — Scripter product information
5. Storii — Life story recording platform
6. Remento — Speech-to-Story technology (Shark Tank)
7. SF Standard — "AI Recording Wearables in Silicon Valley" (August 2025)
8. ekavc Substack — "Living on Record" 10-day Bee Wearable trial
9. mikecann.blog — Limitless and Omi reviews
10. winstonfrancois.com — Limitless vs Plaud comparison
11. SoundGuys — AI voice recorder adoption survey
12. NLRB (2023) — Employee recording rights ruling
13. Hacker News — "Wearable device that records your voice for legal defense" thread
14. Sacha Chua blog — Revisiting wearable computing
15. Product spec — Internal team observations and requirements

---

*This report compiles sourced research data. All quotes and data points are attributed to their respective sources. Use cases should be validated through user interviews and surveys before making product decisions based on this secondary research.*
