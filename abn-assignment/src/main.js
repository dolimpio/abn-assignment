import 'primevue/resources/themes/md-light-indigo/theme.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import App from './App.vue'

const app = createApp(App)

app.use(createPinia())
app.use(PrimeVue, {ripple: true});

app.mount('#app')
