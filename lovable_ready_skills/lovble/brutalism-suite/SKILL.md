---
name: brutalism-suite
description: Combined playbook for brutalism suite.
risk: safe
---

# Brutalism Suite

<!-- SKILL SOURCE: brutalism -->

# Brutalism

> "Raw materials exposed. An intentional rejection of polish, gradients, and soft shadows."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Unstyled Components**: Default browser styling for buttons, inputs, and links is celebrated.
2. **Exposed Structure**: Grid lines, tables with visible borders, and stark boundaries are used instead of whitespace to separate content.
3. **Anti-Aesthetic**: Intentional awkwardness. Elements might slightly overlap in a way that feels broken, or use system default fonts.

## Visual DNA
- **Colors**: High contrast, often clashing. Pure `#0000FF` blue for links, `#FF0000` red for accents, on stark white or `#C0C0C0` grey backgrounds. **Industrial Chic** palette fits best.
- **Typography**: Courier New, Times New Roman, Comic Sans, or default sans-serifs. No web fonts.
- **Visuals**: Dithered images, pixelated graphics, or heavily compressed jpegs.

## Web Implementation
- Use standard HTML tags without overriding their default appearance whenever possible.
- **CSS Example**:
```css
body {
  background-color: #ffffff;
  color: #000000;
  font-family: monospace;
}

/* Expose the structure */
.brutalist-container {
  border: 1px solid #000;
  padding: 10px;
}

.brutalist-section {
  border-bottom: 2px dashed #000;
  margin-bottom: 20px;
  padding-bottom: 20px;
}

/* Default-looking button but massive */
.brutalist-btn {
  background-color: #c0c0c0;
  border: 2px outset #ffffff;
  border-right-color: #000000;
  border-bottom-color: #000000;
  color: #000000;
  font-family: sans-serif;
  font-size: 24px;
  padding: 10px 20px;
  cursor: pointer;
}

.brutalist-btn:active {
  border-style: inset;
}

/* System link blue */
a {
  color: #0000FF;
  text-decoration: underline;
}
```

## App Implementation

### SwiftUI
```swift
struct BrutalistView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Text("BRUTALISM")
                .font(.custom("Courier New", size: 32))
                .foregroundColor(.black)
                .padding(10)
                .border(Color.black, width: 2)
            
            Divider().background(Color.black).padding(.vertical, 20)
            
            Button(action: {}) {
                Text("CLICK_HERE")
                    .font(.custom("Courier New", size: 24))
                    .foregroundColor(.blue)
                    .underline()
            }
            .padding(10)
            
            // Raw structural container
            VStack(alignment: .leading) {
                Text("System Status: RAW").font(.custom("Courier New", size: 14))
            }
            .padding()
            .border(Color.black, width: 1)
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
        .background(Color.white)
    }
}
```
- Avoid all native `ButtonStyle` components. Use `Text` with `.underline()` mapped to system blue.
- Use `.border(Color.black, width: 1)` instead of backgrounds or shadows.
- Force monospace fonts like Courier New or Menlo.

### Flutter
```dart
class BrutalistScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // DO NOT use MaterialApp theme or Scaffold if possible,
    // or strip them down completely.
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.black, width: 2),
                ),
                child: const Text(
                  'BRUTALISM',
                  style: TextStyle(
                    fontFamily: 'Courier',
                    fontSize: 32,
                    color: Colors.black,
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 20),
                child: Divider(color: Colors.black, thickness: 2),
              ),
              GestureDetector(
                onTap: () {},
                child: const Text(
                  'CLICK_HERE',
                  style: TextStyle(
                    fontFamily: 'Courier',
                    fontSize: 24,
                    color: Colors.blue,
                    decoration: TextDecoration.underline,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
- Avoid `ElevatedButton`, `Card`, or `AppBar`.
- Build UI out of raw `Container`s with `Border.all(color: Colors.black)` and `Text` widgets.
- Use `TextDecoration.underline` to indicate interactivity.

### React Native
```jsx
const BrutalistScreen = () => {
  return (
    <View style={{ flex: 1, backgroundColor: '#FFFFFF', padding: 16 }}>
      <View style={{
        borderWidth: 2,
        borderColor: '#000000',
        padding: 10,
        alignSelf: 'flex-start'
      }}>
        <Text style={{ fontFamily: 'monospace', fontSize: 32, color: '#000' }}>
          BRUTALISM
        </Text>
      </View>
      
      <View style={{ height: 2, backgroundColor: '#000', marginVertical: 20 }} />
      
      <TouchableOpacity activeOpacity={1}>
        <Text style={{
          fontFamily: 'monospace',
          fontSize: 24,
          color: '#0000FF',
          textDecorationLine: 'underline'
        }}>
          CLICK_HERE
        </Text>
      </TouchableOpacity>

      <View style={{
        borderWidth: 1,
        borderColor: '#000',
        padding: 16,
        marginTop: 40
      }}>
        <Text style={{ fontFamily: 'monospace', color: '#000' }}>
          System Status: RAW
        </Text>
      </View>
    </View>
  );
};
```
- Strip away all native feel. Do not use `react-native-elements` or `react-native-paper`.
- Set `activeOpacity={1}` on `TouchableOpacity` so there is no smooth fade — it should just click instantly.
- Use pure hex colors: `#FFFFFF`, `#000000`, `#0000FF`.

### Jetpack Compose
```kotlin
@Composable
fun BrutalistScreen() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White)
            .padding(16.dp)
    ) {
        Box(
            modifier = Modifier
                .border(2.dp, Color.Black)
                .padding(10.dp)
        ) {
            BasicText(
                text = "BRUTALISM",
                style = TextStyle(
                    fontFamily = FontFamily.Monospace,
                    fontSize = 32.sp,
                    color = Color.Black
                )
            )
        }
        
        Spacer(Modifier.height(20.dp))
        Box(modifier = Modifier.fillMaxWidth().height(2.dp).background(Color.Black))
        Spacer(Modifier.height(20.dp))
        
        BasicText(
            text = "CLICK_HERE",
            modifier = Modifier.clickable { },
            style = TextStyle(
                fontFamily = FontFamily.Monospace,
                fontSize = 24.sp,
                color = Color.Blue,
                textDecoration = TextDecoration.Underline
            )
        )
    }
}
```
- Use `BasicText` instead of `Text` to bypass Material theme defaults.
- Build structural lines using `Box` with `.background(Color.Black)`.
- **Do not** use `Button` or `Card` or any Material composables. Raw layouts only.

## Do's and Don'ts
- **DO**: Use harsh, high-contrast borders (1px solid black) around everything.
- **DON'T**: Use border-radius, drop shadows, or smooth transitions. If it animates, it should pop instantly (0s transition).

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

<!-- SKILL SOURCE: brutalist-skill -->

# SKILL: Industrial Brutalism & Tactical Telemetry UI

## 1. Skill Meta
**Name:** Industrial Brutalism & Tactical Telemetry Interface Engineering
**Description:** Advanced proficiency in architecting web interfaces that synthesize mid-century Swiss Typographic design, industrial manufacturing manuals, and retro-futuristic aerospace/military terminal interfaces. This discipline requires absolute mastery over rigid modular grids, extreme typographic scale contrast, purely utilitarian color palettes, and the programmatic simulation of analog degradation (halftones, CRT scanlines, bitmap dithering). The objective is to construct digital environments that project raw functionality, mechanical precision, and high data density, deliberately discarding conventional consumer UI patterns.

## 2. Visual Archetypes
The design system operates by merging two distinct but highly compatible visual paradigms. **Pick ONE per project and commit to it. Do not alternate or mix both modes within the same interface.**

### 2.1 Swiss Industrial Print
Derived from 1960s corporate identity systems and heavy machinery blueprints.
*   **Characteristics:** High-contrast light modes (newsprint/off-white substrates). Reliance on monolithic, heavy sans-serif typography. Unforgiving structural grids outlined by visible dividing lines. Aggressive, asymmetric use of negative space punctuated by oversized, viewport-bleeding numerals or letterforms. Heavy use of primary red as an alert/accent color.

### 2.2 Tactical Telemetry & CRT Terminal
Derived from classified military databases, legacy mainframes, and aerospace Heads-Up Displays (HUDs).
*   **Characteristics:** Dark mode exclusivity. High-density tabular data presentation. Absolute dominance of monospaced typography. Integration of technical framing devices (ASCII brackets, crosshairs). Application of simulated hardware limitations (phosphor glow, scanlines, low bit-depth rendering).

## 3. Typographic Architecture
Typography is the primary structural and decorative infrastructure. Imagery is secondary. The system demands extreme variance in scale, weight, and spacing.

### 3.1 Macro-Typography (Structural Headers)
*   **Classification:** Neo-Grotesque / Heavy Sans-Serif.
*   **Optimal Web Fonts:** Neue Haas Grotesk (Black), Inter (Extra Bold/Black), Archivo Black, Roboto Flex (Heavy), Monument Extended.
*   **Implementation Parameters:**
    *   **Scale:** Deployed at massive scales using fluid typography (e.g., `clamp(4rem, 10vw, 15rem)`).
    *   **Tracking (Letter-spacing):** Extremely tight, often negative (`-0.03em` to `-0.06em`), forcing glyphs to form solid architectural blocks.
    *   **Leading (Line-height):** Highly compressed (`0.85` to `0.95`).
    *   **Casing:** Exclusively uppercase for structural impact.

### 3.2 Micro-Typography (Data & Telemetry)
*   **Classification:** Monospace / Technical Sans.
*   **Optimal Web Fonts:** JetBrains Mono, IBM Plex Mono, Space Mono, VT323, Courier Prime.
*   **Implementation Parameters:**
    *   **Scale:** Fixed and small (`10px` to `14px` / `0.7rem` to `0.875rem`).
    *   **Tracking:** Generous (`0.05em` to `0.1em`) to simulate mechanical typewriter spacing or terminal matrices.
    *   **Leading:** Standard to tight (`1.2` to `1.4`).
    *   **Casing:** Exclusively uppercase. Used for all metadata, navigation, unit IDs, and coordinates.

### 3.3 Textural Contrast (Artistic Disruption)
*   **Classification:** High-Contrast Serif.
*   **Optimal Web Fonts:** Playfair Display, EB Garamond, Times New Roman.
*   **Implementation Parameters:** Used exceedingly sparingly. Must be subjected to heavy post-processing (halftone filters, 1-bit dithering) to degrade vector perfection and create textural juxtaposition against the clean sans-serifs.

## 4. Color System
The color architecture is uncompromising. Gradients, soft drop shadows, and modern translucency are strictly prohibited. Colors simulate physical media or primitive emissive displays.

**CRITICAL: Choose ONE substrate palette per project and use it consistently. Never mix light and dark substrates within the same interface.**

### If Swiss Industrial Print (Light):
*   **Background:** `#F4F4F0` or `#EAE8E3` (Matte, unbleached documentation paper).
*   **Foreground:** `#050505` to `#111111` (Carbon Ink).
*   **Accent:** `#E61919` or `#FF2A2A` (Aviation/Hazard Red). This is the ONLY accent color. Used for strike-throughs, thick structural dividing lines, or vital data highlights.

### If Tactical Telemetry (Dark):
*   **Background:** `#0A0A0A` or `#121212` (Deactivated CRT. Avoid pure `#000000`).
*   **Foreground:** `#EAEAEA` (White phosphor). This is the primary text color.
*   **Accent:** `#E61919` or `#FF2A2A` (Aviation/Hazard Red). Same red, same rules.
*   **Terminal Green (`#4AF626`):** Optional. Use ONLY for a single specific UI element (e.g., one status indicator or one data readout) — never as a general text color. If it doesn't serve a clear purpose, omit it entirely.

## 5. Layout and Spatial Engineering
The layout must appear mathematically engineered. It rejects conventional web padding in favor of visible compartmentalization.

*   **The Blueprint Grid:** Strict adherence to CSS Grid architectures. Elements do not float; they are anchored precisely to grid tracks and intersections.
*   **Visible Compartmentalization:** Extensive utilization of solid borders (`1px` or `2px solid`) to delineate distinct zones of information. Horizontal rules (`<hr>`) frequently span the entire container width to segregate operational units.
*   **Bimodal Density:** Layouts oscillate between extreme data density (tightly packed monospace metadata clustered together) and vast expanses of calculated negative space framing macro-typography.
*   **Geometry:** Absolute rejection of `border-radius`. All corners must be exactly 90 degrees to enforce mechanical rigidity.

## 6. UI Components and Symbology
Standard web UI conventions are replaced with utilitarian, industrial graphic elements.

*   **Syntax Decoration:** Utilization of ASCII characters to frame data points.
    *   *Framing:* `[ DELIVERY SYSTEMS ]`, `< RE-IND >`
    *   *Directional:* `>>>`, `///`, `\\\\`
*   **Industrial Markers:** Prominent integration of registration (`®`), copyright (`©`), and trademark (`™`) symbols functioning as structural geometric elements rather than legal text.
*   **Technical Assets:** Integration of crosshairs (`+`) at grid intersections, repeating vertical lines (barcodes), thick horizontal warning stripes, and randomized string data (e.g., `REV 2.6`, `UNIT / D-01`) to simulate active mechanical processes.

## 7. Textural and Post-Processing Effects
To prevent the design from appearing purely digital, simulated analog degradation is engineered into the frontend via CSS and SVG filters.

*   **Halftone and 1-Bit Dithering:** Transforming continuous-tone images or large serif typography into dot-matrix patterns. Achieved via pre-processing or CSS `mix-blend-mode: multiply` overlays combined with SVG radial dot patterns.
*   **CRT Scanlines:** For terminal interfaces, applying a `repeating-linear-gradient` to the background to simulate horizontal electron beam sweeps (e.g., `repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px)`).
*   **Mechanical Noise:** A global, low-opacity SVG static/noise filter applied to the DOM root to introduce a unified physical grain across both dark and light modes.

## 8. Web Engineering Directives
1.  **Grid Determinism:** Utilize `display: grid; gap: 1px;` with contrasting parent/child background colors to generate mathematically perfect, razor-thin dividing lines without complex border declarations.
2.  **Semantic Rigidity:** Construct the DOM using precise semantic tags (`<data>`, `<samp>`, `<kbd>`, `<output>`, `<dl>`) to accurately reflect the technical nature of the telemetry.
3.  **Typography Clamping:** Implement CSS `clamp()` functions exclusively for macro-typography to ensure massive text scales aggressively while maintaining structural integrity across viewports.

---

<!-- SKILL SOURCE: brutalist-typography -->

# Brutalist Typography

> "Aggressive, unpolished, and unapologetic. Text that demands attention by breaking the rules."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Rule Breaking**: Text that overlaps, ignores margins, or deliberately clips off the edge of the screen.
2. **Anti-Design**: Intentional use of system fonts or "ugly" fonts (Times New Roman, Courier) in massive sizes.
3. **Harsh Contrast**: Clashing colors or stark monochrome.

## Visual DNA
- **Colors**: **Industrial Chic** (Black, White, Red) or aggressive neon clashing (e.g., pure blue on pure red).
- **Typography**: System default fonts (`Times New Roman`, `Arial`, `Courier New`) blown up to 150px.
- **Styling**: Marquees, blinking text, underlines that cut through descenders.

## Web Implementation
- Break the grid. Use absolute positioning or negative margins.
- **CSS Example**:
```css
body {
  background-color: #fff;
  color: #000;
  font-family: 'Times New Roman', serif;
}

.brutalist-headline {
  font-size: 15vw;
  line-height: 0.7;
  letter-spacing: -5px;
  margin-left: -10px; /* Bleeds off screen intentionally */
  word-wrap: break-word; /* Let words break awkwardly */
}

.brutalist-highlight {
  background-color: #ff0000;
  color: #fff;
  padding: 0 10px;
}

.marquee-container {
  border-top: 5px solid #000;
  border-bottom: 5px solid #000;
  overflow: hidden;
  white-space: nowrap;
  font-family: 'Courier New', monospace;
  font-size: 2rem;
  font-weight: bold;
  padding: 10px 0;
}

/* A nod to early 90s web */
.brutalist-link {
  color: #0000ee;
  text-decoration: underline;
  text-transform: uppercase;
}
.brutalist-link:hover {
  background-color: #0000ee;
  color: #fff;
}
```

## App Implementation

### SwiftUI
```swift
struct BrutalistTypeView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: -20) {
                // Bleeds off the edge intentionally
                Text("BREAK")
                    .font(.custom("Times New Roman", size: 120))
                    .padding(.leading, -20) 
                
                Text("THE")
                    .font(.custom("Arial", size: 140))
                    .fontWeight(.black)
                    .foregroundColor(.clear)
                    .overlay(
                        Text("THE").stroke(Color.red, lineWidth: 3)
                    )
                    .offset(x: 40)
                
                Text("GRID.")
                    .font(.custom("Courier New", size: 100))
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .rotationEffect(.degrees(-5))
                    .offset(y: -40)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(.top, 50)
        }
        .ignoresSafeArea() // Critical for Brutalist type
        .background(Color.white)
    }
}
```
- `.ignoresSafeArea()` is mandatory. Text must be allowed to clip into the notch and status bar.
- Use negative `spacing` in `VStack` or explicit negative `.offset()` to force text elements to overlap each other aggressively.
- Outline text is achieved by setting `.foregroundColor(.clear)` and overlaying a `.stroke()`.

### Flutter
```dart
class BrutalistTypeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Scaffold without SafeArea
    return Scaffold(
      backgroundColor: Colors.white,
      body: Stack(
        children: [
          Positioned(
            top: -20,
            left: -20,
            child: const Text(
              'BREAK',
              style: TextStyle(
                fontFamily: 'Times New Roman',
                fontSize: 150,
                height: 0.8, // Negative line-spacing
                color: Colors.black,
              ),
            ),
          ),
          Positioned(
            top: 100,
            left: 40,
            child: Text(
              'THE',
              style: TextStyle(
                fontFamily: 'Arial',
                fontSize: 140,
                fontWeight: FontWeight.w900,
                foreground: Paint()
                  ..style = PaintingStyle.stroke
                  ..strokeWidth = 3
                  ..color = Colors.red,
              ),
            ),
          ),
          Positioned(
            top: 220,
            left: 10,
            child: Transform.rotate(
              angle: -0.1,
              child: Container(
                color: Colors.blue,
                child: const Text(
                  'GRID.',
                  style: TextStyle(
                    fontFamily: 'Courier',
                    fontSize: 120,
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
```
- Do not use `SafeArea`.
- Absolute positioning via `Stack` and `Positioned` is the easiest way to break the grid and force overlaps.
- Use `height: 0.8` (or less than 1.0) in `TextStyle` to smash lines of text together.

### React Native
```jsx
const BrutalistTypeScreen = () => {
  return (
    <View style={{ flex: 1, backgroundColor: '#FFF' }}>
      {/* 
        Note: React Native text clipping can be tricky on Android. 
        Ensure parent views don't have overflow: 'hidden'.
      */}
      <Text style={{
        fontFamily: 'Times New Roman',
        fontSize: 130,
        lineHeight: 110,
        color: '#000',
        marginLeft: -15, // Bleed off edge
        marginTop: 40
      }}>
        BREAK
      </Text>
      
      <Text style={{
        fontFamily: 'Arial',
        fontSize: 140,
        fontWeight: '900',
        color: 'transparent',
        textShadowColor: '#FF0000',
        textShadowRadius: 1, // Fake stroke effect
        marginLeft: 40,
        marginTop: -30 // Overlap previous text
      }}>
        THE
      </Text>
      
      <Text style={{
        fontFamily: 'monospace',
        fontSize: 100,
        backgroundColor: '#0000FF',
        color: '#FFF',
        transform: [{ rotate: '-5deg' }],
        marginTop: -20,
        alignSelf: 'flex-start'
      }}>
        GRID.
      </Text>
    </View>
  );
};
```
- React Native doesn't have a native text-stroke property, so you either simulate it with text shadows or use `@shopify/react-native-skia` for true stroked text.
- Use negative `marginTop` and `marginLeft` to force the layout chaos.

### Jetpack Compose
```kotlin
@Composable
fun BrutalistTypeScreen() {
    // Use Box for absolute overlapping layouts
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White)
    ) {
        Text(
            text = "BREAK",
            fontFamily = FontFamily.Serif, // Times New Roman equivalent
            fontSize = 130.sp,
            color = Color.Black,
            lineHeight = 100.sp,
            modifier = Modifier.offset(x = (-15).dp, y = (-20).dp)
        )
        
        Text(
            text = "THE",
            fontFamily = FontFamily.SansSerif,
            fontSize = 140.sp,
            fontWeight = FontWeight.Black,
            style = TextStyle(
                drawStyle = Stroke(width = 5f)
            ),
            color = Color.Red,
            modifier = Modifier.offset(x = 40.dp, y = 100.dp)
        )
        
        Text(
            text = "GRID.",
            fontFamily = FontFamily.Monospace,
            fontSize = 100.sp,
            color = Color.White,
            modifier = Modifier
                .offset(x = 10.dp, y = 220.dp)
                .rotate(-5f)
                .background(Color.Blue)
        )
    }
}
```
- A `Box` with explicit `Modifier.offset(x, y)` allows freeform overlapping placement, breaking away from standard `Column`/`Row` grids.
- Compose `TextStyle` supports `drawStyle = Stroke(width = 5f)`, making outline typography incredibly simple.

## Do's and Don'ts
- **DO**: Mix serif and monospace fonts aggressively.
- **DON'T**: Add drop shadows, gradients, or rounded corners. The design must look raw and unstyled.

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

<!-- SKILL SOURCE: neo-brutalism -->

# Neo-Brutalism

> "Brutalism, but make it pop. Hard lines, stark shadows, and vibrant, unashamed colors."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Hard Drop Shadows**: Solid black shadows with no blur. Usually offset by a few pixels down and to the right.
2. **Thick Outlines**: Everything has a heavy, solid black border (usually 2px-4px).
3. **Flat, High-Contrast Colors**: Bright, saturated pastels or primary colors contrasting against pure white or black.

## Visual DNA
- **Colors**: Start with an off-white background (like `#FDF8F5`), add stark black borders `#000000`, and use saturated accents like lemon yellow, bright cyan, or coral.
- **Typography**: Very bold, geometric sans-serifs (e.g., `Space Grotesk`, `Archivo Black`, `Inter Black`).
- **Shapes**: Sharp rectangles or completely rounded pill shapes, but always with a heavy stroke.

## Web Implementation
- The defining feature is the `box-shadow` with `0` blur.
- **CSS Example**:
```css
:root {
  --neo-border: 3px solid #000000;
  --neo-shadow: 6px 6px 0px #000000;
  --neo-bg: #F4F4F0;
  --neo-accent: #FF3366;
}

body {
  background-color: var(--neo-bg);
  font-family: 'Space Grotesk', sans-serif;
}

.neo-card {
  background-color: #ffffff;
  border: var(--neo-border);
  box-shadow: var(--neo-shadow);
  border-radius: 8px; /* Optional, sharp is fine too */
  padding: 32px;
  transition: transform 0.1s, box-shadow 0.1s;
}

.neo-btn {
  background-color: var(--neo-accent);
  color: #000;
  font-weight: 800;
  text-transform: uppercase;
  border: var(--neo-border);
  box-shadow: 4px 4px 0px #000000;
  padding: 16px 32px;
  cursor: pointer;
  transition: all 0.1s ease;
}

.neo-btn:active {
  /* The "press" effect is removing the shadow and moving it down */
  transform: translate(4px, 4px);
  box-shadow: 0px 0px 0px #000000;
}
```

## App Implementation

### SwiftUI
```swift
struct NeoCard: View {
    @State private var isPressed = false
    let neoBorder: CGFloat = 3
    let neoShadow: CGFloat = 6
    
    var body: some View {
        Button(action: {}) {
            VStack(alignment: .leading, spacing: 16) {
                Text("NEO-BRUTALISM")
                    .font(.system(size: 24, weight: .black, design: .default))
                    .foregroundColor(.black)
                Text("Stark shadows, bright colors.")
                    .font(.system(size: 16, weight: .bold))
                    .foregroundColor(.black)
            }
            .padding(24)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Color(red: 1.0, green: 0.2, blue: 0.4)) // Bright Coral
            // Neo-brutalist solid outline
            .overlay(
                Rectangle()
                    .stroke(Color.black, lineWidth: neoBorder)
            )
        }
        .buttonStyle(.plain)
        // Hard drop shadow (0 blur)
        .shadow(color: .black, radius: 0, x: isPressed ? 0 : neoShadow, y: isPressed ? 0 : neoShadow)
        // Translate the button physically when pressed to cover the shadow
        .offset(x: isPressed ? neoShadow : 0, y: isPressed ? neoShadow : 0)
        .simultaneousGesture(
            DragGesture(minimumDistance: 0)
                .onChanged { _ in isPressed = true }
                .onEnded { _ in isPressed = false }
        )
        // Instant pop, no smooth animation
        .animation(.none, value: isPressed)
    }
}
```
- `.shadow(radius: 0)` is the secret. Set an offset (e.g. `x: 6, y: 6`).
- For interactions, remove the shadow and translate the element by the same offset amounts using `.offset()`.
- Ensure `.animation(.none)` — Neo-brutalism interactions should be instant, snapping like physical switches.

### Flutter
```dart
class NeoCard extends StatefulWidget {
  @override
  State<NeoCard> createState() => _NeoCardState();
}

class _NeoCardState extends State<NeoCard> {
  bool _isPressed = false;
  final double neoOffset = 6.0;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTapDown: (_) => setState(() => _isPressed = true),
      onTapUp: (_) => setState(() => _isPressed = false),
      onTapCancel: () => setState(() => _isPressed = false),
      child: Transform.translate(
        // Move the container when pressed
        offset: Offset(_isPressed ? neoOffset : 0, _isPressed ? neoOffset : 0),
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: const Color(0xFFFF3366), // Bright coral
            border: Border.all(color: Colors.black, width: 3),
            // Sharp shadow disappears on press
            boxShadow: _isPressed ? [] : [
              BoxShadow(
                color: Colors.black,
                blurRadius: 0,     // Critical: 0 blur
                spreadRadius: 0,
                offset: Offset(neoOffset, neoOffset),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: const [
              Text('NEO-BRUTALISM',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w900, color: Colors.black)),
              SizedBox(height: 16),
              Text('Stark shadows, bright colors.',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black)),
            ],
          ),
        ),
      ),
    );
  }
}
```
- `blurRadius: 0` inside `BoxShadow` creates the solid block color.
- Remove the shadow array entirely when `_isPressed` is true, and simultaneously use `Transform.translate` to shift the widget down-right.

### React Native
```jsx
const NeoCard = () => {
  const [pressed, setPressed] = useState(false);
  const offset = 6;

  return (
    <Pressable
      onPressIn={() => setPressed(true)}
      onPressOut={() => setPressed(false)}
      style={{
        backgroundColor: '#FF3366',
        padding: 24,
        borderWidth: 3,
        borderColor: '#000',
        transform: [
          { translateX: pressed ? offset : 0 },
          { translateY: pressed ? offset : 0 }
        ],
        // iOS Hard Shadow
        shadowColor: '#000',
        shadowOffset: { width: pressed ? 0 : offset, height: pressed ? 0 : offset },
        shadowOpacity: pressed ? 0 : 1,
        shadowRadius: 0,
        // Android elevation cannot do 0-blur offset shadows natively
        // elevation: 0
      }}
    >
      <Text style={{ fontSize: 24, fontWeight: '900', color: '#000' }}>
        NEO-BRUTALISM
      </Text>
    </Pressable>
  );
};
```
- **Android Limitation**: Standard `elevation` CANNOT create an unblurred, offset drop shadow. 
- **Solution**: To make this work on Android, you MUST use the `react-native-drop-shadow` library or fake it by rendering an identical black `<View>` absolutely positioned directly behind the main card.

### Jetpack Compose
```kotlin
@Composable
fun NeoCard() {
    var isPressed by remember { mutableStateOf(false) }
    val neoOffset = 6.dp
    
    // Compose Modifier.shadow() always blurs. 
    // To get a solid hard shadow, we use Modifier.drawBehind.
    Box(
        modifier = Modifier
            .padding(16.dp)
            .offset(
                x = if (isPressed) neoOffset else 0.dp,
                y = if (isPressed) neoOffset else 0.dp
            )
            .drawBehind {
                if (!isPressed) {
                    drawRect(
                        color = Color.Black,
                        topLeft = Offset(neoOffset.toPx(), neoOffset.toPx()),
                        size = size
                    )
                }
            }
            .background(Color(0xFFFF3366))
            .border(3.dp, Color.Black)
            .pointerInput(Unit) {
                detectTapGestures(
                    onPress = {
                        isPressed = true
                        tryAwaitRelease()
                        isPressed = false
                    }
                )
            }
            .padding(24.dp)
    ) {
        Column {
            Text("NEO-BRUTALISM",
                fontSize = 24.sp, fontWeight = FontWeight.Black, color = Color.Black)
            Spacer(Modifier.height(16.dp))
            Text("Stark shadows, bright colors.",
                fontSize = 16.sp, fontWeight = FontWeight.Bold, color = Color.Black)
        }
    }
}
```
- **Compose Limitation**: Native `Modifier.shadow()` applies ambient blur which breaks the neo-brutalist aesthetic.
- Use `Modifier.drawBehind { drawRect(...) }` with an offset to manually draw the solid shadow block behind the container.
- Shift the container using `Modifier.offset` on press, while hiding the shadow layer.

## Do's and Don'ts
- **DO**: Make the active/pressed state visually translate the button to cover its shadow, creating a physical "click" feel.
- **DON'T**: Use gradients or blurred shadows. The aesthetic relies entirely on flat, sharp vectors.

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

