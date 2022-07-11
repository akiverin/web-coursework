<template>
  <div id="levels">
    <section class="levels">
      <div class="levels__wrapper">
        <h1 class="levels__title">Упс! Страница не найдена.</h1>
        <h2 class="levels__subtitle">
          Нам очень жаль, что вам пришлось столкнуться с неработающей страницей. Надеемся эта неловкость не отразится на вашем настроении!
        </h2>
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
  name: "NotFoundPage",
  props: {
    me: Object,
  },
  data() {
    return {

    };
  },
};
</script>

<style scoped></style>
