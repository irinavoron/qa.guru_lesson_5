# qa.guru_lesson_5

В новом проекте, соответствующему базовому формату «проекта для автотестов», разработай автотест на полное заполнение и отправку формы https://demoqa.com/automation-practice-form, а также проверку заполненных данных в поп-апе



Запушь код в github-репозиторий и дай на него ссылку в качестве ответа на домашнее задание.



Условия:

- Библиотеки, разрешенные к использованию: pytest, selene.

- Тест должен жить в своем модуле python 

- Запрещено создавать свои собственные:

- функции

- кроме функции с тестом и опционально функции-фикстуры с настройкой браузера внутри conftest.py

- переменные

- дополнительные python модули кроме модуля с тестом

- кроме опционального conftest.py



Учитывая ограничения, упомянутые выше – постарайся написать максимально читабельный и легкий в последующей поддержке код. В основном это будет касаться именно подбора локаторов для нахождения соответствующих элементов.

ЧАСТЬ I (реализовать в бренче mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).
Дополнительные условия и подсказки:

* Все элементы выносить в отдельные поля объекта класса не обязательно, но стоит это сделать с теми элементами, которые будут повторяться.

* Класс для PageObject должен лежать в выделенном модуле в выделенном пакете внутри проекта, как было показано на уроке.
