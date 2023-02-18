# StoreProjects
<p>Проект называется StoreProjects и представляет собой магазин с возможно добавлять продукты в корзину, удалять их из корзины, получать основную информацию о продуктах и сумме корзины. Есть возможность регистрации, авторизации, аутентификации.</p>
<h3>Необходимые зависимости</h3>
<p>asgiref==3.6.0</p>
<p>Django==4.1.5</p>
<p>django_debug_toolbar==3.8.1</p>
<p>Pillow==9.4.0</p>
<p>sqlparse==0.4.3</p>
<p>tzdata==2022.7</p>
<h3>Скачивание необходимых пакетов</h3>
<p>pip install -r requirements.txt</p>
<p>pip install sqlite</p>  
<h4>для создания всех миграций вы должны находиться в папке StoreProject\store</h4>
<p>python manage.py makemigrations</p> 
<p>python manage.py migrate</p> 
<h3>Запуск сайта</h3>
<p>Для запуска сайта введите в терминал python manage.py runserver, для корректной работы вы должны находиться в папке StoreProject\store</p> 
