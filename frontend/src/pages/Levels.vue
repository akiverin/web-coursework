<template>
  <div id="levels">
    <section class="levels">
      <div class="levels__wrapper">
        <h1 class="levels__title">Игровые уровни и локации</h1>
        <h2 class="levels__subtitle" v-if="me == 0">
          Чтобы видеть прогресс пройденных уровней, нужно пройти
          <a href="/login" class="enemies__link">авторизацию</a> на сайте.
        </h2>
        <ul class="levels__list" v-if="me!=0">
          <li
            v-for="level in levels"
            :key="level.id"
            class="levels__item"
            v-bind:class="{
              levels__item_easy: level.difficulty == 'easy',
              levels__item_norm: level.difficulty == 'normal',
              levels__item_hard: level.difficulty == 'hard',
            }"
          >
            <img
              v-if="level.id < me.levels + 2"
              src="../../public/images/skyland01.jpeg"
              alt="Cover for location"
              class="levels__image"
            />
            <!-- <img :src="level.image" alt="Cover for location" class="levels__image"> -->
            <div v-if="level.id < me.levels + 2" class="levels__info">
              <h2 class="levels__name">{{ level.name }}</h2>
              <p class="levels__description">
                {{ level.description }}
              </p>
              <div class="levels__other">
                <p class="levels__coins">Награда: {{ level.reward }}</p>
                <p class="levels__best">Лучший: {{ BestUser(level.best_user)}}</p>
              </div>
            </div>
            <div class="levels__empty" v-if="level.id >= me.levels + 2">
              <h2 class="levels__name">Уровень #{{ level.id }}</h2>
              <p class="levels__alert">
                Не доступно! <br />Новая локация откроется при успешном
                прохождении предыдушего уровня.
              </p>
            </div>
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
  name: "LevelsPage",
  props: {
    me: Object,
  },
  data() {
    return {
      levels: [],
      users: [],
    };
  },
  methods: {
    GetLevels: function () {
      let api = "http://127.0.0.1:8000/api/levels/";
      // Vue.axios.get(api)
      axios({
        // headers: {Authorization: `Bearer ${this.$emit('post-token')}`},
        method: "get",
        url: api,
      }).then((response) => {
        this.levels = response.data;
      });
    },
    GetUsers: function () {
        let api = 'http://127.0.0.1:8000/api/users/';
        Vue.axios.get(api).then((response) => {
            console.log(response.data);
            this.users = response.data;
        });
    },
    BestUser(idBest){
         for (let i = 0; i < this.users.length; i++){
            if (this.users[i].id == idBest){
                return this.users[i].username
            }
        }
        return 'None'
    }
  },
  mounted() {
    this.GetLevels();
    this.GetUsers();
  },
};
</script>

<style scoped></style>
