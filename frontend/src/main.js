import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import 'primeicons/primeicons.css'
import 'primevue/resources/themes/md-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css';

const app = createApp(App)

app.use(createPinia())
app.use(PrimeVue, { ripple: true })

app.mount('#app')
