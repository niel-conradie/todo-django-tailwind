# **To Do Django Tailwind**

**Django with Tailwind To Do Web Application.**

A To Do web application is a computer program that uses online technology, including browsers, to help users manage their tasks. It allows users to create, read, update, and delete data, also known as CRUD operations. Users can add tasks, manage them, and mark them as completed.

---

## **Requirements**

- [Backend](https://github.com/niel-conradie/todo-django-tailwind/blob/master/requirements.txt)

  - [python - 3.12.X](https://www.python.org/)
  - [django - 4.2.9](https://pypi.org/project/Django/)
  - [django-allauth - 0.60.0](https://pypi.org/project/django-allauth/)
  - [django-browser-reload - 1.12.1](https://pypi.org/project/django-browser-reload/)
  - [django-debug-toolbar - 4.2.0](https://pypi.org/project/django-debug-toolbar/)
  - [docker - 4.25.2](https://www.docker.com/)
  - [environs - 10.0.0](https://pypi.org/project/environs/)
  - [gunicorn - 21.2.0](https://pypi.org/project/gunicorn/)
  - [postgreSQL - 13.13.0](https://www.postgresql.org/)
  - [psycopg - 3.1.17](https://pypi.org/project/psycopg/)
  - [psycopg-binary - 3.1.17](https://pypi.org/project/psycopg-binary/)
  - [whitenoise - 6.6.0](https://pypi.org/project/whitenoise/)

- [Frontend](https://github.com/niel-conradie/todo-django-tailwind/blob/master/package.json)

  - [node.js - 20.10.0](https://nodejs.org/en)
  - [npm.js - 10.2.3](https://www.npmjs.com/)
  - [autoprefixer - 10.4.16](https://www.npmjs.com/package/autoprefixer)
  - [babel/core - 7.23.7](https://www.npmjs.com/package/@babel/core)
  - [babel/preset-env - 7.23.7](https://www.npmjs.com/package/@babel/preset-env)
  - [cssnano - 6.0.3](https://www.npmjs.com/package/cssnano)
  - [gulp - 4.0.2](https://www.npmjs.com/package/gulp)
  - [gulp-babel - 8.0.0](https://www.npmjs.com/package/gulp-babel)
  - [gulp-concat - 2.6.1](https://www.npmjs.com/package/gulp-concat)
  - [gulp-postcss - 9.0.1](https://www.npmjs.com/package/gulp-postcss)
  - [gulp-rename - 2.0.0](https://www.npmjs.com/package/gulp-rename)
  - [gulp-terser - 2.1.0](https://www.npmjs.com/package/gulp-terser)
  - [postcss - 8.4.33](https://www.npmjs.com/package/postcss)
  - [postcss-import - 16.0.0](https://www.npmjs.com/package/postcss-import)
  - [prettier 3.1.1](https://www.npmjs.com/package/prettier)
  - [prettier-plugin-tailwindcss 0.5.11](https://www.npmjs.com/package/prettier-plugin-tailwindcss)
  - [tailwindcss - 3.4.1](https://www.npmjs.com/package/tailwindcss)

---

## **Installation**

To Do Django Tailwind can be installed via [docker](https://www.docker.com/) & [npm](https://www.npmjs.com/). To start, clone the repository to your local computer and change into the proper directory, then use the commands to build the docker image and install the required dependencies.

- **Clone Repository**

```bash
git clone https://github.com/niel-conradie/todo-django-tailwind.git
```

- **Change Directory**

```bash
cd todo-django-tailwind
```

### **Docker**

- **Build Docker Image**

```bash
docker build .
```

- **Compose Docker Image**

```bash
docker compose up
```

- **Migrate Database**

```bash
docker compose exec web python manage.py migrate
```

- **Create Superuser**

```bash
docker compose exec web python manage.py createsuperuser
```

### **NPM**

- **Install Dependencies**

```bash
npm install
```

---

## **Usage**

Use the following commands for your desired outcome:

### **Backend**

- Starting a Docker development server.

```bash
docker compose up
```

- Ending a Docker development server.

```bash
docker compose down
```

### **Frontend**

- Starting a Gulp development server.

```bash
gulp
```

- Ending a Gulp development server.

```bash
CTRL + C
```

- Building Frontend for production.

```bash
gulp build
```

---

## **License**

[MIT License](https://github.com/niel-conradie/todo-django-tailwind/blob/master/LICENSE)

---
