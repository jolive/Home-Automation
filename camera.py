import pygame, pygame.camera

pygame.camera.init()
pygame.camera.list.camera()
cam = pygame.camera.Camera("/dev/video0", (640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"filename.jpg")
