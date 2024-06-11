import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    pn_img = pg.image.load("fig/3.png")
    bgg_img = pg.transform.flip(bg_img, True, False)
    pn_img = pg.transform.flip(pn_img, True, False)
    img_rct = pn_img.get_rect()
    img_rct.center = 300, 200
    tmr = 0
    mvx = 0
    mvy = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bgg_img, [-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bgg_img, [-x+4800, 0])
        key_lst = pg.key.get_pressed()
        key_lst = pg.key.get_pressed()  # 全キーの押下状態を取得
        # if key_lst[pg.K_UP]:  # 上矢印キーが押されたら
        #     img_rct.move_ip(0, -1)
        # if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
        #     img_rct.move_ip(0, +1)
        # if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
        #     img_rct.move_ip(-1, 0)
        # if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
        #     img_rct.move_ip(+2, 0)
        if key_lst[pg.K_UP]:
            mvy = -1
        if key_lst[pg.K_DOWN]:
            mvy = +1
        if key_lst[pg.K_LEFT]:
            mvx = -1
        if key_lst[pg.K_RIGHT]:
            mvx = +2
        img_rct.move_ip(mvx, mvy)
        img_rct.move_ip(-1,0)
        
        screen.blit(pn_img, img_rct)
        pg.display.update()
        tmr += 1 
        mvx = 0
        mvy = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()