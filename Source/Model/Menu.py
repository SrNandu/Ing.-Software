from Subject import Subject
import sys, time, random, pygame
from unittest import result
from collections import deque
import cv2 as cv, mediapipe as mp

class Menu(Subject):
    __boton: int = 0
    __cantBotones: int

    def __init__(self, cantBotones):
        super().__init__()
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_face_mesh = mp.solutions.face_mesh
        drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        pygame.init()

        # Initialize required elements/environment
        VID_CAP = cv.VideoCapture(0)
        window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT)) # width by height
        screen = pygame.display.set_mode(window_size)

        # Bird and pipe init
        bird_img = pygame.image.load("Sprites/arrow.png")
        bird_img = pygame.transform.scale(bird_img, (bird_img.get_width() / 6, bird_img.get_height() / 6))
        bird_frame = bird_img.get_rect()
        bird_frame.center = (window_size[0] // 6, window_size[1] // 2)

        config_img = pygame.image.load("Sprites/config.png")
        config_img = pygame.transform.scale(config_img, (config_img.get_width() / 8, config_img.get_height() / 8))
        config_frame = config_img.get_rect()
        config_frame.center = (160, 50)

        head_img = pygame.image.load("Sprites/head.png")
        head_img = pygame.transform.scale(head_img, (head_img.get_width() / 8, head_img.get_height() / 8))
        head_frame = head_img.get_rect()
        head_frame.center = (160, 140)

        hand_img = pygame.image.load("Sprites/hand.png")
        hand_img = pygame.transform.scale(hand_img, (hand_img.get_width() / 8, hand_img.get_height() / 8))
        hand_frame = hand_img.get_rect()
        hand_frame.center = (160, 230)

        play_img = pygame.image.load("Sprites/play.png")
        play_img = pygame.transform.scale(play_img, (play_img.get_width() / 8, play_img.get_height() / 8))
        play_frame = play_img.get_rect()
        play_frame.center = (160, 320)

        exit_img = pygame.image.load("Sprites/exit.png")
        exit_img = pygame.transform.scale(exit_img, (exit_img.get_width() / 8, exit_img.get_height() / 8))
        exit_frame = exit_img.get_rect()
        exit_frame.center = (160, 410)

        pajaro_img = pygame.image.load("Sprites/bird_menu.png")
        pajaro_img = pygame.transform.scale(pajaro_img, (pajaro_img.get_width() / 4, pajaro_img.get_height() / 4))
        pajaro_frame = pajaro_img.get_rect()
        pajaro_frame.center = (400, 200)

        logo_img = pygame.image.load("Sprites/TheBigBug-icon.png")
        logo_img = pygame.transform.scale(logo_img, (logo_img.get_width() / 3, logo_img.get_height() / 3))
        logo_frame = logo_img.get_rect()
        logo_frame.center = (400, 350)


        pipe_frames = deque()
        pipe_img = pygame.image.load("Sprites/config.png")

        pipe_starting_template = pipe_img.get_rect()
        #space_between_pipes = 250

        # Game loop
        game_clock = time.time()
        stage = 1
        pipeSpawnTimer = 0
        time_between_pipe_spawn = 40
        dist_between_pipes = 500
        pipe_velocity = lambda: dist_between_pipes / time_between_pipe_spawn
        level = 0
        score = 0
        didUpdateScore = False
        game_is_running = True


        with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as face_mesh:
            while True:
                # Check if game is running
                
                if not game_is_running:
                    text = pygame.font.SysFont("Helvetica Bold.ttf", 64).render('Config Touch!', True, (99, 245, 255))
                    tr = text.get_rect()
                    tr.center = (window_size[0]/2, window_size[1]/2)
                    screen.blit(text, tr)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    VID_CAP.release()
                    cv.destroyAllWindows()
                    pygame.quit()
                    sys.exit()

                # Check if user quit window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        VID_CAP.release()
                        cv.destroyAllWindows()
                        pygame.quit()
                        sys.exit()

                # Get frame
                ret, frame = VID_CAP.read()
                if not ret:
                    print("Empty frame, continuing...")
                    continue

                # Clear screen
                screen.fill((125, 220, 232))

                

                # Face mesh
                frame.flags.writeable = False
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                results = face_mesh.process(frame)
                frame.flags.writeable = True

                # Draw mesh
                if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
                    # 94 = Tip of nose
                    marker = results.multi_face_landmarks[0].landmark[94].y
                    bird_frame.centery = (marker - 0.5) * 1.5 * window_size[1] + window_size[1]/2
                    if bird_frame.top < 0: bird_frame.y = 0
                    if bird_frame.bottom > window_size[1]: bird_frame.y = window_size[1] - bird_frame.height

                # Mirror frame, swap axes because opencv != pygame
                frame = cv.flip(frame, 1).swapaxes(0, 1)

                

                # Update pipe positions
        #       for pf in pipe_frames:
        #           pf[0].x -= pipe_velocity()
        #           pf[1].x -= pipe_velocity()

        #       if len(pipe_frames) > 0 and pipe_frames[0][0].right < 0:
        #           pipe_frames.popleft()

                # Update screen
                pygame.surfarray.blit_array(screen, frame)
                pygame.draw.rect(screen,(255, 255, 255), (0, 0, 1000, 1000))
                screen.blit(bird_img, bird_frame)
        #        checker = True
        #        for pf in pipe_frames:
        #            # Check if bird went through to update score
        #            if pf[0].left <= bird_frame.x <= pf[0].right:
        #                checker = False
        #                if not didUpdateScore:
        #                    score += 1
        #                    didUpdateScore = True
                    # Update screen
        #            screen.blit(pipe_img, pf[1])
        #            screen.blit(pygame.transform.flip(pipe_img, 0, 1), pf[0])
        #            if checker: didUpdateScore = False

                # Static
                pygame.draw.rect(screen,(255, 255, 255), (160, 0, 1000, 1000))
                
                screen.blit(config_img, config_frame)
                screen.blit(head_img, head_frame)
                screen.blit(hand_img, hand_frame)
                screen.blit(pajaro_img, pajaro_frame)
                screen.blit(logo_img, logo_frame)
                screen.blit(play_img, play_frame)
                screen.blit(exit_img, exit_frame)

                text = pygame.font.SysFont("Helvetica Bold.ttf", 80).render(f'Flappy Bird', True, (0, 0, 0))
                tr = text.get_rect()
                tr.center = (400, 100)
                screen.blit(text, tr)

                text = pygame.font.SysFont("Helvetica Bold.ttf", 79).render(f'Flappy Bird', True, (255, 255, 0))
                tr = text.get_rect()
                tr.center = (400, 100)
                screen.blit(text, tr)

                # Update screen
                pygame.display.flip()

                # Check if bird is touching a pipe
                if (bird_frame.colliderect(config_frame) or bird_frame.colliderect(config_frame)):
                    #game_is_running = False
                    config_img = pygame.image.load("Sprites/config_selected.png")
                    config_img = pygame.transform.scale(config_img, (config_img.get_width() / 8, config_img.get_height() / 8))
                    config_frame = config_img.get_rect()
                    config_frame.center = (160, 50)
                else:
                    config_img = pygame.image.load("Sprites/config.png")
                    config_img = pygame.transform.scale(config_img, (config_img.get_width() / 8, config_img.get_height() / 8))
                    config_frame = config_img.get_rect()
                    config_frame.center = (160, 50)
                
                
                if (bird_frame.colliderect(head_frame) or bird_frame.colliderect(head_frame)):
                    head_img = pygame.image.load("Sprites/head_selected.png")
                    head_img = pygame.transform.scale(head_img, (head_img.get_width() / 8, head_img.get_height() / 8))
                    head_frame = head_img.get_rect()
                    head_frame.center = (160, 140)
                else:
                    head_img = pygame.image.load("Sprites/head.png")
                    head_img = pygame.transform.scale(head_img, (head_img.get_width() / 8, head_img.get_height() / 8))
                    head_frame = head_img.get_rect()
                    head_frame.center = (160, 140)

                if (bird_frame.colliderect(hand_frame) or bird_frame.colliderect(hand_frame)):
                    hand_img = pygame.image.load("Sprites/hand_selected.png")
                    hand_img = pygame.transform.scale(hand_img, (hand_img.get_width() / 8, hand_img.get_height() / 8))
                    hand_frame = hand_img.get_rect()
                    hand_frame.center = (160, 230)
                else:
                    hand_img = pygame.image.load("Sprites/hand.png")
                    hand_img = pygame.transform.scale(hand_img, (hand_img.get_width() / 8, hand_img.get_height() / 8))
                    hand_frame = hand_img.get_rect()
                    hand_frame.center = (160, 230)

                if (bird_frame.colliderect(play_frame) or bird_frame.colliderect(play_frame)):
                    play_img = pygame.image.load("Sprites/play_selected.png")
                    play_img = pygame.transform.scale(play_img, (play_img.get_width() / 8, play_img.get_height() / 8))
                    play_frame = play_img.get_rect()
                    play_frame.center = (160, 320)
                else:
                    play_img = pygame.image.load("Sprites/play.png")
                    play_img = pygame.transform.scale(play_img, (play_img.get_width() / 8, play_img.get_height() / 8))
                    play_frame = play_img.get_rect()
                    play_frame.center = (160, 320)
                
                if (bird_frame.colliderect(exit_frame) or bird_frame.colliderect(exit_frame)):
                    exit_img = pygame.image.load("Sprites/exit_selected.png")
                    exit_img = pygame.transform.scale(exit_img, (exit_img.get_width() / 8, exit_img.get_height() / 8))
                    exit_frame = exit_img.get_rect()
                    exit_frame.center = (160, 410)
                else:
                    exit_img = pygame.image.load("Sprites/exit.png")
                    exit_img = pygame.transform.scale(exit_img, (exit_img.get_width() / 8, exit_img.get_height() / 8))
                    exit_frame = exit_img.get_rect()
                    exit_frame.center = (160, 410)

    def botonSig(self):
        self.__boton = self.__boton + 1
        if self.__boton == self.__cantBotones:
            self.__boton = 0

        self._notify(self)

    def botonAnt(self):
        self.__boton = self.__boton - 1
        if self.__boton == -1:
            self.__boton = self.__cantBotones

        self._notify(self)

    def getBoton(self) -> int:
        return self.__boton
