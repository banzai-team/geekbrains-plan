courses_grouped = """
name: Курсы
children:
  - children:
      - desc: Базовые навыки работы за компьютером
        id: '5455'
        name: Компьютерная грамотность
      - desc: Cоздание техники, роботов, и систем, которые реагируют на внешние факторы
          и управляются через интернет.
        id: '7347'
        name: Кибернетика умных устройств

      - name: Управление проектами и продуктами
        children:
          - id: '7918'
            name: Продакт-менеджер в ИТ
          - id: '7916'
            name: Проджект-менеджер в ИТ

      - children:
          - name: Для детей
            children:
              - id: '6870'
                name: Разработчик для школьников
              - id: '8016'
                name: Программирование на Python для детей
              - id: '5880'
                name: 'Программирование на Python в Minecraft: углублённый курс'
              - id: '5578'
                name: Графический дизайн
          - children:
              - name: Веб разработка
                children:
                  - name: Frontend-разработчик
                    children:
                      - name: Junior
                        id: '7325'
                      - name: Middle
                        id: '6261'
                  - id: '6265'
                    name: Fullstack-разработчик
                  - name: Веб-разработчик
                    children:
                      - name: Junior
                        id: '8766'
                      - name: Middle
                        id: '5876'
              - name: Разработка программного обеспечения
                children:
                  - id: '6144'
                    name: Разработчик
                  - id: '6239'
                    name: Инженер-программист

                  - name: Разработчик C++
                    children:
                    - id: '7628'
                      name: "Быстрый старт в профессию"
                    - id: '6247'
                      name: "Junior"
                  - name: Программист Java
                    children:
                      - name: Junior
                        id: '7267'
                      - name: Middle
                        id: '6277'

              - children:
                  - id: '7283'
                    name: iOS-разработчик
                  - id: '6215'
                    name: Разработчик приложений на Android
                  - id: '7606'
                    name: Android-разработчик
                name: Мобильная разработка
              - children:
                  - id: '7426'
                    name: Backend-разработчик
                  - id: '6265'
                    name: Fullstack-разработчик
                name: Бэкенд разработка
              - children:
                  - id: '7355'
                    name: Разработчик C#
                name: Разработка на C#
              - children:
                  - name: Python-разработчик
                    children:
                      - name: Junior
                        id: '8767'
                      - name: Middle
                        id: '6292'
                  - id: '6265'
                    name: Fullstack-разработчик
                name: Разработка на Python
              - id: '7783'
                name: 1С-разработчик
                children:
                  - id: '7783'
                    name: "Быстрый старт в профессию"
                  - id: '6783'
                    name: "С нуля до junior"
            name: Для взрослых
        name: Разработка ПО
      - children:
          - name: Инженер по тестированию
            children:
              - name: Junior
                id: '6302'
              - name: Middle
                id: '6304'
          - id: '7404'
            name: Ручной тестировщик
          - id: '8615'
            name: Автоматизация тестирования на Python
        name: Тестирование ПО
      - children:
          - name: ИТ-инженер Data Science Мастер
            children:
              - name: Junior
                id: '7295'
              - name: Middle
                id: '6340'
          - id: '7596'
            name: Искусственный интеллект
            desc: Общая программа
          - id: '9037'
            name: Специалист по внедрению ИИ
          - name: Data Science в медицине
            children:
              - name: Junior
                id: '7598'
              - name: Middle
                id: '6644'
          - desc: "Научитесь использовать ChatGPT, Midjourney и другие нейронные сети , чтобы зарабатывать, учиться быстрее и повышать личную эффективность"
            id: '7952'
            name: Нейрохищник
        name: Искусственный интеллект
      - name: DevOps-инженер
        children:
          - name: Junior
            id: '8979'
          - name: Middle
            id: '6652'
      - children:
          - id: '7849'
            name: Data Engineer
        name: Базы данных
      - children:
          - id: '5878'
            name: Кибербезопасность и приложения на Python
          - id: '6794'
            name: Информационная безопасность
        id: '6794'
        name: Информационная безопасность
      - children:
          - id: '6648'
            name: Сетевой инженер
        name: Сетевые технологии
      - children:
          - id: '4020'
            name: Дизайн и программирование в Roblox Studio

          - id: '7614'
            name: Гейм-дизайнер. Специалист
          - id: '8636'
            name: Геймдизайнер с нуля до PRO

          - id: '5802'
            name: Программирование и разработка игр на Scratch
          - id: '8539'
            name: Разработка игр на Unity для детей
          - id: '8680'
            name: Разработчик Игр на Unreal Engine
          - id: '8688'
            name: Разработчик Игр на Unity

          - id: '6104'
            name: Программирование и 3D-моделирование в Minecraft
          - id: '5880'
            name: 'Программирование на Python в Minecraft: углублённый курс'
        name: Разработка игр
    name: Информационные технологии
  - children:
      - id: '9181'
        name: Бухгалтер
    name: Финансы
  - children:
      - id: '8682'
        name: Сценарист
      - id: '8639'
        name: Фотограф
      - id: '8637'
        name: Режиссёр монтажа
    name: Кино и видео
  - children:
      - children:
          - id: '4020'
            name: Дизайн и программирование в Roblox Studio
          - id: '6104'
            name: Программирование и 3D-моделирование в Minecraft
          - children:
              - name: Быстрый старт карьеры
                id: '7614'
              - name: с нуля до Middle
                id: '8636'
            name: Гейм-дизайнер
        name: Игровой дизайн и разработка
      - children:
          - id: '6411'
            name: Бренд-менеджер
          - name: Графический дизайнер
            children:
              - name: Junior
                id: '6496'
              - name: Middle
                id: '6498'
          - id: '6496'
            name: Графический дизайнер
          - name: Цифровой дизайнер
            children:
              - name: Junior
                id: '6504'
              - name: Middle
                id: '6506'
          - id: '6475'
            name: Дизайнер
          - id: '5873'
            name: 'Веб-дизайн: углублённый курс'
          - id: '5793'
            name: Компьютерная графика
          - id: '7599'
            name: Веб-дизайнер
          - id: '7600'
            name: Моушн-дизайнер
          - id: '7601'
            name: Fullstack-дизайнер
          - name: UX/UI дизайнер Мастер
            children:
              - name: Junior
                id: '7603'
              - name: Middle
                id: '6540'
          - id: '7613'
            name: Графический дизайнер
          - id: '8638'
            name: Коммерческий иллюстратор
          - add_desc: true
            id: '7952'
            name: Нейрохищник
        name: Графический дизайн
      - children:
          - id: '5191'
            name: 3D-моделирование в Blender
          - id: '8635'
            name: 3D-дженералист
          - id: '5579'
            name: Углублённый курс по анимации
          - id: '7615'
            name: 3D моделирование
          - id: '8684'
            name: 3D-художник
          - id: '8686'
            name: Концепт-художник
        name: 3D моделирование и анимация
      - children:
          - id: '6500'
            name: Дизайнер интерьеров
          - name: Ландшафтный дизайнер
            children:
              - name: Быстрый старт карьеры
                id: '7605'
              - name: с нуля до Middle
                id: '6524'
        name: Дизайн интерьеров и ландшафтов
      - children:
          - id: '8637'
            name: Режиссёр монтажа
        name: Видеомонтаж
    name: Дизайн
  - children:
      - id: '6397'
        name: Digital-маркетолог
      - id: '6401'
        name: Интернет-маркетолог
      - id: '6416'
        name: Редактор
      - id: '6424'
        name: SEO-специалист
      - id: '6406'
        name: Продуктовый маркетолог
      - id: '6420'
        name: SMM-менеджер
      - id: '6466'
        name: Perfomance менеджер
      - id: '6428'
        name: Таргетолог
      - id: '6432'
        name: Специалист по работе с маркетплейсами
      - id: '8285'
        name: Контекстная реклама
      - id: '8458'
        name: Трафик-менеджер
      - id: '7617'
        name: Таргетолог
      - id: '7618'
        name: SMM-менеджер
      - id: '8745'
        name: Менеджер по работе с маркетплейсами и e-commerce
      - id: '9182'
        name: Как продавать на Wildberries (совместно со SkillBox)
    name: Маркетинг
  - children:
      - id: '6156'
        name: Инженер-аналитик
      - id: '6163'
        name: BI (Business Intelligence) аналитик
      - id: '6203'
        name: Продуктовый аналитик
      - id: '7287'
        name: Финансовый аналитик
      - id: '7323'
        name: Аналитик данных
      - id: '7339'
        name: Бизнес-аналитик
      - id: '6656'
        name: Системный и бизнес аналитик
      - id: '7414'
        name: Системный аналитик
    name: Аналитика
"""

SIMULAR_COURSES = {
    '5873': {'simular': [{'match_score': 1.0, 'matches': 6, 'program_id': '6540'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6506'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6504'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '6475'}],
             'tech_num': 6},
    '6144': {'simular': [{'match_score': 1.0, 'matches': 21, 'program_id': '6239'},
                         {'match_score': 0.47619047619047616,
                          'matches': 10,
                          'program_id': '6302'},
                         {'match_score': 0.38095238095238093,
                          'matches': 8,
                          'program_id': '6304'},
                         {'match_score': 0.38095238095238093,
                          'matches': 8,
                          'program_id': '8615'},
                         {'match_score': 0.3333333333333333,
                          'matches': 7,
                          'program_id': '6156'}],
             'tech_num': 21},
    '6156': {'simular': [{'match_score': 0.5833333333333334,
                          'matches': 7,
                          'program_id': '6144'},
                         {'match_score': 0.5833333333333334,
                          'matches': 7,
                          'program_id': '6239'},
                         {'match_score': 0.5, 'matches': 6, 'program_id': '6163'},
                         {'match_score': 0.5, 'matches': 6, 'program_id': '7414'},
                         {'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '6203'}],
             'tech_num': 12},
    '6163': {'simular': [{'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6156'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '7414'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6144'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6239'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '6203'}],
             'tech_num': 9},
    '6203': {'simular': [{'match_score': 0.6, 'matches': 6, 'program_id': '7287'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '6144'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '6156'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '6239'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '7339'}],
             'tech_num': 10},
    '6215': {'simular': [{'match_score': 1.0, 'matches': 11, 'program_id': '7606'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6870'}],
             'tech_num': 11},
    '6239': {'simular': [{'match_score': 1.0, 'matches': 21, 'program_id': '6144'},
                         {'match_score': 0.47619047619047616,
                          'matches': 10,
                          'program_id': '6302'},
                         {'match_score': 0.38095238095238093,
                          'matches': 8,
                          'program_id': '6304'},
                         {'match_score': 0.38095238095238093,
                          'matches': 8,
                          'program_id': '8615'},
                         {'match_score': 0.3333333333333333,
                          'matches': 7,
                          'program_id': '6156'}],
             'tech_num': 21},
    '6247': {'simular': [{'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6144'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6239'}],
             'tech_num': 8},
    '6261': {'simular': [{'match_score': 0.6, 'matches': 6, 'program_id': '7325'},
                         {'match_score': 0.3, 'matches': 3, 'program_id': '6144'},
                         {'match_score': 0.3, 'matches': 3, 'program_id': '6239'},
                         {'match_score': 0.3, 'matches': 3, 'program_id': '6302'},
                         {'match_score': 0.3, 'matches': 3, 'program_id': '6265'}],
             'tech_num': 10},
    '6265': {'simular': [{'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6292'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '8766'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '8767'}],
             'tech_num': 6},
    '6277': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '7267'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6144'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6239'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6302'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6304'}],
             'tech_num': 9},
    '6292': {'simular': [{'match_score': 1.0, 'matches': 7, 'program_id': '8767'},
                         {'match_score': 0.8571428571428571,
                          'matches': 6,
                          'program_id': '6144'},
                         {'match_score': 0.8571428571428571,
                          'matches': 6,
                          'program_id': '6239'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '6302'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '6304'}],
             'tech_num': 7},
    '6302': {'simular': [{'match_score': 0.43478260869565216,
                          'matches': 10,
                          'program_id': '6144'},
                         {'match_score': 0.43478260869565216,
                          'matches': 10,
                          'program_id': '6239'},
                         {'match_score': 0.391304347826087,
                          'matches': 9,
                          'program_id': '6304'},
                         {'match_score': 0.391304347826087,
                          'matches': 9,
                          'program_id': '8615'},
                         {'match_score': 0.2608695652173913,
                          'matches': 6,
                          'program_id': '6277'}],
             'tech_num': 23},
    '6304': {'simular': [{'match_score': 1.0, 'matches': 13, 'program_id': '8615'},
                         {'match_score': 0.6923076923076923,
                          'matches': 9,
                          'program_id': '6302'},
                         {'match_score': 0.6153846153846154,
                          'matches': 8,
                          'program_id': '6144'},
                         {'match_score': 0.6153846153846154,
                          'matches': 8,
                          'program_id': '6239'},
                         {'match_score': 0.46153846153846156,
                          'matches': 6,
                          'program_id': '6870'}],
             'tech_num': 13},
    '6340': {'simular': [{'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6644'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '7295'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '7596'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '7598'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '7849'}],
             'tech_num': 9},
    '6397': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6406'},
                         {'match_score': 0.7777777777777778,
                          'matches': 7,
                          'program_id': '6401'},
                         {'match_score': 0.7777777777777778,
                          'matches': 7,
                          'program_id': '6424'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '8458'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '8285'}],
             'tech_num': 9},
    '6401': {'simular': [{'match_score': 1.0, 'matches': 7, 'program_id': '6397'},
                         {'match_score': 1.0, 'matches': 7, 'program_id': '6424'},
                         {'match_score': 1.0, 'matches': 7, 'program_id': '6406'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '8458'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '8285'}],
             'tech_num': 7},
    '6406': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6397'},
                         {'match_score': 0.7777777777777778,
                          'matches': 7,
                          'program_id': '6401'},
                         {'match_score': 0.7777777777777778,
                          'matches': 7,
                          'program_id': '6424'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '8458'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '8285'}],
             'tech_num': 9},
    '6411': {'simular': [{'match_score': 0.8, 'matches': 4, 'program_id': '6466'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '7618'}],
             'tech_num': 5},
    '6420': {'simular': [{'match_score': 1.0, 'matches': 4, 'program_id': '6428'},
                         {'match_score': 1.0, 'matches': 4, 'program_id': '7617'},
                         {'match_score': 0.75, 'matches': 3, 'program_id': '6397'},
                         {'match_score': 0.75, 'matches': 3, 'program_id': '6401'},
                         {'match_score': 0.75,
                          'matches': 3,
                          'program_id': '6424'}],
             'tech_num': 4},
    '6424': {'simular': [{'match_score': 1.0, 'matches': 7, 'program_id': '6397'},
                         {'match_score': 1.0, 'matches': 7, 'program_id': '6401'},
                         {'match_score': 1.0, 'matches': 7, 'program_id': '6406'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '8458'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '8285'}],
             'tech_num': 7},
    '6428': {'simular': [{'match_score': 0.8, 'matches': 4, 'program_id': '6420'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '7617'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6397'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6401'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6424'}],
             'tech_num': 5},
    '6466': {'simular': [{'match_score': 0.5, 'matches': 4, 'program_id': '6411'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '7618'}],
             'tech_num': 8},
    '6475': {'simular': [{'match_score': 0.5, 'matches': 5, 'program_id': '6496'},
                         {'match_score': 0.4, 'matches': 4, 'program_id': '6524'},
                         {'match_score': 0.4, 'matches': 4, 'program_id': '7601'},
                         {'match_score': 0.4, 'matches': 4, 'program_id': '7615'},
                         {'match_score': 0.4, 'matches': 4, 'program_id': '7618'}],
             'tech_num': 10},
    '6496': {'simular': [{'match_score': 1.0, 'matches': 5, 'program_id': '6475'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '7601'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '7618'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6506'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6504'}],
             'tech_num': 5},
    '6504': {'simular': [{'match_score': 1.0, 'matches': 5, 'program_id': '6506'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6540'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '5873'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6475'}],
             'tech_num': 5},
    '6506': {'simular': [{'match_score': 1.0, 'matches': 5, 'program_id': '6504'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6540'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '5873'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6475'}],
             'tech_num': 5},
    '6524': {'simular': [{'match_score': 1.0, 'matches': 4, 'program_id': '6475'},
                         {'match_score': 0.75,
                          'matches': 3,
                          'program_id': '7615'}],
             'tech_num': 4},
    '6540': {'simular': [{'match_score': 1.0, 'matches': 6, 'program_id': '5873'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6506'},
                         {'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6504'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '6475'}],
             'tech_num': 6},
    '6644': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '7295'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7596'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7598'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7849'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6340'}],
             'tech_num': 9},
    '6648': {'simular': [{'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6144'},
                         {'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6239'},
                         {'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6794'}],
             'tech_num': 7},
    '6652': {'simular': [{'match_score': 1.0, 'matches': 11, 'program_id': '8979'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6304'}],
             'tech_num': 11},
    '6656': {'simular': [{'match_score': 1.0, 'matches': 7, 'program_id': '7414'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '6156'},
                         {'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6144'},
                         {'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6163'},
                         {'match_score': 0.42857142857142855,
                          'matches': 3,
                          'program_id': '6239'}],
             'tech_num': 7},
    '6783': {'simular': [{'match_score': 1.0, 'matches': 6, 'program_id': '7783'}],
             'tech_num': 6},
    '6794': {'simular': [{'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6144'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6239'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6648'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6652'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '8979'}],
             'tech_num': 8},
    '6870': {'simular': [{'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6304'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '8615'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6144'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6239'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6302'}],
             'tech_num': 9},
    '7267': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6277'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6144'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6239'},
                         {'match_score': 0.6666666666666666,
                          'matches': 6,
                          'program_id': '6302'},
                         {'match_score': 0.5555555555555556,
                          'matches': 5,
                          'program_id': '6304'}],
             'tech_num': 9},
    '7283': {'simular': [{'match_score': 0.5, 'matches': 4, 'program_id': '6215'},
                         {'match_score': 0.5, 'matches': 4, 'program_id': '7606'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6144'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6239'},
                         {'match_score': 0.375,
                          'matches': 3,
                          'program_id': '6302'}],
             'tech_num': 8},
    '7287': {'simular': [{'match_score': 0.75, 'matches': 6, 'program_id': '6203'},
                         {'match_score': 0.625,
                          'matches': 5,
                          'program_id': '6144'},
                         {'match_score': 0.625,
                          'matches': 5,
                          'program_id': '6156'},
                         {'match_score': 0.625,
                          'matches': 5,
                          'program_id': '6239'},
                         {'match_score': 0.625,
                          'matches': 5,
                          'program_id': '7339'}],
             'tech_num': 8},
    '7295': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6644'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7596'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7598'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7849'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6340'}],
             'tech_num': 9},
    '7323': {'simular': [{'match_score': 0.6666666666666666,
                          'matches': 4,
                          'program_id': '6203'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '6156'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '8285'},
                         {'match_score': 0.5, 'matches': 3, 'program_id': '8458'}],
             'tech_num': 6},
    '7325': {'simular': [{'match_score': 0.8571428571428571,
                          'matches': 6,
                          'program_id': '6261'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.5714285714285714,
                          'matches': 4,
                          'program_id': '6292'}],
             'tech_num': 7},
    '7339': {'simular': [{'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '6144'},
                         {'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '6156'},
                         {'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '6203'},
                         {'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '6239'},
                         {'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '7287'}],
             'tech_num': 12},
    '7355': {'simular': [{'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '6292'},
                         {'match_score': 0.4444444444444444,
                          'matches': 4,
                          'program_id': '7325'}],
             'tech_num': 9},
    '7404': {'simular': [{'match_score': 0.75,
                          'matches': 3,
                          'program_id': '6302'}],
             'tech_num': 4},
    '7414': {'simular': [{'match_score': 0.4375,
                          'matches': 7,
                          'program_id': '6656'},
                         {'match_score': 0.375,
                          'matches': 6,
                          'program_id': '6156'},
                         {'match_score': 0.375,
                          'matches': 6,
                          'program_id': '6163'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '6302'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '7339'}],
             'tech_num': 16},
    '7426': {'simular': [{'match_score': 0.7, 'matches': 7, 'program_id': '6144'},
                         {'match_score': 0.7, 'matches': 7, 'program_id': '6239'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '6302'},
                         {'match_score': 0.5, 'matches': 5, 'program_id': '6870'},
                         {'match_score': 0.4, 'matches': 4, 'program_id': '6304'}],
             'tech_num': 10},
    '7596': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6644'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7295'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7598'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7849'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6340'}],
             'tech_num': 9},
    '7598': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6644'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7295'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7596'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7849'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6340'}],
             'tech_num': 9},
    '7599': {'simular': [{'match_score': 1.0, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 1.0, 'matches': 3, 'program_id': '6506'},
                         {'match_score': 1.0, 'matches': 3, 'program_id': '6504'},
                         {'match_score': 1.0, 'matches': 3, 'program_id': '6475'},
                         {'match_score': 1.0, 'matches': 3, 'program_id': '6540'}],
             'tech_num': 3},
    '7601': {'simular': [{'match_score': 0.8, 'matches': 4, 'program_id': '6496'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6475'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '7618'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6506'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6504'}],
             'tech_num': 5},
    '7605': {'simular': [{'match_score': 0.75,
                          'matches': 3,
                          'program_id': '6475'}],
             'tech_num': 4},
    '7606': {'simular': [{'match_score': 1.0, 'matches': 11, 'program_id': '6215'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6870'}],
             'tech_num': 11},
    '7613': {'simular': [{'match_score': 1.0, 'matches': 3, 'program_id': '6496'},
                         {'match_score': 1.0, 'matches': 3, 'program_id': '6475'}],
             'tech_num': 3},
    '7615': {'simular': [{'match_score': 1.0, 'matches': 4, 'program_id': '6475'},
                         {'match_score': 0.75,
                          'matches': 3,
                          'program_id': '6524'}],
             'tech_num': 4},
    '7617': {'simular': [{'match_score': 1.0, 'matches': 4, 'program_id': '6420'},
                         {'match_score': 1.0, 'matches': 4, 'program_id': '6428'},
                         {'match_score': 0.75, 'matches': 3, 'program_id': '6397'},
                         {'match_score': 0.75, 'matches': 3, 'program_id': '6401'},
                         {'match_score': 0.75,
                          'matches': 3,
                          'program_id': '6424'}],
             'tech_num': 4},
    '7618': {'simular': [{'match_score': 0.4166666666666667,
                          'matches': 5,
                          'program_id': '8458'},
                         {'match_score': 0.3333333333333333,
                          'matches': 4,
                          'program_id': '6496'},
                         {'match_score': 0.3333333333333333,
                          'matches': 4,
                          'program_id': '6475'},
                         {'match_score': 0.3333333333333333,
                          'matches': 4,
                          'program_id': '7601'},
                         {'match_score': 0.25,
                          'matches': 3,
                          'program_id': '6411'}],
             'tech_num': 12},
    '7628': {'simular': [{'match_score': 0.6, 'matches': 3, 'program_id': '6144'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6239'},
                         {'match_score': 0.6, 'matches': 3, 'program_id': '6302'}],
             'tech_num': 5},
    '7783': {'simular': [{'match_score': 0.6, 'matches': 6, 'program_id': '6783'}],
             'tech_num': 10},
    '7849': {'simular': [{'match_score': 1.0, 'matches': 9, 'program_id': '6644'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7295'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7596'},
                         {'match_score': 1.0, 'matches': 9, 'program_id': '7598'},
                         {'match_score': 0.8888888888888888,
                          'matches': 8,
                          'program_id': '6340'}],
             'tech_num': 9},
    '8285': {'simular': [{'match_score': 1.0, 'matches': 13, 'program_id': '8458'},
                         {'match_score': 0.3076923076923077,
                          'matches': 4,
                          'program_id': '6397'},
                         {'match_score': 0.3076923076923077,
                          'matches': 4,
                          'program_id': '6401'},
                         {'match_score': 0.3076923076923077,
                          'matches': 4,
                          'program_id': '6424'},
                         {'match_score': 0.3076923076923077,
                          'matches': 4,
                          'program_id': '6406'}],
             'tech_num': 13},
    '8458': {'simular': [{'match_score': 0.8125,
                          'matches': 13,
                          'program_id': '8285'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '6397'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '6401'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '6424'},
                         {'match_score': 0.3125,
                          'matches': 5,
                          'program_id': '6406'}],
             'tech_num': 16},
    '8615': {'simular': [{'match_score': 1.0, 'matches': 13, 'program_id': '6304'},
                         {'match_score': 0.6923076923076923,
                          'matches': 9,
                          'program_id': '6302'},
                         {'match_score': 0.6153846153846154,
                          'matches': 8,
                          'program_id': '6144'},
                         {'match_score': 0.6153846153846154,
                          'matches': 8,
                          'program_id': '6239'},
                         {'match_score': 0.46153846153846156,
                          'matches': 6,
                          'program_id': '6870'}],
             'tech_num': 13},
    '8635': {'simular': [{'match_score': 0.5, 'matches': 5, 'program_id': '8684'}],
             'tech_num': 10},
    '8684': {'simular': [{'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '8635'}],
             'tech_num': 7},
    '8766': {'simular': [{'match_score': 0.8, 'matches': 4, 'program_id': '6144'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6239'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6265'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '6292'},
                         {'match_score': 0.8, 'matches': 4, 'program_id': '8767'}],
             'tech_num': 5},
    '8767': {'simular': [{'match_score': 1.0, 'matches': 7, 'program_id': '6292'},
                         {'match_score': 0.8571428571428571,
                          'matches': 6,
                          'program_id': '6144'},
                         {'match_score': 0.8571428571428571,
                          'matches': 6,
                          'program_id': '6239'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '6302'},
                         {'match_score': 0.7142857142857143,
                          'matches': 5,
                          'program_id': '6304'}],
             'tech_num': 7},
    '8979': {'simular': [{'match_score': 1.0, 'matches': 11, 'program_id': '6652'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6144'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6239'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6302'},
                         {'match_score': 0.36363636363636365,
                          'matches': 4,
                          'program_id': '6304'}],
             'tech_num': 11}}
