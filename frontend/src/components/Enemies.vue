<template>
  <div id="enemies">
    <section class="enemies">
      <div class="enemies__wrapper">
        <h1 class="enemies__title">Вражеские воины и монстры</h1>
        <h2 class="enemies__subtitle" v-if="me==0">Чтобы видеть коллекцию поверженых вами врагов, нужно пройти <a href="/login" class="enemies__link">авторизацию</a> на сайте.</h2>
        <ul class="enemies__list">
          <li v-for="enemy in enemies" :key="enemy.id" class="enemies__item">
            <img
              v-if="showEnemy(enemy,me.levels)"
              src="../../public/images/skyland01.jpeg"
              alt="Cover for location"
              class="enemies__image"
              v-bind:class="{
                enemies__image_easy: enemy.difficulty == 'easy',
                enemies__image_norm: enemy.difficulty == 'normal',
                enemies__image_hard: enemy.difficulty == 'hard',
              }"
            />
            <!-- <img :src="enemy.image" alt="Cover for location" class="enemies__image"> -->
            <div class="enemies__info" v-if="showEnemy(enemy,me.levels)">
              <h2 class="enemies__name">{{ enemy.name }}</h2>
              <p class="enemies__description">
                {{ enemy.description }}
              </p>
              <div class="enemies__other">
                <p class="enemies__coin">{{ enemy.reward }}</p>
                <p class="enemies__power">{{ enemy.power }}</p>
                <p class="enemies__heart">{{ enemy.hp }}</p>
              </div>
              <div class="enemies__levels">
                <p class="enemies__levels-head">Встречается в уровнях:</p>
                <p
                  v-for="level in enemy.levels_data"
                  :key="level.name"
                  class="enemies__levels-body"
                >
                  {{ level.name }}
                </p>
              </div>
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
  name: "EnemiesPage",
   props: {
    me: Object
  },
  data() {
    return {
      enemies: [],
    };
  },
  methods: {
    GetEnemies: function () {
      let api = "http://127.0.0.1:8000/api/enemies/";
      Vue.axios.get(api).then((response) => {
        console.log(response.data);
        this.enemies = response.data;
      });
    },
    showEnemy(enemy,count){
        let enemyLevels = enemy.levels_data;
        for (let i = 0; i < enemyLevels.length; i++){
            if (enemyLevels[i].id < count){
                return true
                } else {
                    return false
                }
        }
        return false
    }
  },
  mounted() {
    this.GetEnemies();
  },
};
</script>

<style scoped></style>
