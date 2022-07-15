<template>
    <section class="products" id="products">
        <div class="products__wrapper">
            <h1 class="products__title">Магазин "Все для злоключений"</h1>
            <p class="products__error" v-if="!this.token">Чтобы приобрести товары, <router-link :to="'/login'" class="products__link">авторизуйтесь</router-link>!</p>
            <p class="products__error" v-if="this.err_money">Не хватает монет для данной покупки!</p>
            <p class="products__money" v-if="this.token">Ваш кошелек: {{this.me.money}}</p>
            <ul class="products__list">
                <li v-for="product in products" :key="product.id" class="products__item">
                    <img :src="product.image" alt="Cover for location" class="products__image">
                    <div class="products__info">
                        <h2 class="products__name">{{ product.name }}</h2>
                        <p class="products__description">
                            {{ product.description }}                       
                        </p>
                        <div class="products__other">
                            <p class="products__coins">{{ product.price }}</p>
                            <button class="products__button" v-if="!OldBuy(product.user)"  @click="Buy(product)">Купить</button>
                            <button class="products__button products__button_old" v-if="OldBuy(product.user)" disabled>Куплено</button>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </section>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
  name: 'ShopPage',
  props:{
    me: {},
    token: String,
  },
  data(){
    return {
        products: [],
        err_money: 0,
    }
  },
  methods: {
    GetProducts: function(){
        let api = '/api/products/';
        Vue.axios.get(api).then((response) => {
            this.products = response.data;
            this.err_money = 0;
        });
    },
    OldBuy(arr){
        return arr.indexOf(this.me.id) != -1;
    },
    Buy(product){
        if(product.price<=this.me.money){
        let api = '/api/users/'+this.me.id+'/';
        axios({
        method: "patch",
        url: api,
        data: {
          money: this.me.money - product.price,
        },
      }).then(() => {
        this.AddProduct(product)
        window.location.reload();
      })
      .catch(() => {
        console.log('err');
    })}else {this.err_money=1}},
    AddProduct(product){
        let apiAdd = '/api/products/'+product.id+'/';
        let new_array = product.user;
        new_array.push(this.me.id);
        axios({
        method: "patch",
        url: apiAdd,
        data: {
          user: new_array,
        },
      })
    }
  },
  mounted (){
    this.GetProducts();
  }
}
</script>

<style scoped>
</style>
