# Research Summary: Hardware Design for Voice Memo Wearable

## Key Findings

### 1. Audio Quality — The #1 Challenge

The dominant complaint across ALL existing wearable recorders is audio quality. The core issues are:

- **Fabric occlusion/muffling** — the single biggest cause of poor audio. Any mic covered by clothing loses 10-20dB of high-frequency content, making speech unintelligible for ASR
- **Distance from mouth** — sound pressure drops 6dB for every doubling of distance. A chest mic (20-25cm) is dramatically better than wrist (60-70cm)
- **Keyboard/contact noise** — wrist and ring placements pick up heavy typing noise
- **Environmental noise** — cafes, cars, open offices all degrade transcription below usable thresholds

**Critical threshold**: ASR needs +10dB SNR minimum (WER <15%). Below +5dB SNR, transcription becomes unusable.

**What's solvable in software vs hardware**:
| Problem | Hardware | Software | Both |
|---------|----------|----------|------|
| Muffled/occluded audio | Must solve with placement/design | Cannot fix | |
| Keyboard noise | | Transient suppression works well | |
| Wind noise | Recessed port, mesh | Coherence-based detection | Best with both |
| Background noise | Multi-mic beamforming (5-8dB gain) | DNN denoising (8-15dB gain) | Best with both |
| Distant speakers | More/better mics | Limited help | Physics limit ~2-3m |

### 2. Wearable Placement — Top 3 Recommendations

After scoring 15 body locations across audio quality, comfort, social acceptability, security, clothing compatibility, and gesture feasibility:

| Rank | Placement | Score | Verdict |
|------|-----------|-------|---------|
| 1 | **Smart glasses** | 4.28 | Best audio + comfort balance. Limitation: requires glasses adoption |
| 2 | **Wristband** | 4.13 | Best all-around wearability. Weakness: audio quality (60-70cm from mouth) |
| 3 | **Lapel pin/brooch** | 3.83 | Best audio at chest level. Weakness: fails with casual clothing |

**Primary recommendation: Wristband** — despite weaker audio, it wins on compliance (80-90% at 6 months), universal wearability, zero social friction, best gesture platform, and security. Audio weakness can be partially mitigated by multi-mic beamforming + AI noise suppression.

**Key insight**: During high-value moments (conversations, meetings), hands are usually NOT on the keyboard, so wrist audio quality naturally improves when it matters most.

**Multi-device strategy worth exploring**: Wristband (primary, always worn) + optional clip-on booster mic (for important meetings) + future smart ring (secondary mic/gesture device).

### 3. Competitive Landscape — Gaps to Exploit

Current products and their biggest weaknesses:

| Product | Price | Battery | Audio Quality | Key Weakness |
|---------|-------|---------|---------------|-------------|
| Plaud NotePin | $169 | ~20h | Best in class | Muffled when clipped inside clothing; weak magnet |
| Limitless Pendant | $99 | ~6-8h | Adequate | Battery too short; fabric noise |
| Omi | $89 | ~5-8h | Worst | Single mic; feels like prototype |
| Humane AI Pin | $699 | ~2-4h | Good (multi-mic) | Battery, overheating, price |

**Top 10 user complaints** (from Reddit, reviews):
1. Muffled/distant audio (>70% of negative reviews)
2. Insufficient battery life (>60%)
3. Poor transcription in noise (~55%)
4. Fear of losing device (~45%)
5. Poor speaker identification (~40%)
6. Privacy/social awkwardness (~35%)
7. Slow file transfer (~30%)
8. Subscription fatigue (~30%)
9. No earphone audio capture (~25%)
10. Can't distinguish commands from conversation (~20%)

**Biggest untapped opportunities**:
1. **Apply hearing aid tech** (adaptive beamforming, scene classification, own-voice detection) — none of the competitors do this
2. **True all-day battery** (15h+) — police body cams prove this is achievable for audio
3. **Earphone/headphone audio capture** — knowledge workers listen to hours of podcasts/calls daily; almost no product captures this
4. **Event-based organization** (not file-based) — nobody does this well
5. **Robust speaker enrollment and ID** — all products do this poorly

## Hardware Design Recommendations

1. **Use at least 2 MEMS mics** — dual-mic beamforming gives 5-8dB noise reduction
2. **High-SNR mics** (>=68 dB(A), >=128 dB SPL AOP) — e.g., Infineon IM73D122, Knowles SPH0655
3. **Mic port must face outward**, away from body/fabric — this is non-negotiable
4. **Vibration isolation** (silicone gasket between mic and PCB)
5. **On-device VAD** for battery life (can extend 2-3x during silence)
6. **Opus codec at 32-48 kbps** — 15h recording in <350MB, negligible ASR impact
7. **On-device lightweight noise reduction** (RNNoise runs on ESP32-S3) for real-time preview; store raw audio for cloud processing

## Conclusions

The market is wide open. No existing product has solved the fundamental tension between **audio quality** (needs to be close to mouth, exposed) and **wearability** (needs to be discreet, comfortable, secure). The team that cracks this — likely through a combination of better mic engineering, hearing-aid-derived DSP, and smart industrial design — will win.

Your product spec's instinct is correct: **a specific, opinionated wearing position** (not "wear it anywhere") combined with **professional-grade audio engineering in a consumer form factor** is the path forward.

## Recommended Next Steps

### Immediate (Next 2-4 weeks)
1. **Prototype audio comparison test** — Record the same conversations with mics at wrist, chest, collar, and glasses positions. Compare raw audio quality and ASR accuracy. This will give you hard data on the placement tradeoff.
2. **Tear down a Plaud NotePin** — Understand their mic, PCB, and acoustic design firsthand
3. **Talk to 2-3 hearing aid audio engineers** — They have decades of relevant expertise in small-form-factor audio processing

### Short-term (1-2 months)
4. **User survey (n=50-100)** — Target knowledge workers who already use voice recording. Key questions:
   - Where would they be willing to wear a device all day?
   - What form factor feels most natural? (Show mockups of wristband, pendant, pin, ring)
   - What's their biggest pain point with current recording tools?
   - How much would they pay?
   - Privacy concerns — would they tell colleagues they're recording?
5. **Diary study (n=5-10, 1 week each)** — Give participants a current recorder (Plaud NotePin) and have them log: when they forgot to wear it, when audio quality was bad, when it was socially awkward, what they wished it captured
6. **Evaluate dual-mic DSP dev kits** — Get hands-on with beamforming on small MEMS arrays (Knowles, Infineon, TDK all have eval boards)

### Medium-term (2-4 months)
7. **Build a "Wizard of Oz" prototype** — A wristband with good mics + phone app that simulates the ideal software experience. Test with 10-20 users for 1 week.
8. **Benchmark earphone audio capture approaches** — Test iFlytek earbuds, explore iOS/Android audio routing APIs, evaluate BLE audio streaming from companion earbuds
9. **Design the event-based daily diary UX** — Paper prototype the "podcast editing for your life" concept from the spec

### Research to Commission
10. **Acoustic simulation** — Model mic array configurations (2-mic, 4-mic) at different body positions in simulated office/meeting room environments. An acoustic engineer can do this in COMSOL or similar.
11. **Multilingual ASR benchmarking** — You already have English and Chinese benchmark data. Systematically test code-switching scenarios with Whisper, and evaluate fine-tuning for your specific use case.

---

*See detailed research in:*
- [Audio Quality Issues](audio_quality_issues.md)
- [Wearable Placement Options](wearable_placement_options.md)
- [Competitive Landscape](competitive_landscape.md)
