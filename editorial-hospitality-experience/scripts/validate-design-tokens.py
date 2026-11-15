#!/usr/bin/env python3
import sys, json, os

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    return [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]

def relative_luminance(rgb):
    srgb = [v / 255.0 for v in rgb]
    lum = []
    for c in srgb:
        if c <= 0.03928:
            lum.append(c / 12.92)
        else:
            lum.append(((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * lum[0] + 0.7152 * lum[1] + 0.0722 * lum[2]

def contrast_ratio(hex1, hex2):
    lum1 = relative_luminance(hex_to_rgb(hex1))
    lum2 = relative_luminance(hex_to_rgb(hex2))
    brightest = max(lum1, lum2)
    darkest = min(lum1, lum2)
    return (brightest + 0.05) / (darkest + 0.05)

def validate_tokens(token_file):
    print(f"=== Validating Design Tokens: {token_file} ===")
    if not os.path.exists(token_file):
        print(f"ERROR: File not found: {token_file}")
        return False

    with open(token_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    errors = []
    warnings = []
    passed = 0

    required_sections = ['typography', 'color', 'spacing', 'motion']
    for sec in required_sections:
        if sec in data:
            passed += 1
            print(f"  [PASS] Section '{sec}' present.")
        else:
            errors.append(f"Missing required token section: '{sec}'")

    colors = data.get('color', {})
    bg_primary = colors.get('bgPrimary', {}).get('value', '#0D0D0C')
    text_primary = colors.get('textPrimary', {}).get('value', '#F4F3EF')
    text_secondary = colors.get('textSecondary', {}).get('value', '#B0ABA0')
    border_subtle = colors.get('borderSubtle', {}).get('value', '#2A2A28')

    ratio_body = contrast_ratio(bg_primary, text_primary)
    if ratio_body >= 4.5:
        passed += 1
        print(f"  [PASS] Body Text Contrast ({text_primary} on {bg_primary}): {ratio_body:.2f}:1 (Target: >= 4.5:1)")
    else:
        errors.append(f"WCAG VIOLATION: Body text contrast is {ratio_body:.2f}:1, failing WCAG 2.2 AA 4.5:1 threshold.")

    ratio_sec = contrast_ratio(bg_primary, text_secondary)
    if ratio_sec >= 4.5:
        passed += 1
        print(f"  [PASS] Secondary Text Contrast ({text_secondary} on {bg_primary}): {ratio_sec:.2f}:1 (Target: >= 4.5:1)")
    elif ratio_sec >= 3.0:
        warnings.append(f"WCAG WARNING: Secondary text contrast is {ratio_sec:.2f}:1. Below 4.5:1 for body copy.")
    else:
        errors.append(f"WCAG VIOLATION: Secondary text contrast is {ratio_sec:.2f}:1, failing WCAG 3.0:1 minimum.")

    typo = data.get('typography', {})
    line_measure = typo.get('lineMeasureMax', {}).get('value', '80ch')
    if 'ch' in line_measure:
        ch_val = int(line_measure.replace('ch', ''))
        if ch_val <= 80:
            passed += 1
            print(f"  [PASS] Line Measure Cap ({line_measure}): Ergonomic line length (<= 80ch).")
        else:
            errors.append(f"ERGONOMIC VIOLATION: Line measure '{line_measure}' exceeds 80ch maximum.")

    print(f"\n=== TOKEN VALIDATION SUMMARY: {passed} passed, {len(warnings)} warnings, {len(errors)} errors ===")
    return len(errors) == 0

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '/workspace/scratch/editorial-hospitality-experience/assets/design-token-schema.json'
    success = validate_tokens(target)
    sys.exit(0 if success else 1)
