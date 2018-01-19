from PIL import Image
import sys

iconPath = sys.argv[1]
tagPath = sys.argv[2]
pkgPath = sys.argv[3]
print iconPath
print tagPath

icon = Image.open(iconPath)
tag = Image.open(tagPath)
print "icon.mode: " + icon.mode
print "tag.mode: " + tag.mode
if icon.mode != "RGBA":
	icon = icon.convert("RGBA")
	print icon.mode

new_icon = icon.resize((192, 192), Image.ANTIALIAS)
new_icon.paste(tag, (0, 0), tag)
new_icon.save(pkgPath + "ic_launcher.png")