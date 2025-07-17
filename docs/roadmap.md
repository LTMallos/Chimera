# 🧭 Chimera Roadmap

> Chimera is an open-source experimental compatibility layer designed to make iOS `.ipa` apps function on Android devices - not through full emulation, but via a dynamic translation and simulation system.

## 🌌 Vision

To create a platform-agnostic layer that:
- Deconstructs `.ipa` packages
- Reconstructs their behavior on Android through native or adapted equivalents
- Bridges iOS APIs like UIKit and Foundation into usable, mapped Android behaviors
- Enables open-source research in mobile compatibility without relying on closed emulators

> This project is for learning, development, and non-commercial purposes only.

---

## 🧱 Core Pillars

1. **IPA Compatibility Tools**  
   - Parse `.ipa` files
   - Read `Info.plist`, extract metadata
   - Collect assets and metadata for runtime use

2. **Android Runtime Host (Kotlin)**  
   - Loads the translated app structure
   - Hosts visual and logical layers dynamically
   - Modular structure for plug-and-play API adapters

3. **Bridge Layer (C++/Kotlin)**  
   - API mapping engine
   - UIKit simulation
   - Foundation logic remapping
   - iOS animation/audio/networking translation

4. **UI Translator** *(future)*  
   - Storyboard/XIB-to-Android layout converter
   - Jetpack Compose or View-based rendering layer

5. **Adaptive Learning Layer** *(future idea)*  
   - ML-backed auto-mapper for unknown APIs
   - Community-fed API map database

---

## 🛠️ Milestones

### ✅ Phase 0 – Project Kickoff
- [x] Setup GitHub
- [x] Create project structure
- [x] Write README and Roadmap

---

### 🔧 Phase 1 – IPA Tooling (Python)
- [ ] Write `ipa_parser.py` to unzip `.ipa`
- [ ] Read and parse `Info.plist`
- [ ] Extract and list assets (images, binaries, UI files)
- [ ] Output a JSON “App Profile”

---

### 🔧 Phase 2 – Android Host Runtime (Kotlin)
- [ ] Set up basic Android app in `android_host`
- [ ] Create placeholder screen for app loading
- [ ] Add ability to inject dynamic components
- [ ] Show parsed app metadata on-screen

---

### 🔧 Phase 3 – Bridge Layer Core
- [ ] Create `mappings.json` with initial UIKit/Core API targets
- [ ] Implement `UILabel`, `UIButton`, and basic views in Kotlin
- [ ] Handle tap events and navigation simulation
- [ ] Simulate simple layout loading from App Profile

---

### 🧠 Phase 4 – UI Translation System
- [ ] Parse layout/storyboard files (if present)
- [ ] Render dynamic layout on Android using Jetpack Compose
- [ ] Align iOS spacing/padding/naming conventions

---

### 🧬 Phase 5 – Future: Adaptive Learning Layer
- [ ] Track unknown API usage
- [ ] Suggest best matches from crowd-sourced DB
- [ ] Learn over time which APIs to map automatically

---

## 📣 Want to Help?
This project is in early development. PRs are welcome once core foundation is stable.

---

## ⚖️ Legal Notice
Chimera is not affiliated with or endorsed by Apple Inc. It does not include proprietary Apple components, and exists purely to experiment with public interface compatibility for educational and developmental purposes. And It does **NOT** encourage piracy or the distribution of copyrighted `.ipa` apps. Only use Chimera for testing open-source apps or apps you legally own.

---

## 👑 Maintainer
[@LTMallos](https://github.com/LTMallos) – idea, vision, structure, and madness.

