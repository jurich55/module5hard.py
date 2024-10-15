import time


class User:                                 # пользаватель и его :
    def __init__(self, nickname, password, age):
        self.nickname = nickname            # имя
        self.password = hash(password)      # пароль
        self.age = age                      # возраст


    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    def get_info(self):
        return self.nickname, self.password


class Video:                                  # фильм и его :
    def __init__(self, title, duration, adult_mode=False):
        self.title = title                    # название
        self.duration = duration              # продолжительность
        self.adult_mode = adult_mode          # возрастной ценз
        self.time_now = 0


class UrTube:
    def __init__(self):
        self.users = []              # список пользователей
        self.videos = []             # список фильмов
        self.current_user = None     # текущий пользователь

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                break

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f"пользователь {nickname} уже существует")

    def log_out(self):                   # сброс текущего пользователя
        self.current_user = None

    def add(self, *files):              # добавление film в список videos
        for film in files:
            if film.title not in [video.title for video in self.videos]:
                self.videos.append(film)

    def get_videos(self, text: str):
        files = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                files.append(video.title)
        return files         # список названий всех видео

    def watch_video(self, film: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if self.current_user.age < 18 and video.adult_mode == True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                if film in video.title:
                    for i in range(1, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')

              # создание экземпляров классов (ur, v1, v2)
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 8, adult_mode=True)

                             # Добавление видео
ur.add(v1, v2)

                             # Проверка поиска по поисковому слову
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

                 # Проверка пользователя на доступ к просмотру по возрасту
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

                            # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
