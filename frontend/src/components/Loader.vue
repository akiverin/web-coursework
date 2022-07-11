<template>
  <div id="loader" class="loader">
    <div class="loader__wrapper">
      <div class="loader__main">
        <div class="loader__block">
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
          <div class="loader__item"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
  name: "LoaderComponent",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
