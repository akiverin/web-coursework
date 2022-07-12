<template>
  <body id="app">
    <Header :me="this.me" :token="this.token"/>
    <input type="text" v-model="token" class="visually-hidden">
    <input type="text" v-model="me" class="visually-hidden">
    <router-view @get-token="getToken" @post-token="postToken" :me="this.me" :token="this.token"></router-view>
    <Footer :me="this.me" :token="this.token"/>
  </body>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

export default {
  name: 'App',
  data(){
    return {
      token: '',
      me: {},
    }
  },
  components: {
    Header,
    Footer
  },
  methods: {
    getToken (token){
      this.token = token;
      if (this.token != ""){
        this.getMe()
      }
    },
    postToken (){
      return this.token;
    },
    getMe(){
        let api = '/api/users/me/';
        axios ({
        headers: {Authorization: `Bearer ${this.token}`},
        method: 'get',
        url: api,
      })
        .then((response) => {
            if (response.data.is_activ == true){this.me = response.data;}
        })
        .catch(()=>{
          this.me = {};
        });
    }
  },
  mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
    }
     
    if (this.token != ""){
        this.getMe()
    }
  },
  watch: {
    token(newToken) {
      console.log(5)
      if (newToken!=""){
        localStorage.token = newToken;
        this.getMe()
        }
    }
  },
}
</script>
