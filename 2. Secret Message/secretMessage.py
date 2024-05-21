import qrcode

# secret message
message = "Here's to the memories we've created and the ones we will make together."

# generate qrcode
image = qrcode.make(data=message)

# save image
image.save("secret message.png")