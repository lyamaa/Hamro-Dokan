<template>
  <div class="home">
    <section class="hero is-medium mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome, to Hamro Dokan..</p>
        <p class="subtitle">Hami sabaiko dokan, Hamro Dokan..</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <ProductList
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductList from "../components/ProductList";
export default {
  components: {
    ProductList,
  },
  data() {
    return {
      latestProducts: [],
    };
  },
  mounted() {
    this.getLatestProducts();
    document.title = " Home | Hamro Dokan";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("latest-products/")
        .then((res) => {
          this.latestProducts = res.data;
        })
        .catch((err) => console.log(err));
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped>
.hero {
  background-color: #202020;
}
.title {
  color: #ffffff;
}
.subtitle {
  color: #ffffff;
}
</style>