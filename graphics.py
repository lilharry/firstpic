


file = open("image.ppm","w+")
file.write("P3 500 500 255\n")
for x in range(0,500):
    for y in range(0,500):
        file.write("%d %d %d\n" % (255,0,y%256) )



        
file.close()
