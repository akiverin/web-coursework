<template>
    <div id="products">
        <section class="products">
            <div class="products__wrapper">
                <h1 class="products__title">Магазин "Все для злоключений"</h1>
                <ul class="products__list">
                    <li v-for="product in products" :key="product.id" class="products__item">
                        <img src="../../public/images/skyland01.jpeg" alt="Cover for location" class="products__image">
                        <!-- <img :src="product.image" alt="Cover for location" class="products__image"> -->
                        <div class="products__info">
                            <h2 class="products__name">{{ product.name }}</h2>
                            <p class="products__description">
                                {{ product.description }}                       
                            </p>
                            <div class="products__other">
                                <p class="products__coins"> {{ product.price }} </p>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </section>
    </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
  name: 'ShopPage',
  data(){
    return {
        products: [],
    }
  },
  methods: {
    GetProducts: function(){
        let api = 'http://127.0.0.1:8000/api/products/';
        Vue.axios.get(api).then((response) => {
            this.products = response.data;
        });
    }
  },
  mounted (){
    this.GetProducts();
  }
}
</script>

<style scoped>
</style>
