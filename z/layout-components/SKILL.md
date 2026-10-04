---
name: layout-components
description: Combined playbook for layout components.
risk: safe
---

# Layout Components

<!-- SKILL SOURCE: layout-grid -->

# Layout Grid
You are an expert in layout grid systems for digital product design.
## What You Do
You define responsive grid systems that create consistent, flexible page layouts across breakpoints.
## Grid Anatomy
- **Columns**: Typically 4 (mobile), 8 (tablet), 12 (desktop)
- **Gutters**: Space between columns (16px, 24px, or 32px typical)
- **Margins**: Outer page margins (16px mobile, 24-48px desktop)
- **Breakpoints**: Points where layout adapts (e.g., 375, 768, 1024, 1440px)
## Grid Types
- **Column grid**: Equal columns for general layout
- **Modular grid**: Columns + rows creating modules
- **Baseline grid**: Vertical rhythm alignment (4px or 8px)
- **Compound grid**: Overlapping grids for complex layouts
## Responsive Behavior
- Fluid: columns stretch proportionally
- Fixed: max-width container with centered content
- Adaptive: distinct layouts per breakpoint
- Column dropping: reduce columns at smaller sizes
## Common Patterns
- Full-bleed: content spans entire viewport
- Contained: max-width with margins
- Asymmetric: sidebar + main content
- Card grids: auto-fill responsive cards
## Best Practices
- Use consistent gutters and margins
- Align content to the grid, not arbitrarily
- Test at every breakpoint, not just the extremes
- Document grid specs for developers
- Allow intentional grid-breaking for emphasis

---

<!-- SKILL SOURCE: layered-design -->

# Layered Design

> "Stacking context. Interfaces built from overlapping, independent layers."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Explicit Overlap**: Elements intentionally overlap each other to break the grid and show depth.
2. **Clear Stratification**: Every layer must be visually distinct via shadow, border, or contrasting color.
3. **Parallax Scrolling**: Background layers move slower than foreground layers during interaction/scrolling.

## Visual DNA
- **Colors**: **Monochromatic Brown** or **Sophisticated Neutral**. Layering works best when the background is distinct from the floating elements.
- **Typography**: Often large, overlapping text that spans across image and background layers.
- **Spacing**: Negative space is required around overlapping elements so they don't feel cluttered.

## Web Implementation
- Heavy use of `position: absolute`, negative margins, and `z-index`.
- **CSS Example**:
```css
.layer-container {
  position: relative;
  padding: 100px;
}

.layer-bg-image {
  position: absolute;
  top: 0; right: 0;
  width: 60%;
  height: 400px;
  object-fit: cover;
  z-index: 1;
}

.layer-text-box {
  position: relative;
  z-index: 2; /* Sits above the image */
  background: white;
  padding: 40px;
  width: 50%;
  margin-top: 200px; /* Pulls it down over the image */
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  /* Optional: border to define edge */
  border-left: 4px solid var(--cta-highlight);
}
```

## App Implementation

### SwiftUI
```swift
struct LayeredDesignView: View {
    var body: some View {
        ScrollView {
            ZStack(alignment: .top) {
                // Background Image Layer (Back)
                Image("architectural-bg")
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(height: 400)
                    .offset(x: 40, y: 0) // Shifted right
                    .zIndex(1)
                
                // Content Card Layer (Front)
                VStack(alignment: .leading, spacing: 16) {
                    Text("Stacking Context")
                        .font(.largeTitle).bold()
                    Text("This card intentionally overlaps the background image to create depth without relying on a grid.")
                        .foregroundColor(.secondary)
                }
                .padding(40)
                .background(Color.white)
                .shadow(color: Color.black.opacity(0.1), radius: 30, y: 20)
                .offset(x: -40, y: 200) // Shifted left and pulled down
                .zIndex(2)
            }
            .padding(.bottom, 200) // Account for the offset
        }
    }
}
```
- `ZStack` is the foundation of layered design in SwiftUI.
- Use `.offset()` to intentionally break the alignment and create overlapping compositions.
- Explicitly set `.zIndex()` if your offsets might cause unexpected paint orders.

### Flutter
```dart
class LayeredDesignScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: SizedBox(
          height: 600, // Fixed height stack or use constraints
          child: Stack(
            children: [
              // Background Image Layer
              Positioned(
                top: 0,
                right: -40, // Shifted offscreen right
                width: MediaQuery.of(context).size.width * 0.8,
                height: 400,
                child: Image.asset('assets/architectural-bg.jpg', fit: BoxFit.cover),
              ),
              
              // Content Card Layer
              Positioned(
                top: 250, // Overlaps the bottom of the image
                left: 20, // Overlaps the left of the image
                width: MediaQuery.of(context).size.width * 0.7,
                child: Container(
                  padding: const EdgeInsets.all(40),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    boxShadow: [
                      BoxShadow(color: Colors.black.withOpacity(0.1), blurRadius: 30, offset: const Offset(0, 20))
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: const [
                      Text('Stacking Context', style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
                      SizedBox(height: 16),
                      Text('This card intentionally overlaps the background image.', style: TextStyle(color: Colors.grey)),
                    ],
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
- The `Stack` widget with `Positioned` children is required.
- You can use negative values in `Positioned` (e.g., `right: -40`) to bleed layers off the edge of the screen, which is a common trope in layered design.

### React Native
```jsx
const LayeredDesignScreen = () => {
  return (
    <ScrollView style={{ flex: 1, backgroundColor: '#F8F8F8' }}>
      <View style={{ height: 600 }}>
        
        {/* Background Image Layer */}
        <Image 
          source={{ uri: 'https://example.com/architectural-bg.jpg' }}
          style={{
            position: 'absolute',
            top: 0,
            right: -40,
            width: '80%',
            height: 400,
            zIndex: 1,
          }}
        />

        {/* Content Card Layer */}
        <View style={{
          position: 'absolute',
          top: 250,
          left: 20,
          width: '70%',
          backgroundColor: '#FFF',
          padding: 40,
          zIndex: 2,
          // Deep shadow to separate the layers
          shadowColor: '#000', shadowOffset: { width: 0, height: 20 },
          shadowOpacity: 0.1, shadowRadius: 30, elevation: 15,
        }}>
          <Text style={{ fontSize: 32, fontWeight: 'bold', marginBottom: 16 }}>Stacking Context</Text>
          <Text style={{ color: '#666' }}>This card intentionally overlaps the background image.</Text>
        </View>

      </View>
    </ScrollView>
  );
};
```
- Heavy use of `position: 'absolute'` inside a relative container.
- Manage `zIndex` explicitly. Note that on Android, `elevation` also controls Z-indexing, so the card must have a higher `elevation` than the image.

### Jetpack Compose
```kotlin
@Composable
fun LayeredDesignScreen() {
    Column(modifier = Modifier.verticalScroll(rememberScrollState())) {
        Box(modifier = Modifier.height(600.dp).fillMaxWidth()) {
            
            // Background Image Layer
            Image(
                painter = painterResource(id = R.drawable.architectural_bg),
                contentDescription = null,
                contentScale = ContentScale.Crop,
                modifier = Modifier
                    .align(Alignment.TopEnd)
                    .offset(x = 40.dp) // Bleed off right edge
                    .width(300.dp)
                    .height(400.dp)
                    .zIndex(1f)
            )
            
            // Content Card Layer
            Box(
                modifier = Modifier
                    .align(Alignment.TopStart)
                    .offset(x = 20.dp, y = 250.dp) // Overlap the image
                    .width(280.dp)
                    .zIndex(2f)
                    .shadow(30.dp)
                    .background(Color.White)
                    .padding(40.dp)
            ) {
                Column {
                    Text("Stacking Context", fontSize = 32.sp, fontWeight = FontWeight.Bold)
                    Spacer(Modifier.height(16.dp))
                    Text("This card intentionally overlaps the background image.", color = Color.Gray)
                }
            }
        }
    }
}
```
- `Box` acts as your stack.
- Use `Modifier.align()` to set the baseline position, then `Modifier.offset()` to push it out of grid alignment.
- `Modifier.zIndex()` ensures the content card always renders on top of the image.

## Do's and Don'ts
- **DO**: Use contrasting colors or drop shadows where layers intersect so the boundary is clear.
- **DON'T**: Trap interactive elements (like buttons) underneath other layers where they cannot be clicked.

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

<!-- SKILL SOURCE: card-based-design -->

# Card-Based Design

> "Bite-sized consumption. Encapsulating discrete pieces of information into distinct visual containers."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Encapsulation**: Every card is self-contained. It has an image, a title, a short description, and usually an action (like a button or a 'like' icon).
2. **Responsive Flow**: Cards easily reflow on different screen sizes (from a 4-column grid on desktop to a single column on mobile).
3. **Clear Boundaries**: Cards must visually pop off the background.

## Visual DNA
- **Colors**: Very flexible. The background should be slightly darker or distinct from the card color. **Sophisticated Neutral** works well for a premium feel.
- **Typography**: Clear hierarchy within the card (Header, Subheader, Body).
- **Styling**: Standard `border-radius: 8px` and a medium drop shadow.

## Web Implementation
- CSS Grid with `auto-fit` or a Masonry layout.
- **CSS Example**:
```css
body {
  background-color: #f0f2f5; /* Standard app background */
  padding: 40px;
}

.card-grid {
  display: grid;
  /* Auto-responsive magic */
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.card {
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden; /* Keep images inside the rounded corners */
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.card-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-bottom: 1px solid #eee;
}

.card-content {
  padding: 20px;
  flex-grow: 1; /* Pushes footer to the bottom */
}

.card-footer {
  padding: 16px 20px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: space-between;
}
```

## App Implementation

### SwiftUI
```swift
struct ContentCard: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Image Area
            Rectangle()
                .fill(Color.gray.opacity(0.2))
                .frame(height: 160)
            
            // Content Area
            VStack(alignment: .leading, spacing: 8) {
                Text("Card Title")
                    .font(.headline)
                Text("A brief description of the content inside this discrete card container.")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .lineLimit(2)
            }
            .padding(16)
        }
        .background(Color.white)
        .cornerRadius(12)
        // Clean, subtle drop shadow
        .shadow(color: Color.black.opacity(0.08), radius: 12, x: 0, y: 4)
    }
}

// In your view:
// LazyVGrid(columns: [GridItem(.adaptive(minimum: 160), spacing: 16)]) { ... }
```
- `VStack` inside a background with `.cornerRadius` and `.shadow` is the standard.
- Use `LazyVGrid` with `.adaptive(minimum: 160)` to automatically create a multi-column card grid that flows perfectly on iPad or iPhone.

### Flutter
```dart
class ContentCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4, // Handles shadow natively
      shadowColor: Colors.black.withOpacity(0.4),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      clipBehavior: Clip.antiAlias, // Critical: stops images from bleeding over corners
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          // Image Area
          Container(
            height: 160,
            color: Colors.grey[300],
            width: double.infinity,
          ),
          // Content Area
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Card Title', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18)),
                SizedBox(height: 8),
                Text(
                  'A brief description of the content inside this discrete card container.',
                  style: TextStyle(color: Colors.black54),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
// In your view: Use GridView.builder for the layout
```
- The native `Card` widget does almost all the heavy lifting.
- **Critical fix**: You must set `clipBehavior: Clip.antiAlias` on the `Card`, otherwise the top corners of your images will peek outside the border radius.

### React Native
```jsx
const ContentCard = () => {
  return (
    <View style={styles.card}>
      <View style={styles.imageArea} />
      <View style={styles.contentArea}>
        <Text style={styles.title}>Card Title</Text>
        <Text style={styles.description} numberOfLines={2}>
          A brief description of the content inside this discrete card container.
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#FFF',
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 12,
    elevation: 4,
    margin: 8,
    overflow: 'hidden', // Keeps image inside borders
  },
  imageArea: {
    height: 160,
    backgroundColor: '#E0E0E0',
  },
  contentArea: {
    padding: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 8,
  },
  description: {
    color: '#666',
  }
});
// In your view: <FlatList numColumns={2} data={data} renderItem={...} />
```
- Wrap everything in a View with `borderRadius` and `overflow: 'hidden'`.
- `elevation: 4` provides the drop shadow on Android, while the `shadow*` props handle iOS.
- For a Pinterest/Masonry style (columns of different heights), you must use a third-party library like `react-native-masonry-list`, as `FlatList` cannot do varying row heights in columns.

### Jetpack Compose
```kotlin
@Composable
fun ContentCard() {
    // ElevatedCard provides the shadow and shape natively
    ElevatedCard(
        elevation = CardDefaults.elevatedCardElevation(defaultElevation = 4.dp),
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.elevatedCardColors(containerColor = Color.White),
        modifier = Modifier.fillMaxWidth().padding(8.dp)
    ) {
        Column {
            // Image Area
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(160.dp)
                    .background(Color.LightGray)
            )
            
            // Content Area
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Card Title",
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Bold
                )
                Spacer(Modifier.height(8.dp))
                Text(
                    text = "A brief description of the content inside this discrete card container.",
                    style = MaterialTheme.typography.bodyMedium,
                    color = Color.Gray,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
        }
    }
}
// In your view: LazyVerticalGrid(columns = GridCells.Adaptive(minSize = 160.dp)) { ... }
```
- `ElevatedCard` is the perfect Material 3 component for this. It handles clipping and shadows automatically.
- Use `GridCells.Adaptive(minSize = 160.dp)` in a `LazyVerticalGrid` to achieve an auto-flowing grid identical to CSS Grid `auto-fit`.

## Do's and Don'ts
- **DO**: Make the entire card clickable, not just the title or image.
- **DON'T**: Put too much text in a card. If the user has to scroll *within* a card, the card is too big.

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

<!-- SKILL SOURCE: tile-design -->

# Tile Design (Metro UI)

> "Authentically digital. Clean, sharp squares relying purely on typography and flat color."


## When to Use
Use this sub-style when the user's request matches the aesthetic described above. This is a child reference of the `design-it` skill and is not meant to be triggered directly.

## Core Principles
1. **Sharp Corners**: Absolutely no border-radius. Everything is a perfect square or sharp rectangle.
2. **Live Data**: Tiles flip, scroll, or fade internally to show live updates without the user interacting.
3. **Horizontal Panning**: The grid often expands infinitely to the right, encouraging horizontal scrolling.

## Visual DNA
- **Colors**: High saturation, flat colors. A dark background (pure black) with bright cyan, magenta, orange, and green tiles.
- **Typography**: Extremely clean, light sans-serifs (like `Segoe UI Light`). Text is almost always pure white.
- **Icons**: Simple, wireframe, monochromatic glyphs placed centrally or in the corner.

## Web Implementation
- **CSS Example**:
```css
body {
  background-color: #111;
  color: #fff;
  font-family: 'Segoe UI', sans-serif;
  overflow-x: auto; /* Horizontal scroll */
}

.tile-group {
  display: grid;
  grid-template-columns: repeat(4, 150px);
  grid-auto-rows: 150px;
  gap: 8px;
  padding: 40px;
}

.tile {
  background-color: #0078D7; /* Classic Windows Blue */
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  
  /* The "tilt" click effect */
  transition: transform 0.1s;
  transform-origin: center;
}

.tile:active {
  transform: scale(0.95);
}

.tile-wide { grid-column: span 2; }
.tile-large { grid-column: span 2; grid-row: span 2; }

/* Live Tile Animation */
.tile-live-content {
  animation: slideUp 5s infinite;
}

@keyframes slideUp {
  0%, 45% { transform: translateY(0); }
  50%, 95% { transform: translateY(-100%); } /* Slides up to reveal next item */
  100% { transform: translateY(0); }
}
```

## App Implementation

### SwiftUI
```swift
struct TileDesignView: View {
    let rows = [GridItem(.fixed(150), spacing: 8), GridItem(.fixed(150), spacing: 8)]
    
    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            LazyHGrid(rows: rows, spacing: 8) {
                TileView(title: "Mail", color: Color(hex: "0078D7"), icon: "envelope")
                TileView(title: "Photos", color: Color(hex: "00CC6A"), icon: "photo", isLarge: true)
                TileView(title: "Weather", color: Color(hex: "2D7D9A"), icon: "cloud.sun")
                TileView(title: "Calendar", color: Color(hex: "D13438"), icon: "calendar")
            }
            .padding(40)
        }
        .background(Color(hex: "111111").ignoresSafeArea())
    }
}

struct TileView: View {
    let title: String
    let color: Color
    let icon: String
    var isLarge: Bool = false
    
    @State private var isPressed = false
    
    var body: some View {
        VStack(alignment: .leading) {
            Image(systemName: icon)
                .font(.system(size: 32, weight: .light))
                .foregroundColor(.white)
            Spacer()
            Text(title)
                .font(.custom("Segoe UI", size: 16))
                .foregroundColor(.white)
        }
        .padding(16)
        // Sharp corners are mandatory
        .frame(width: isLarge ? 308 : 150, height: isLarge ? 308 : 150, alignment: .leading)
        .background(color)
        .scaleEffect(isPressed ? 0.95 : 1.0)
        .animation(.spring(response: 0.2, dampingFraction: 0.5), value: isPressed)
        .onLongPressGesture(minimumDuration: .infinity, maximumDistance: .infinity, pressing: { pressing in
            isPressed = pressing
        }, perform: {})
    }
}
```
- A `LazyHGrid` inside a horizontal `ScrollView` perfectly replicates the Windows Phone / Windows 8 start screen.
- Absolutely NO corner radius.
- The `isPressed` state triggering a `.scaleEffect(0.95)` replicates the physical "tilt" interaction of Metro tiles.

### Flutter
```dart
class TileDesignScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF111111),
      body: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.all(40),
        child: SizedBox(
          height: 308, // Two rows of 150px + 8px spacing
          child: Wrap(
            direction: Axis.vertical,
            spacing: 8,
            runSpacing: 8,
            children: [
              _buildTile('Mail', const Color(0xFF0078D7), Icons.mail_outline),
              _buildTile('Weather', const Color(0xFF2D7D9A), Icons.cloud_outlined),
              _buildTile('Photos', const Color(0xFF00CC6A), Icons.photo_outlined, isLarge: true),
              _buildTile('Calendar', const Color(0xFFD13438), Icons.calendar_today),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTile(String title, Color color, IconData icon, {bool isLarge = false}) {
    return StatefulBuilder(
      builder: (context, setState) {
        bool isPressed = false;
        return GestureDetector(
          onTapDown: (_) => setState(() => isPressed = true),
          onTapUp: (_) => setState(() => isPressed = false),
          onTapCancel: () => setState(() => isPressed = false),
          child: AnimatedScale(
            scale: isPressed ? 0.95 : 1.0,
            duration: const Duration(milliseconds: 100),
            child: Container(
              width: isLarge ? 308 : 150,
              height: isLarge ? 308 : 150,
              color: color, // Sharp corners
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Icon(icon, color: Colors.white, size: 32),
                  Text(title, style: const TextStyle(color: Colors.white, fontFamily: 'Segoe UI', fontSize: 16)),
                ],
              ),
            ),
          ),
        );
      }
    );
  }
}
```
- `Wrap` with `direction: Axis.vertical` inside a horizontally scrolling `SizedBox` is the easiest way to build a Metro grid that flows left-to-right.
- Wrap tiles in `GestureDetector` and `AnimatedScale` to handle the press animation.

### React Native
```jsx
const TileDesignScreen = () => {
  return (
    <ScrollView horizontal style={{ flex: 1, backgroundColor: '#111' }} contentContainerStyle={{ padding: 40 }}>
      <View style={{ flexDirection: 'column', flexWrap: 'wrap', height: 308, gap: 8 }}>
        
        <Tile title="Mail" color="#0078D7" />
        <Tile title="Weather" color="#2D7D9A" />
        <Tile title="Photos" color="#00CC6A" isLarge />
        <Tile title="Calendar" color="#D13438" />

      </View>
    </ScrollView>
  );
};

const Tile = ({ title, color, isLarge }) => {
  const scale = useRef(new Animated.Value(1)).current;

  const handlePressIn = () => Animated.spring(scale, { toValue: 0.95, useNativeDriver: true }).start();
  const handlePressOut = () => Animated.spring(scale, { toValue: 1, useNativeDriver: true }).start();

  return (
    <TouchableWithoutFeedback onPressIn={handlePressIn} onPressOut={handlePressOut}>
      <Animated.View style={{
        width: isLarge ? 308 : 150, height: isLarge ? 308 : 150,
        backgroundColor: color, padding: 16, justifyContent: 'space-between',
        transform: [{ scale }] // The Metro tilt effect
      }}>
        <View style={{ width: 32, height: 32, backgroundColor: '#FFF', opacity: 0.5 }} />
        <Text style={{ color: '#FFF', fontFamily: 'Segoe UI', fontSize: 16 }}>{title}</Text>
      </Animated.View>
    </TouchableWithoutFeedback>
  );
};
```
- Use a `<ScrollView horizontal>` combined with a child `<View>` that has a fixed `height` and `flexWrap: 'wrap', flexDirection: 'column'`. This forces children to form columns and flow horizontally.
- Use `Animated.View` and `TouchableWithoutFeedback` to create the scale animation.

### Jetpack Compose
```kotlin
@Composable
fun TileDesignScreen() {
    LazyHorizontalGrid(
        rows = GridCells.Fixed(2),
        modifier = Modifier.fillMaxSize().background(Color(0xFF111111)),
        contentPadding = PaddingValues(40.dp),
        horizontalArrangement = Arrangement.spacedBy(8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        item(span = { GridItemSpan(1) }) { Tile("Mail", Color(0xFF0078D7)) }
        // Note: LazyHorizontalGrid doesn't easily support spanning multiple rows (2x2 tiles).
        // For a true Metro layout, you often have to build a custom Layout or use staggered grids.
        item(span = { GridItemSpan(2) }) { Tile("Photos Wide", Color(0xFF00CC6A)) } 
        item(span = { GridItemSpan(1) }) { Tile("Weather", Color(0xFF2D7D9A)) }
    }
}

@Composable
fun Tile(title: String, color: Color) {
    var isPressed by remember { mutableStateOf(false) }
    val scale by animateFloatAsState(if (isPressed) 0.95f else 1.0f)

    Box(
        modifier = Modifier
            .size(150.dp) // Or wide/large based on params
            .scale(scale)
            .background(color) // Sharp corners! No RoundedCornerShape
            .pointerInput(Unit) {
                detectTapGestures(
                    onPress = {
                        isPressed = true
                        tryAwaitRelease()
                        isPressed = false
                    }
                )
            }
            .padding(16.dp)
    ) {
        // Icon
        Box(modifier = Modifier.size(32.dp).background(Color.White.copy(alpha = 0.5f)).align(Alignment.TopStart))
        // Text
        Text(
            text = title,
            color = Color.White,
            fontFamily = FontFamily.SansSerif,
            modifier = Modifier.align(Alignment.BottomStart)
        )
    }
}
```
- `LazyHorizontalGrid` is the right tool, though building true 2x2 "Large" tiles requires custom layout math in Compose if mixing with 1x1 tiles.
- `Modifier.scale()` paired with `pointerInput` `detectTapGestures` handles the Metro interaction.

## Do's and Don'ts
- **DO**: Place the tile label text strictly in the bottom-left corner of the tile.
- **DON'T**: Add drop shadows or gradients to the tiles.

## Limitations
- This is a styling reference and does not replace environment-specific validation, accessibility testing, or expert review.
- Ensure appropriate contrast ratios and responsive behaviors are verified separately.

---

