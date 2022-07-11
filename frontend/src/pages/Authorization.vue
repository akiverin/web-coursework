<template>
  <div id="authorization">
    <section class="authorization">
      <div class="authorization__wrapper">
        <h1 class="authorization__title">Авторизация</h1>
        <p class="authorization__info">Если у вас нет игрового аккаунта, то перейдите на <a class="authorization__link" href="/register">страницу регистрации</a></p>
        <form class="authorization__form form" @submit.prevent="LoginUser">
          <div class="form__box">
            <label class="form__label" for="email"
              >Адрес электронной почты</label
            >
            <input
              class="form__input"
              v-model="email"
              name="email"
              id="email"
              type="email"
              required
            />
          </div>
          <div class="form__box">
            <label class="form__label" for="password">Пароль</label>
            <input
              class="form__input"
              v-model="password"
              name="password"
              id="password"
              type="password"
              required
            />
          </div>
          <div class="form__box">
            <button class="form__button" type="submit">Войти в игру</button>
          </div>
        </form>
        <p class="authorization__error" v-if="this.error">Не правильно введен адрес электронной почты или пароль!</p>
      </div>
    </section>
    <Loader/>
  </div>
</template>

<script>
import Loader from '@/components/Loader'

import Vue from "vue";
import axios from "axios";
import router from '@/routes'
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
  name: "AuthorizationPage",
  props: {
    msg: String,
  },
  data() {
    return {
      email: "",
      password: "",
      error: 0
    };
  },
  components: {Loader},
  methods: {
    LoginUser: function () {
      let api = "http://127.0.0.1:8000/api/users/login/";
      axios({
        // headers: {Authorization: `Bearer ${this.token}`},
        method: "post",
        url: api,
        data: {
          email: this.email,
          password: this.password,
        },
      }).then((response) => {
        this.$emit("get-token", response.data.access);
        this.error = !this.error;
        router.push({path:'/'})

      })
      .catch((response) => {
        console.log(response);
        this.error = !this.error});
    },
  },
};
</script>

<style scoped></style>
