import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from '@/routes'

Vue.use(VueRouter)

// import '@/assets/styles/main.scss';

new Vue({
  render: h => h(App),
  el: '#app',
  router
})

