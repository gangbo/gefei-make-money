# E-009 exact prompts

Built-in image_gen, no CLI or TikTomato API. Both edits reference baseline.png independently, not the previous edit. No retries. Model/version/settings not exposed by tool; do not claim identical configuration to production GPT Image 2.

## Baseline
Create one photorealistic synthetic baseline photo for a controlled hairstyle-editing experiment. A fictional East Asian woman age 30, shoulder-length straight dark brown hair parted in the middle, all hair visible with space above head, looking straight at camera, neutral gentle closed-mouth expression, natural unretouched skin with subtle texture and a small mole on her left cheek, brown eyes. Simple dark blue crew-neck shirt. Head and shoulders, square framing. Plain light gray wall, even daylight. Normal candid smartphone photo, not glamour or beauty retouching. No jewelry, no text, no collage. This is the BASELINE only; do not show alternative hairstyles.

## Bob
Controlled hairstyle edit of the provided baseline photograph. Change ONLY her hairstyle to a chin-length blunt bob with straight eyebrow-length bangs. Keep original dark brown hair color. Preserve exactly the same person: facial geometry, eyes, nose, mouth, expression, left cheek mole, natural skin texture and skin tone. Preserve pose, dark blue shirt, gray wall, lighting, camera angle and square crop. Do not beautify, slim face, enlarge eyes or smooth skin. Hair may naturally occlude the forehead and uncover some neck/shirt. Output one edited photograph, no text, no collage.

## Color
Controlled hair-color-only editing experiment. In the supplied original photo change ONLY dark brown hair color to natural copper auburn. Keep EXACTLY the existing shoulder-length straight haircut, middle part, length, flyaway strands and hair shape. Preserve the same person's facial geometry, eyes, nose, mouth, expression, visible small mole on her left cheek (viewer right), natural skin texture, skin tone. Preserve dark blue shirt, gray wall, lighting, pose, camera angle, crop and image dimensions. No beauty retouching, no face reshaping, no skin smoothing. One edited photograph, no text, no collage.
