import './assets/main.css'

import { createApp, markRaw } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// vuetify
import vuetify from '@/plugins/vuetify'

const pinia = createPinia()
// To allow using `this.router.xxx` in @/store/*.js
pinia.use(({ store }) => {
    store.router = markRaw(router)
})

const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(vuetify)

app.mount('#app')
