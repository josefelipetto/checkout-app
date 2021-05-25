import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import 'bootstrap'

const app = createApp(App)
app.config.globalProperties.baseAPIUrl = 'http://localhost:5000'
app.use(store).use(router).mount('#app')
