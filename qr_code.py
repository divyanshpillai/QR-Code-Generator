import qrcode

img = qrcode.make("https://leetcode.com/pillaidivyansh/")

img.save("div_leetcode.png")