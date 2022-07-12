<template>
  <main id="registration">
    <section class="authorization">
      <div class="authorization__wrapper">
        <h1 class="authorization__title">Регистрация</h1>
        <form class="authorization__form form" @submit.prevent="RegistrationUser" v-if="this.flag<1">
        <div class="form__box">
            <label class="form__label" for="username"
              >Имя пользователя</label
            >
            <input
              class="form__input"
              v-model="username"
              name="username"
              id="username"
              type="text"
              required
            />
          </div>
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
          <!-- <div class="form__box">
            <label class="form__label" for="file">Аватар</label>
            <input
              class="form__input"
              @change="handleFileUpload()"
              name="file"
              id="file"
              type="file"
              ref="file"
              accept="image/png, image/jpeg"
              required
            />
          </div> -->
          <div class="form__box">
            <button class="form__button" type="submit">Зарегистрироваться</button>
          </div>
        </form>
        <ul class="authorization__errors"  v-if="this.flag<0">
            <li class="authorization__error" v-for="error in this.error" :key="error.id">
                <p class="authorization__error-text"> {{error}} </p>
            </li>
        </ul>
      </div>
    </section>
  </main>
</template>

<script>
import Vue from "vue";
import router from '@/routes'
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
  name: "RegistrationPage",
  data() {
    return {
      email: "",
      password: "",
      username: "",
      flag: 0,
      error: {},
    };
  },
  methods: {
    RegistrationUser: function () {
      let api = "/api/users/register/";
      axios({
        // headers: {Authorization: `Bearer ${this.token}`},
        method: "post",
        url: api,
        data: {
          username: this.username,
          email: this.email,
          password: this.password,
        },
      }).then(() => {
        this.flag = 1
        router.push({path:'/login'})
      }).catch((error) => {
        this.error = error.response.data.username;
        this.flag = -1;
        });
      // },
    },
  },
};
</script>

<style scoped></style>
