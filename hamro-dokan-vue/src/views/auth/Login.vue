<template>
  <div class="login-page">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Login</h1>
        <form @submit.prevent="onSubmit">
          <div class="field">
            <p class="control has-icons-left has-icons-right">
              <input
                class="input"
                type="text"
                placeholder="Username"
                v-model="username"
              />
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
            </p>
          </div>

          <div class="field">
            <p class="control has-icons-left has-icons-right">
              <input
                class="input"
                type="password"
                placeholder="password"
                v-model="password"
              />
              <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
              </span>
            </p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Login</button>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <button class="delete"></button>
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </form>
        <hr />
        <p>New here? <router-link to="/register"> Sign-Up</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },

  mounted() {
    document.title = "Login | Hamro Dokan";
  },
  methods: {
    async onSubmit() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      axios
        .post("/token/login/", formData)
        .then((res) => {
          const token = res.data.authToken;
          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Token " + token;

          localStorage.setItem("token", token);

          const toPath = this.$route.query.to || "/cart";

          this.$router.push(toPath);
        })
        .catch((err) => {
          if (err.res) {
            for (const property in err.res.data) {
              this.errors.push(`${property}: ${err.res.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong, please try again. 😥😥😥");
          }
        });
    },
  },
};
</script>