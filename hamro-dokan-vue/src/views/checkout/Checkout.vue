<template>
  <div class="checkout-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Qty</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in cart.items" v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>{{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>{{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ cartTotalLength }}</td>
              <td>{{ cartTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
      </div>
      <div class="column is-12 box mt-5">
        <h2 class="subtitle">Shipping Details</h2>
        <p class="has-text-grey mb-4">* All fields are required..</p>
        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label class="label">First Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="First Name"
                  v-model="first_name"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Middle Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="First Name"
                  v-model="first_name"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Last Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Last Name"
                  v-model="last_name"
                />
              </div>
            </div>

            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="First Name"
                  v-model="email"
                />
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label class="label">Phone</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Phone number"
                  v-model="phone"
                />
              </div>
            </div>

            <div class="field">
              <label class="label">Address</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Address"
                  v-model="address"
                />
              </div>
            </div>

            <div class="field">
              <label class="label">Zip Code</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Zip Code"
                  v-model="zipcode"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Place</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Place"
                  v-model="place"
                />
              </div>
            </div>
          </div>
          <div class="column is-12">
            <div class="button is-outlined is-fullwidth is-success">Submit</div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <button class="delete"></button>
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </div>
      </div>
    </div>

    <hr />
    <div id="card-element" class="mb-5"></div>

    <template v-if="cartTotalLength">
      <hr />

      <button class="button is-dark" @click="submitForm">
        Pay with Stripe
      </button>
    </template>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Checkout",
  data() {
    return {
      cart: {
        items: [],
      },
      stripe: {},
      card: {},
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout | Hamro Dokan";

    this.cart = this.$store.state.cart;
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    submitForm() {
      this.errors = [];
      if (this.first_name === "") {
        this.errors.push("The first name field is missing!");
      }
      if (this.last_name === "") {
        this.errors.push("The last name field is missing!");
      }
      if (this.email === "") {
        this.errors.push("The email field is missing!");
      }
      if (this.phone === "") {
        this.errors.push("The phone field is missing!");
      }
      if (this.address === "") {
        this.errors.push("The address field is missing!");
      }
      if (this.zipcode === "") {
        this.errors.push("The zip code field is missing!");
      }
      if (this.place === "") {
        this.errors.push("The place field is missing!");
      }
      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true);
        this.stripe.createToken(this.card).then((result) => {
          if (result.error) {
            this.$store.commit("setIsLoading", false);
            this.errors.push(
              "Something went wrong with Stripe. Please try again"
            );
            console.log(result.error.message);
          } else {
            this.stripeTokenHandler(result.token);
          }
        });
      }
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>