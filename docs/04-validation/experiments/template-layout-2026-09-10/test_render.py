"""Synthetic layout probe, not a customer-quality or AI-generation benchmark."""
from pathlib import Path
import json
from decimal import Decimal, InvalidOperation
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
CASES = [
    ('short', 'Summer essentials', '29.99'),
    ('long', 'A practical everyday collection for your next weekend away', '129.00'),
    ('wide_letters', 'WWW PREMIUM COLLECTION MMM', '9999.00'),
    ('unbroken', 'SUMMERCOLLECTIONLIMITEDITION2026', '39.00'),
    ('overlong', 'A collection for everyday life and special occasions. ' * 12, '29.99'),
    ('bad_price', 'Summer essentials', 'twenty dollars'),
]
SIZES = [(1080,1080),(1080,1350),(1080,1920)]

def layout(draw, text, width, height):
    # Character wrapping deliberately supports long unbroken input as well.
    # A real brand may reject mid-word breaks; that requires a separate rule.
    for size in range(72,35,-2):
        font = ImageFont.truetype(FONT,size)
        lines, line = [], ''
        for ch in text:
            if draw.textlength(line+ch,font=font)>width and line:
                lines.append(line.rstrip()); line=ch.lstrip()
            else:
                line+=ch
        if line: lines.append(line.rstrip())
        step=size+12
        if len(lines)*step<=height:
            return lines,font,step,size
    return None

results=[]
thumbs=[]
for name,title,price in CASES:
    for w,h in SIZES:
        im=Image.new('RGB',(w,h),'#f3efe6'); d=ImageDraw.Draw(im)
        record={'case':name,'size':[w,h],'synthetic':True}
        try:
            amount=Decimal(price)
            if not amount.is_finite() or amount<=0: raise ValueError('invalid price')
        except (InvalidOperation,ValueError):
            record.update(status='rejected',reason='invalid price')
        else:
            fitted=layout(d,title,w-144,300)
            if fitted is None:
                record.update(status='rejected',reason='copy exceeds layout at minimum font 36px')
            else:
                lines,font,step,font_size=fitted
                d.text((72,50),'SYNTHETIC LAYOUT TEST',font=ImageFont.truetype(FONT,24),fill='#56635d')
                for i,line in enumerate(lines): d.text((72,115+i*step),line,font=font,fill='#19382c')
                d.rounded_rectangle((72,440,w-72,h-230),radius=24,fill='#d6dfd4')
                d.text((108,475),'PRODUCT PLACEHOLDER',font=ImageFont.truetype(FONT,30),fill='#19382c')
                d.text((72,h-175),f'${amount:,.2f}',font=ImageFont.truetype(FONT,64),fill='#19382c')
                d.text((72,h-80),'SHOP COLLECTION',font=ImageFont.truetype(FONT,28),fill='#19382c')
                record.update(status='rendered',font_px=font_size,lines=len(lines),file=f'{name}-{w}x{h}.png')
                im.save(ROOT/record['file'])
        if record['status']=='rejected':
            d.text((72,115),'REJECTED INPUT',font=ImageFont.truetype(FONT,50),fill='#93312c')
            d.text((72,210),name,font=ImageFont.truetype(FONT,32),fill='#93312c')
        tile=Image.new('RGB',(240,460),'white')
        im.thumbnail((220,400)); tile.paste(im,((240-im.width)//2,35))
        ImageDraw.Draw(tile).text((8,10),f'{name} {w}x{h}',fill='black')
        thumbs.append(tile); results.append(record)
sheet=Image.new('RGB',(240*3,460*len(CASES)),'#cccccc')
for i,tile in enumerate(thumbs): sheet.paste(tile,((i%3)*240,(i//3)*460))
sheet.save(ROOT/'contact-sheet.png')
(ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'attempts':len(results),'rendered':sum(r['status']=='rendered' for r in results),'rejected':sum(r['status']=='rejected' for r in results)}))
