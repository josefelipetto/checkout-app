<template>
  <header class="p-3 bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <router-link to="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
          <BIconBasket /> &nbsp; Magic Restaurant
        </router-link>

        <div class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        </div>

        <div class="text-end">
          <button type="button" class="btn btn-dark">
            <BIconCart4 />
            <span class="badge rounded-circle bg-danger" id="lblCartCount">{{ cartTotalItems }}</span>
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { BIconBasket, BIconCart4 } from 'bootstrap-icons-vue'

export default {
  name: 'Header',
  components: {
    BIconBasket,
    BIconCart4
  },
  computed: {
    cartTotalItems () {
      return this.$store.getters.getCartTotalItems
    }
  }
}
</script>

<style scoped>
  #lblCartCount {
    font-size: 12px;
    padding: 3px 5px 3px 5px;
    vertical-align: top;
  }
</style>
