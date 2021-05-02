<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
      </div>

      <ProductList
        v-for="product in category.products"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductList from "../../components/ProductList";
export default {
  name: "Category",
  components: {
    ProductList,
  },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name == "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`products/${categorySlug}/`)
        .then((res) => {
          this.category = res.data;

          document.title = this.category.name + " | Hamro Dokan";
        })
        .catch((err) => {
          console.log(err);
          toast({
            message: "Something went wrong..",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>