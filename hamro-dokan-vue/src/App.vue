<template>
  <body>
    <div id="wrapper">
      <nav class="navbar">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"
            ><strong>हाम्रो दोकान</strong></router-link
          >
          <a
            href=""
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div
          class="navbar-menu"
          id="navbar-menu"
          v-bind:class="{ 'is-active': showMobileMenu }"
        >
          <div class="navbar-start">
            <div class="navbar-item">
              <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      name="query"
                      placeholder="खोज्जनुहोस...."
                    />
                  </div>
                  <div class="control">
                    <button class="button is-info">
                      <span><i class="fas fa-search"></i></span>
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="navbar-end">
            <router-link to="/electronics" class="navbar-item"
              >Electronics</router-link
            >
            <router-link class="navbar-item" to="/winter">Winter</router-link>
            <div class="navbar-item">
              <div class="buttons">
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/profile" class="button is-info"
                    >Profile</router-link
                  >
                </template>
                <template v-else>
                  <router-link to="/login" class="button is-info"
                    >LogIn</router-link
                  >
                </template>
                <router-link to="/cart" class="button is-success">
                  <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                  <span>Cart ({{ cartTotalLength }})</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
      <div
        class="is-loading-bar has-text-centered"
        v-bind:class="{ 'is-loading': $store.state.isLoading }"
      >
        <div class="lds-dual-ring"></div>
      </div>
      <section class="section">
        <router-view />
      </section>
    </div>
    <footer class="footer">
      <p class="has-text-centered">Copyright ©️ 2021</p>
    </footer>
  </body>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }
      return totalLength;
    },
  },
};
</script>
<style lang="scss">
@import "../node_modules/bulma";
#wrapper {
  flex: 1;
}
body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  background-color: #ffffff;
}

.box {
  box-shadow: 50px, 50px;
  -webkit-box-shadow: 0 0 10px #707070;
  -moz-box-shadow: 0 0 10px #ffdf6c;
}

.navbar {
  background-color: #202020;
  color: #ffffff;
}
.navbar-item {
  color: #ffffff;
}
.footer {
  background-color: #202020;
  color: #ffffff;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring::after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
