# Unity Prototype - "Office Escape: The Caffeinated Chronicles"

🎮 **A quirky, funny office-themed Unity demo with modern systems and achievements!**

## 🎯 Demo Concept

You're the new intern at **Cubicle Corp**, and your mission is simple: survive the corporate environment for 2 minutes while collecting coffee cups to stay caffeinated! Avoid possessed red staplers, find the legendary golden donut, and don't let the boss catch you slacking off!

## 🚀 Quick Setup

1. **Create a new Unity project** (Unity 2021.3 LTS or later recommended)
2. **Copy the `Assets` folder** from this directory into your Unity project
3. **Open the project in Unity** and you're ready to play!
4. **Create a simple scene** with a player capsule, some collectibles, and ground plane
5. **Hit play** and start your corporate adventure!

## ✨ Features & Systems

### 🎮 Core Gameplay
- **Modern Player Controller** - Smooth movement with camera-relative controls
- **Shooting System** - Fire projectiles at hostile office supplies
- **Object Pooling** - Performance-optimized spawning system
- **Event-Driven Architecture** - Clean, maintainable code structure

### 🏆 Achievement System (25+ Achievements!)
- **Tutorial achievements** - "Baby Steps", "Trigger Happy"
- **Combat achievements** - "Sharpshooter", "Bug Exterminator" 
- **Funny achievements** - "Statue Mode", "Spin Cycle", "AFK Champion"
- **Special achievements** - "Golden Donut", "TPS Report", "Fish Survivor"
- **Meta achievements** - "Achievement Hunter", "Completionist"

### 💾 Save System
- **Multiple save slots** (3 slots by default)
- **JSON serialization** with persistent storage
- **Auto-save functionality** (every 60 seconds)
- **Comprehensive game state** tracking

### ⚙️ Settings System
- **Audio controls** - Master/Music/SFX volume with AudioMixer support
- **Graphics settings** - Quality levels, fullscreen, VSync, framerate
- **Accessibility options** - Colorblind support, text scaling, motion sickness reduction
- **Gameplay preferences** - Mouse sensitivity, auto-save, subtitles

### 🎨 Visual Effects
- **Particle effect system** with object pooling
- **Screen flash effects** for feedback
- **Camera shake** for impact
- **Achievement popup animations**
- **Trail effects** for special items

### 🎭 Quirky Demo Elements
- **Office-themed collectibles** - Coffee cups, paperclips, sticky notes
- **Crazy Mode** - Random speed boosts and visual chaos
- **Funny story messages** - Corporate humor throughout
- **Interactive elements** - Possessed staplers, boss encounters
- **Time pressure** - 2-minute survival challenge

## 🕹️ How to Play

### Controls
- **WASD/Arrow Keys** - Move around the office
- **Mouse/Space** - Fire at hostile office supplies
- **Escape** - Pause/unpause game
- **Click UI elements** - Interact with menus

### Objectives
1. **Survive 2 minutes** in the corporate environment
2. **Collect coffee cups** to stay caffeinated (50 points each)
3. **Avoid red staplers** - they're possessed!
4. **Find the golden donut** (500 points + special achievement)
5. **Unlock achievements** by playing naturally

### Items & Collectibles
- ☕ **Coffee Cups** - Your lifeline! Collect to stay energized
- 🍩 **Golden Donut** - Legendary rare item worth massive points
- 📎 **Office Supplies** - Paperclips, rubber bands, sticky notes (10 points each)
- 📋 **TPS Reports** - Reference to Office Space (100 points)
- 🔑 **Keycards** - "John Smith - Bathroom Monitor"

## 🛠️ Technical Architecture

### Modern Unity Patterns
```
Assets/Scripts/
├── Controllers/        # Player and input controllers
├── Managers/          # Game state and system managers  
├── Systems/           # Reusable systems (save, settings, achievements)
├── Components/        # Modular component scripts
├── Interfaces/        # Clean abstractions
├── UI/               # User interface components
├── ScriptableObjects/ # Data-driven configuration
└── QuirkyDemo/       # Demo-specific gameplay
```

### Key Scripts
- **ModernGameManager** - Event-driven game state management
- **ModernPlayerController** - Smooth, responsive movement
- **SettingsManager** - Comprehensive preferences system
- **SaveSystem** - Multi-slot save/load with JSON
- **AchievementSystem** - 25+ quirky achievements with popups
- **ParticleEffectManager** - Pooled visual effects system
- **DemoController** - Office-themed narrative and events
- **QuirkyCollectible** - Animated collectible items

### Performance Features
- **Object pooling** for projectiles and effects
- **Event-driven updates** to minimize Update() calls
- **Efficient particle management** with reusable pools
- **Smart save system** with delta compression

## 🎨 Customization Ideas

### Easy Modifications
- **Change the theme** - Space office, medieval office, underwater office?
- **Add new collectibles** - Donuts, energy drinks, stress balls
- **New enemy types** - Aggressive printers, haunted keyboards
- **More achievements** - "Meetings Survivor", "Printer Whisperer"
- **Power-ups** - Speed boost, invincibility, double points

### Advanced Features
- **Multiplayer** - Co-op office survival
- **Level progression** - Different floors of the building
- **Boss fights** - The ultimate manager encounter
- **Mini-games** - Photocopier rhythm game, email sorting
- **Story mode** - Career progression system

## 🐛 Known Quirks (Features!)

- Staplers occasionally develop sentience
- Coffee may cause time dilation effects
- The office printer is definitely haunted
- Fish in the microwave creates temporary speed boost
- Golden donuts are rarer than promotions

## 🎯 Making It Your Own

1. **Fork the concept** - Change the office theme to anything!
2. **Add your humor** - Replace office jokes with your style
3. **Expand the systems** - All scripts are modular and extensible
4. **Create new achievements** - The system supports unlimited achievements
5. **Build and share** - Perfect for game jams and prototypes!

## 📋 Development Checklist

To turn this into a complete playable demo:

- [ ] Create a simple office scene with cubicles
- [ ] Set up player prefab with ModernPlayerController
- [ ] Place quirky collectibles around the scene  
- [ ] Add UI canvas with achievement popups
- [ ] Configure AudioMixer for the SettingsManager
- [ ] Set up particle effect prefabs
- [ ] Add some office-themed 3D models or sprites
- [ ] Test the 2-minute gameplay loop
- [ ] Build and deploy!

## 🤝 Contributing

This is a demo/prototype, but feel free to:
- Submit funny achievement ideas
- Add new quirky collectibles
- Improve the office humor
- Optimize the systems further
- Create art assets for the office theme

---

*"Remember: In corporate America, the coffee is never strong enough, and the staplers are always plotting against you."* ☕📎

**Built with Unity 2021.3+ | Tested on PC/Mac | Mobile-friendly architecture**
