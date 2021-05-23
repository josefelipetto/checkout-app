<template>
  <div class="col-md-5 col-lg-4 order-md-last">
    <h4 class="d-flex justify-content-between align-items-center mb-3">
      <span class="text-primary">Your cart</span>
      <span class="badge bg-primary rounded-pill">{{ totalItems }}</span>
    </h4>
    <ul class="list-group mb-3">
      <li class="list-group-item d-flex justify-content-between lh-sm" v-for="(productId, idx) of cartIterator" :key="idx">
        <div>
          <h6 class="my-0">{{ cart[productId].name }}</h6>
          <small class="text-muted">Unitary price: ${{ cart[productId].price.toFixed(2) }}</small><br>
          <small class="text-muted">Amount: {{ cart[productId].quantity }}</small>
        </div>
        <span class="text-muted">${{ (cart[productId].price * cart[productId].quantity).toFixed(2) }}</span>
      </li>
      <li class="list-group-item d-flex justify-content-between">
        <span>Total (USD)</span>
        <strong>${{ cartTotalSpent }}</strong>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'CartItems',
  computed: {
    cart () {
      return this.$store.getters.getCart
    },
    cartIterator () {
      return Object.keys(this.$store.getters.getCart)
    },
    totalItems () {
      return this.$store.getters.getCartTotalItems
    },
    cartTotalSpent () {
      return this.$store.getters.getCartTotalSpent.toFixed(2)
    }
  }
}
</script>
