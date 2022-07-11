import VueRouter from 'vue-router'

import Home from '@/components/Home'
import Levels from '@/components/Levels'
import Registration from '@/components/Registration'
import Shop from '@/components/Shop'
import Rating from '@/components/Rating'
import Enemies from '@/components/Enemies'
import Authorization from '@/components/Authorization'
// import NotFound from '../pages/404'

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/rating',
      name: 'rating',
      component: Rating
    },
    {
      path: '/enemies',
      name: 'enemies',
      component: Enemies
    },
    {
      path: '/login',
      name: 'login',
      component: Authorization
    },
    {
      path: '/register',
      name: 'register',
      component: Registration
    },
    {
      path: '/shop',
      name: 'shop',
      component: Shop
    },
    {
      path: '/levels',
      name: 'Levels',
      component: Levels,
      // children: [
      //   {
      //     path: '',
      //     name: 'films',
      //     component: AllFilmsPage
      //   },
      //   {
      //     path: ':id',
      //     name: 'filmPage',
      //     component: FilmPage,
      //     beforeEnter: (to, from, next) => {
      //       if(localStorage.getItem('auth')) {
      //         next()
      //       } else {
      //         next({ name: 'films' })
      //       }
      //     }
      //   },
      //   {
      //     path: '*/*',
      //     redirect: { name: 'films' }
      //   },
      // ]
    },
    // {
    //   path: '*',
    //   name: 'notFound',
    //   component: NotFound
    // },
  ]
})