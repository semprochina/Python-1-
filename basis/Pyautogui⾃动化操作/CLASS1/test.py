import pyautogui as pg
box=pg.locateOnScreen('img.png',confidence=0.8)
center=pg.center(box)
print(center)
pg.doubleClick(center,button='left')
sc=pg.screenshot(region=(1176,36,80,80))
sc.show('屏幕截图')
sc.save("屏幕截图")