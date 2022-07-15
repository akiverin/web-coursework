import VueRouter from 'vue-router'

import Home from '@/pages/Home'
import Levels from '@/pages/Levels'
import Registration from '@/pages/Registration'
import Shop from '@/pages/Shop'
import Profile from '@/pages/Profile'
import Rating from '@/pages/Rating'
import NotFound from '@/pages/NotFound'
import Enemies from '@/pages/Enemies'
import Authorization from '@/pages/Authorization'

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
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
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/levels',
      name: 'Levels',
      component: Levels,
    },
    {
      path: '/:pathMatch(.*)*',
      beforeEnter: (to, from, next) => {
      next('/404');
      },
      },
    {
      path: '*',
      name: 'notFound',
      component: NotFound
    },
    
  ]
})
