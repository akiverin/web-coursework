<template>
  <div id="rating">
    <section class="rating">
      <div class="rating__wrapper">
        <h1 class="rating__title">Рейтинг игроков</h1>
        <ul class="rating__list">
          <li v-for="user in sortArray()" :key="user.id" class="rating__item" v-bind:class="{rating__item_me: user.username == me.username}">
            <img
              src="../../public/images/skyland01.jpeg"
              alt="Cover for location"
              class="rating__image"
            />
            <!-- <img :src="user.image" alt="Cover for location" class="rating__image"> -->
            <div class="rating__info">
              <h2 class="rating__name">{{ user.username }}</h2>
              <p class="rating__scores">{{ user.scores }}</p>
              <p class="rating__levels">
                {{ user.levels }}'ый уровень
              </p>
              <p class="rating__coins">{{ user.money }}</p>
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
  name: "RatingPage",
  props: {
    me: Object
  },
  data() {
    return {
      users: [],
    };
  },
  methods: {
    GetUsers: function () {
      let api = "http://127.0.0.1:8000/api/users/";
      Vue.axios.get(api).then((response) => {
        this.users = response.data;
      });
      this.sort_users = this.sortArray(this.users);
    },
    sortArray: function () {
      return this.users.slice().sort(function (a, b) {
        return a.scores < b.scores ? 1 : -1;
      });
    },
  },
  mounted() {
    this.GetUsers();
  },
};
</script>

<style scoped></style>
