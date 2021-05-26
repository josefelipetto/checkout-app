<template>
  <div class="col-md-5 col-lg-4 order-md-last">
    <h4 class="d-flex justify-content-between align-items-center mb-3">
      <span class="text-primary">Your cart</span>
      <span class="badge bg-primary rounded-pill">{{ totalItems }}</span>
    </h4>
    <ul class="list-group mb-3">
      <li
        class="list-group-item d-flex justify-content-between lh-sm"
        v-for="(productId, idx) of cartIterator"
        :key="idx"
      >
        <div>
          <div class="d-flex flex-row">
            <h6 class="my-0">{{ cart[productId].name }} </h6>
            &nbsp;
            <BIconTrash @click="deleteItem(productId)" title="Delete this item from the cart"/>
          </div>
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
import { BIconTrash } from 'bootstrap-icons-vue'

/**
 * Cart Items module responsible for hold a list of added products to the cart
 * @displayName Cart Items
*/
export default {
  name: 'CartItems',
  components: {
    BIconTrash
  },
  methods: {
    /**
     * delete an item from the cart
     * @param productId
     */
    deleteItem (productId) {
      this.$store.commit('deleteCartItem', productId)
    }
  },
  computed: {
    /**
     * Returns the current cart
     * @return {(function(*): {})|*}
     */
    cart () {
      return this.$store.getters.getCart
    },
    /**
     * Returns cart keys(products) to be iterated
     * @returns {string[]}
     */
    cartIterator () {
      return Object.keys(this.$store.getters.getCart).filter(key => this.cart[key].quantity > 0)
    },
    /**
     * Returns the number of items on the cart
     */
    totalItems () {
      return this.$store.getters.getCartTotalItems
    },
    /**
     * Returns the total spent so far
     */
    cartTotalSpent () {
      return this.$store.getters.getCartTotalSpent.toFixed(2)
    }
  }
}
</script>
