<template>
  <body id="app">
    <Header :me="this.me"/>
    <input type="text" v-model="token" class="visually-hidden">
    <input type="text" v-model="me" class="visually-hidden">
    <router-view @get-token="getToken" @post-token="postToken" :me="this.me"></router-view>
    <Footer :me="this.me"/>
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
      me: 0
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
        let api = 'http://127.0.0.1:8000/api/users/me/';
        axios ({
        headers: {Authorization: `Bearer ${this.token}`},
        method: 'get',
        url: api,
      })
        .then((response) => {
            console.log(response.data);
            this.me = response.data;
        })
        .catch(()=>{
          console.log(`Bearer ${this.token}`);
          this.me = 0;
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
      console.log(newToken)
      if (newToken!=""){localStorage.token = newToken}
    }
  },
}
</script>
