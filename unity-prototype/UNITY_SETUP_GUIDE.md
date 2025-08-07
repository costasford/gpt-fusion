# Unity Setup Guide - Office Escape Demo

## 🎯 Complete Step-by-Step Unity Setup

### Phase 1: Project Setup
1. **Create New Unity Project**
   - Unity Hub → New Project → 3D Template
   - Name: "OfficeEscape" or similar
   - Location: Anywhere you prefer

2. **Import Scripts**
   - Copy the entire `Assets/Scripts` folder from this repository
   - Paste into your Unity project's `Assets` folder

### Phase 2: Basic Scene Setup

#### Create the Office Environment
1. **Create Ground**
   - GameObject → 3D Object → Plane
   - Name: "Floor"
   - Scale: (10, 1, 10) - makes a 100x100 unit floor
   - Material: Create a gray/white material for office floor

2. **Add Office Cubicles (Placeholder)**
   ```
   Create several cubes for cubicles:
   - GameObject → 3D Object → Cube
   - Name: "Cubicle_01", "Cubicle_02", etc.
   - Scale: (2, 2, 2) for each
   - Position them around the scene at:
     • Cubicle_01: (3, 1, 3)
     • Cubicle_02: (-3, 1, 3) 
     • Cubicle_03: (3, 1, -3)
     • Cubicle_04: (-3, 1, -3)
     • Cubicle_05: (0, 1, 6)
     • Cubicle_06: (0, 1, -6)
   - Create brown/beige materials for office look
   ```

3. **Add Walls (Optional)**
   - Create scaled cubes as walls around the perimeter
   - Position: (±12, 2, 0) and (0, 2, ±12)
   - Scale: (1, 4, 24) for side walls, (24, 4, 1) for front/back

### Phase 3: Player Setup

#### Create Player GameObject
1. **Create Player**
   - GameObject → 3D Object → Capsule
   - Name: "Player"
   - Position: (0, 1, 0)
   - Tag: "Player" (create if doesn't exist)

2. **Add Player Components**
   ```csharp
   // Add these components to the Player capsule:
   - CharacterController (remove Capsule Collider first)
   - ModernPlayerController script
   - ModernHealth script
   ```

3. **Create Fire Point**
   - Create Empty GameObject as child of Player
   - Name: "FirePoint"
   - Position: (0, 0.5, 0.8) - slightly in front and up from player center

4. **Configure Player Controller**
   - Drag FirePoint to "Fire Point" field in ModernPlayerController
   - Set "Projectile Pool Tag" to "Projectile"

### Phase 4: Game Managers

#### Setup Core Managers
1. **Create Empty GameObject**
   - Name: "GameManagers"
   - Position: (0, 0, 0)

2. **Add Manager Scripts as Children**
   ```
   Create empty GameObjects as children of GameManagers:
   - ModernGameManager (add ModernGameManager script)
   - SettingsManager (add SettingsManager script)  
   - SaveSystem (add SaveSystem script)
   - AchievementSystem (add AchievementSystem script)
   - ParticleEffectManager (add ParticleEffectManager script)
   - ObjectPool (add ObjectPool script)
   - DemoController (add DemoController script)
   ```

#### Create GameConfig ScriptableObject
1. **Create GameConfig**
   - Right-click in Project → Create → (find GameConfig option)
   - Name: "DemoGameConfig"
   - Set values:
     - Player Max Health: 100
     - Player Move Speed: 8.0
     - (other default values)

2. **Assign to ModernGameManager**
   - Drag DemoGameConfig to "Game Config" field

### Phase 5: Collectibles

#### Create Coffee Cup Collectible
1. **Create Coffee Prefab**
   - GameObject → 3D Object → Cylinder
   - Name: "CoffeeCup"
   - Scale: (0.3, 0.4, 0.3)
   - Add brown material

2. **Configure Coffee Cup**
   - Add components:
     - BoxCollider (set as Trigger)
     - QuirkyCollectible script
   - Set Collectible Type: "CoffeeCup"
   - Set Point Value: 50

3. **Create Collectible Prefab**
   - Drag CoffeeCup from Hierarchy to Project window
   - Delete from scene (we'll place instances)

4. **Place Coffee Cups in Scene**
   - Drag CoffeeCup prefab into scene multiple times
   - Position around cubicles: (2, 1.5, 2), (-2, 1.5, 2), etc.
   - Create 8-10 coffee cups total

#### Create Golden Donut (Rare Item)
1. **Create Golden Donut**
   - GameObject → 3D Object → Torus
   - Name: "GoldenDonut"  
   - Scale: (0.5, 0.5, 0.5)
   - Add bright yellow/gold material
   - Add QuirkyCollectible script
   - Set Type: "GoldenDonut", Points: 500, Is Rare: true
   - Position: (0, 2, 0) - center of map, elevated

### Phase 6: Enemies (Red Staplers)

#### Create Possessed Stapler
1. **Create Stapler Enemy**
   - GameObject → 3D Object → Cube (placeholder)
   - Name: "RedStapler"
   - Scale: (0.8, 0.3, 0.4)
   - Add red material
   - Add components:
     - BoxCollider
     - Rigidbody
     - EnemyAI script (from your existing scripts)

2. **Configure Enemy**
   - Set to move toward player
   - Place 2-3 around the scene

### Phase 7: UI Setup

#### Create UI Canvas
1. **Create UI**
   - GameObject → UI → Canvas
   - Name: "MainUI"
   - Canvas Scaler: Scale with Screen Size

2. **Create Achievement Popup Prefab**
   - GameObject → UI → Panel (as child of Canvas)
   - Name: "AchievementPopup"
   - Add components:
     - AchievementPopup script
     - Image (for background)
     - 2x Text components (Title and Description)
   - Style with colors and fonts
   - Create as prefab, then delete from scene

3. **Create Basic HUD**
   - Add Text for Score: Top-left corner
   - Add Text for Health: Top-right corner  
   - Add Text for Time: Center-top

#### Link UI to Systems
1. **Configure AchievementSystem**
   - Drag AchievementPopup prefab to "Achievement Popup Prefab" field
   - Drag Canvas to "UI Parent" field

### Phase 8: Audio Setup (Optional)

#### Create AudioMixer
1. **Create Mixer**
   - Right-click → Create → Audio Mixer
   - Create groups: Master, Music, SFX
   - Expose parameters: "MasterVolume", "MusicVolume", "SFXVolume"

2. **Link to SettingsManager**
   - Drag AudioMixer to SettingsManager's "Audio Mixer" field

### Phase 9: Final Testing

#### Test Basic Functionality
1. **Hit Play**
2. **Test Movement** - WASD should move player
3. **Test Collecting** - Walk into coffee cups
4. **Test Achievements** - Should unlock "Baby Steps", "First Caffeine Fix"
5. **Test Pause** - ESC should pause game

#### Debug Common Issues
- **Player falls through floor**: Add Rigidbody to player, check CharacterController
- **Collectibles don't trigger**: Ensure they have trigger colliders
- **No achievements**: Check AchievementSystem has popup prefab assigned
- **Can't move**: Ensure player has CharacterController, not Rigidbody

## 🎮 You're Done!

Once set up, you'll have:
- ✅ Playable office environment
- ✅ Coffee cup collection gameplay
- ✅ Achievement system with popups
- ✅ Save/load functionality
- ✅ Settings menu support
- ✅ 2-minute survival timer

## 🚀 Next Steps

1. **Add more collectibles** using the QuirkyCollectible script
2. **Create better art assets** (or download from Asset Store)
3. **Add sound effects** and background music
4. **Polish the UI** with better fonts and styling
5. **Build and share** your corporate nightmare simulator!

---

*Remember: The staplers are always plotting against you.* 📎☕