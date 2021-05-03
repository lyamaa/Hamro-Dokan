<template>
  <div class="register-page">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign Up</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label class="label">Username</label>
            <div class="control">
              <input type="text" class="input" v-model="username" />
            </div>
          </div>

          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>

          <div class="field">
            <label class="label">Confirm Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2" />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <button class="delete"></button>
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </form>
        <hr />
        <p>
          Already Have an account? <router-link to="/login">Login</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username == "") {
        this.errors.push("User name must not be empty 😎😎");
      }
      if (this.password === "") {
        this.errors.push("Please input password. 🥺🥺🥺");
      }
      if (this.password === this.username) {
        this.errors.push("Give a good password, which is simalar to username");
      }
      if (this.password != this.password2) {
        this.errors.push("Password does match. 🧐🧐🧐");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post("/users/", formData)
          .then((res) => {
            toast({
              message:
                "Account Successfully Created, Please Login to continue. 🎉🎉🎉",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
            this.$router.push("/login");
          })
          .catch((err) => {
            if (err.res) {
              for (const property in error.res.data) {
                this.errors.push(`${property}: ${err.res.data[property]}`);
              }
              console.log(JSON.stringify(err.res.data));
            } else if (err.message) {
              this.errors.push(
                "Something went wrong, please try again. 😥😥😥"
              );
              console.log(JSON.stringify(err));
            }
          });
      }
    },
  },
};
</script>