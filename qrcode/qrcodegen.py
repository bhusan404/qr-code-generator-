import qrcode  #by Bibhuti Bhusan Ghosh
import image
qr = qrcode.QRCode ( 
    version = 15, 
    box_size = 10, 
    border = 5 ,
)
data = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white")
img = qr.make_image(fill = "black", back_color = "white")
img.save("test0.png")

data = "https://www.youtube.com/watch?v=pkYVOmU3MgA"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white")
img = qr.make_image(fill = "black", back_color = "white")
img.save("test1.png")

