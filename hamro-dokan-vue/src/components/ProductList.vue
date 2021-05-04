<template>
  <div class="column is-3">
    <a v-bind:href="product.getAbsoluteUrl">
      <div class="box">
        <figure class="image is-5by4 mb-4">
          <img :src="product.getThumbnail" alt="product thumbnail" />
        </figure>
        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-grey">
          <span class="tag is-warning is-medium mt-2"
            >&#8360; {{ product.price }}</span
          >
        </p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: "ProductList",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
