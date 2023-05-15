# client
This template should help get you started developing with Vue 3 in Vite.

## 報告 PDF 位置
See [documents](https://github.com/ZhiRongDev/ProjectMgmt/tree/main/documents)

## Flask Setup
```
$ cd server

$ python3.11 -m venv env
$ source env/bin/activate
(env)$
```

Next install Flask along with the Flask-CORS extension:
```
(env)$ pip install Flask==2.2.3 Flask-Cors==3.0.10
(env)$ flask run --port=5001 --debug
```



## Recommended IDE Setup
[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
npm run test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
npm run build
npm run test:e2e
```
