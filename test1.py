# import datetime

# a = str(datetime.datetime.now()).split()
# b = a[1].split(':')
# c = ':'.join(b[0]+b[1]+b[2][:2])
# print(a)
# print()
# print(b)
# print(c)

# import time

# a = time.localtime()
# b = time.strftime('%H:%M:%S',a)

# print(a)
# print(b)


# b = str(time.perf_counter()).split('.')
# print('.'.join(b[0]+b[1][0]))

# print(time.ctime().split())

# h = int(input('hour: '))
# m= int(input('minute: '))
# s = int(input('second: '))

# f = 60

# true_s = s%f
# true_m = m%f + s// f
# true_h = h+ m//f 

# print('Hour: '+str(true_h))
# print('Minute: '+str(true_m))
# print('Second:'+str(true_s))

# while true_h > -1:
#     while true_m > -1:
#         while true_s> -1:
#             print('%02d:%02d:%02d'% (true_h,true_m,true_s),end = '\r')
#             true_s = true_s-1
#             time.sleep(1)
#         true_m = true_m-1
#         true_s = 59
#     true_h = true_h-1
#     true_m = 59

# print('12345'.isdigit())







# while True:
#     count = 0
#     count1 = 0
#     for i in range(h,-1,-1):
#         if m != 59 and count1 == 0:
#             count1+=1
#             for j in range(m,-1,-1):
#                 if s != 59 and count == 0:
#                     count+=1
#                     for k in range(s,-1,-1):
#                         time.sleep(1)
#                         print('%02d:%02d:%02d'% (i,j,k))
#                 else:
#                     for k in range(59,-1,-1):
#                         time.sleep(1)
#                         print('%02d:%02d:%02d'% (i,j,k))
#         else:
#             for j in range(59,-1,-1):
#                 if s != 59 and count == 0:
#                     count+=1
#                     for k in range(s,-1,-1):
#                         time.sleep(1)
#                         print('%02d:%02d:%02d'% (i,j,k))
#                 else:
#                     for k in range(59,-1,-1):
#                         time.sleep(1)
#                         print('%02d:%02d:%02d'% (i,j,k))
            
#     break





# import pygame 
# pygame.mixer.init()
# pygame.display.set_mode([500,500])
# music = pygame.mixer.Sound('unlasting-LiSA.mp3')
# while True:
#     music.play()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

from pydub import AudioSegment
from pydub.playback import play
music = AudioSegment.from_mp3('unlasting-LiSA.mp3')
play(music)
