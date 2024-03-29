# Docker

1. Объяснить установку докер

2. DockerHUB регистрация

3. Показать основные команды докер (можно с конспекта показать)

4. Работа с Docker Desktop

5. Докерезация приложения: `app_flask`. Если есть желание выгрузить полученный образ на DockerHUB

6. Если группа понимает можно пойти дальше и показать docker compose: `app_compose`. В БД вручную добавить данные, простой документ с полем `name`. Контейнер вернет JSON. Важен просто принцип работы.

Взаємодія з контейнерами в Docker

1. Вхід в контейнер

  Команда `docker exec`` дозволяє виконувати команди в запущеному контейнері. Щоб увійти в контейнер та отримати оболонку (shell), ви можете використовувати наступну команду:

  ```bash
  docker exec -it [CONTAINER_ID_OR_NAME] /bin/sh
  ```

    Тут:

- `-it` дозволяє вам взаємодіяти з контейнером.
- `/bin/sh`` - це оболонка, яку ви хочете запустити. В залежності від образу, ви можливо захочете використовувати /bin/bash або іншу оболонку.

2. Копіювання файлів між контейнером та локальною системою

  Щоб копіювати файли з контейнера на вашу локальну машину, ви можете використовувати команду `docker cp`:

  ```shell
  docker cp [CONTAINER_ID_OR_NAME]:/path/in/container /local/path
  ```

  Наприклад:

  ```bash
  docker cp mycontainer:/app/config.txt ./config.txt
  ```

  Щоб копіювати файли з вашої локальної машини до контейнера:

  ```shell
  docker cp /local/path [CONTAINER_ID_OR_NAME]:/path/in/container
  ```

  Наприклад:

  ```bash
  docker cp ./config.txt mycontainer:/app/config.txt
  ```

Додаткові поради

Якщо ви хочете переглянути файли та директорії в контейнері без входу в нього, ви можете використовувати команду `docker exec` з командою `ls`:

```bash
docker exec [CONTAINER_ID_OR_NAME] ls /path/in/container
```

Коли ви взаємодієте з контейнером за допомогою `docker exec`, будьте обережні з командами, які можуть змінити стан контейнера або його конфігурацію. Завжди краще мати резервну копію даних перед внесенням змін.
