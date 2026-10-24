import os
from PIL import Image, ImageDraw, ImageFont

# Ensure icon directories exist
dirs = ["icons", "mobile/icons"]
for d in dirs:
    os.makedirs(d, exist_ok=True)

def create_pwa_icon(size, is_maskable=False):
    # Create high-res image
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    margin = int(size * 0.1) if is_maskable else int(size * 0.04)
    radius = int(size * 0.22) if not is_maskable else 0

    # Background gradient or solid rounded rectangle
    # Base dark sapphire / galactic gradient
    for y in range(size):
        r = int(11 + (y / size) * 20)
        g = int(15 + (y / size) * 35)
        b = int(28 + (y / size) * 80)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # Inner glowing border
    if not is_maskable:
        # Rounded mask
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(margin, margin), (size - margin, size - margin)], radius=radius, fill=255)
        
        # Border
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=radius,
            outline=(59, 130, 246, 200),
            width=max(2, int(size * 0.015))
        )

    # Core Glowing Circle
    center_x, center_y = size // 2, int(size * 0.44)
    circle_r = int(size * 0.28)
    
    # Outer glow
    for i in range(15, 0, -1):
        alpha = int(8 + (15 - i) * 6)
        glow_r = circle_r + i * 2
        draw.ellipse(
            [(center_x - glow_r, center_y - glow_r), (center_x + glow_r, center_y + glow_r)],
            fill=(37, 99, 235, alpha)
        )

    # Core circle
    draw.ellipse(
        [(center_x - circle_r, center_y - circle_r), (center_x + circle_r, center_y + circle_r)],
        fill=(30, 58, 138, 255),
        outline=(96, 165, 250, 255),
        width=max(2, int(size * 0.02))
    )

    # Brain / Spark / Lightning symbol
    # Draw stylized stylized neuron nodes and connections
    node_color = (250, 204, 21, 255) # Yellow gold
    conn_color = (147, 197, 253, 220)
    
    points = [
        (center_x, center_y - int(circle_r * 0.55)), # Top
        (center_x - int(circle_r * 0.5), center_y - int(circle_r * 0.15)), # Left
        (center_x + int(circle_r * 0.5), center_y - int(circle_r * 0.15)), # Right
        (center_x - int(circle_r * 0.35), center_y + int(circle_r * 0.4)), # Bottom left
        (center_x + int(circle_r * 0.35), center_y + int(circle_r * 0.4)), # Bottom right
        (center_x, center_y), # Center
    ]

    # Draw lines connecting nodes
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                draw.line([p1, p2], fill=conn_color, width=max(2, int(size * 0.012)))

    # Draw nodes
    node_r = max(4, int(size * 0.035))
    for p in points:
        draw.ellipse([(p[0] - node_r, p[1] - node_r), (p[0] + node_r, p[1] + node_r)], fill=node_color, outline=(255, 255, 255, 255), width=max(1, int(size * 0.008)))

    # Central diamond
    diamond_size = int(size * 0.04)
    draw.polygon([
        (center_x, center_y - diamond_size),
        (center_x + diamond_size, center_y),
        (center_x, center_y + diamond_size),
        (center_x - diamond_size, center_y)
    ], fill=(255, 255, 255, 255))

    # Text Banner at bottom
    # "CORTEX"
    try:
        font_size = int(size * 0.11)
        # Try loading default or arial
        font = ImageFont.truetype("arial.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()

    text = "CORTEX"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_w = text_bbox[2] - text_bbox[0]
    text_h = text_bbox[3] - text_bbox[1]
    text_x = (size - text_w) // 2
    text_y = int(size * 0.78)

    # Shadow
    draw.text((text_x + 2, text_y + 2), text, font=font, fill=(0, 0, 0, 180))
    # Text
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, 255))

    return img

# Generate all standard PWA icon sizes
sizes = [
    (192, "icon-192.png", False),
    (512, "icon-512.png", False),
    (512, "icon-maskable-512.png", True),
    (180, "apple-touch-icon.png", False),
    (64, "favicon.png", False),
    (32, "favicon-32.png", False)
]

for s, filename, is_mask in sizes:
    icon_img = create_pwa_icon(s, is_mask)
    for d in dirs:
        target_path = os.path.join(d, filename)
        icon_img.save(target_path, "PNG")
        print(f"Generated: {target_path} ({s}x{s})")

print("All PWA icons generated successfully!")
