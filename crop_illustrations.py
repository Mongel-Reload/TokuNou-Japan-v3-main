from PIL import Image
import os

# Open master illustration
master_path = 'assets/images/illustrations/tokunou-illustration-master.png'
img = Image.open(master_path)
width, height = img.size

print(f"Master image size: {width}x{height}")

# Define crop regions based on typical grid layout for illustration sheets
# These are estimates - adjust based on actual master layout
crops = {
    # Hero section (top-left large area)
    'hero-tokunou.png': (0, 0, 627, 627),
    
    # Start program cards (middle row)
    'start-program.png': (0, 627, 418, 836),
    'start-language.png': (418, 627, 836, 836),
    'start-ready.png': (836, 627, 1254, 836),
    
    # Roadmap steps (bottom row)
    'roadmap-program.png': (0, 836, 251, 1045),
    'roadmap-language.png': (251, 836, 502, 1045),
    'roadmap-exam.png': (502, 836, 753, 1045),
    'roadmap-interview.png': (753, 836, 1004, 1045),
    'roadmap-departure.png': (1004, 836, 1254, 1045),
    
    # Farm sections (right side)
    'farm-cattle.png': (627, 0, 836, 314),
    'farm-poultry.png': (836, 0, 1045, 314),
    'farm-pig.png': (1045, 0, 1254, 314),
    
    # Tools section
    'tool-readiness.png': (627, 314, 743, 470),
    'tool-salary.png': (743, 314, 859, 470),
    'tool-quiz.png': (859, 314, 975, 470),
    'tool-ai.png': (975, 314, 1091, 470),
    
    # Japan life
    'japan-life.png': (1091, 314, 1254, 627),
}

# Crop and save each asset
output_dir = 'assets/images/illustrations'
for filename, (left, top, right, bottom) in crops.items():
    # Ensure coordinates are within bounds
    left = max(0, min(left, width))
    top = max(0, min(top, height))
    right = max(0, min(right, width))
    bottom = max(0, min(bottom, height))
    
    crop = img.crop((left, top, right, bottom))
    output_path = os.path.join(output_dir, filename)
    crop.save(output_path, 'PNG')
    print(f"Saved: {filename} ({right-left}x{bottom-top})")

print("\nCropping complete!")
