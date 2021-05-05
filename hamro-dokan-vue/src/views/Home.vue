<template>
  <div class="home">
    <!-- Start Hero Carousel -->
    <section class="section" id="carousel-section">
      <div class="container">
        <div id="carousel-demo" class="carousel pb-6" style="overflow: hidden">
          <div class="item-1">
            <div class="columns">
              <div class="column is-half">
                <h2 class="title is-1">Welcome to Hamro Dokan</h2>
                <p>
                  Hamro Dokan strives to provide customers the best shopping
                  experience in Nepal. The online store is updated daily and new
                  products are added every day to cater to all your needs. Visit
                  <a href="/">hamro-dokan.com.np</a> to experience shopping in
                  Nepal as never before.
                </p>
                <br />

                <div class="buttons is-left">
                  <button
                    class="button is-medium is-orange button is-link is-light"
                  >
                    SHOP NOW
                  </button>
                  <button class="button is-medium is-black is-primary is-light">
                    CONTACT US
                  </button>
                </div>
              </div>
              <div class="column is-half">
                <figure class="image is is-covered">
                  <img
                    loading="lazy"
                    src="https://res.cloudinary.com/dazyxzm1e/image/upload/v1620129151/undraw_shopping_app_flsj_k5vifw.svg"
                    alt=""
                  />
                </figure>
              </div>
            </div>
          </div>
          <div class="item-2">
            <div class="columns">
              <div class="column is-half">
                <h2 class="title is-1">Welcome to Hamro Dokan</h2>
                <p>
                  There are many variations of passages of Lorem Ipsum
                  available, but the majority have suffered alteration in some
                  form, by injected humour, or randomised words which don't look
                  even slightly believable.
                </p>
                <br />

                <div class="buttons is-left">
                  <button
                    class="button is-medium is-orange button is-link is-light"
                  >
                    SHOP NOW
                  </button>
                  <button class="button is-medium is-black is-primary is-light">
                    CONTACT US
                  </button>
                </div>
              </div>
              <div class="column is-half">
                <figure class="image is is-covered">
                  <img
                    loading="lazy"
                    src="https://res.cloudinary.com/dazyxzm1e/image/upload/v1620129151/undraw_add_to_cart_vkjp_seg44h.svg"
                    alt=""
                  />
                </figure>
              </div>
            </div>
            <!-- Slide Content -->
          </div>
          <div class="item-3">
            <!-- Slide Content -->
            <div class="columns">
              <div class="column is-half">
                <h2 class="title is-1">Welcome to Hamro Dokan</h2>
                <p>
                  There are many variations of passages of Lorem Ipsum
                  available, but the majority have suffered alteration in some
                  form, by injected humour, or randomised words which don't look
                  even slightly believable.
                </p>
                <br />

                <div class="buttons is-left">
                  <button
                    class="button is-medium is-orange button is-link is-light"
                  >
                    SHOP NOW
                  </button>
                  <button class="button is-medium is-black is-primary is-light">
                    CONTACT US
                  </button>
                </div>
              </div>
              <div class="column is-half">
                <figure class="image is is-covered">
                  <img
                    loading="lazy"
                    src="https://res.cloudinary.com/dazyxzm1e/image/upload/v1620129151/undraw_web_shopping_dd4l_fszlmm.svg"
                    alt=""
                  />
                </figure>
              </div>
            </div>
          </div>
        </div>
        <!-- End Carousel -->
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
    <!-- LIST SECTION -->

    <section class="section">
      <div class="container">
        <div class="has-text-centered pb-6">
          <h1 class="title is-1">Best Products</h1>
          <h3 class="subtitle">
            There are many variations of passages of Lorem Ipsum available, but
            the majority have
          </h3>
        </div>
        <div class="columns">
          <div
            class="column is-three-quarters is-flex is-justify-content-center is-flex-direction-column"
          >
            <h3 class="title is-3">Best Fresh Product</h3>
            <p class="hast-text-centered">
              but the majority have suffered alteration in some form, by
              injected humour, or randomised words which don't look even
              slightly believable. If you are going to use a passage of Lorem
              Ipsum, you need to be
            </p>
            <br />
            <div class="buttons is-left">
              <button class="button is-medium is-black is-light is-link">
                Buy Now
              </button>
            </div>
          </div>
          <div class="column">
            <figure class="image">
              <img
                loading="lazy"
                width="100"
                height="100"
                src="https://res.cloudinary.com/dazyxzm1e/image/upload/v1620129151/undraw_shopping_app_flsj_k5vifw.svg"
              />
            </figure>
          </div>
        </div>
      </div>
    </section>

    <!-- MAP SECTION -->
    <section class="map-section">
      <iframe
        class="box"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14131.341213024258!2d85.28326908165225!3d27.69148477477402!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb1868199f2d47%3A0xf48b0ab8d867e77a!2z4KSV4KWB4KSy4KWH4KS24KWN4KS14KSwLCDgpJXgpL7gpKDgpK7gpL7gpKHgpYzgpIEgNDQ2MDA!5e0!3m2!1sne!2snp!4v1620141109682!5m2!1sne!2snp"
        id="map"
        allowfullscreen=""
        loading="lazy"
      ></iframe>
    </section>

    <section class="section">
      <div class="container">
        <div class="footer-main">
          <div class="columns">
            <div class="column">
              <h4 class="title is-4">Products</h4>
              <p class="">
                randomised words which don't look even slightly believable. If
                you are going to use a passage of Lorem Ipsum,
              </p>
            </div>
            <div class="column">
              <h4 class="title is-4">Services</h4>
              <p class="">
                randomised words which don't look even slightly believable. If
                you are going to use a passage of Lorem Ipsum,
              </p>
            </div>
            <div class="column">
              <h4 class="title is-4">List</h4>
              <p class="">
                randomised words which don't look even slightly believable. If
                you are going to use a passage of Lorem Ipsum,
              </p>
            </div>

            <div class="column">
              <h4 class="title is-4">Follow Us</h4>

              <div class="buttons">
                <a
                  class="button is-medium is-facebook is-inverted is-black-social"
                >
                  <span class="icon">
                    <i class="fab fa-facebook fa-lg"></i>
                  </span>
                </a>
                <a
                  class="button is-medium is-instagram is-inverted is-black-social"
                >
                  <span class="icon">
                    <i class="fab fa-instagram fa-lg"></i>
                  </span>
                </a>
                <a
                  class="button is-medium is-twitter is-inverted is-black-social"
                >
                  <span class="icon">
                    <i class="fab fa-twitter fa-lg"></i>
                  </span>
                </a>
                <a
                  class="button is-medium is-youtube is-inverted is-black-social"
                >
                  <span class="icon">
                    <i class="fab fa-youtube fa-lg"></i>
                  </span>
                </a>
              </div>
              <h4 class="title is-4">Subscribe Now</h4>
              <div class="field">
                <input class="input" type="text" placeholder="Email" />
              </div>
              <div class="buttons">
                <button class="button is-left is-medium is-orange">
                  Subscribe
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

import bulmaCarousel from "bulma-carousel";
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
    bulmaCarousel.attach("#carousel-demo", {
      initialSlide: 0,
      slidesToScroll: 1,
      slidesToShow: 1,
    });
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
@import "../assets/css/bulma-carousel.min.css";
.hero {
  background-color: #202020;
}
.title {
  color: #ffffff;
}
.subtitle {
  color: #ffffff;
}
#carousel-section {
  background-color: #f7f7f7 !important;
  padding: 50px 0;
  margin-bottom: 50px;
}

#carousel-demo {
  margin-top: 50px;
}
.title {
  color: #202020;
}
.button.is-black {
  background-color: black !important;
  color: white !important;
}

.button.is-orange {
  background-color: #fc5d35 !important;
  color: white !important;
}

.button.is-orange:hover {
  background-color: white !important;
  color: #fc5d35 !important;
}
.button.is-black:hover {
  background-color: white !important;
  color: black !important;
}

.is-black-social {
  color: black !important;
}
.is-black-social:hover {
  background-color: white !important;
  color: #fc5d35 !important;
}

.footer-main {
  background-color: white !important;
  padding: 0 !important;
}
</style>