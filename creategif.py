from PIL import Image

def create_gifs_from_pngs():
    def create(files:list, name:str):
        imgs = []

        for i in files:
            img = Image.open(i)
            imgs.append(img)

        last_frame = (len(imgs)) 

        for x in range(0, 9):
            img = imgs[last_frame-1]
            imgs.append(img)

        imgs[0].save(f'./fox/{name}.gif', format="GIF", save_all=True, append_images=imgs[1:], optimize=True, duration=500, loop=0)

    # right
    r = ["./fox/r1.jpg", "./fox/r2.jpg", "./fox/r3.jpg"]
    # left
    l = ["./fox/l1.jpg", "./fox/l2.jpg", "./fox/l3.jpg"]
    # front
    f = ["./fox/f1.jpg", "./fox/f2.jpg", "./fox/f3.jpg"]

    create(r, "r")
    create(l, "l")
    create(f, "f")